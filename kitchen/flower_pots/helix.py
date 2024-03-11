from solid2 import *
from solid2.extensions.bosl2 import *
from solid2.extensions.bosl2 import skin, threading

set_global_fn(180)

SKEW = 3 / (36.5 - 2)

mid_plate = zcyl(d=150, h=5, anchor=BOTTOM) - zcyl(d=119, h=7, anchor=BOTTOM).down(1)


model = zcyl(d=180, h=5, anchor=BOTTOM) + mid_plate.up(345 / 2)

for a in (0, 90, 180, 270):
    model += skew(sxz=SKEW)(
        zcyl(d=15, h=345 + 1, anchor=BOTTOM + LEFT).left(180 / 2)
    ).rotateZ(a)

pot_holder = zcyl(
    d=130,
    h=20,
    anchor=BOTTOM,
) - zcyl(
    d=120,
    h=20,
    anchor=BOTTOM,
).up(5)

model += pot_holder.up(345)

model.save_as_scad("helix.scad")
