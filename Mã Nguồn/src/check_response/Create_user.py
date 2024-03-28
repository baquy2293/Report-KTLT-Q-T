import requests
import datetime

# Test case to verify that the API endpoint URL is correct and accessible
def test_api_endpoint_accessible():
    data = {"name": "NGUYEN VAN A", "job": "student"}
    response = requests.post("https://reqres.in/api/users", data=data)
    assert response.status_code == 201
    print("status-code : OK")


# Test case to verify that the API endpoint returns the expected response format
def test_api_returns_expected_format():
    data = {"name": "NGUYEN VAN A", "job": "student"}
    response = requests.post("https://reqres.in/api/users", data=data)
    assert response.headers["Content-Type"] == "application/json; charset=utf-8"
    print("Content-Type : OK")
# Test case to verify when create user failed
def test_api_returns_correct_status_code_when_wrong_type_data():
    data = {"name": 1, "job": 2}

    response = requests.post("https://reqres.in/api/users", data=data)
    assert response.status_code == 400
    print("Status-code : OK")
# test case expected data
def test_api_returns_expected_data():
    data = {"name": "NGUYEN VAN A", "job": "student"}
    response = requests.post("https://reqres.in/api/users", data=data)

    format = "%Y-%m-%dT%H:%M:%S.%fZ"
    assert response.json()["data"]["name"] == data["name"]
    print("name : OK")
    assert response.json()["data"]["job"] == data["job"]
    print("job : OK")
    assert response.json()["data"]["id"].isdigit() == True
    print("id : OK")
    assert datetime.strptime(response.json()["data"]["createdAt"], format), "Dateformat not as expect"
    print("createdAt : OK")


# Test case to verify that the API endpoint returns the correct headers
def test_api_returns_correct_headers():
    data = {"name": "NGUYEN VAN A", "job": "student"}
    response = requests.post("https://reqres.in/api/users", data=data)
    assert response.headers["Server"] == "cloudflare"
    assert response.headers["X-Powered-By"] == "Express"
    assert response.headers["Access-Control-Allow-Origin"] == "*"
    assert response.headers["Connection"] == "keep-alive"
    assert response.headers["CF-Cache-Status"] == "DYNAMIC"
    print("Server : OK")
    print("X-Powered-By : OK")
    print("Access-Control-Allow-Origin : OK")
    print("Connection : OK")
    print("CF-Cache-Status : OK")



# Test case to verify that the API endpoint returns data in a reasonable amount of time and does not time out
def test_api_returns_data_in_reasonable_time():
    data = {"name": "NGUYEN VAN A", "job": "student"}
    response = requests.post("https://reqres.in/api/users", data=data)
    assert response.elapsed.total_seconds() < 5  # Verify that the request took less than 5 seconds
    print("total_time : OK")


