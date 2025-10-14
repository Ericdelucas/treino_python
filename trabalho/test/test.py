import pyautogui
import pytesseract
from PIL import Image
import cv2
import numpy as np
import time

# Tempo para posicionar a tela
time.sleep(3)

# 1️⃣ Captura a região da tela (substitua conforme sua necessidade)
screenshot = pyautogui.screenshot(region=(100, 100, 200, 200))

# 2️⃣ Converte para numpy array
imagem_np = np.array(screenshot)

# 3️⃣ Converte para escala de cinza
gray = cv2.cvtColor(imagem_np, cv2.COLOR_BGR2GRAY)

# 4️⃣ Aplica threshold (binarização) para melhorar contraste do texto
_, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# 5️⃣ Converte de volta para imagem PIL
imagem_processada = Image.fromarray(thresh)

# 6️⃣ Usa pytesseract para ler o texto
texto = pytesseract.image_to_string(imagem_processada, lang="por")

# 7️⃣ Mostra o texto detectado
print("Texto detectado:")
print(texto)
