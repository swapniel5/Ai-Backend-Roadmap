# FastAPI Service

This guide explains how to install and run the FastAPI service in this
repository.

## 1. Check Python

From the repository root, verify that Python is available:

```bash
/opt/homebrew/bin/python3 --version
```

## 2. Create a virtual environment

Create a project-local virtual environment:

```bash
/opt/homebrew/bin/python3 -m venv .venv
```

The virtual environment keeps FastAPI dependencies separate from the
system/Homebrew Python installation.

## 3. Activate the virtual environment

On macOS or Linux:

```bash
source .venv/bin/activate
```

On Windows:

```powershell
.venv\Scripts\Activate.ps1
```

After activation, the shell prompt usually shows `(.venv)`.

## 4. Install FastAPI

Install FastAPI and its standard command-line/server dependencies:

```bash
python -m pip install "fastapi[standard]"
```

Verify the installation:

```bash
python -c "import fastapi; print(fastapi.__version__)"
```

## 5. Understand the application structure

```text
fastapi-service/
  app/
    main.py
```

The `main.py` file creates the FastAPI application and defines the root
endpoint:

```python
app = FastAPI(title="FastAPI Service")
```

## 6. Start the development server

Run this command from the repository root:

```bash
uvicorn --app-dir fastapi-service app.main:app --reload
```

Explanation:

- `uvicorn` runs the ASGI application.
- `--app-dir fastapi-service` adds the service directory to Python's import
  path.
- `app.main:app` means `app` package, `main.py` module, and `app` variable.
- `--reload` restarts the server when source files change.

The service will be available at:

```text
http://127.0.0.1:8000
```

## 7. Test the endpoint

In another terminal:

```bash
curl http://127.0.0.1:8000/
```

Expected response:

```json
{"message":"FastAPI service is running"}
```

## 8. Try the task CRUD API

Create a task:

```bash
curl -X POST http://127.0.0.1:8000/tasks \
  -H "Content-Type: application/json" \
  -d '{"title":"Learn FastAPI","description":"Build a CRUD endpoint"}'
```

List all tasks:

```bash
curl http://127.0.0.1:8000/tasks
```

Get one task:

```bash
curl http://127.0.0.1:8000/tasks/1
```

Update a task:

```bash
curl -X PUT http://127.0.0.1:8000/tasks/1 \
  -H "Content-Type: application/json" \
  -d '{"title":"Learn FastAPI CRUD","description":"Practice update requests"}'
```

Delete a task:

```bash
curl -i -X DELETE http://127.0.0.1:8000/tasks/1
```

The task data is stored only in memory and is reset when the server restarts.

## 9. Open the automatic API documentation

FastAPI generates interactive documentation automatically:

- Swagger UI: http://127.0.0.1:8000/docs
- ReDoc: http://127.0.0.1:8000/redoc
- OpenAPI JSON: http://127.0.0.1:8000/openapi.json

## 10. Stop the server and leave the environment

In the terminal running Uvicorn, press:

```text
Ctrl+C
```

Then deactivate the virtual environment:

```bash
deactivate
```

## Common commands

Run the application without auto-reload:

```bash
uvicorn --app-dir fastapi-service app.main:app
```

Run on a different port:

```bash
uvicorn --app-dir fastapi-service app.main:app --reload --port 8080
```
