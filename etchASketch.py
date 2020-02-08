# --------------------------- E T C H   A   S K E T C H ---------------------------

from gfxhat import backlight, lcd, fonts
from PIL import Image, ImageFont, ImageDraw
import click
import time

backlight.set_all(255,255,255)
backlight.show()

def drawingMachine(x=0, y=63, choice=0):
    displayText()
    time.sleep(3)
    clearScreen()
    while(True):
        choice = chooseDirection()
        if(choice=='\x1b[A'):
            y-=1
            if(y<0): y=63
        elif(choice=='\x1b[B'):
            y+=1
            if(y>63): y=0
        elif(choice=='\x1b[D'):
            x-=1
            if(x<0): x=127
        elif(choice=='\x1b[C'):
            x+=1
            if(x>127): x=0
        elif(choice=='q'):
            bye()
            time.sleep(2)
            clearScreen()
            backlightOff()
            break
        elif(choice=='s'):
            clearScreen()
            drawingMachine()
        else:
            print("Invalid move.")
            chooseDirection()
        lcd.set_pixel(x,y,1)
        lcd.show()

def chooseDirection():
    print("""---E T C H   A   S K E T C H---
    Use arrows to move | S to start again | Q to quit""")
    choice = click.getchar()
    return(choice)

def clearScreen():
    lcd.clear()
    lcd.show()

def backlightOff():
    backlight.set_all(0,0,0)
    backlight.show()

def displayText(text="Etch a Sketch",x=5,y=5):
    lcd.clear()
    width, height = lcd.dimensions()
    image = Image.new('P', (width, height))
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype(fonts.AmaticSCBold, 30)
    w, h = font.getsize(text)
    draw.text((x,y), text, 1, font)
    for x1 in range(x,x+w):
        for y1 in range(y,y+h):
            pixel = image.getpixel((x1, y1))
            lcd.set_pixel(x1, y1, pixel)
    lcd.show()

def bye():
    text="Goodbye!"
    displayText(text)
   
drawingMachine()