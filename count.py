from PIL import Image

def calculate_color_areas(image_path):
    # 打開圖片
    img = Image.open(image_path)

    # 獲取圖片的RGB數據
    rgb_data = img.getdata()

    # 初始化一個字典來存儲每種顏色的像素數量
    color_count = {}

    # 遍歷每個像素
    for pixel in rgb_data:
        if pixel in color_count:
            color_count[pixel] += 1
        else:
            color_count[pixel] = 1

    # 打印每種顏色的像素數量
    for color, count in color_count.items():
        print(f"顏色 {color} 佔據面積: {count} 像素")

src = 'src\\'
img = 'kaido.jpg'

# 執行範例
calculate_color_areas(src+img)
