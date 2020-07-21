class StickMan(SVGMobject):
CONFIG = {
"color" : BLUE_E,
"stroke_width" : 2,
"stroke_color" : WHITE,
"fill_opacity" : 1.0,
"propagate_style_to_family" : True,
"height" : 3,
"corner_scale_factor" : 0.75,
"flip_at_start" : False,
"is_looking_direction_purposeful" : False,
"start_corner" : None,
#Range of proportions along body where arms are
"right_arm_range" : [0.55, 0.7],
"left_arm_range" : [.34, .462],
}
def __init__(self, mode = "plain", **kwargs):
self.parts_named = False
try:
svg_file = os.path.join(
SVG_IMAGE_DIR,
"stick_man_%s.svg"%mode
)
SVGMobject.__init__(self, file_name = svg_file, **kwargs)
except:
warnings.warn("No StickMan design with mode %s"%mode)
svg_file = os.path.join(
SVG_IMAGE_DIR,
"stick_man.svg"
)
SVGMobject.__init__(self, file_name = svg_file, **kwargs)
 
if self.flip_at_start:
self.flip()
if self.start_corner is not None:
self.to_corner(self.start_corner)
 
def name_parts(self):
#self.mouth = self.submobjects[MOUTH_INDEX]
self.head = self.submobjects[HEAD_INDEX]
self.body = self.submobjects[BODY_INDEX]
self.arms = self.submobjects[ARMS_INDEX]
self.legs = self.submobjects[LEGS_INDEX]
self.parts_named = True
 
def init_colors(self):
SVGMobject.init_colors(self)
if not self.parts_named:
self.name_parts()
self.head.set_fill(RED, opacity = 0)
self.body.set_fill(self.color, opacity = 1)
self.arms.set_fill(YELLOW, opacity = 0)
self.legs.set_fill(GREEN, opacity = 0)
return self