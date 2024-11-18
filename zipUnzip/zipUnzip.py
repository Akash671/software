# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 16:05:48 2024

@author: akash
"""

import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
import os
import zipfile
import time

def zip_subfolders(parent_folder, progress_label, progress_bar):
    # Function to zip subfolders within a parent folder

    subfolders = [f for f in os.listdir(parent_folder) if os.path.isdir(os.path.join(parent_folder, f))]
    total_subfolders = len(subfolders)
    progress_bar["maximum"] = total_subfolders
    progress = 0

    for subfolder_name in subfolders:
        subfolder_path = os.path.join(parent_folder, subfolder_name)
        zip_file_path = os.path.join(parent_folder, f"{subfolder_name}.zip")

        try:
            with zipfile.ZipFile(zip_file_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
                for root, _, files in os.walk(subfolder_path):
                    for file in files:
                        file_path = os.path.join(root, file)
                        arcname = os.path.relpath(file_path, subfolder_path)
                        zipf.write(file_path, arcname=arcname)

            progress += 1
            progress_label.config(text=f"Zipping... {progress}/{total_subfolders} subfolders ({int(progress/total_subfolders*100)}% done)")
            progress_label.update()
            progress_bar["value"] = progress
            progress_bar.update()

            time.sleep(0.1)  # Add a small delay for smoothness

        except Exception as e:
            progress_label.config(text=f"Error zipping {subfolder_name}: {e}")
            progress_label.update()

def unzip_files(parent_folder, progress_label, progress_bar):
    # Function to unzip files within a parent folder

    zip_files = [f for f in os.listdir(parent_folder) if f.endswith('.zip')]
    total_files = len(zip_files)
    progress_bar["maximum"] = total_files
    progress = 0

    for zip_file_name in zip_files:
        zip_file_path = os.path.join(parent_folder, zip_file_name)
        unzip_folder_path = os.path.join(parent_folder, os.path.splitext(zip_file_name)[0])

        try:
            with zipfile.ZipFile(zip_file_path, 'r') as zipf:
                zipf.extractall(unzip_folder_path)

            progress += 1
            progress_label.config(text=f"Unzipping... {progress}/{total_files} files ({int(progress/total_files*100)}% done)")
            progress_label.update()
            progress_bar["value"] = progress
            progress_bar.update()

            time.sleep(0.1)  # Add a small delay for smoothness

        except Exception as e:
            progress_label.config(text=f"Error unzipping {zip_file_name}: {e}")
            progress_label.update()

def browse_folder_zip():
    folder_path = filedialog.askdirectory()
    if folder_path:
        progress_label.config(text="Zipping subfolders...")
        progress_bar["value"] = 0
        zip_subfolders(folder_path, progress_label, progress_bar)

def browse_folder_unzip():
    folder_path = filedialog.askdirectory()
    if folder_path:
        progress_label.config(text="Unzipping files...")
        progress_bar["value"] = 0
        unzip_files(folder_path, progress_label, progress_bar)

# Create the GUI
root = tk.Tk()
root.title("Zip/Unzip Subfolders developed by Akash")
root.geometry("400x250")

zip_button = tk.Button(root, text="Zip folders", command=browse_folder_zip)
zip_button.pack(pady=10)

unzip_button = tk.Button(root, text="Unzip Files", command=browse_folder_unzip)
unzip_button.pack(pady=10)

progress_label = tk.Label(root, text="")
progress_label.pack(pady=10)

progress_bar = ttk.Progressbar(root, orient="horizontal", length=300, mode="determinate", style="blue.Horizontal.TProgressbar")
progress_bar.pack(pady=10)

root.mainloop()