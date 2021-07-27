from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
import json
from datetime import datetime
import glob
from pathlib import Path
import random

Builder.load_file('design.kv')

class LoginScreen(Screen):
    def sign_up(self):
        self.manager.transition.direction = "down"
        self.manager.current = "Sign_up_screen"

    def login(self, uname, pword):
        with open("users.json") as file:
            users = json.load(file)
        if uname in users and users[uname]['password'] == pword:
            self.manager.transition.direction = "down"
            self.manager.current = "login_success"
        else:
            self.ids.login_wrong.text = "Your details are incorrect"

class LoginSuccess(Screen):
    def log_out(self):
        self.manager.transition.direction = "up"
        self.manager.current = "login_screen"

    def get_quote(self, feel):
        feel = feel.lower()
        available_feelings = glob.glob("quotes/*txt")
        available_feelings = [Path(filename).stem for filename in
                              available_feelings]
        if feel in available_feelings:
            with open(f"quotes/{feel}.txt", encoding="utf8") as file:
                quotes = file.readlines()
            self.ids.quote.text = random.choice(quotes)

class SignUpScreen(Screen):
    def add_user(self, uname, pword):
        with open("users.json") as file:
            users = json.load(file)
        users[uname] = {
                        'username': uname,
                        'password': pword, 
                        'created': datetime.now().strftime("%Y-%m-%d %H-%M-%S")
                       }
        with open("users.json", 'w') as file:
            json.dump(users, file)
        self.manager.transition.direction = "down"
        self.manager.current = "sign_up_success"

class SignUpSuccess(Screen):
    def log_in(self):
        self.manager.transition.direction = "up"
        self.manager.current = "login_screen"

class RootWidget(ScreenManager):
    pass


class MainApp(App):
    def build(self):
        return RootWidget()


if __name__ == "__main__":
    MainApp().run()