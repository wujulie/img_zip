from PIL import Image
import os
import tkinter as tk
from tkinter import filedialog

def main():
    # 使用image壓縮
    # 指定A和B資料夾的路徑
    print("請選擇你的原始圖片資料夾\n")
    root = tk.Tk()
    root.withdraw()
    source_folder = filedialog.askdirectory()
    print("你的原始路徑為:", source_folder)
    print("請選擇你的輸出圖片資料夾\n")
    output = tk.Tk()
    output.withdraw()
    target_folder = filedialog.askdirectory()
    print("你的輸出路徑為:", target_folder)
    # 設定圖片壓縮的目標大小（以KB為單位）
    target_size = 50
    # 迭代A資料夾中的所有圖片
    for filename in os.listdir(source_folder):
        # 確定檔案是圖片
        if filename.endswith(".jpg") or filename.endswith(".png") or filename.endswith(".jpeg"):
            # 開啟圖片
            img = Image.open(os.path.join(source_folder, filename))
            # 計算目前圖片大小
            current_size = os.path.getsize(os.path.join(source_folder, filename)) / 1024  # 以KB為單位
            # 如果目前圖片大小已經小於等於目標大小，則不需要壓縮
            if current_size <= target_size:
                img.save(os.path.join(target_folder, filename))
                continue
            img.save(os.path.join(target_folder, filename), optimize=True, quality=30)
            print(filename + " 已壓縮")
if __name__ == '__main__':
    main()
    input("處理完成!!!按下Enter即可結束!!!")