from subprocess import Popen

def ktoc(n):
    return n - 273.15


def render_marquee(index, marquee, length):
    return marquee \
        if len(marquee) <= length \
        else (marquee + ' ')[index % len(marquee):index % len(marquee) + length]


def speak(text):
    Popen(['./speak', text])
