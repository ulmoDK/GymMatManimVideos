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
    
        
        text = TextMobject("To ligninger, 2 ubekendte,")
        text.scale(1.5)
        formula1 = TexMobject("y=3 \cdot x -2")       
        formula1.scale(1.5)
        formula2 = TexMobject("2 \cdot x","+","y","=","5","-2 \cdot x")
        formula2.scale(1.5)
        ab = TexMobject("a","b")
        
        self.play(Write(text))
        self.play(text.shift,2*UP)
        self.play(Write(formula1))
        
        self.play(formula1.shift,1*UP)
        
        self.play(Write(formula2[:-1]))
        self.wait(5)
        self.play(
                ReplacementTransform(formula2[0].copy(),formula2[-1]),
                FadeOut(formula2[:2]),
                run_time=2,
                  )
        self.play(formula2[2:].shift,1.2*LEFT)
        
        self.wait(2)
        
        #self.play(Transform(for
        
class FormulaColor1(Scene): 
    def construct(self):
        text = TexMobject("x","=","{a","\\over","b}")
        text[0].set_color(RED)
        text[1].set_color(BLUE)
        text[2].set_color(GREEN)
        text[3].set_color(ORANGE)
        text[4].set_color("#DC28E2")
        self.play(Write(text))
        self.wait(2)      
       
if __name__ == "__main__":
    
    S1 = Scene1()
    S2 = Scene2()
    manimlib.play(S1)
    manimlib.play(S2)
    

