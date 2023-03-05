
import os
from os import walk
from PIL import Image
from os.path import join
import tkinter as tk
from tkinter import filedialog




def img_zip(ori_path,new_path):
    all_img_name = [f for f in os.listdir(ori_path) if os.path.isfile(os.path.join(ori_path, f))]  # 圖片名稱
    target_size = 80 * 1024  # 單位B
    quality = 90  # 保留質量，1-100，1 最差，100 最好，
    step = 10  # 降低質量的步長
    for root, dirs, files in walk(ori_path):  # 取得完整檔案路徑
        for f in files:
            fullpath = join(root, f)
            current_img = Image.open(fullpath)  # 初始化當前圖片為原圖
            current_size = os.path.getsize(fullpath)  # 初始化當前大小為原圖大小
            while current_size > target_size and quality > 0:
                for name in all_img_name:
                    current_img.save(new_path + "/" + name, quality=quality,
                                     optimize=True)  # 壓縮新圖片到new_img_path
                    current_img = Image.open(new_path + "/" + name)  # 更新 current_img 為壓縮後的圖片
                    # 更新 current_size 為壓縮後新圖片大小
                    current_size = os.path.getsize(new_path + "/" + name)
                    quality -= step


def main():
    print("請選擇你的原始圖片資料夾\n")
    root = tk.Tk()
    root.withdraw()
    dirpath = filedialog.askdirectory()
    print(dirpath)
    print("請選擇你的輸出圖片資料夾\n")
    output = tk.Tk()
    output.withdraw()
    newpath = filedialog.askdirectory()
    print(newpath)
    img_zip(dirpath, newpath)


#
#
#
if __name__ == '__main__':
    main()

