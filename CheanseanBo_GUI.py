from tkinter import*
import tkinter.font
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

green = 8
red = 10
blue = 12

GPIO.setup(8, GPIO.OUT)
GPIO.setup(10, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)

def reset():
    GPIO.output(8, GPIO.LOW)
    GPIO.output(10, GPIO.LOW)
    GPIO.output(12, GPIO.LOW)

reset()

#Setup GUI window
win = Tk()
win.title("CheanseanBo GUI")
myFont = tkinter.font.Font(family = "Calibri", size = 12)
#width x height of the window and position
win.geometry("250x130+300+300")

#define function to toggle the LED on
def toggleLED(ledPin):
    #it will first set everything to off
    reset()
    #depending on the input, it will turn that LED on
    GPIO.output(ledPin, GPIO.HIGH)
    
#define a close function to exit the window
def close():
    GPIO.cleanup()
    win.destroy()

#create buttons to click on the window
greenButton = Button(win, text = 'Turn Green LED On', font = myFont,
                     command = lambda led = green : toggleLED(led),
                     bg = 'green', height = 1, width = 24)
greenButton.grid(row = 0, column = 0)

redButton = Button(win, text = 'Turn Red LED On', font = myFont,
                    command = lambda led = red : toggleLED(led),
                    bg = 'red', height = 1, width = 24)
redButton.grid(row = 1, column = 0)

blueButton = Button(win, text = 'Turn Blue LED On', font = myFont,
                    command = lambda led = blue : toggleLED(led),
                    bg = 'blue', height = 1, width = 24)
blueButton.grid(row = 2, column = 0)

closeButton = Button(win, text = 'Exit', font = myFont,
                    command = close, bg = 'red', height = 1,
                    width = 10)
closeButton.grid(row = 3, column = 0)

#exit window through the close function
win.protocol("WM_DELETE_WINDOW", close)
win.mainloop()



