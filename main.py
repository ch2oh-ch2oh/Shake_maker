import eel
import cgi
import json
import re


def save_values(values):
    return values


@eel.expose
def convert_value_py(values):
    return save_values(values)


if __name__ == '__main__':
    eel.init("web")
    eel.start("main_html.html", size=(1200, 800))
