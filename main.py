from os.path import join, exists
import json
import kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager, SlideTransition
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import ListProperty, StringProperty, NumericProperty, BooleanProperty, AliasProperty


Window.borderless = True

class NoteView(Screen):
    pass

class NoteListItem(BoxLayout):
    pass

class Notes(Screen):
    pass

class MutableTextInput(FloatLayout):
    pass

class MainApp(App):
    pass



MainApp().run()
