import webbrowser, html
import pyperclip

def collectradii():
    tlradius = str(input('What is your top left border radius?'))
    trradius = str(input('What is your top right border radius?'))
    blradius = str(input('What is your bottom left border radius?'))
    brradius = str(input('What is your bottom right border radius?'))
    return tlradius, trradius, blradius, brradius

def generateborder(payload):
    f = open("border.html", "w")
    f.write(payload)
    f.close()
    webbrowser.open_new("file:///Users/andrewadrian-karlin/PycharmProjects/border-range/border.html")

def borderflow():
    tlradius, trradius, blradius, brradius = collectradii()
    payload = '<!DOCTYPE html><html lang="en"><head></head><body><div style="border-top-left-radius: '+tlradius+'px; border-top-right-radius: '+trradius+'px; border-bottom-left-radius: '+blradius+'px; border-bottom-right-radius: '+brradius+'px; background-color: #cfc ; padding: 10px; border: 1px solid green;"</div></body></html>'
    generateborder(payload)
    return payload

payload = borderflow()

while True:
    copyyn = str(input('Do you like your borders? (only enter yes or no)'))
    if copyyn != "yes":
        payload = borderflow()
        continue
    else:
        pyperclip.copy(payload)
        break
