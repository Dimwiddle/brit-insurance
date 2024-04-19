from utilities.api import Client 
import pytest

@pytest.fixture(scope="session")
def client() -> Client:
    return Client()

@pytest.fixture(scope="function")
def sample_object(client: Client) -> dict:
    """Retrieve an object for testing purposes."""
    obj = {
        "name": "Apple MacBook Pro 2",
        "data": {
            "year": 2022,
            "price": 1899.99,
            "CPU model": "Apple Silicon M2",
            "Hard disk size": "1 TB"
        }
    }
    response = client.post_object(obj)
    assert response.status_code == 200, "Sample object was not created successfully"
    return response.json()

def test_update_object_id(client: Client, sample_object: dict):
    """Attempt to update an existing object's ID."""
    object_id = sample_object['id']
    data = {"id": 1000}
    response = client.patch_object(object_id, data)
    assert response.status_code == 404, "Object ID should not be updated"
    expected_error = "No valid field(s) to update have been passed as part of a request body."
    assert response.json()['error'] == expected_error, "Object ID should not be updated"

def test_update_name_success(client: Client, sample_object: dict):
    """Test scenarios updating the object's name"""
    object_id = sample_object['id']
    data = {"name": "Apple MacBook Pro 3"}
    response = client.patch_object(object_id, data)
    assert response.status_code == 200, "Object name should be updated"
    assert response.json()['name'] == data['name'], "Object name should be updated"

def test_update_name_failure(client: Client, sample_object: dict):
    """Test scenarios updating the object's name with invalid values"""
    object_id = sample_object['id']
    scenarios = [
        {"name": ""},
        {"name": None},
        {"name": 12345}
    ]
    error = "400 Bad Request. If you are trying to create or update the data, potential issue is that you are sending incorrect body json or it is missing at all."
    for data in scenarios:
        data = {"name": data}
        response = client.patch_object(object_id, data)
        assert response.status_code == 400, "Object's name should not be updated with invalid values."
        assert response.json()['error'] == error, "Error message is not as expected."

def test_update_data_content_success(client: Client, sample_object: dict):
    """Test scenarios for updating the object's data field."""
    object_id = sample_object['id']
    scenarios = [
        {"data": {"year": 2023}},
        {"data": {"price": 1999.99}},
        {"data": {"price": 2001}},
        {"data": {"CPU model": "Apple Silicon M3"}},
        {"data": {"Hard disk size": "2 TB"}}
    ]
    for data in scenarios:
        response = client.patch_object(object_id, data)
        assert response.status_code == 200, "Object's data should be updated"
        assert response.json()['data'] == data['data'], "Object's data should be updated"

@pytest.mark.xfail(reason="This test is expected to fail due to the server not handling invalid data. Potential bugs or just expected behaviour.")
def test_update_data_content_failure(client: Client, sample_object: dict):
    """Test scenarios for updating the object's data field with invalid values."""
    object_id = sample_object['id']
    scenarios = [
        {"data": {"year": "2023"}},
        {"data": {"year": -2023}},
        {"data": {"price": "1999.99"}},
        {"data": {"price": -200}},
        {"data": {"CPU model": 12345}},
        {"data": {"Hard disk size": None}}
    ]
    error = "400 Bad Request. If you are trying to create or update the data, potential issue is that you are sending incorrect body json or it is missing at all."
    for data in scenarios:
        response = client.patch_object(object_id, data)
        assert response.status_code == 400, "Object's data should not be updated with invalid values."
        assert response.json()['error'] == error, "Error message is not as expected."
