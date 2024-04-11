import requests
from datetime import datetime

# Test case to verify that the API endpoint URL is correct and accessible

def test_api_endpoint_accessible():
    data = {"name": "NGUYEN THE U", "job": "student"}
    response = requests.put("https://reqres.in/api/users/3", data=data)
    assert response.status_code == 200
    print("Status-code : OK")
#Test case to verify status code when update failed
def test_api_returns_correct_status_code_when_wrong_type_data():
    data = {"name": 1, "job": 2}
    response = requests.post("https://reqres.in/api/users", data=data)
    assert response.status_code == 400
    print("Error-Status : OK")
# Test case to verify that the API endpoint returns the expected response format
def test_api_returns_expected_format():
    data = {"name": "NGUYEN THE U", "job": "student"}
    response = requests.put("https://reqres.in/api/users/3", data=data)
    assert response.headers["Content-Type"] == "application/json; charset=utf-8"
    print("Content-Type : OK")

# Test case to verify that the API endpoint returns the expected data according to the API documentation
# sửa lại
def test_api_returns_expected_data():
    data = {"name": "NGUYEN THE U", "job": "student"}
    response = requests.put("https://reqres.in/api/users/3", data=data)

    format = "%Y-%m-%dT%H:%M:%S.%fZ"
    assert response.json()["name"] == data["name"]
    assert response.json()["job"] == data["job"]
    assert datetime.strptime(response.json()["updatedAt"], format), "Dateformat not as expect"
    print("name : OK")
    print("job : OK")
    print("updatedAt : OK")


# Test case to verify that the API endpoint returns the correct headers
def test_api_returns_correct_headers():
    data = {"name": "NGUYEN THE U", "job": "student"}
    response = requests.put("https://reqres.in/api/users/3", data=data)

    response = requests.delete("https://reqres.in/api/users/3")
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


