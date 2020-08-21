from kivy.app import App
from kivy.uix.label import Label


class PlayGround(Label):
    pass


class Playground(App):

    def build(self):
        return PlayGround()


if __name__ == "__main__":
    Playground().run()