import telethon
from telethon import TelegramClient
import python_socks
import asyncio
import tkinter as tk
from tkinter import scrolledtext

# 创建并配置窗体
def create_gui():
    root = tk.Tk()
    root.title("Telegram 清理已注销用户")

    # 设置窗体大小并且不允许用户调整大小
    root.geometry("700x600")  # 增大窗口尺寸以保证控件协调显示
    root.resizable(False, False)

    # 设置标题标签
    tk.Label(root, text="Telegram 清理工具", font=("Arial", 16)).grid(row=0, column=0, columnspan=2, pady=15)

    # 设置输入框的标签和控件
    tk.Label(root, text="API ID").grid(row=1, column=0, padx=10, pady=10, sticky="e")
    api_id_entry = tk.Entry(root, width=45)
    api_id_entry.grid(row=1, column=1, padx=10, pady=10)

    tk.Label(root, text="API Hash").grid(row=2, column=0, padx=10, pady=10, sticky="e")
    api_hash_entry = tk.Entry(root, width=45)
    api_hash_entry.grid(row=2, column=1, padx=10, pady=10)

    tk.Label(root, text="手机号(例+8613012341234  带+号)").grid(row=3, column=0, padx=10, pady=10, sticky="e")
    phone_entry = tk.Entry(root, width=45)
    phone_entry.grid(row=3, column=1, padx=10, pady=10)

    tk.Label(root, text="SOCK5代理地址").grid(row=4, column=0, padx=10, pady=10, sticky="e")
    proxy_addr_entry = tk.Entry(root, width=45)
    proxy_addr_entry.grid(row=4, column=1, padx=10, pady=10)

    tk.Label(root, text="SOCK5代理端口").grid(row=5, column=0, padx=10, pady=10, sticky="e")
    proxy_port_entry = tk.Entry(root, width=45)
    proxy_port_entry.grid(row=5, column=1, padx=10, pady=10)

    # 创建日志输出框
    log_box = scrolledtext.ScrolledText(root, width=80, height=12, wrap=tk.WORD)  # 增加日志框宽度和高度
    log_box.grid(row=6, column=0, columnspan=2, padx=10, pady=15)

    # 设置按钮的回调函数
    def start_cleaning():
        # 获取用户输入的参数
        api_id = api_id_entry.get()
        api_hash = api_hash_entry.get()
        phone_number = phone_entry.get()
        proxy_addr = proxy_addr_entry.get()
        proxy_port = int(proxy_port_entry.get())

        # 在日志框中打印输入的参数
        log_box.insert(tk.END, f"使用的参数：API ID={api_id}, API Hash={api_hash}, 电话号={phone_number}\n")
        log_box.insert(tk.END, f"SOCK5代理地址：{proxy_addr}, SOCK5代理端口：{proxy_port}\n")
        log_box.yview(tk.END)  # 滚动到最后一行

        # 启动清理的异步任务
        asyncio.run(run_cleanup(api_id, api_hash, phone_number, proxy_addr, proxy_port, log_box))

    # 启动清理按钮
    start_button = tk.Button(root, text="开始清理", command=start_cleaning, width=20)
    start_button.grid(row=7, column=0, columnspan=2, pady=20)

    # 运行 GUI 窗体
    root.mainloop()


async def run_cleanup(api_id, api_hash, phone_number, proxy_addr, proxy_port, log_box):
    # 创建 TelegramClient 实例并连接
    my_proxy = {
        'proxy_type': python_socks.ProxyType.SOCKS5,
        'addr': proxy_addr,
        'port': proxy_port,
    }

    client = TelegramClient('delete_session', api_id, api_hash, timeout=10, proxy=(python_socks.ProxyType.SOCKS5, proxy_addr, proxy_port))

    try:
        await client.start(phone=phone_number)
        log_box.insert(tk.END, f"成功登录 Telegram：{phone_number}\n")
        log_box.yview(tk.END)

        # 执行删除已注销用户的对话
        async for dialog in client.iter_dialogs():
            if isinstance(dialog.entity, telethon.tl.types.User):
                log_box.insert(tk.END, f"检查对话: {dialog.name} ({dialog.id}), 是否是已注销用户的对话: {dialog.entity.deleted}\n")
                log_box.yview(tk.END)

                if dialog.entity.deleted:  # 如果用户已注销
                    try:
                        await client.delete_dialog(dialog)
                        log_box.insert(tk.END, f"已删除对话: {dialog.name} ({dialog.id})\n")
                        log_box.yview(tk.END)
                        await asyncio.sleep(1)  # 避免触发速率限制
                    except Exception as e:
                        log_box.insert(tk.END, f"无法删除对话 {dialog.id}: {e}\n")
                        log_box.yview(tk.END)

    except Exception as e:
        log_box.insert(tk.END, f"登录失败: {e}\n")
        log_box.yview(tk.END)


# 启动 GUI
if __name__ == "__main__":
    create_gui()
