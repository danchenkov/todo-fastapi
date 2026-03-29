from fastapi import APIRouter, Form, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates

from app.models.todo import Todo
from app.storage.json_store import load_todos, save_todos

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")


@router.get("/", response_class=HTMLResponse)
def show_todos(request: Request):
    todos = load_todos()
    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "todos": todos,
        },
    )


@router.get("/todos/new", response_class=HTMLResponse)
def new_todo_form(request: Request):
    return templates.TemplateResponse(
        "new.html",
        {
            "request": request,
        },
    )


@router.post("/todos")
def create_todo(text: str = Form(...)):
    todos = load_todos()

    todo = Todo(
        id=len(todos) + 1,
        text=text,
        completed=False,
    )

    todos.append(todo)
    save_todos(todos)

    return RedirectResponse(url="/", status_code=303)


@router.post("/todos/{todo_id}/toggle")
def toggle_todo(todo_id: int):
    todos = load_todos()

    for todo in todos:
        if todo.id == todo_id:
            todo.completed = not todo.completed
            break

    save_todos(todos)

    return RedirectResponse(url="/", status_code=303)


@router.post("/todos/{todo_id}/delete")
def delete_todo(todo_id: int):
    todos = load_todos()

    todos = [todo for todo in todos if todo.id != todo_id]

    save_todos(todos)

    return RedirectResponse(url="/", status_code=303)