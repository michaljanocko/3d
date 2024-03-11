from math import cos, pi, sin, sqrt, tan

from solid2 import *
from solid2.extensions.bosl2 import *

set_global_fn(60)

H = 10
# Thickness
T = 4

hook = (
    pie_slice(h=H, r=T, ang=180).rotateZ(90)
    + cube([T, 16 - T, H], anchor=RIGHT + BOTTOM + FRONT)
    + pie_slice(h=H, r=T, ang=270).translate([0, 16 - T, 0])
    + cube([13, T, H], anchor=LEFT + BOTTOM + FRONT).translateY(16 - T)
    + pie_slice(h=H, r=T, ang=225).rotateZ(315).translate([13, 16 - T, 0])
)

shelf_edge = zcyl(h=3 * H, d=2.25, anchor=RIGHT)

base = (
    pie_slice(h=H, r=T, ang=180).rotateZ(90).translate([-2.25, T + 75 - 60 - 10, 0])
    + cube([T, 10 - T, H], anchor=RIGHT + BOTTOM + BACK).translate([-2.25, 75 - 60, 0])
    + zcyl(h=H, d=2 * T + 2.25, anchor=BOTTOM).translate([-2.25 / 2, 75 - 60, 0])
    + cube([T, 75 - 60 + T, H], anchor=LEFT + BOTTOM + FRONT).translateY(-T)
    - hull()(shelf_edge, shelf_edge.translateY(75 - 60))
    + cube([60, T, H], anchor=LEFT + BOTTOM + BACK)
    + pie_slice(h=H, r=T, ang=270).rotateZ(180).translate([60, 0, 0])
    + cube([T, 28, H], anchor=LEFT + BOTTOM + FRONT).translateX(60)
    + pie_slice(h=H, r=T, ang=225).rotateZ(-90).translate([60, 28, 0])
)

anchor = (
    cube([5.9, T + 6.8, 6.2]) + cube([11.7, 3.3, 6.2]).translateY(T + 3.5)
).translateZ((H - 6.2) / 2)
anchor_offset = 10

slope = (
    cube([(60 - 13) * sqrt(2), T, H])
    + anchor.translateX(anchor_offset)
    + anchor.translateX(anchor_offset + 33)
)

model = base + slope.rotateZ(-45).translate([13, 75, 0]) + hook.translateY(63)

model.save_as_scad("raspberry_pi_hooks.scad")
