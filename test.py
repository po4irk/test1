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
    # Пробуем несколько способов открыть использование данных
    try:
        # Способ 1: Через настройки
        subprocess.run('start ms-settings:datausage', shell=True)
    except:
        try:
            # Способ 2: Через панель управления
            subprocess.run('control.exe /name Microsoft.NetworkAndSharingCenter', shell=True)
        except:
            # Способ 3: Просто открываем настройки сети
            subprocess.run('start ms-settings:network', shell=True)

def open_browser_history():
    """Открывает историю в браузере по умолчанию"""
    # Пробуем универсальный способ для браузера по умолчанию
    try:
        # Для большинства браузеров
        webbrowser.open('about:history')
    except:
        try:
            # Альтернатива
            webbrowser.open('history')
        except:
            # Последняя попытка
            webbrowser.open('chrome://history')

# Создаем главное окно
root = tk.Tk()
root.title("System Tools")
root.geometry("400x300")
root.configure(bg="white")

# Простые кнопки без переноса текста
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

# Запускаем главный цикл
root.mainloop()
