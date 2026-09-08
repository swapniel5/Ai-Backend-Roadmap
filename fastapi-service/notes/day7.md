# Day 7 — FastAPI Introduction

## What is FastAPI?

FastAPI is a Python framework for building HTTP APIs. You define Python functions for HTTP routes, and FastAPI handles request routing, response serialization, validation support, and API documentation generation. It is well suited to AI backend services because it has first-class support for modern Python types and asynchronous request handling.

## `@app.get` and Spring Boot `@GetMapping`

`@app.get("/health")` registers the Python function beneath it as the handler for an HTTP GET request to `/health`. This is the direct equivalent of a Spring Boot controller method annotated with `@GetMapping("/health")`.

```python
@app.get("/health")
def health_check() -> dict[str, str]:
    return {"status": "ok"}
```

```java
@GetMapping("/health")
public Map<String, String> healthCheck() {
    return Map.of("status", "ok");
}
```

Both approaches map an HTTP request to application code. In a later refactor, FastAPI routes will correspond to Spring controllers, while Python service functions will hold business logic.

## Python `dict` and a Java response DTO

A Python dictionary such as `{"status": "ok"}` is automatically serialized to a JSON object by FastAPI. For these simple endpoints, it fills the same role as a Java response DTO (or a `Map`) returned by a Spring controller and serialized by Jackson.

For more complex API contracts, FastAPI uses Pydantic models. They are closer to Java DTOs because they declare fields, types, validation rules, and API schema information. That is the focus of Day 8.

## Swagger and OpenAPI output

FastAPI reads the registered routes and their Python type information to generate an OpenAPI schema automatically. The raw schema is available at `/openapi.json`.

It also provides interactive Swagger UI documentation at `/docs`, where each endpoint can be inspected and invoked in the browser. ReDoc documentation is available at `/redoc`.

For this service, `/docs` should list:

- `GET /` — returns the welcome message.
- `GET /health` — returns the health status.

## Verification

- Confirm `GET /` responds with HTTP 200 and JSON.
- Confirm `GET /health` responds with HTTP 200 and `{ "status": "ok" }`.
- Open `/docs`, execute both routes from Swagger UI, and confirm their responses.
