import requests

# Trường hợp kiểm thử để xác minh rằng URL điểm cuối API là chính xác và có thể truy cập được
def test_api_endpoint_accessible():
    response = requests.get("https://reqres.in/api/users")
    print("Status-code : OK")
    assert response.status_code == 200

# Trường hợp kiểm thử để xác minh rằng điểm cuối API trả về định dạng phản hồi dự kiến
def test_api_returns_expected_format():
    response = requests.get("https://reqres.in/api/users")
    assert response.headers["Content-Type"] == "application/json; charset=utf-8"
    print("Content-Type : OK")
# Trường hợp kiểm thử để xác minh rằng điểm cuối API trả về dữ liệu dự kiến theo tài liệu API
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

# Trường hợp kiểm thử để xác minh rằng điểm cuối API trả về mã trạng thái HTTP chính xác
def test_api_returns_correct_status_code_when_user_single_not_found():
    response = requests.get("https://reqres.in/api/users/23")
    assert response.status_code == 404
    print("Error-status : OK")

# Trường hợp thử nghiệm để xác minh rằng điểm cuối API trả về tiêu đề chính xác
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
# Trường hợp kiểm thử để xác minh rằng điểm cuối API xử lý lỗi và trả về phản hồi lỗi thích hợp cho các yêu cầu không hợp lệ
def test_api_handles_errors():
    response = requests.get("https://reqres.in/api/users?page=99")
    assert response.status_code == 200
    assert response.json()["data"] == []
    print("Status-code : OK")

# Trường hợp thử nghiệm để xác minh rằng điểm cuối API trả về dữ liệu chính xác cho các tham số truy vấn khác nhau
def test_api_returns_correct_data_for_query_params_page():
    response = requests.get("https://reqres.in/api/users?page=2")
    assert response.json()["page"] == 2
    print("page : OK")
    assert len(response.json()["data"]) == response.json()["per_page"]
    print("per_page : OK")


# Trường hợp kiểm thử để xác minh rằng điểm cuối API trả về dữ liệu trong khoảng thời gian hợp lý và không hết thời gian chờ
def test_api_returns_data_in_reasonable_time():
    response = requests.get("https://reqres.in/api/users?delay=3")
    assert response.elapsed.total_seconds() < 5  # Verify that the request took less than 5 seconds
    print("total_time : OK")
