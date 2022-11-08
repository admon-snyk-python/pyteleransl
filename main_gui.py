from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

KV = """
MyBL:
        
        orientation: "vertical"
        size_hint: (0.95, 0.95)
        pos_hint: {"center_x": 0.5, "center_y":0.5}
        
        Label:
                font_size: "30sp"
                text: root.data_label

        TextInput:
                id: Inp
                multline: False
                padding_y: (5,5)
                size_hint: (1,0.5)


        Button:
                
                text: "Upload Photo"
                bold: True
                background_color:'#00FFCE'
                size_hint: (1,0.5)
                on_press: root.selectphoto()
        Button:
                
                text: "Telegram-Version"
                bold: True
                background_color:'#00FFCE'
                size_hint: (1,0.5)
                on_press: root.selectphoto()
"""

class MyBL(BoxLayout):

    data_label = StringProperty("..PyTeleTransl..")
    
    def selectphoto(self):
        print("working!")


class MyApp(App):

    running = True

    def build(self):

        return Builder.load_string(KV)

    def on_stop(self):
        self.running = False

MyApp().run()


