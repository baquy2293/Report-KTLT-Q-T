import requests
import datetime

# Test case to verify that the API endpoint URL is correct and accessible

def test_api_endpoint_accessible():
    response = requests.delete("https://reqres.in/api/users/3")
    assert response.status_code == 204
    print("Status-code : OK")

# Xoá hàm này
def test_api_returns_expected_format():
    response = requests.delete("https://reqres.in/api/users/3")
    assert response.headers.get("Content-Type") == "application/json; charset=utf-8" , "Wrong format response"
    print("Content-Type : OK")


# Xoá hàm này
def test_api_returns_expected_data():
    data = requests.get("https://reqres.in/api/users/3").json()["data"]
    response = requests.delete("https://reqres.in/api/users/3")
    format = "%Y-%m-%dT%H:%M:%S.%fZ"
    try:
        assert response.json()["data"]["name"] == data["name"]
        print("name : OK")
        assert response.json()["data"]["job"] == data["job"]
        print("job : OK")
        assert datetime.strptime(response.json()["updatedAt"], format), "Dateformat not as expect"
    except:
        assert False , "No data response"
# Test case to verify that the API endpoint returns the correct headers
def test_api_returns_correct_headers():
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


