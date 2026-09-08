"""Minimal FastAPI service.

This module creates the web application and defines its routes.
"""

# Import FastAPI so we can create the application object.
from fastapi import FastAPI


# Call the FastAPI constructor, similar to creating a Spring application
# context in Java. The title appears in the generated API documentation.
app = FastAPI(title="FastAPI Service")


# Register the function below for HTTP GET requests to the root path "/".
# This is similar to Spring's @GetMapping("/") annotation.
@app.get("/")
def read_root() -> dict[str, str]:
    # self is not needed here because this is a function, not a class method.
    """Return a welcome message."""
    # FastAPI converts this Python dictionary into a JSON response with
    # HTTP status 200. dict[str, str] means string keys and string values.
    return {"message": "FastAPI service is running"}

@app.get("/health")
def health_check() -> dict[str, str]:
    """Return service health status."""
    return {"status": "ok"}