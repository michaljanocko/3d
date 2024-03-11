from solid2 import *
from solid2.extensions.bosl2 import *

set_global_fn(90)

WIDTH = 75
SCREW_WIDTH = 2.8

bracket = cyl(h=10, d=WIDTH, center=True)

screw_hole = cyl(h=15, d=SCREW_WIDTH, center=True)
bracket -= screw_hole.translateX(54 / 2)
bracket -= screw_hole.translateX(-54 / 2)
bracket -= screw_hole.translateY(62 / 2)
bracket -= screw_hole.translateY(-62 / 2)

cable_hole = cyl(h=15, d=38, center=True) - cube([38, 38, 17], anchor=[0, 1, 0])
bracket -= cable_hole.rotateZ(45)
bracket -= xcyl(h=WIDTH, r=10, anchor=LEFT + BOTTOM).translateX(1).rotateZ(135)

bracket.save_as_scad("chandelier_bracket.scad")
