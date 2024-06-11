import os
import tkinter as tk
from tkinter import filedialog, messagebox

def extract_filenames(directory, output_file="filenames.txt"):
    """
    提取指定文件夹中的文件名，并将其保存到文本文件中。

    Parameters:
    directory (str): 需要提取文件名的文件夹路径。
    output_file (str): 保存文件名的输出文件路径，默认为 "filenames.txt"
    """
    try:
        files = os.listdir(directory)
        files = [f for f in files if os.path.isfile(os.path.join(directory, f))]
        with open(output_file, "w") as f:
            for filename in files:
                f.write(f"{filename}\n")
        messagebox.showinfo("完成", f"文件名提取完成！已保存到 {output_file}")
    except Exception as e:
        messagebox.showerror("错误", f"提取文件名时出错：{str(e)}")

def select_directory():
    directory = filedialog.askdirectory()
    if directory:
        entry_directory.delete(0, tk.END)
        entry_directory.insert(0, directory)

def start_extraction():
    directory = entry_directory.get()
    output_file = entry_output.get()
    if not directory:
        messagebox.showwarning("警告", "请先选择文件夹")
        return
    extract_filenames(directory, output_file)

# 创建主窗口
root = tk.Tk()
root.title("提取文件名工具")

# 创建并放置标签和输入框
label_directory = tk.Label(root, text="选择文件夹:")
label_directory.grid(row=0, column=0, padx=10, pady=10)
entry_directory = tk.Entry(root, width=50)
entry_directory.grid(row=0, column=1, padx=10, pady=10)
button_browse = tk.Button(root, text="浏览...", command=select_directory)
button_browse.grid(row=0, column=2, padx=10, pady=10)

label_output = tk.Label(root, text="输出文件:")
label_output.grid(row=1, column=0, padx=10, pady=10)
entry_output = tk.Entry(root, width=50)
entry_output.grid(row=1, column=1, padx=10, pady=10)
entry_output.insert(0, "filenames.txt")

# 创建并放置启动按钮
button_start = tk.Button(root, text="开始提取", command=start_extraction)
button_start.grid(row=2, column=0, columnspan=3, pady=20)

# 运行主循环
root.mainloop()
