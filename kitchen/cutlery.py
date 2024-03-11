from solid2 import *
from solid2.extensions.bosl2 import *

set_global_fn(60)

sizes = [d - 6 - 6 for d in (303, 82)]
bottom_shrink = sizes[0] / 265
print(bottom_shrink)

base = prismoid(
    size1=[d / bottom_shrink for d in sizes], size2=sizes, height=70 - 3 - 3
).translateZ(3 + 3)

model = (
    hull()(
        minkowski()(base, sphere(6)),
        minkowski()(base.translateZ(6), cube(6, anchor=CENTER)),
    )
    - hull()(
        minkowski()(base, sphere(3)),
        minkowski()(base.translate([0, 0, 70]), sphere(3)),
    )
    - cube([d * 1.2 for d in (303, 82, 8)], anchor=BOTTOM).translateZ(70)
)

model.save_as_scad("cutlery.scad")
