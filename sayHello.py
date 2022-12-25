from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class SayHello(App):
    def build(self):
        self.window = GridLayout()
        self.window.cols = 1
        self.window.size_hint= (0.6,0.7)
        self.window.pos_hint = {"center_x":0.5, "center_y":0.5}
        #add widgets to window
        #image widget
        self.window.add_widget(Image(source="catt.jpg"))
        #label widget
        self.greeting=Label(
            text="Do you like cats?",
            font_size=15,
            color='#A348A6'
            )
        self.window.add_widget(self.greeting)
        #text input widget
        self.user= TextInput(
                multiline=False,
                padding_y=(20,20),
                size_hint=(1,0.5)
                )
        self.window.add_widget(self.user)
        #button widget
        self.button =Button(text="Paw",
                            size_hint=(1,0.5),
                            bold=True,
                            background_color ='#674AB3'
                            )    
        self.window.add_widget(self.button)
                
        return self.window

            

if __name__ == "__main__":
    SayHello().run()