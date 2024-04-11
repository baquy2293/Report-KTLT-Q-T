import requests
import threading


def test_dos_attack():
    # Thiết lập số lượng yêu cầu tối đa
    MAX_REQUESTS = 10000

    # Tạo một đối tượng Event để theo dõi kết thúc của tất cả các luồng
    event = threading.Event()

    # Địa chỉ URL của API cần kiểm tra
    api_url = 'ttps://reqres.in/api/users'

    # Hàm thực hiện yêu cầu tới API
    def make_request():
        try:
            requests.get(api_url)
        except requests.exceptions.RequestException:
            pass

        # Báo cáo rằng một yêu cầu đã hoàn thành
        event.set()

    # Khởi tạo một danh sách các luồng để gửi yêu cầu tới API
    threads = []
    for i in range(MAX_REQUESTS):
        t = threading.Thread(target=make_request)
        t.start()
        threads.append(t)

    # Chờ tất cả các luồng hoàn thành
    event.wait()

    # Kiểm tra xem tất cả các yêu cầu đã được xử lý thành công hay không
    assert all([t.is_alive() == False for t in threads])