# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 21:28:25 2020

@author: ulmo
"""
import manimlib
from manimlib.imports import *

"""
def set_background(self):
    background = Rectangle(
    width = FRAME_WIDTH,
    height = FRAME_HEIGHT,
    stroke_width = 0,
    fill_color = "#3E746F",
    fill_opacity = 1)
    self.add(background)
"""

class Scene1(Scene): 
    def construct(self): 
        #text = TextMobject("This is a regular text")
        #self.play(Write(text))
        #self.wait(3)
        #set_background(self)
        
        
        text1 = TextMobject("Det her er en sætning")
        text2 = TextMobject("Grafisk løsning? På hvad? Og hvorfor?")
        #text2.shift(DOWN*0.1,buff=1)
        text2.next_to(text1,DOWN,buff=1)
        self.add(text1)
        self.wait(1)
        self.play(Write(text2))
        self.wait(3)

class Scene2(Scene): 
    def construct(self): 
        
        text1 = TextMobject("Det her er en sætning")
        self.add(text1)
        self.wait(1)
        
        
if __name__ == "__main__":
    
    S1 = Scene1()
    S2 = Scene2()
    manimlib.play(S1)
    manimlib.play(S2)
    

