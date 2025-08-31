import tkinter as tk
import os
import webbrowser
import subprocess

def open_appdata_roaming():
    """Открывает папку AppData\Roaming текущего пользователя"""
    roaming_path = os.path.join(os.environ['APPDATA'])
    os.startfile(roaming_path)

def open_network_usage():
    """Открывает настройки использования сети"""
    subprocess.run('start ms-settings:network-usage', shell=True)

def open_browser_history():
    """Пытается открыть историю браузера"""
    webbrowser.open('chrome://history')
    webbrowser.open('edge://history')

# Создаем главное окно
root = tk.Tk()
root.title("Системные утилиты")
root.geometry("400x300")
root.configure(bg="white")

# Стиль для кнопок
button_style = {
    "font": ("Arial", 12),
    "height": 2,
    "width": 30,
    "bg": "lightblue"
}

# Кнопка 1: AppData\Roaming
btn_appdata = tk.Button(
    root, 
    text="📁 Открыть AppData\\Roaming", 
    command=open_appdata_roaming,
    **button_style
)
btn_appdata.pack(pady=10)

# Кнопка 2: Сетевой трафик
btn_network = tk.Button(
    root,
    text="🌐 Потребление интернета", 
    command=open_network_usage,
    **button_style
)
btn_network.pack(pady=10)

# Кнопка 3: История браузера
btn_history = tk.Button(
    root,
    text="🔍 История браузера", 
    command=open_browser_history,
    **button_style
)
btn_history.pack(pady=10)

# Запускаем главный цикл
root.mainloop()
