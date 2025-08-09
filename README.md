-----

# 批量音频提取器 GUI

一个使用 Python 和 Tkinter 构建的简单图形用户界面 (GUI) 工具，用于从视频和媒体文件中批量提取音频。它将提取的音频保存为 `.m4a` 格式，并提供有损 (AAC) 和无损 (ALAC) 两种编码器选项。

-----

## 功能特点

  * **易用界面**: 简单直观的图形界面，方便选择文件和选项。
  * **批量处理**: 从所选文件夹中的所有有效媒体文件中提取音频。
  * **编码器选择**: 可在高质量的无损 `ALAC` 编码器和高效、文件更小的 `AAC` 编码器之间进行选择。
  * **有序输出**: 自动为提取的音频文件创建一个新的子文件夹（例如 `YourFolder_aac`），保持源目录整洁。
  * **跨平台**: 可在 Windows、macOS 和 Linux 上运行。
  * **便捷操作**: 转换过程完成后，会自动打开输出文件夹。

-----

## 前置要求

在运行此脚本之前，您必须在系统上安装以下软件：

1.  **Python 3**: 该脚本使用 Python 3 编写。您可以从 [python.org](https://www.python.org/) 下载。
2.  **FFmpeg**: 这是处理媒体文件的关键依赖项。
      * 您必须从官方网站下载并安装 FFmpeg: [ffmpeg.org](https://ffmpeg.org/download.html)。
      * **重要提示**: 请确保 `ffmpeg` 和 `ffprobe` 的可执行文件路径已添加到您系统的 **PATH** 环境变量中，以便脚本可以从命令行调用它们。

-----

## 如何使用

1.  **保存脚本**: 将提供的代码保存为一个 Python 文件（例如 `audio_extractor.py`）。
2.  **从终端运行**: 打开终端或命令提示符，切换到您保存文件的目录。使用以下命令运行脚本：
    ```bash
    python audio_extractor.py
    ```
3.  **选择文件夹**: 点击 **浏览... (Browse...)** 按钮，选择包含您要处理的视频或媒体文件的文件夹。
4.  **选择编码器**:
      * 选择 **AAC** 可生成较小的有损文件（适用于大多数情况）。
      * 选择 **ALAC** 可生成较大的无损文件（适合存档）。
5.  **开始转换**: 点击 **开始转换 (Start Conversion)** 按钮。此时会弹出一个确认对话框，点击“是”即可开始。
6.  **完成**: 等待处理结束。程序会显示一个完成通知，并且包含新 `.m4a` 音频文件的文件夹将自动打开。

-----


# Bulk Audio Extractor GUI

A simple graphical user interface (GUI) tool built with Python and Tkinter to batch extract audio from video and media files. It saves the extracted audio in `.m4a` format, offering a choice between lossy (AAC) and lossless (ALAC) codecs.

-----

## Features

  * **Easy-to-use Interface**: Simple and intuitive GUI for selecting files and options.
  * **Batch Processing**: Extracts audio from all valid media files within a selected folder.
  * **Codec Selection**: Choose between high-quality lossless `ALAC` or efficient, smaller `AAC` codecs.
  * **Organized Output**: Automatically creates a new subfolder (e.g., `YourFolder_aac`) for the extracted audio files, keeping your source directory clean.
  * **Cross-Platform**: Works on Windows, macOS, and Linux.
  * **Convenience**: Automatically opens the output folder once the conversion process is complete.

-----

## Prerequisites

Before running this script, you must have the following installed on your system:

1.  **Python 3**: The script is written in Python 3. You can download it from [python.org](https://www.python.org/).
2.  **FFmpeg**: This is a crucial dependency for processing media files.
      * You must download and install FFmpeg from the official website: [ffmpeg.org](https://ffmpeg.org/download.html).
      * **Important**: Ensure that the `ffmpeg` and `ffprobe` executables are included in your system's **PATH** environment variable so the script can access them from the command line.

-----

## How to Use

1.  **Save the Script**: Save the provided code as a Python file (e.g., `audio_extractor.py`).
2.  **Run from Terminal**: Open a terminal or command prompt and navigate to the directory where you saved the file. Run the script using the command:
    ```bash
    python audio_extractor.py
    ```
3.  **Select Folder**: Click the **Browse...** button to choose the folder containing the video or media files you want to process.
4.  **Choose Codec**:
      * Select **AAC** for smaller, lossy files (good for most use cases).
      * Select **ALAC** for larger, lossless files (ideal for archival purposes).
5.  **Start Conversion**: Click the **Start Conversion** button. A confirmation dialog will appear. Click "Yes" to begin.
6.  **Done**: Wait for the process to finish. A notification will appear, and the folder containing your new `.m4a` audio files will open automatically.

-----

