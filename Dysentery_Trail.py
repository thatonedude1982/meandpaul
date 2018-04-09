
import kivy
kivy.require('1.9.0')

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.popup import Popup
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

from player import Player as pl 

Builder.load_string("""
<PlayerUI>:
    FloatLayout:
        canvas:
            Rectangle:
                source: '00start.jpg'
                pos: 0, 500
                size: 150, 250
            Rectangle:
                source: '0end.jpg'
                pos: 1775, 500
                size: 150, 250
        Button:
            text: "Player's Supplies"
            size_hint: .2, .2
            on_press: root.player_supplies()
        Button:
            text: "Player's Trails"
            size_hint: .2, .2
            on_press: root.player_trails()
""")

class PlayerUI(FloatLayout):

    def player_trails(self):
        box = BoxLayout(spacing = 10)

        calamityPath = 'calamityPath.jpg'
        calamityDown = 'calamityDown.jpg'
        clearPath = 'clearPath.jpg'
        riverSupply = 'riverSupply.jpg'
        riverDrown = 'riverDrown.jpg'
        
        #close = Button(text = "Close", size_hint = (.05, .05))
        for x in pl.inventory:
            if x == "calamityPath":
                box.add_widget(Button(background_normal = calamityPath, background_down = calamityDown, size_hint = (.2, 1)))
            if x == "clearPath":
                box.add_widget(Button(background_normal = clearPath, size_hint = (.2, 1)))
            if x == "riverSupply":
                box.add_widget(Button(background_normal = riverSupply, size_hint = (.2, 1)))
            if x == "riverDrown":
                box.add_widget(Button(background_normal = riverDrown, size_hint = (.2, 1)))

        try:
            s = self.box_popup
        except AttributeError:
            self.box_popup = Popup(content = box, title = 'Trails', size_hint = (0.8, 0.8))
            s = self.box_popup

        #close.bind(on_press = s.dismiss)
        if s.content is not box:
            s.content = box
        s.open()

    """def player_supplies(self):
        box = BoxLayout(spacing = 10)
        
        #close = Button(text = "Close", size_hint = (.05, .05))
        for x in trailHand:
            if x == "calamityPath":
                box.add_widget(Button(background_normal = calamityPath, background_down = calamityDown, size_hint = (.2, 1)))
            if x == "clearPath":
                box.add_widget(Button(background_normal = clearPath, size_hint = (.2, 1)))
            if x == "riverSupply":
                box.add_widget(Button(background_normal = riverSupply, size_hint = (.2, 1)))
            if x == "riverDrown":
                box.add_widget(Button(background_normal = riverDrown, size_hint = (.2, 1)))

        try:
            s = self.box_popup
        except AttributeError:
            self.box_popup = Popup(content = box, title = 'Trails', size_hint = (0.8, 0.8))
            s = self.box_popup

        #close.bind(on_press = s.dismiss)
        if s.content is not box:
            s.content = box
        s.open()   """






class DysenteryApp(App):
    def build(self):
        return PlayerUI()
    

if __name__ =='__main__':
    DysenteryApp().run() 