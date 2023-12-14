import pyperclip
import pystray
import PIL.Image
from win10toast import ToastNotifier

icon_image = PIL.Image.open('icon.png')
toast = ToastNotifier()


def showToast(notification_):
    toast.show_toast(
        "LCBrackets",
        f"{notification_}",
        duration = 3,
        icon_path = "icon.ico",
        threaded = True,
    )

def changeSBrackets():
    input_text = pyperclip.paste()
    if input_text.count('[') == 0 and input_text.count(']') == 0:
        showToast("There are no [] brackets 😥")
        return
    changed_text = input_text.replace('[','{').replace(']','}')
    pyperclip.copy(changed_text)
    showToast("Done [] to {}")
    
def changeRBrackets():
    input_text = pyperclip.paste()
    if input_text.count('{') == 0 and input_text.count('}') == 0:
        showToast("There are no {} brackets 😥")
        return
    changed_text = input_text.replace('{','[').replace('}',']')
    pyperclip.copy(changed_text)
    showToast("Done {} to []")

def swapBrackets():
    input_text = pyperclip.paste()
    
    or_count = input_text.count('{')
    cr_count = input_text.count('}')
    os_count = input_text.count('[')
    cs_count = input_text.count(']')
    
    if not or_count and not cr_count and not os_count and not cs_count:
        showToast("There are no brackets 😥")
        return

    changed_text = input_text.replace('[', '•l♣0•').replace(']', '•l♣1•')
    changed_text = changed_text.replace('{', '[').replace('}', ']')
    changed_text = changed_text.replace('•l♣0•', '{').replace('•l♣1•', '}')

    pyperclip.copy(changed_text)
    showToast("Done Swapping Brackets")

def upperText():
    input_text = pyperclip.paste().upper()
    pyperclip.copy(input_text)
    showToast("Done `CONSTANT IT`")

def lowerText():
    input_text = pyperclip.paste().lower()
    pyperclip.copy(input_text)
    showToast("Done `DECONSTANT IT`")

def sendCredits():
    showToast("LCBrackets made by Obektev, 2023'\nGitHub: https://github.com/Obektev")

def setup():
    try:
        icon = pystray.Icon("LCBrackets", icon_image, title="LCBrackets", menu=pystray.Menu(
            pystray.MenuItem("Change [] Brackets", changeSBrackets),
            pystray.MenuItem("Change {} Brackets", changeRBrackets),
            pystray.MenuItem("🔄 Swap Brackets 🔄", swapBrackets),
            pystray.MenuItem("⬆ CONSTANT IT ⬆", upperText),
            pystray.MenuItem("⬇ DECONSTANT IT ⬇", lowerText),
            pystray.MenuItem("Made by Obektev", sendCredits)
        ))
        print("DEBUG LOG: LCBrackets started successfuly.")
        icon.run()
        
        
    except:
        print("DEBUG LOG: Something went wrong during LCBrackets starting!")

if __name__ == "__main__":
    setup()