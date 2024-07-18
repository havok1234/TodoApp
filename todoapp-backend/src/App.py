from fastapi import FastAPI, HTTPException, Query, Path, Body
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from typing import List
import uuid
import uvicorn
import pytest
import sys

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8080"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)

# Mock database for demonstration purposes
items = [
    {"id": "1", "title": "Jog around the park 3x", "done": False},
    {"id": "2", "title": "10 minutes meditation", "done": False},
    {"id": "3", "title": "Read for 1 hour", "done": False},
    {"id": "4", "title": "Pick up groceries", "done": True},
    {"id": "5", "title": "Complete Todo App on Frontend Mentor", "done": True},
    {"id": "6", "title": "Pick up laundry", "done": False},
]

class Todo(BaseModel):
    id: str = str(uuid.uuid4())
    title: str
    done: bool

# Endpoint to get todos with filter
@app.get("/todos", response_model=List[Todo])
async def get_todos(filter: str = Query("All", regex="^(All|Active|Completed)$")):
    if filter == "All":
        return [Todo(**todo) for todo in items]
    elif filter == "Active":
        active_todos = [todo for todo in items if not todo["done"]]
        return [Todo(**todo) for todo in active_todos]
    elif filter == "Completed":
        completed_todos = [todo for todo in items if todo["done"]]
        return [Todo(**todo) for todo in completed_todos]
    else:
        raise HTTPException(status_code=400, detail="Invalid filter parameter. Use 'All', 'Active', or 'Completed'.")
    
# Endpoint to add a new todo
@app.post("/todos", response_model=Todo)
async def add_todo(todo: Todo):
    # Generate a new unique ID for the new todo
    # Assign a new UUID for the todo
    todo.id = str(uuid.uuid4())
    # Append to items list
    items.append(todo.model_dump())
    return todo

# Endpoint to mark a todo as complete
@app.put("/todos/{todo_id}/toggle", response_model=Todo)
async def toggle_todo_state(
    todo_id: str = Path(..., title="The ID of the todo to mark as complete"), 
    done: bool = Body(True, title="The bool value to mark todo as complete or incomplete")):
    todo_to_complete = next((todo for todo in items if todo['id'] == str(todo_id)), None)
    if not todo_to_complete:
        raise HTTPException(status_code=404, detail="Todo not found")
    if todo_to_complete['done'] != done:
        todo_to_complete['done'] = done
    return todo_to_complete

@app.delete("/todos/completed")
async def delete_completed_todos():
    global items
    items = [todo for todo in items if not todo['done']]
    return items

@app.put("/todos/reorder")
async def update_todos_order(order: List[str]):
    global items 
    try:
        # Validate that all IDs in order exist in todos
        for todo_id in order:
            if not any(todo["id"] == todo_id for todo in items):
                raise HTTPException(status_code=404, detail=f"Todo with ID {todo_id} not found")
        
        # Create a new list of todos in the order specified
        items = sorted(items, key=lambda x: order.index(x["id"]))

        return {"message": "Todos order updated successfully"}
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to reorder todos: {str(e)}")

@app.delete("/todos/{todo_id}")
async def delete_todo(todo_id: str = Path(..., title="The ID of the todo to delete")):
    global items
    items = [todo for todo in items if todo['id'] != str(todo_id)]
    return items

def run_app():
    uvicorn.run(app, host="0.0.0.0", port=8000)

if __name__ == "__main__":    
    # Synchronously run tests before starting the FastAPI application
    result_code = pytest.main(["tests/test_app.py"])
    if result_code == 0:
        run_app()
    else:
        sys.exit(result_code)


