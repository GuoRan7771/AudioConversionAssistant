import os
import subprocess

#将编码格式改为AAC而不是ALAC 只需要将-acodec", "alac修改为-acodec aac

FFMPEG_PATH = "/opt/homebrew/bin/ffmpeg"

def extract_audio_to_alac(input_folder):
    base_folder_name = os.path.basename(os.path.normpath(input_folder))
    output_folder_name = f"{base_folder_name}_alac"
    output_folder_path = os.path.join(input_folder, output_folder_name)

    os.makedirs(output_folder_path, exist_ok=True)

    for filename in os.listdir(input_folder):
        if filename.lower().endswith(".mp4"):
            input_path = os.path.join(input_folder, filename)
            output_filename = os.path.splitext(filename)[0] + ".m4a"
            output_path = os.path.join(output_folder_path, output_filename)

            print(f"正在处理: {filename} → {output_folder_name}/{output_filename}")
            command = [
                FFMPEG_PATH, "-i", input_path, "-vn",
                "-acodec", "alac", output_path###
            ]
            subprocess.run(command, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)

    print(f"全部处理完成，文件已保存到: {output_folder_path}")

if __name__ == "__main__":
    folder = input("请输入视频文件夹路径: ").strip()
    extract_audio_to_alac(folder)
