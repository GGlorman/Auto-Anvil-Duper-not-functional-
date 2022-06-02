from pynput import keyboard

COMBINATIONS = [
    {keyboard.KeyCode(char='l')},
    {keyboard.KeyCode(char='L')}
]

current = set()


def execute():
    import pyautogui

    pyautogui.click(748, 432)
    pyautogui.typewrite(' ')

    pyautogui.click(1178, 427)

    pyautogui.click(748, 432)

    pyautogui.hotkey('Backspace')

    pyautogui.click(1178, 427)


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
