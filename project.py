from kivymd.app import MDApp
from kivy.config import Config
from kivyauth.google_auth import initialize_google , login_google, logout_google
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import Screen,ScreenManager,FadeTransition
from kivy.core.window import Window
from kivymd.uix.behaviors import FakeRectangularElevationBehavior
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.list import OneLineAvatarListItem
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.properties import StringProperty
from kivymd.uix.card import MDCard
import json

Config.set('input', 'mouse', 'mouse,multitouch_on_demand')
Window.size = (350,600)
Window.resize = False
class LoginPageScreen(Screen):
    pass
class MessageScreen(Screen):
    def on_enter(self):
        #for chat code start from here 
        #setting theme properties       
        
        self.title = "Let's Connect" 

        screens = [
            MessageScreen(name = 'message')
        ]

        #Adding all screen in screen to the window manager 
        # self.wm = WindowManager("")#creating on instance of Screen manager and setting the animation when switching between screens
        # for screen in screens:
        #     self.wm.add_widget(Screen)

        # return self.wm
        #self.theme_cls.theme_style="Dark"""
class Home(Screen):
    
    profile_picture = "photos/9.jpg"

    def on_enter(self):
        
        self.list_posts()

    def list_posts(self):
        
        Builder.load_file('post_card.kv')
        with open('posts.json') as f_obj:
            data = json.load(f_obj)
            for username in data:
                self.ids.timeline.add_widget(PostCard(
                    username = username,
                    avatar = data[username]['avatar'],
                    profile_pic = self.profile_picture,
                    post = data[username]['post'],
                    caption = data[username]['caption'],
                    likes = data[username]['likes'],
                    comments = data[username]['comments'],
                    posted_ago = data[username]['posted_ago'],
                ))
class Connection(Screen):
    pass
class Profile(Screen):
    pass
class ProfileCard(MDFloatLayout,FakeRectangularElevationBehavior):
    pass


class PostCard(MDCard):
    profile_pic = StringProperty()
    avatar = StringProperty()
    username = StringProperty()
    post = StringProperty()
    caption = StringProperty()
    likes = StringProperty()
    posted_ago = StringProperty()
    comments = StringProperty()
    
class SignUpPageScreen(Screen):
    pass

class SetUpProfile(Screen):
    pass   

class Manager(ScreenManager):
    pass
class WindowManager(Screen):
    pass
class LetsConnectApp(MDApp):
    
        
    def build(self):
         client_id = open("client_id.txt")
         client_secret= open("client_secret.txt")
         initialize_google(self.after_login,self.error_listener, client_id.read() , client_secret.read())
         
    def changeScreen(self):
        self.root.transition.direction = "left"
        self.root.current = "profile"

    def after_login(self,name,email,photo_uri):
        self.root.ids.label.text = f"Logged in as {name}"
        self.root.transition.direction = "left"
        self.root.current = "chat"

    def error_listener(self):
        print("Login Failed !")

    def login(self):
        login_google()
    
    def logout(self):
        logout_google(self.after_logout())
    
    def after_logout(self,name,email,photo_uri):
        self.root.ids.label.text = f"Logged in as {name}"
        self.root.transition.direction = "left"
        self.root.current = "login"

    def verify_data(self,email,password):
        from firebase import firebase
        #Initialise Database 
        firebase = firebase.FirebaseApplication('https://test-a5e66-default-rtdb.firebaseio.com/',None)
        #Get Data
        result = firebase.get('test-a5e66-default-rtdb/Users','')
    
        #Get specific column like email or password  
        #Verification
        for i in result.keys():

            if result[i]['Email'] == email.strip():
                if result[i]['Password'] == password.strip():
                    print(email + "Logged In!")
                    self.root.transition.direction = "left"
                    self.root.current = "home"

       
                
            
        # Importing Data
        # data = {
        #     'Email':email,
        #     'Password':password
        # }
        #Database Name /Table Name
        # firebase.post("test-a5e66-default-rtdb/Users",data)

if __name__ == "__main__":
    LetsConnectApp().run()
