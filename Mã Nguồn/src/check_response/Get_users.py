import requests

# Test case to verify that the API endpoint URL is correct and accessible
def test_api_endpoint_accessible():
    response = requests.get("https://reqres.in/api/users")
    print("Status-code : OK")
    assert response.status_code == 200

# Test case to verify that the API endpoint returns the expected response format
def test_api_returns_expected_format():
    response = requests.get("https://reqres.in/api/users")
    assert response.headers["Content-Type"] == "application/json; charset=utf-8"
    print("Content-Type : OK")
# Test case to verify that the API endpoint returns the expected data according to the API documentation
def test_api_returns_expected_data():
    response = requests.get("https://reqres.in/api/users/2")
    data_expect = {
            "id": 2,
            "email": "janet.weaver@reqres.in",
            "first_name": "Janet",
            "last_name": "Weaver",
            "avatar": "https://reqres.in/img/faces/2-image.jpg"
        }
    support_expect = {
        "url": "https://reqres.in/#support-heading",
        "text": "To keep ReqRes free, contributions towards server costs are appreciated!"
    }
    assert response.json()['support'] == support_expect
    print("support : OK")
    assert response.json()["data"] == data_expect
    print("data : OK")

# Test case to verify that the API endpoint returns the correct HTTP status code
def test_api_returns_correct_status_code_when_user_single_not_found():
    response = requests.get("https://reqres.in/api/users/23")
    assert response.status_code == 404
    print("Error-status : OK")

# Test case to verify that the API endpoint returns the correct headers
def test_api_returns_correct_headers():
    response = requests.get("https://reqres.in/api/users")
    assert response.headers["Cache-Control"] == "max-age=14400"
    print("Cache-Control : OK")
    assert response.headers["Server"] == "cloudflare"
    print("Server : OKE")
    assert response.headers["X-Powered-By"] == "Express"
    print("X-Powered-By : OK")
    assert response.headers["Content-Encoding"] == "gzip"
    print("Content-Encoding : OK")
    assert response.headers["Access-Control-Allow-Origin"] == "*"
    print("Access-Control-Allow-Origin : OK")
    assert response.headers["Connection"] == "keep-alive"
    print("Connection : OK")
# Test case to verify that the API endpoint handles errors and returns appropriate error responses for invalid requests
def test_api_handles_errors():
    response = requests.get("https://reqres.in/api/users?page=99")
    assert response.status_code == 200
    assert response.json()["data"] == []
    print("Status-code : OK")

# Test case to verify that the API endpoint returns the correct data for different query parameters
def test_api_returns_correct_data_for_query_params_page():
    response = requests.get("https://reqres.in/api/users?page=2")
    assert response.json()["page"] == 2
    print("page : OK")
    assert len(response.json()["data"]) == response.json()["per_page"]
    print("per_page : OK")


# Test case to verify that the API endpoint returns data in a reasonable amount of time and does not time out
def test_api_returns_data_in_reasonable_time():
    response = requests.get("https://reqres.in/api/users?delay=3")
    assert response.elapsed.total_seconds() < 5  # Verify that the request took less than 5 seconds
    print("total_time : OK")
