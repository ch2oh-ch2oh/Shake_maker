import eel
import apps
import cgi
import json
import re

if __name__ == '__main__':
    apps.create_Cocktails()
    eel.init("web")
    eel.start("main_html.html", size=(1200, 800))
