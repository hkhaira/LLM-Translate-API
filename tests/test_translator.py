import pytest
from fastapi.testclient import TestClient

# Import the FastAPI application from our project.
from app.main import app

# Create a TestClient instance to interact with our API
client = TestClient(app)


# -------------------------------------------------------------------
# Fake translation functions for testing
# -------------------------------------------------------------------

def fake_translate_text_success(input_str: str) -> str:
    """
    Fake translation function for successful calls.
    Simply returns the input prefixed with "French: ".
    """
    return f"French: {input_str}"


def fake_translate_text_exception(input_str: str) -> str:
    """
    Fake translation function that simulates an error.
    """
    raise Exception("Translation error")


# -------------------------------------------------------------------
# Pytest fixture to override the translation function by default.
# This makes all tests use the fake successful translator
# unless overridden later.
# -------------------------------------------------------------------

@pytest.fixture(autouse=True)
def override_translate(monkeypatch):
    # Patch the translate_text function in app.main where it is used.
    monkeypatch.setattr("app.main.translate_text", fake_translate_text_success)


# -------------------------------------------------------------------
# Test Cases
# -------------------------------------------------------------------

def test_translate_success():
    """
    Test a valid translation request.
    Given an input, our fake translator returns "French: {input}".
    """
    payload = {"input_str": "Hello, world!"}
    response = client.post("/translate/", json=payload)
    assert response.status_code == 200
    json_data = response.json()
    assert "translated_text" in json_data
    # Our fake_translate_text_success should yield "French: Hello, world!"
    assert json_data["translated_text"] == "French: Hello, world!"


def test_translate_empty_input():
    """
    Test the case where the input string is empty.
    """
    payload = {"input_str": ""}
    response = client.post("/translate/", json=payload)
    assert response.status_code == 200
    json_data = response.json()
    # Expect the fake translator to return "French: " (with nothing appended)
    assert json_data["translated_text"] == "French: "


def test_translate_missing_field():
    """
    Test that a request missing the required 'input_str' field fails with a validation error.
    """
    payload = {}  # No "input_str"
    response = client.post("/translate/", json=payload)
    # FastAPI (via Pydantic) should return a 422 Unprocessable Entity error.
    assert response.status_code == 422


def test_translate_invalid_input_type():
    """
    Test that if a non-string type is provided for input_str,
    Pydantic should either coerce it or return a validation error.
    Here we assume Pydantic coerces numbers to strings.
    """
    payload = {"input_str": 123}
    response = client.post("/translate/", json=payload)
    assert response.status_code == 200
    json_data = response.json()
    # With coercion, our fake translator will see the number as a string "123".
    assert json_data["translated_text"] == "French: 123"


def test_translate_exception(monkeypatch):
    """
    Simulate an exception in the translation function.
    The endpoint should return HTTP 500 with an appropriate error message.
    """
    # Override the translate_text function to simulate an error.
    monkeypatch.setattr("app.main.translate_text", fake_translate_text_exception)
    payload = {"input_str": "Hello"}
    response = client.post("/translate/", json=payload)
    assert response.status_code == 500
    json_data = response.json()
    assert "detail" in json_data
    assert "Translation error" in json_data["detail"]


def test_translate_special_characters():
    """
    Test with special characters and non-ASCII text.
    """
    payload = {"input_str": "Café 😊"}
    response = client.post("/translate/", json=payload)
    assert response.status_code == 200
    json_data = response.json()
    # Our fake translator simply echoes the input.
    assert json_data["translated_text"] == "French: Café 😊"


def test_translate_long_input():
    """
    Test with a very long input string to simulate edge cases with large data.
    """
    long_text = "Hello " * 1000  # Create a long string by repeating "Hello "
    payload = {"input_str": long_text}
    response = client.post("/translate/", json=payload)
    assert response.status_code == 200
    json_data = response.json()
    # Check that the returned translation starts with the expected prefix.
    assert json_data["translated_text"].startswith("French: Hello ")