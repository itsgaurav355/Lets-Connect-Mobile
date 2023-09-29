from kivy.core.text import LabelBase
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivymd.uix.behaviors import FakeRectangularElevationBehavior
from kivymd.uix.floatlayout import MDFloatLayout

Window.size = (310,580)

kv="""
MDFloatLayout:
	md_bg_color: rgba(246,250,255,255)
	ProfileCard:
		size_hint_y:0.65
		pos_hint:{"center_y": 0.7}
		elevation : 6
		md_bg_color:1,1,1,1
		radius: [0,0,20,20]
		MDIconButton:
			icon:"arrow-left"
			pos_hint:{"center_y": 0.91}
			user_font_size:"20sp"
			theme_text_color:"Custom"
			text_color: rgba(71,92,119,255)
		MDIconButton:
			icon:"dots-vertical"
			pos_hint:{"center_x":.93,"center_y": 0.91}
			user_font_size:"20sp"
			theme_text_color:"Custom"
			text_color: rgba(71,92,119,255)
		MDLabel:
			text:"My Profile"
			font_name:"font"
			font_size:"20sp"
			pos_hint:{"center_x": 0.56,"center_y":0.82}
			color: rgba(71,92,119,255)
		Image:
			source:"photos/7.jpg"
			pos_hint:{"center_x": 0.5,"center_Y":0.62}
		MDLabel:
			text:"Atharva Parab"
			font_name:"font"
			pos_hint:{"center_y":0.82}
			halign:"center"
			color: rgba(71,92,119,255)
		MDLabel:
			text:"Company Name"
			font_name:"font"
			pos_hint:{"center_y":0.36}
			halign:"center"
			font_size:"12sp"
			color: rgba(188,202,220,255)
		MDLabel:
			text:"Mumbai,India"
			font_name:"font"
			pos_hint:{"center_y":0.3}
			halign:"center"
			font_size:"12sp"
			color: rgba(188,202,220,255)
		MDGridLayout:
			rows:2
			cols:3
			size_hint: 0.85,0.12
			pos_hint:{"center_x":0.5,"center_y":0.15}
			MDLabel:
				text:"Post"
				halign:"center"
				font_name:"font"
				font_size:"12sp"
				color: rgba(188,202,228,255)
			MDLabel:
				text:"Followers"
				halign:"center"
				font_name:"font"
				font_size:"12sp"
				color: rgba(188,202,228,255)
			MDLabel:
				text:"Follows"
				halign:"center"
				font_name:"font"
				font_size:"12sp"
				color: rgba(188,202,228,255)
			MDLabel:
				text:"456"
				halign:"center"
				font_name:"font"
				font_size:"14sp"
				color: rgba(71,92,119,255)
			MDLabel:
				text:"602"
				halign:"center"
				font_name:"font"
				font_size:"14sp"
				color: rgba(71,92,119,255)
			MDLabel:
				text:"290"
				halign:"center"
				font_name:"font"
				font_size:"14sp"
				color: rgba(71,92,119,255)
	Image:
		source:"photos/1.jpg"
		size_hint:0.35,0.35
		pos_hint:{"center_x":0.32,"center_y":0.185}
	Image:
		source:"photos/2.jpg"
		size_hint:0.35,0.35
		pos_hint:{"center_x":0.68,"center_y":0.26}
	Image:
		source:"photos/3.jpg"
		size_hint:0.35,0.35
		pos_hint:{"center_x":0.68,"center_y":0.11}


"""
class ProfileCard(MDFloatLayout,FakeRectangularElevationBehavior):
	pass

class Social(MDApp):
	
    def build(self):
        return Builder.load_string(kv)
    
if __name__=="__main__":
     Social().run()