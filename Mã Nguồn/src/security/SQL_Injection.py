import os
import subprocess

# Mở file log để ghi kết quả vào
def test_sql_injection_db():
    # Xác định đường dẫn đến thư mục logs
    log_folder = "/home/nv/Documents/study/KTLT_final/logs"
    # Tạo thư mục logs nếu chưa tồn tại
    os.makedirs(log_folder, exist_ok=True)
    log_file_path = os.path.join(log_folder, f'sqlmap.log')
    with open(log_file_path, 'w') as log_file:
        # Thực hiện kiểm thử SQL Injection bằng sqlmap và ghi log
        result = subprocess.run(
            ['sqlmap', '-u', 'https://reqres.in/api/users?id=2', '--dbs', "--batch"],
            capture_output=True, text=True)
        log_file.write(result.stdout)
        assert "the back-end DBMS is" not in result.stdout



def test_sql_injection_tables():
    # Xác định đường dẫn đến thư mục logs
    log_folder = "/home/nv/Documents/study/KTLT_final/logs"
    # Tạo thư mục logs nếu chưa tồn tại
    os.makedirs(log_folder, exist_ok=True)
    log_file_path = os.path.join(log_folder, f'sqlmap.log')
    with open(log_file_path, 'w') as log_file:
        # Thực hiện kiểm thử SQL Injection bằng sqlmap và ghi log
        result = subprocess.run(
            ['sqlmap', '-u', 'http://testphp.vulnweb.com/listproducts.php?cat=1', '--tables', "--batch"],
            capture_output=True, text=True)
        log_file.write(result.stdout)
        assert "fetching tables for databases: " not in result.stdout

