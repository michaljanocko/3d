from solid2 import *
from solid2.extensions.bosl2 import *

set_global_fn(60)

model = cyl(h=5, d=25)
model -= cyl(h=7, d=6).translateX(-7)
model -= cube([11, 9, 1.8], anchor=LEFT).translateX(25 / 2 - 11)

model.save_as_scad("postbox_key.scad")
