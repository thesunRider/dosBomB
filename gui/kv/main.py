# main.py
# -*- coding: utf-8 -*-

import os

from kivy.app import App
from kivy.core.window import Window
from kivy.lang import Builder
from kivymd.theming import ThemeManager
from playground import PlayGround


class MainApp(App):
    def build(self):
        return MainApp()

if __name__ == "__main__":
    MainApp().run()