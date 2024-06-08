import wave
import tkinter as tk
from tkinter import filedialog, messagebox

def unhide_file():
    inputfile = filedialog.askopenfilename(title="选择要解除隐藏的文件")
    inputtype = entry_inputtype.get()  # 获取用户输入的文件后缀名

    # 打开藏有其它文件的歌曲文件，读取数据
    with wave.open(str(inputfile), 'rb') as f:
        wav_data = f.readframes(-1)

    # 提取wav_data中的特殊位置数据
    extract_data = bytearray()
    for index in range(0, len(wav_data), 4):
        extract_data += (wav_data[index]).to_bytes(1, byteorder='little')

    # 得到被隐藏的文件的大小
    file_len = int.from_bytes(extract_data[0:3], 'little')

    # 重新生成被隐藏的文件
    output_file = filedialog.asksaveasfilename(title="选择解除隐藏后的文件保存位置", defaultextension=f".{inputtype}", filetypes=[(f"{inputtype.upper()} files", f"*.{inputtype}")])
    if output_file:
        with open(output_file, 'wb') as f:
            f.write(extract_data[3: file_len+3])
        messagebox.showinfo("处理完成", "文件解除隐藏完成！")

# 创建GUI窗口
root = tk.Tk()
root.title("隐藏文件解除")
root.geometry("500x600")

# 添加文本标签和文本框
label_inputtype = tk.Label(root, text="1.请输入要解除隐藏的文件后缀名：")
label_inputtype.pack(pady=5)

entry_inputtype = tk.Entry(root)
entry_inputtype.pack(pady=5)

# 添加按钮
unhide_button = tk.Button(root, text="2.选择要解除隐藏的文件", command=unhide_file)
unhide_button.pack(pady=20)

label_inputtype = tk.Label(root, text="3.等待弹出解除隐藏后的文件另存窗口")
label_inputtype.pack(pady=5)

# Adding text box
text_box = tk.Text(root, height=100, width=200)
text_box.insert(tk.END, "#非GUI版本开源地址：https://github.com/3150601355/HideFileInMusic\n\n#GUI版本开源地址：https://github.com/SodiumSulfate/HideFileInMusic-GUI\n\n#加密原理研究：偶尔有点小迷糊\nBiliBili:https://space.bilibili.com/39665558\n\n#GUI编写：Sodium_Sulfate\nBiliBili:https://space.bilibili.com/495692557\n个人官网：https://sodium.ren")
text_box.pack()

# 运行程序
root.mainloop()
