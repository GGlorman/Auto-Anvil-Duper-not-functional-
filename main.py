import pyautogui
from pynput import keyboard
from time import sleep

print("Program is running!")

COMBINATIONS = [
    {keyboard.KeyCode(char='l')},
    {keyboard.KeyCode(char='L')}
]

current = set()


def execute():
    print("Bot is on!")
    pyautogui.moveTo(748, 432)
    sleep(0.2)
    pyautogui.click()
    sleep(0.2)
    pyautogui.press("space")
    sleep(0.2)
    pyautogui.moveTo(1178, 432)
    sleep(0.2)
    pyautogui.click()


def on_press(key):
    if any([key in COMBO for COMBO in COMBINATIONS]):
        current.add(key)
        if any(all(k in current for k in COMBO)for COMBO in COMBINATIONS):
            execute()


def on_release(key):
    if any([key in COMBO for COMBO in COMBINATIONS]):
        current.remove(key)


with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()