import keyboard
import pyautogui
import pytesseract
import pyperclip


pytesseract.pytesseract.tesseract_cmd = r"C:\\Program Files\\Tesseract-OCR\\tesseract.exe"


def OCR():
    # Define the coordinates by using pixel printer
    coordinates = [
        (335, 320),     # top-right:    (x,y)
        (969, 666)      # bottom-left:  (x,y)
    ]

    text = ""
    x1, y1 = coordinates[0]
    x2, y2 = coordinates[1]

    # Calculate width and height for screenshot
    width = x2 - x1
    height = y2 - y1

    screenshot = pyautogui.screenshot(region=(x1, y1, width, height))
    screenshot_text = pytesseract.image_to_string(screenshot)
    if not screenshot_text.strip():
        print("No text detected.")
    text += f"{screenshot_text}"

    pyperclip.copy(text)
    print(text)


# Bind the function to a hotkey
keyboard.add_hotkey("ctrl", OCR)
# Keep the program running
keyboard.wait()
