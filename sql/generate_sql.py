import os
import glob

def generate_sql():
    # 定义基础路径
    base_path = "./static"
    
    # 创建SQL文件
    with open('road_data.sql', 'w', encoding='utf-8') as sql_file:
        # 写入创建数据库和表的SQL语句
        sql_file.write("""
CREATE DATABASE IF NOT EXISTS road_defect;
USE road_defect;

CREATE TABLE IF NOT EXISTS road_images (
    id INT PRIMARY KEY AUTO_INCREMENT,
    base_name VARCHAR(100) NOT NULL,
    image_path VARCHAR(255) NOT NULL,
    coordinate_x FLOAT,
    coordinate_y FLOAT,
    confidence FLOAT,
    UNIQUE KEY unique_image (image_path)
);
        """)
        
        # 遍历所有图片目录
        for dir_path in glob.glob(os.path.join(base_path, "road_images/1st/image_*")) + \
                        glob.glob(os.path.join(base_path, "road_images/2st/packet_*")):

            base_name = os.path.basename(dir_path) # base_name
            image_file = glob.glob(os.path.join(dir_path, "*.jpg"))[0]
            txt_file = glob.glob(os.path.join(dir_path, "*.txt"))[0]

            with open(txt_file, 'r') as f:
                first_line = f.readline().strip()
                y, x, conf = first_line.split(',') # y, x, conf

            relative_path = os.path.relpath(image_file, base_path) # image_path
            sql_file.write(f"INSERT INTO road_images (base_name, image_path, coordinate_x, coordinate_y, confidence) "
                                         f"VALUES ('{base_name}', '{relative_path}', {x}, {y}, {conf});\n")


if __name__ == "__main__":
    generate_sql()