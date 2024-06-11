import os
import tkinter as tk
from tkinter import filedialog, messagebox


def rename_files(directory, prefix="file_", new_extension=None):
    """
    批量重命名指定文件夹中的文件，并可选择修改文件后缀。

    Parameters:
    directory (str): 需要重命名的文件夹路径。
    prefix (str): 文件重命名的前缀，默认为 "file_"
    new_extension (str): 新的文件后缀，默认为 None 表示不修改后缀
    """
    try:
        files = os.listdir(directory)
        files = [f for f in files if os.path.isfile(
            os.path.join(directory, f))]
        print(f"找到文件: {files}")

        for i, filename in enumerate(files):
            extension = os.path.splitext(
                filename)[1] if new_extension is None else f".{new_extension}"
            new_name = f"{prefix}{i + 1}{extension}"
            old_path = os.path.join(directory, filename)
            new_path = os.path.join(directory, new_name)
            os.rename(old_path, new_path)
            print(f"{filename} 重命名为 {new_name}")

        messagebox.showinfo("完成", "文件重命名完成！")
    except Exception as e:
        print(f"发生错误: {e}")
        messagebox.showerror("错误", f"重命名文件时出错：{str(e)}")


def select_directory():
    directory = filedialog.askdirectory()
    if directory:
        entry_directory.delete(0, tk.END)
        entry_directory.insert(0, directory)
        print(f"选择文件夹: {directory}")


def start_renaming():
    directory = entry_directory.get()
    prefix = entry_prefix.get()
    new_extension = entry_extension.get()
    if not directory:
        print("警告: 未选择文件夹")
        messagebox.showwarning("警告", "请先选择文件夹")
        return
    if new_extension == "":
        new_extension = None
    print(
        f"开始重命名: {directory} with prefix: {prefix} and new extension: {new_extension}")
    rename_files(directory, prefix, new_extension)


# 创建主窗口
root = tk.Tk()
root.title("批量重命名工具")

# 创建并放置标签和输入框
label_directory = tk.Label(root, text="选择文件夹:")
label_directory.grid(row=0, column=0, padx=10, pady=10)
entry_directory = tk.Entry(root, width=50)
entry_directory.grid(row=0, column=1, padx=10, pady=10)
button_browse = tk.Button(root, text="浏览...", command=select_directory)
button_browse.grid(row=0, column=2, padx=10, pady=10)

label_prefix = tk.Label(root, text="文件名前缀:")
label_prefix.grid(row=1, column=0, padx=10, pady=10)
entry_prefix = tk.Entry(root, width=50)
entry_prefix.grid(row=1, column=1, padx=10, pady=10)
entry_prefix.insert(0, "file_")

label_extension = tk.Label(root, text="新的文件后缀 (可选):")
label_extension.grid(row=2, column=0, padx=10, pady=10)
entry_extension = tk.Entry(root, width=50)
entry_extension.grid(row=2, column=1, padx=10, pady=10)

# 创建并放置启动按钮
button_start = tk.Button(root, text="开始重命名", command=start_renaming)
button_start.grid(row=3, column=0, columnspan=3, pady=20)

# 运行主循环
try:
    print("开始主循环")
    root.mainloop()
    print("主循环结束")
except Exception as e:
    print(f"运行时出错：{e}")
