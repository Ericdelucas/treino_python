import pyautogui
import pytesseract
from PIL import Image
import time


time.sleep(3)
# x=pyautogui.position()
# print(x)


# Captura uma screenshot de uma região específica da tela (x, y, largura, altura)
screenshot = pyautogui.screenshot(region=(100, 100, 200, 200))
texto = pytesseract.image_to_string(screenshot, lang="por")

print("Texto detectado:")
print(texto)
