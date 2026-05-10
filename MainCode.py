import flet as ft
import pyautogui as pag
import time as time
import keyboard as kb
import winsound

def main(page: ft.Page):

    page.add(
        key := ft.Dropdown(options=[ft.dropdown.Option("W")]),
        delay := ft.TextField(value="0.1"),
        hotkey := ft.Dropdown(options=[ft.dropdown.Option("shift+q")]),
        ft.Button("Start", on_click=lambda _: loop(key.value, delay.value, hotkey.value)),
        ft.Text("")
    )

def loop(key,delay,hotkey):
    time.sleep(1)
    while True:
        pag.press(key.lower())
        time.sleep(float(delay))
        if kb.is_pressed(hotkey):
            winsound.Beep(1000,200)
            print(hotkey)
            break
        
ft.app(target=main)
