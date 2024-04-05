import os
import subprocess

import os

# Đường dẫn đến thư mục bạn muốn mở
# folder_path = "../GroupTQ/Source/logs"
#
# try:
#     # Mở thư mục
#     os.chdir(folder_path)
#     print("Thư mục đã được mở:", os.getcwd())
# except FileNotFoundError:
#     print("Thư mục không tồn tại.")
# except PermissionError:
#     print("Bạn không có quyền truy cập vào thư mục.")
log_folder = "Source/logs"
os.makedirs(log_folder, exist_ok=True)

log_file_path = os.path.join(log_folder, f'sqlmap.log')
print(log_file_path)
with open(log_file_path, 'w') as log_file:
    print()

#
# # Mở file log để ghi kết quả vào
# def test_sql_injection_db():
#     # Xác định đường dẫn đến thư mục logs
#     log_folder = "Mã Nguồn/logs"
#     # Tạo thư mục logs nếu chưa tồn tại
#     os.makedirs(log_folder, exist_ok=True)
#     log_file_path = os.path.join(log_folder, f'sqlmap.log')
#     with open(log_file_path, 'w') as log_file:
#         # Thực hiện kiểm thử SQL Injection bằng sqlmap và ghi log
#         result = subprocess.run(
#             ['sqlmap', '-u', 'https://reqres.in/api/users?id=2', '--dbs', "--batch"],
#             capture_output=True, text=True)
#         log_file.write(result.stdout)
#         assert "the back-end DBMS is" not in result.stdout
#
#
#
# def test_sql_injection_tables():
#     # Xác định đường dẫn đến thư mục logs
#     log_folder = "Mã Nguồn/logs"
#
#
#     # Tạo thư mục logs nếu chưa tồn tại
#     os.makedirs(log_folder, exist_ok=True)
#     log_file_path = os.path.join(log_folder, f'sqlmap.log')
#     with open(log_file_path, 'w') as log_file:
#         # Thực hiện kiểm thử SQL Injection bằng sqlmap và ghi log
#         result = subprocess.run(
#             ['sqlmap', '-u', 'http://testphp.vulnweb.com/listproducts.php?cat=1', '--tables', "--batch"],
#             capture_output=True, text=True)
#         log_file.write(result.stdout)
#         assert "fetching tables for databases: " not in result.stdout
#
