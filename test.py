import tkinter as tk
import os
import webbrowser
import subprocess

def open_appdata_roaming():
    """Открывает папку AppData\Roaming текущего пользователя"""
    roaming_path = os.environ['APPDATA']
    os.startfile(roaming_path)

def open_network_usage():
    """Открывает использование данных в настройках Windows"""
    # Точный путь к использованию данных
    subprocess.run('start ms-settings:datausage', shell=True)

def open_browser_history():
    """Открывает историю в браузере по умолчанию"""
    # Просто открываем историю - браузер по умолчанию сам обработает
    webbrowser.open('https://history')  # Универсальный способ

# Создаем главное окно
root = tk.Tk()
root.title("System Utilities")
root.geometry("500x400")
root.configure(bg="white")

# Стиль для кнопок
button_style = {
    "font": ("Arial", 11),
    "height": 2,
    "width": 35,
    "bg": "lightblue",
    "wraplength": 300
}

# Кнопка 1: AppData\Roaming
btn_appdata = tk.Button(
    root, 
    text="Open AppData\\Roaming", 
    command=open_appdata_roaming,
    **button_style
)
btn_appdata.pack(pady=15)

# Кнопка 2: Использование данных
btn_network = tk.Button(
    root,
    text="Open Data Usage", 
    command=open_network_usage,
    **button_style
)
btn_network.pack(pady=15)

# Кнопка 3: История браузера
btn_history = tk.Button(
    root,
    text="Open Browser History", 
    command=open_browser_history,
    **button_style
)
btn_history.pack(pady=15)

# Запускаем главный цикл
root.mainloop()
