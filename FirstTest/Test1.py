# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 21:28:25 2020

@author: ulmo
"""
import manimlib
from manimlib.imports import *

class WriteText(Scene): 
    def construct(self): 
        text = TextMobject("This is a regular text")
        self.play(Write(text))
        self.wait(3)
        
        
        
        
if __name__ == "__main__":
    
    W = WriteText()
    manimlib.play(W)

