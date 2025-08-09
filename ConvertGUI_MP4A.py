import os
import sys
import subprocess
import tkinter as tk
from tkinter import filedialog, messagebox

# --- NEW: Function to open a folder in the default file explorer ---
def open_folder(path):
    """
    Opens the specified folder in the default file explorer.
    Works on Windows, macOS, and Linux.
    """
    if sys.platform == "win32":
        # On Windows, use os.startfile
        os.startfile(os.path.realpath(path))
    elif sys.platform == "darwin":
        # On macOS, use the 'open' command
        subprocess.run(["open", path])
    else:
        # On Linux and other Unix-like systems, use 'xdg-open'
        subprocess.run(["xdg-open", path])

def is_media_file(file_path):
    # Use ffprobe to check if it is a media file
    cmd = [
        "ffprobe",
        "-v", "error",
        "-show_entries", "format=format_name",
        "-of", "default=noprint_wrappers=1:nokey=1",
        file_path
    ]
    try:
        result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True)
        return bool(result.stdout.strip())
    except (subprocess.CalledProcessError, FileNotFoundError):
        return False

def extract_audio_gui(input_folder, codec):
    base_folder_name = os.path.basename(os.path.normpath(input_folder))
    output_folder_name = f"{base_folder_name}_{codec}"
    output_folder_path = os.path.join(input_folder, output_folder_name)
    os.makedirs(output_folder_path, exist_ok=True)

    files = os.listdir(input_folder)
    
    media_files = [
        f for f in files 
        if os.path.isfile(os.path.join(input_folder, f)) and is_media_file(os.path.join(input_folder, f))
    ]

    if not media_files:
        messagebox.showinfo("Info", "No valid media files found in the selected folder!")
        return

    for filename in media_files:
        input_path = os.path.join(input_folder, filename)
        output_filename = os.path.splitext(filename)[0] + ".m4a"
        output_path = os.path.join(output_folder_path, output_filename)

        print(f"Processing: {filename} → {output_folder_name}/{output_filename}")
        command = [
            "ffmpeg", "-i", input_path, "-vn",
            "-acodec", codec, 
            "-y",
            output_path
        ]
        subprocess.run(command, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)

    messagebox.showinfo("Complete", f"All conversions finished. Files are saved to:\n{output_folder_path}")
    
    # --- NEW: Open the output folder after conversion ---
    open_folder(output_folder_path)

def choose_folder():
    folder_selected = filedialog.askdirectory()
    if folder_selected:
        folder_path_var.set(folder_selected)

def start_conversion():
    folder = folder_path_var.get()
    codec = codec_var.get()
    if not folder:
        messagebox.showwarning("Warning", "Please select an input folder!")
        return

    # --- NEW: Ask for confirmation before starting ---
    confirm = messagebox.askyesno(
        "Confirm Conversion",
        f"This will extract audio from all media files in:\n\n{folder}\n\nDo you want to proceed?"
    )

    # If the user clicks "No", the function will stop here
    if not confirm:
        return
        
    extract_audio_gui(folder, codec)

# --- GUI Setup ---
root = tk.Tk()
root.title("Bulk Audio Extractor (M4A)")

folder_path_var = tk.StringVar()
codec_var = tk.StringVar(value="aac")

# --- Widgets ---
main_frame = tk.Frame(root, padx=10, pady=10)
main_frame.pack(fill="both", expand=True)

# Folder Selection Row
tk.Label(main_frame, text="Select Folder:").grid(row=0, column=0, padx=5, pady=8, sticky="e")
folder_entry = tk.Entry(main_frame, textvariable=folder_path_var, width=50)
folder_entry.grid(row=0, column=1, padx=5, pady=8)
tk.Button(main_frame, text="Browse...", command=choose_folder).grid(row=0, column=2, padx=5, pady=8)

# Codec Selection Row
tk.Label(main_frame, text="Select Codec:").grid(row=1, column=0, padx=5, pady=8, sticky="e")
codec_frame = tk.Frame(main_frame)
codec_frame.grid(row=1, column=1, padx=5, pady=8, sticky="w")
tk.Radiobutton(codec_frame, text="AAC (Lossy, Smaller File)", variable=codec_var, value="aac").pack(side="left", padx=5)
tk.Radiobutton(codec_frame, text="ALAC (Lossless, Larger File)", variable=codec_var, value="alac").pack(side="left", padx=10)

# Start Button Row
start_btn = tk.Button(main_frame, text="Start Conversion", command=start_conversion, font=("Helvetica", 12, "bold"), bg="#4CAF50", fg="white")
start_btn.grid(row=2, column=0, columnspan=3, pady=20, ipadx=10, ipady=5)

# --- Run GUI ---
root.mainloop()