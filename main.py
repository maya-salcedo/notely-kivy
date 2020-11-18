from os.path import join, exists
import json
from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager, SlideTransition
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import ListProperty, StringProperty, NumericProperty, BooleanProperty, AliasProperty


Window.borderless = True

class NoteView(Screen):
    note_index: NumericProperty()
    note_title: StringProperty()
    note_content: StringProperty()

class NoteListItem(BoxLayout):
    note_index: NumericProperty()
    note_title: StringProperty()
    note_content: StringProperty()

class Notes(Screen):
    data = ListProperty()

    def _get_data_for_widgets(self):
        return [{
            "note_index": index,
            "note_content": item["content"],
            "note_title": item["title"]}
            for index, item in enumerate(self.data)]

    data_for_widgets = AliasProperty(_get_data_for_widgets,bind= ["data"])

class MutableTextInput(FloatLayout):
    pass

class MainApp(App):

    def build(self):
        self.notes = Notes(name="notes")
        root = ScreenManager()
        root.add_widget(self.notes)
        return root

    def go_notes(self):
        self.transition.direction = "right"
        self.root.current = "notes"

    def save_notes(self):
        with open(self.notes_fn, "w") as fd:
            json.dump(self.notes.data, fd)

    def refresh_notes(self):
        data = self.notes.data
        self.notes.data = []
        self.notes.data = data

    def del_note(self, note_index):
        del self.notes.data[note_index]
        self.save_notes()
        self.refresh_notes()
        self.go_notes()

    def edit_note(self, note_index):
        note = self.notes.data[note_index]
        name = "notes{}".format(note_index)

        if self.root.has_screen(name):
            self.root.remove_widget(self.root.get_screen(name))

        view = NoteView(
            name = name,
            note_index = note_index,
            note_title = note.get("title")
            note_content = note.get("content"))
        self.root.add_widget(view)
        self.transition.direction = "left"
        self.root.current = view.name

    def add_note(self):
        self.notes.data.append({"title": "New note", "content": ""})
        note_index = len(self.notes.data)-1
        self.edit_note(note_index)


    @property
    def note_fn(self):
        return join(self.user_data_dir, "notes.json")

if __name__ == "__main__":
    MainApp().run()
