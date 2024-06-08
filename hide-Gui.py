import tkinter as tk
from tkinter import filedialog
import wave

def hide_data():
    inputfile = entry_inputfile.get()
    inputcar = entry_inputcar.get()
    output_path = entry_output_path.get()

    # 打开要隐藏的文件，读取数据
    with open(str(inputfile), 'rb') as f:
        txt_data = f.read()
        file_len = len(txt_data)
        txt_data = file_len.to_bytes(3, byteorder='little') + txt_data

    # 打开wav格式的歌曲文件，读取数据
    with wave.open(str(inputcar), "rb") as f:
        attrib = f.getparams()  # 获取音频属性
        wav_data = bytearray(f.readframes(-1))

    # 隐藏txt_data中的数据到wav_data中
    for index in range(len(txt_data)):
        wav_data[index * 4] = txt_data[index]

    # 生成新的歌曲文件
    if output_path:
        # 生成新的歌曲文件
        with wave.open(output_path, "wb") as f:
            f.setparams(attrib)  # 设置音频属性
            f.writeframes(wav_data)  # 写入数据
            tk.messagebox.showinfo("成功", "文件已成功隐藏")


# 创建窗口
window = tk.Tk()
window.title("文件隐藏")
window.geometry("500x600")  # Increased height to accommodate the new text box

# 输入要隐藏的文件路径
label_inputfile = tk.Label(window, text="请输入要隐藏的文件路径：")
label_inputfile.pack()
entry_inputfile = tk.Entry(window)
entry_inputfile.pack()
button_browse_inputfile = tk.Button(window, text="浏览",
                                    command=lambda: entry_inputfile.insert(tk.END, filedialog.askopenfilename()))
button_browse_inputfile.pack()

# 输入载体文件路径
label_inputcar = tk.Label(window, text="请输入载体的文件路径：")
label_inputcar.pack()
entry_inputcar = tk.Entry(window)
entry_inputcar.pack()
button_browse_inputcar = tk.Button(window, text="浏览",
                                   command=lambda: entry_inputcar.insert(tk.END, filedialog.askopenfilename()))
button_browse_inputcar.pack()

# 选择输出路径按钮
label_output_path = tk.Label(window, text="请选择输出路径：")
label_output_path.pack()
entry_output_path = tk.Entry(window)
entry_output_path.pack()
button_browse_output_path = tk.Button(window, text="浏览", command=lambda: entry_output_path.insert(tk.END,
                                                                                                    filedialog.asksaveasfilename(
                                                                                                        defaultextension=".wav",
                                                                                                        filetypes=[(
                                                                                                                   "Wave files",
                                                                                                                   "*.wav")])))
button_browse_output_path.pack()

# 执行隐藏操作按钮
button_hide = tk.Button(window, text="执行隐藏操作", command=hide_data)
button_hide.pack()

# Adding text box
text_box = tk.Text(window, height=100, width=200)
text_box.insert(tk.END, "！注意：wav文件不能包含作者名、专辑名、封面等非音频数据\n！注意：wav文件不能包含作者名、专辑名、封面等非音频数据\n\n！注意：wav文件大小应大于要隐藏的文件的4倍以上\n例：要隐藏的文件大小为1MB，则WAV文件须大于4MB\n\n#非GUI版本开源地址：https://github.com/3150601355/HideFileInMusic\n\n#GUI版本开源地址：https://github.com/SodiumSulfate/HideFileInMusic-GUI\n\n#加密原理研究：偶尔有点小迷糊\nBiliBili:https://space.bilibili.com/39665558\n\n#GUI编写：Sodium_Sulfate\nBiliBili:https://space.bilibili.com/495692557\n个人官网：https://sodium.ren")
text_box.pack()

window.mainloop()
