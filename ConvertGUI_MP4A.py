import os
import subprocess
import tkinter as tk
from tkinter import filedialog, messagebox

FFMPEG_PATH = "/opt/homebrew/bin/ffmpeg"
FFPROBE_PATH = "/opt/homebrew/bin/ffprobe"

def is_media_file(file_path):
    # 用 ffprobe 检查是否为音视频文件
    cmd = [
        FFPROBE_PATH,
        "-v", "error",
        "-show_entries", "format=format_name",
        "-of", "default=noprint_wrappers=1:nokey=1",
        file_path
    ]
    result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    return bool(result.stdout.strip())

def extract_audio_gui(input_folder, codec):
    base_folder_name = os.path.basename(os.path.normpath(input_folder))
    output_folder_name = f"{base_folder_name}_{codec}"
    output_folder_path = os.path.join(input_folder, output_folder_name)
    os.makedirs(output_folder_path, exist_ok=True)

    files = os.listdir(input_folder)
    media_files = [f for f in files if is_media_file(os.path.join(input_folder, f))]

    if not media_files:
        messagebox.showinfo("提示", "指定文件夹内没有有效的音视频文件！")
        return

    for filename in media_files:
        input_path = os.path.join(input_folder, filename)
        output_filename = os.path.splitext(filename)[0] + ".m4a"
        output_path = os.path.join(output_folder_path, output_filename)

        print(f"正在处理: {filename} → {output_folder_name}/{output_filename}")
        command = [
            FFMPEG_PATH, "-i", input_path, "-vn",
            "-acodec", codec, output_path
        ]
        subprocess.run(command, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)

    messagebox.showinfo("完成", f"全部转换完成，文件已保存到：\n{output_folder_path}")

def choose_folder():
    folder_selected = filedialog.askdirectory()
    if folder_selected:
        folder_path_var.set(folder_selected)

def start_conversion():
    folder = folder_path_var.get()
    codec = codec_var.get()
    if not folder:
        messagebox.showwarning("警告", "请选择输入文件夹！")
        return
    extract_audio_gui(folder, codec)

root = tk.Tk()
root.title("将音视频文件以aac或alac编码后保存为m4a格式")

folder_path_var = tk.StringVar()
codec_var = tk.StringVar(value="aac")

tk.Label(root, text="选择文件夹：").grid(row=0, column=0, padx=5, pady=5, sticky="e")
folder_entry = tk.Entry(root, textvariable=folder_path_var, width=40)
folder_entry.grid(row=0, column=1, padx=5, pady=5)
tk.Button(root, text="浏览", command=choose_folder).grid(row=0, column=2, padx=5, pady=5)

tk.Label(root, text="选择编码：").grid(row=1, column=0, padx=5, pady=5, sticky="e")
codec_frame = tk.Frame(root)
codec_frame.grid(row=1, column=1, padx=5, pady=5, sticky="w")

tk.Radiobutton(codec_frame, text="AAC", variable=codec_var, value="aac").pack(side="left", padx=10)
tk.Radiobutton(codec_frame, text="ALAC", variable=codec_var, value="alac").pack(side="left", padx=10)

start_btn = tk.Button(root, text="开始转换", command=start_conversion, width=20)
start_btn.grid(row=2, column=0, columnspan=3, pady=15)

root.mainloop()
