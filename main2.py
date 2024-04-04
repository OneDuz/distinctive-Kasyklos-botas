import pyautogui
import keyboard
import subprocess
import time
import sys

def check_screen_resolution(target_width=1920, target_height=1080):
    screenWidth, screenHeight = pyautogui.size()
    if screenWidth == target_width and screenHeight == target_height:
        print(f"Screen resolution is {screenWidth}x{screenHeight}, as expected.")
    else:
        print(f"Warning: Screen resolution is {screenWidth}x{screenHeight}, not the expected {target_width}x{target_height}.")
        sys.exit(1)

def check_dpi_scaling_windows():
    try:
        reg_query = subprocess.check_output('reg query "HKCU\\Control Panel\\Desktop" /v LogPixels', shell=True)
        dpi_setting = int(reg_query.split()[-1], 16)
        if dpi_setting == 96:
            print("DPI scaling is set to 100%, as expected.")
        else:
            print(f"Warning: DPI scaling is set to {dpi_setting / 96 * 100}%, which may affect image recognition accuracy.")
            sys.exit(1)
    except Exception as e:
        print(f"Failed to check DPI scaling: {e}")
        sys.exit(1)

def main():
    check_screen_resolution()
    #check_dpi_scaling_windows()

if __name__ == "__main__":
    main()

screenshot_region = (118, 22, 35, 35)

def take_and_save_screenshot(key):
    """
    Takes a screenshot in the defined region and saves it with the name of the key pressed.
    """
    screenshot = pyautogui.screenshot(region=screenshot_region)
    screenshot_name = f"{key}.png"
    screenshot.save(screenshot_name)
    print(f"Screenshot saved as {screenshot_name}")

while True:
    time.sleep(0.1)
    for key in map(str, range(1, 10)):
        if keyboard.is_pressed(key):
            take_and_save_screenshot(key)
            while keyboard.is_pressed(key):
                time.sleep(0.1)