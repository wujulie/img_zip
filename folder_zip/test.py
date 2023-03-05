import os
import glob
import cv2
import tkinter as tk
from tkinter import filedialog



def main():
    print("請選擇你的原始圖片資料夾\n")
    root = tk.Tk()
    root.withdraw()
    dirpath = filedialog.askdirectory()
    full_path = glob.glob(os.path.join(dirpath, "*jpg"))
    print("請選擇你的輸出圖片資料夾\n")
    all_img_name = [f for f in os.listdir(dirpath) if os.path.isfile(os.path.join(dirpath, f))]  # 圖片名稱
    output = tk.Tk()
    output.withdraw()
    newpath = filedialog.askdirectory()
    print(newpath)
    for path, img_name in zip(full_path, all_img_name):
        img = cv2.imread(path)
        cv2.imwrite(newpath + "\\" + img_name, img, [cv2.IMWRITE_JPEG_QUALITY, 30])

if __name__ == '__main__':
    main()#使用opencv壓縮
