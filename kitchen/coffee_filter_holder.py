from math import cos

from solid2 import *
from solid2.extensions.bosl2 import *

set_global_fn(360)

HEIGHT = 50
SMALL = (100, 107)
LARGE = (125, 128)


def holder(dimensions):
    x, y = dimensions
    ratio = y / x
    # +2 for each wall, +1 for tolerance
    x += 2 * 2
    y += 2 * 2

    angle_offset = 3

    return (
        # Skew to get the weird shape
        skew(axy=angle_offset)(
            # Base
            pie_slice(h=HEIGHT, r=x, ang=90 + angle_offset)
            # Hole for the filters
            - pie_slice(h=HEIGHT, r=x - 2, ang=90 + angle_offset).translateZ(2)
            # Hole for filter tabs
            - pie_slice(h=HEIGHT, r=x, ang=13).translate([2, 2, 2]).rotateZ(26)
        ).scaleY(ratio * (1 / -cos(angle_offset)))
        # Walls
        + cube([x, 2, HEIGHT])
        + cube([2, y, HEIGHT])
    )


holder(SMALL).save_as_scad("coffee_filter_holder_1.scad")
holder(LARGE).save_as_scad("coffee_filter_holder_2.scad")
