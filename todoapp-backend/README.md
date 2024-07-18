### About
This is the backend service for the todoApp. This service uses FastAPIs to provide an in-memory backend to store Todos and expose various operations on them
The backend service instantiates with 5 preexisting elements in the memory

```
    {"id": "1", "title": "Jog around the park 3x", "done": False},
    {"id": "2", "title": "10 minutes meditation", "done": False},
    {"id": "3", "title": "Read for 1 hour", "done": False},
    {"id": "4", "title": "Pick up groceries", "done": True},
    {"id": "5", "title": "Complete Todo App on Frontend Mentor", "done": True}
```

### Pre-requisites
This service requires following tools and modules:
- python
- pip 
- fastapi
- pytest
- pytest-asyncio
- httpx 
- pydantic

### Usage
- Once the pre-requisites are installed, this backend can be started by executing the App.py file

### API Documentation
Once the service is up, FastAPI docs will be available here: http://localhost:8000/docs

### Test Suite
Test suite for the service is available in the tests/ folder and is executed before the service starts
