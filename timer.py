# 导入模块
import time
import tkinter as tk

# 创建一个窗口
window = tk.Tk()
window.title("计时器")

# 创建一个标签显示当前时间
label = tk.Label(window, text="", font=("Arial", 20))
label.pack()

# 定义一个函数更新时间
def update_time():
    # 获取当前时间
    current_time = time.strftime("%H:%M:%S")
    # 更新标签的文本
    label.config(text=current_time)
    # 每隔一秒调用一次函数
    window.after(1000, update_time)

# 调用函数
update_time()

# 运行窗口
window.mainloop()
