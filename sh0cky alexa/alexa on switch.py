from pynput import keyboard
import subprocess
import threading

class MyException(Exception): pass

class Listening:
    """Is allways waiting for the keyboard input"""
    def __init__(self):
        self.notepad_open = False # to know the state
        with keyboard.Listener(
                on_press=self.on_press) as listener:
            try:
                listener.join()
            except:
                pass
    
    def on_press(self, key):
        try:
            if key.char == "]":
                if not self.notepad_open:
                    self.subprocess = \
                        subprocess.Popen('C:\Users\sh0cky\Desktop\Desktop2\sh0cky alexa\bot.py')
                    self.notepad_open = True # update state
                else:
                    self.subprocess.kill()
                    self.notepad_open = False # update state
        except: # special key was pressed
            pass

thread = threading.Thread(target=lambda: Listening())
thread.start()