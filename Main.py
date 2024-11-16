from tkinter import *
from tkinter import messagebox as mb
from tkinter import simpledialog as sd
import datetime
import time
import pygame

def sett():
    rem=sd.askstring("Время напоминания", "Введите время напоминания в формате ЧЧ:ММ")
    if rem:
        try:
            hour=int((rem.split(":")[0]))#нулевой элемент из списка
            minute=int((rem.split(":")[1]))
            now=datetime.datetime.now()
            print(now)
            dt=now.replace(hour=hour,minute=minute, second=0)
            print(dt)
            label.config(text=f"Напоминание установлено на {hour}:{minute}")
        except ValueError:
            mb.showerror("Ошибка", "Неверный формат времени")
        except Exception as e:
            print(e)
window=Tk()
window.title("Напоминание со звуком")

label=Label(text="Установите напоминание", font=('Courier', 20))
label.pack(pady=20)

button=Button(text="Установить", font=('Courier', 20), command=sett)
button.pack(pady=20)


window.mainloop()
