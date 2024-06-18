import os
import subprocess as sp

paths = {
    'notepad': "C:\\Windows\\notepad.exe",
    'word': "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Word.lnk",
    'calculator': "C:\\Windows\\system32\\calc.exe"
}


def open_notepad():
    os.startfile(paths['notepad'])


def open_word():
    os.startfile(paths['word'])


def open_cmd():
    os.system('start cmd')


def open_camera():
    sp.run('start microsoft.windows.camera:', shell=True)


def open_calculator():
    sp.Popen(paths['calculator'])

def open_music():
    musicPath = "C:/Users/DELL/Downloads/tvari-hawaii-vacation-159069.mp3"
    os.system(f"open {musicPath}")

