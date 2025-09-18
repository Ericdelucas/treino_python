import pyautogui
import time

# import keyboard

# # ...existing code...

# if keyboard.is_pressed('esc'):  # ou qualquer tecla, como 'q'
#     exit()
#     print("Parando o script!")
#     exit()

# # while True:


# time.sleep(3)
# x=pyautogui.position()
# print(x)
# # time.sleep(0.1)

#_______________________________


nam=input("digite o nome do arquivo: ")
ano=input("digite o ano do arquivo: ")





time.sleep(1)
pyautogui.click(x=951, y=745)


time.sleep(5)

# impresora 
pyautogui.click(x=941, y=93)

# digitalizar
time.sleep(1)
pyautogui.click(x=941, y=93)

time.sleep(5)
pyautogui.click(x=729, y=419)

time.sleep(8)
pyautogui.click(x=1127, y=138)

time.sleep(1)
pyautogui.press('backspace')
time.sleep(0.5)
pyautogui.write(nam)

# ________________________________

time.sleep(9)
pyautogui.click(x=710, y=529)



time.sleep(2)
pyautogui.click(x=773, y=747)

time.sleep(2)
pyautogui.click(x=678, y=81)
time.sleep(2)   
pyautogui.click(x=618, y=95)


time.sleep(3)
pyautogui.write(nam)
time.sleep(2)
pyautogui.press('enter')





time.sleep(9)
pyautogui.click(x=1346, y=418)







time.sleep(3)
pyautogui.click(x=408, y=171)
time.sleep(1)
pyautogui.click(x=408, y=171)
pyautogui.click(x=408, y=171)
time.sleep(2)


pyautogui.click(x=402, y=193)



time.sleep(3)
pyautogui.click(x=845, y=246)
time.sleep(0.5)
pyautogui.click(x=845, y=246)
time.sleep(3)



# #-----------------------------


pyautogui.click(x=726, y=311)
time.sleep(0.5)
pyautogui.hotkey('enter')
time.sleep(0.8) 


pyautogui.click(x=745, y=279)
time.sleep(0.8)



pyautogui.hotkey('ctrl', 'c')
time.sleep(0.8)
pyautogui.click(x=679, y=262)
time.sleep(0.8)
pyautogui.hotkey('ctrl', 'v')
time.sleep(0.8)






pyautogui.click(x=722, y=389)

time.sleep(0.8)
pyautogui.write(ano)


time.sleep(0.8)
pyautogui.click(x=951, y=745)
time.sleep(0.8)
pyautogui.click(x=54, y=181)
time.sleep(0.5)
pyautogui.click(x=54, y=181)  
time.sleep(0.5)
pyautogui.click(x=690, y=413)  

time.sleep(0.8)
pyautogui.click(x=54, y=181)
time.sleep(0.5)
pyautogui.click(x=54, y=181)  
time.sleep(0.5)
pyautogui.click(x=690, y=413) 

time.sleep(0.8)
pyautogui.click(x=54, y=181)
time.sleep(0.5)
pyautogui.click(x=54, y=181)  
time.sleep(0.5)
pyautogui.click(x=690, y=413) 

time.sleep(0.8)
pyautogui.click(x=776, y=745)


# time.sleep(0.5)
# pyautogui.click(x=595, y=623)
