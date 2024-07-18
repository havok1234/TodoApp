import pytest
from httpx import AsyncClient
from fastapi import status
from src.App import app

# Test case for getting all todos
@pytest.mark.asyncio
async def test_get_all_todos():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        # Add a new todo to ensure it exists
        new_todo = {"title": "Get All Todos Todo", "done": False}
        await ac.post("/todos", json=new_todo)
        response = await ac.get("/todos?filter=All")
    assert response.status_code == status.HTTP_200_OK
    assert len(response.json()) >= 1  # Adjust according to your initial mock database

# Test case for getting active todos
@pytest.mark.asyncio
async def test_get_active_todos():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        # Add a new todo to ensure it exists
        new_todo = {"title": "Get All Active Todos Todo", "done": False}
        await ac.post("/todos", json=new_todo)
        response = await ac.get("/todos?filter=Active")
        active_todos = [todo for todo in response.json() if not todo['done']]
    assert response.status_code == status.HTTP_200_OK
    assert len(response.json()) == len(active_todos)


# Test case for adding a new todo
@pytest.mark.asyncio
async def test_add_todo():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        new_todo = {"title": "New Todo", "done": False}
        response = await ac.post("/todos", json=new_todo)
    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    assert data["title"] == new_todo["title"]
    assert data["done"] == new_todo["done"]

# Test case for toggling a todo's state
@pytest.mark.asyncio
async def test_toggle_todo_state():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        # Add a new todo to ensure it exists
        new_todo = {"title": "Toggle Test Todo", "done": False}
        add_response = await ac.post("/todos", json=new_todo)
        todo_id = add_response.json()["id"]

        # Toggle the todo's state
        response = await ac.put(f"/todos/{todo_id}/toggle?done=true")
    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    assert data["done"] is True

# Test case for deleting a todo by ID
@pytest.mark.asyncio
async def test_delete_todo_by_id():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        # Add a new todo to ensure it exists
        new_todo = {"title": "Delete Test Todo", "done": False}
        add_response = await ac.post("/todos", json=new_todo)
        todo_id = add_response.json()["id"]

        # Delete the todo by ID
        response = await ac.delete(f"/todos/{todo_id}")
        assert response.status_code == status.HTTP_200_OK

    # Check that the todo is no longer in the list
        get_response = await ac.get("/todos?filter=All")
    todos = get_response.json()
    for todo in todos:
        assert todo["id"] != todo_id

# Test case for deleting all completed todos
@pytest.mark.asyncio
async def test_delete_completed_todos():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.delete("/todos/completed")
    assert response.status_code == status.HTTP_200_OK
    remaining_todos = [todo for todo in response.json() if not todo["done"]]
    assert len(response.json()) == len(remaining_todos)
