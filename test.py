import tkinter as tk
import os
import webbrowser
import subprocess
import shutil

def open_appdata_roaming():
    """Открывает папку AppData\Roaming текущего пользователя"""
    roaming_path = os.environ['APPDATA']
    os.startfile(roaming_path)

def open_network_usage():
    """Открывает использование данных в настройках Windows"""
    subprocess.run('start ms-settings:datausage', shell=True)

def open_browser_history():
    """Определяет браузер по умолчанию и открывает историю"""
    # Получаем браузер по умолчанию
    default_browser = webbrowser.get().name.lower()
    
    # Определяем команду в зависимости от браузера
    if 'chrome' in default_browser or 'google' in default_browser:
        subprocess.run('start chrome://history', shell=True)
    elif 'yandex' in default_browser:
        subprocess.run('start yandex://history', shell=True)
    elif 'edge' in default_browser or 'microsoft' in default_browser:
        subprocess.run('start msedge://history', shell=True)
    elif 'firefox' in default_browser:
        subprocess.run('start firefox://history', shell=True)
    elif 'opera' in default_browser:
        subprocess.run('start opera://history', shell=True)
    else:
        # Если браузер не определен, пробуем все варианты
        subprocess.run('start chrome://history', shell=True)
        subprocess.run('start yandex://history', shell=True)

# Создаем главное окно
root = tk.Tk()
root.title("System Tools")
root.geometry("400x300")
root.configure(bg="white")

# Кнопки
btn_appdata = tk.Button(
    root, 
    text="Open AppData",
    command=open_appdata_roaming,
    font=("Arial", 12),
    height=2,
    width=20,
    bg="lightblue"
)
btn_appdata.pack(pady=10)

btn_network = tk.Button(
    root,
    text="Data Usage", 
    command=open_network_usage,
    font=("Arial", 12),
    height=2,
    width=20,
    bg="lightgreen"
)
btn_network.pack(pady=10)

btn_history = tk.Button(
    root,
    text="Browser History", 
    command=open_browser_history,
    font=("Arial", 12),
    height=2,
    width=20,
    bg="lightyellow"
)
btn_history.pack(pady=10)

root.mainloop()
