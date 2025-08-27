import os
import shutil

source_dir = 'images'
dest_dir = 'images/pub_img'

# 确保目标文件夹存在
os.makedirs(dest_dir, exist_ok=True)

# 移动所有以picsum-开头的.jpg文件
for filename in os.listdir(source_dir):
    if filename.startswith('picsum-') and filename.endswith('.jpg'):
        src_path = os.path.join(source_dir, filename)
        dest_path = os.path.join(dest_dir, filename)
        shutil.move(src_path, dest_path)
        print(f"Moved: {filename}")

print("所有图片移动完成")