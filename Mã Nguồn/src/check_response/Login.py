import requests
import datetime

# Test case to verify that the API endpoint URL is correct and accessible
def test_api_endpoint_accessible():
    data = {
    "email": "eve.holt@reqres.in",
    "password": "pistol"
}
    response = requests.post("https://reqres.in/api/login", data=data)
    assert response.status_code == 200
    print("status-code : OK")


# Test case to verify that the API endpoint returns the expected response format
def test_api_returns_expected_format():
    data = {
        "email": "eve.holt@reqres.in",
        "password": "pistol"
    }
    response = requests.post("https://reqres.in/api/login", data=data)
    assert response.headers["Content-Type"] == "application/json; charset=utf-8"
    print("Content-Type : OK")
# Test case to verify when create user failed
def test_api_returns_correct_status_code_when_wrong_type_data():
    data = {
        "email": 1,
        "password": 2
    }
    response = requests.post("https://reqres.in/api/login", data=data)
    assert response.status_code == 400
    print("Error-Status : OK")
# Test case to verify that the API endpoint returns the expected data according to the API documentation
def test_api_handles_errors():
    data = {
        "email": "eve.holt@reqres.in"
    }
    data_2 = {
        "password": "pistol"
    }
    response = requests.post("https://reqres.in/api/login", data=data)
    assert response.status_code == 400
    assert response.json()["error"] == "Missing password"
    response1 = requests.post("https://reqres.in/api/register", data=data_2)
    assert response1.status_code == 400
    assert response1.json()["error"] == "Missing email or username"
    print("Handle-Error : OK")
def test_api_returns_expected_data():
    data = {
        "email": "eve.holt@reqres.in",
        "password": "pistol"
    }
    response = requests.post("https://reqres.in/api/login", data=data)
    assert response.json()["token"] != ""
    print("Response-data : OK")

#sửa lại
def test_api_resturn_unauthorize():
    data = {
        "email": "nvlong@reqres.in",
        "password": "1234"
    }
    response = requests.post("https://reqres.in/api/login", data=data)
    assert response.json()["error"] == "user not found"
    print("Unauthorized-code : OK")


# Test case to verify that the API endpoint returns the correct headers
def test_api_returns_correct_headers():
    data = {
        "email": "eve.holt@reqres.in",
        "password": "pistol"
    }
    response = requests.post("https://reqres.in/api/login", data=data)
    assert response.headers.get("Server") == "cloudflare"
    print("server : OK")
    assert response.headers.get("X-Powered-By") == "Express"
    print("X-Powered-By : OK")
    assert response.headers.get("Access-Control-Allow-Origin") == "*"
    print("Access-Control-Allow-Origin : :")
    assert response.headers.get("Connection") == "keep-alive"
    print("Connect : OK")
    assert response.headers.get("CF-Cache-Status") == "DYNAMIC"
    print("CF-Cache-Status : OK")


