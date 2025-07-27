# Import TestClient to simulate API requests
from fastapi.testclient import TestClient

# Import the FastAPI app instance from the controller module
from main import app

# Create a TestClient instance for the FastAPI app
client = TestClient(app)

# Define a test function for reading a specific sheep
def test_read_sheep():
    # Send a GET request to the endpoint "/sheep/1"
    response = client.get("/sheep/1")

    # Assert that the response status code is 200 (OK)
    assert response.status_code == 200

    # Assert that the response JSON matches the expected data
    assert response.json() == {
        # Expected JSON structure
        "id": 1,
        "name": "Spice",
        "breed": "Gotland",
        "sex": "ewe"
    }

# Define a test function for adding a new sheep
def test_add_sheep():
    # TODO: Prepare the new sheep data in a dictionary format.
    sheep_data_name = {
        "id": 7,
        "name": "Sheepy",
        "breed": "Suffolk",
        "sex": "ewe"
    }

    # TODO: Send a POST request to the endpoint "/sheep" with the new sheep data.
    # Arguments should be your endpoint and new sheep data.
    response = client.post("/sheep", json=sheep_data_name)

    # TODO: Assert that the response status code is 201 (Created)
    assert response.status_code == 201

    # TODO: Assert that the response JSON matches the new sheep data
    assert response.json() == {
        # Expected JSON structure
        "id": 7,
        "name": "Sheepy",
        "breed": "Suffolk",
        "sex": "ewe"
    }

    # TODO: Verify that the sheep was actually added to the database by retrieving the new sheep by ID.
    get_response = client.get(f"/sheep/7")

    # include an assert statement to see if the new sheep data can be retrieved.
    assert get_response.status_code == 200
    assert get_response.json() == sheep_data_name


# Define a test function for deleting a specific sheep
def test_delete_sheep():
    # Send a delete request to the endpoint "/sheep/1"
    response = client.delete("/sheep/1")

    # Assert that the response status code is 200 (OK)
    assert response.status_code == 204


# Define a test function for updating a specific sheep
def test_update_sheep():
    sheep_data_name = {
        "id": 1,
        "name": "Sheepo",
        "breed": "F1",
        "sex": "ewe"
    }

    # Send a PUT request to the endpoint "/sheep/1"
    response = client.put("/sheep/2", json=sheep_data_name)

    # Assert that the response status code is 200 (OK)
    assert response.status_code == 200
    assert response.json() == sheep_data_name



def test_read_all_sheep():
    # Send a GET request to retrieve all sheep
    response = client.get("/sheep/")
    data = response.json()

    assert response.status_code == 200

    assert isinstance(data, list)

    for item in data:
        assert "id" in item
        assert "name" in item
        assert "breed" in item
        assert "sex" in item