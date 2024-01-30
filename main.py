import os
import shutil
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


source_folder = r'C:\Users\Oryza-JSC\Downloads\lfw\lfw'
target_folder = r'C:\Users\Oryza-JSC\Downloads\lfw\lfw\collect'

# Lấy danh sách tất cả các folder trong thư mục nguồn
folders = os.listdir(source_folder)

# Lấy 500 folder đầu tiên
selected_folders = folders[:500]

# Tạo thư mục đích nếu chưa tồn tại
os.makedirs(target_folder, exist_ok=True)

# Gộp hình từ các folder đã chọn vào thư mục đích
for folder in selected_folders:
    folder_path = os.path.join(source_folder, folder)
    image_files = os.listdir(folder_path)
    for image_file in image_files:
        source_path = os.path.join(folder_path, image_file)
        target_path = os.path.join(target_folder, image_file)
        shutil.copy(source_path, target_path)

print("Đã gộp hình thành công!")
