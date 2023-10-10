# README

## Optical Character Recognition (OCR) Tool

A simple yet powerful OCR tool created using Python. This application helps users to capture a specific region of their screen, extract any text present in that region, and copy it directly to their clipboard, all with a simple hotkey.

### Prerequisites

#### Tesseract-OCR
This tool uses Tesseract-OCR, an optical character recognition engine, to extract text from images. It must be installed separately and the path must be specified within the script. 

Follow the installation guide here: [Tesseract-OCR GitHub](https://github.com/tesseract-ocr/tessdoc)

📝 **Note**: After installation, make sure to replace the path in the script with your own path to the Tesseract-OCR executable.

In the script, find and replace the following line with your own path:
```python
pytesseract.pytesseract.tesseract_cmd = r"C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
```

### Installing Python Packages

Make sure to install the necessary Python packages which are used in the script. You can do so using pip:

```bash
pip install pyautogui pytesseract pyperclip keyboard
```

### Usage

After ensuring all prerequisites are installed and paths are correctly specified, you can use the tool by running the script.

The script is programmed to capture a specified region on the screen. Adjust the coordinates as per your requirements. 

```python
coordinates = [
    (335, 320),     # top-right:    (x,y)
    (969, 666)      # bottom-left:  (x,y)
]
```

After executing the script, press `Ctrl` (or the key you set up as the hotkey) to activate the OCR function. The text found in the specified region will be copied to your clipboard and printed to the console. If no text is found, a corresponding message will be printed.

### Customizing Hotkey

You can change the hotkey used to trigger the OCR function by modifying the following line of code:

```python
keyboard.add_hotkey("ctrl", OCR)
```

Replace `"ctrl"` with the key of your choice. For a combination of keys, separate them with `+`, e.g., `"ctrl+shift"`.

### Contributing

Contributions, bug reports, and feature requests are welcome! Feel free to open an issue or create a pull request.

### License

This project is open source. Refer to the LICENSE file for more information.

---

Feel free to customize the README further to fit any additional functionalities or specific details you add to your project in the future!
