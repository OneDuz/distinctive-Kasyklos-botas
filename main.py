import pyautogui
import pydirectinput
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

search_region = (118, 22, 35, 35)

def extract_boxed_number():
    screenshot = pyautogui.screenshot(region=(118, 22, 35, 35))
    screenshot_path = "screenshot.png"
    screenshot.save(screenshot_path)

def extract_boxed_number2():
    screenshot = pyautogui.screenshot(region=(118, 22, 35, 35))
    screenshot_path = "screenshot2.png"
    screenshot.save(screenshot_path)

images_and_keys = [
    ('1.png', '1', 0.99),
    ('2.png', '2', 0.99),
    ('3.png', '3', 0.99),
    ('4.png', '4', 0.99),
    ('5.png', '5', 0.99),
    ('6.png', '6', 0.99),
    ('7.png', '7', 0.99),
    ('8.png', '8', 0.99),
    ('9.png', '9', 0.99),
]

while True:
    time.sleep(0.5)
    
    for image, key, confidence in images_and_keys:
        try:
            if pyautogui.locateOnScreen(image, region=search_region, grayscale=True, confidence=confidence) is not None:
                extract_boxed_number2()
                pydirectinput.press(key)
                time.sleep(1)
                print(f"Pressed key {key} due to found image.")
        except pyautogui.ImageNotFoundException:
            extract_boxed_number()
            print(f"Image {image} not found.")
        except Exception as e:
            print(f"An error occurred: {e}")