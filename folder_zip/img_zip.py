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
    print("你的原始路徑為:",dirpath)
    IMG_EXTS = (".jpg", ".jpeg", ".png" ,".JPG")
    full_path = [file for file in glob.glob(dirpath +'\\*') if file.endswith(IMG_EXTS)]
    print("請選擇你的輸出圖片資料夾\n")
    all_img_name = [f for f in os.listdir(dirpath) if os.path.isfile(os.path.join(dirpath, f))]  # 圖片名稱
    output = tk.Tk()
    output.withdraw()
    newpath = filedialog.askdirectory()
    print("你的輸出路徑為:", newpath)
    for path, img_name in zip(full_path, all_img_name):
        img = cv2.imread(path)
        cv2.imwrite(newpath + "\\" + img_name, img, [cv2.IMWRITE_JPEG_QUALITY, 30])
        print(img_name + " 已壓縮")

if __name__ == '__main__':
    main()
    input("處理完成!!!按下Enter即可結束!!!")