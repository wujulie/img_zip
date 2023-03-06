import os
import glob
import tkinter as tk
from tkinter import filedialog
from PIL import Image




def img_zip(source_folder,target_folder):
    target_size = 80*1024 # 單位B
    quality =90  # 保留質量，1-100，1 最差，100 最好，
    step = 10  # 降低質量的步長
    for filename in os.listdir(source_folder):
        if filename.endswith(".jpg") or filename.endswith(".png") or filename.endswith(".jpeg"):
         current_img = Image.open(os.path.join(source_folder, filename))
         current_size = os.path.getsize(os.path.join(source_folder, filename))  # 初始化當前大小為原圖大小
        while current_size > target_size and quality > 0:
            current_img.save(os.path.join(target_folder, filename),
                             optimize=True,quality=quality)
                          # 壓縮新圖片到new_img_path
            current_img = Image.open(os.path.join(source_folder, filename))  # 更新 current_img 為壓縮後的圖片
            # 更新 current_size 為壓縮後新圖片大小
            current_size = os.path.getsize(os.path.join(source_folder, filename))
            quality -= step
            continue
        current_img.save(os.path.join(target_folder, filename))
        print(filename + " 已壓縮")


def main():
    print("請選擇你的原始圖片資料夾\n")
    root = tk.Tk()
    root.withdraw()
    source_folder = filedialog.askdirectory()
    print("請選擇你的輸出圖片資料夾\n")
    output = tk.Tk()
    output.withdraw()
    target_folder  = filedialog.askdirectory()
    print(target_folder)
    img_zip(source_folder,target_folder)



if __name__ == '__main__':
    main()
