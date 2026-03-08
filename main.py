from fastapi import FastAPI, HTTPException

app = FastAPI()


def validate_number(value: float, name: str) -> float:
    """
    Validate that the provided value is a real number.
    Raises an HTTP 422 error with a friendly message if invalid.
    """
    try:
        return float(value)
    except (TypeError, ValueError):
        raise HTTPException(
            status_code=422,
            detail=f"{name} must be a valid number."
        )


@app.get("/")
def root():
    """
    Health check endpoint.
    Returns a simple message indicating that the API is running.
    """
    return {"status": "healthy"}


@app.get("/add/{a}/{b}")
def add(a: float, b: float):
    """
    Add two numbers and return the result as JSON.
    Expected output includes the operation name, inputs, and result.
    """
    a = validate_number(a, "a")
    b = validate_number(b, "b")
    return {"operation": "add", "a": a, "b": b, "result": a + b}


@app.get("/subtract/{a}/{b}")
def subtract(a: float, b: float):
    """
    Subtract the second number from the first number and return the result as JSON.
    Expected output includes the operation name, inputs, and result.
    """
    a = validate_number(a, "a")
    b = validate_number(b, "b")
    return {"operation": "subtract", "a": a, "b": b, "result": a - b}


@app.get("/multiply/{a}/{b}")
def multiply(a: float, b: float):
    """
    Multiply two numbers and return the result as JSON.
    Expected output includes the operation name, inputs, and result.
    """
    a = validate_number(a, "a")
    b = validate_number(b, "b")
    return {"operation": "multiply", "a": a, "b": b, "result": a * b}


@app.get("/divide/{a}/{b}")
def divide(a: float, b: float):
    """
    Divide the first number by the second number and return the result as JSON.
    Returns a friendly error if division by zero is attempted.
    """
    a = validate_number(a, "a")
    b = validate_number(b, "b")

    if b == 0:
        raise HTTPException(
            status_code=422,
            detail="Division by zero is not allowed. Please provide a non-zero value for b."
        )

    return {"operation": "divide", "a": a, "b": b, "result": a / b}


@app.get("/average/{a}/{b}/{c}")
def average(a: float, b: float, c: float):
    """
    Calculate the average of three numbers and return the result as JSON.
    Expected output includes the operation name, inputs, and result.
    """
    a = validate_number(a, "a")
    b = validate_number(b, "b")
    c = validate_number(c, "c")
    return {"operation": "average", "a": a, "b": b, "c": c, "result": (a + b + c) / 3}


@app.get("/percent/{part}/{whole}")
def percent(part: float, whole: float):
    """
    Calculate what percentage the first number is of the second number.
    Returns a friendly error if the whole value is zero.
    """
    part = validate_number(part, "part")
    whole = validate_number(whole, "whole")

    if whole == 0:
        raise HTTPException(
            status_code=422,
            detail="The whole value cannot be zero when calculating a percentage."
        )

    return {
        "operation": "percent",
        "part": part,
        "whole": whole,
        "result": (part / whole) * 100
    }


@app.get("/rectangle-area/{length}/{width}")
def rectangle_area(length: float, width: float):
    """
    Calculate the area of a rectangle using length and width.
    Returns a friendly error if either value is negative.
    """
    length = validate_number(length, "length")
    width = validate_number(width, "width")

    if length < 0 or width < 0:
        raise HTTPException(
            status_code=422,
            detail="Length and width must be non-negative numbers."
        )

    return {
        "operation": "rectangle_area",
        "length": length,
        "width": width,
        "result": length * width
    }