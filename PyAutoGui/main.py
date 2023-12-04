import pyautogui
import time

def main():

    # Initialized PyAutoGUI
    pyautogui.FAILSAFE = True

    # Countdown timer
    print("Starting", end="")
    for i in range(0, 10):
        print(".", end="", flush=True)
        time.sleep(1)
    print("Go")

    # Do anything
    pyautogui.keyDown('w')
    time.sleep(1)
    pyautogui.keyUp('w')

    # Done
    print("Done")

if __name__ == "__main__":
    main()