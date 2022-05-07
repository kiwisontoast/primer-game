from pickle import TRUE
import pyautogui as gui
import pynput 
from pynput.mouse import Listener as MouseListener
from pynput.keyboard import Listener as KeyboardListener
from PIL import Image
import pytesseract
from time import sleep

exiting = False

path_to_tesseract = r"C:\Users\devbs\AppData\Local\python\Tesseract-OCR\tesseract.exe"

mouseX, mouseY = 0, 0

tailsbox1X, tailsbox1Y = 0, 0
tailsbox2X, tailsbox2Y = 0, 0
headsbox1X, headsbox1Y = 0, 0
headsbox2X, headsbox2Y = 0, 0

flipboxX, flipboxY = 0, 0

cheaterboxX, cheaterboxY = 0, 0
fairboxX, fairboxY = 0, 0

def getText(image_path):
    # Opening the image & storing it in an image object
    img = Image.open(image_path)
    
    # Providing the tesseract executable
    # location to pytesseract library
    pytesseract.tesseract_cmd = path_to_tesseract
    
    return pytesseract.image_to_string(img)

def exit():
    if exiting:
        quit()

checking = 0
mouse = pynput.mouse.Controller()
def loop():

    print(headsbox1X, headsbox1Y)
    print(headsbox2X, headsbox2Y)

    exit()

    # flipping
    sleep(1)
    mouse.position = (flipboxX, flipboxY)
    sleep(1)
    mouse.position = (flipboxX, flipboxY)

    exit()
    
    # reading heads
    headimg = gui.screenshot("head.png", region=(headsbox1X,headsbox1Y, headsbox2X-headsbox1X, headsbox2Y- headsbox1Y))


# im = pyautogui.screenshot(region=(0,0, 300, 400))

def on_move(x, y):
    global mouseX, mouseY

    mouseX = x 
    mouseY = y

# Collect events until released
ml = MouseListener(
        on_move=on_move)
ml.start()

def OnPress(key):
    global checking
    global tailsbox1X, tailsbox1Y
    global tailsbox2X, tailsbox2Y
    global headsbox1X, headsbox1Y
    global headsbox2X, headsbox2Y
    global cheaterboxX, cheaterboxY
    global fairboxX, fairboxY
    global flipboxX, flipboxY

    # try:
    k = '{0}'.format(key)
    if (k == "'s'"):
        if checking == 0:
            tailsbox1X, tailsbox1Y = mouseX, mouseY
        elif checking == 1:
            tailsbox2X, tailsbox2Y = mouseX, mouseY
        elif checking == 2:
            headsbox1X, headsbox1Y = mouseX, mouseY
        elif checking == 3:
            headsbox2X, headsbox2Y = mouseX, mouseY
        elif checking == 4:
            cheaterboxX, cheaterboxY = mouseX, mouseY
        elif checking == 5:
            fairboxX, fairboxY = mouseX, mouseY
        elif checking == 6:
            flipboxX, flipboxY = mouseX, mouseY
        checking = ( checking + 1 ) % 7
    elif (k == "'l'"):
        print("Loop started")
        while True:
            loop()

        checking = (checking + 1)%6
    elif (k == "'\\x03'"):
        exiting = True
        quit()
    # except:
    #     print("error")
    #     pass


kl = KeyboardListener(on_press=OnPress)
kl.start()
kl.join()