from solid2 import *
from solid2.extensions.bosl2 import *

set_global_fn(90)

MAGNET_HOLE_DIAMETER = 21.5
MAGNET_DIAMETER = 57
MAGNET_HEIGHT = 11.5

model = diff()(
    zcyl(d=MAGNET_HOLE_DIAMETER, h=MAGNET_HEIGHT, anchor=BOTTOM)(
        position(TOP)(zcyl(h=11, d=3.2, anchor=TOP, _tag="remove").up(1))
    )
)
model += zcyl(d=MAGNET_DIAMETER, h=0.8, anchor=BOTTOM)

model.save_as_scad("knife_bar_holder.scad")
