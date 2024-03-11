from solid2 import polygon, set_global_fn
from solid2.extensions.bosl2 import *
from solid2.extensions.bosl2.rounding import *

set_global_fn(360)

FEEDER_LENGTH = 17.3
AXLE_D = 3.2
TUBE_D = 6.05

FEEDER_WHEEL_H = 3.8
FEEDER_WHEEL_D = 12.2

feeder = tube(h=FEEDER_LENGTH, od=TUBE_D, id=AXLE_D, center=False)


# Model the rubber wheel base that feeds the tape
feeder_wheel_path = circle(d=FEEDER_WHEEL_D) - circle(d=AXLE_D)

ridge_path = circle(r=1).translateX(FEEDER_WHEEL_D / 2)
for i in range(8):
    feeder_wheel_path -= ridge_path.rotateZ(i * 45)

feeder += (
    round2d(r=0.1)(feeder_wheel_path).linear_extrude(FEEDER_WHEEL_H).translateZ(0.25)
)


# Model the rubber ring for the feeder wheel
FEEDER_RUBBER_D = 15

feeder_rubber_path = circle(d=FEEDER_RUBBER_D) - circle(d=FEEDER_WHEEL_D)

for i in range(8):
    feeder_rubber_path += ridge_path.rotateZ(i * 45)

feeder_rubber = round2d(r=0.1)(feeder_rubber_path).linear_extrude(FEEDER_WHEEL_H)


# Model the stepper teeth
TEETH_WIDTH = 3.7

tooth_path = polygon(
    [
        # Root (outside point)
        (TUBE_D / 2, 0),
        (TUBE_D / 2, 4),
        (AXLE_D / 2 + 1, 4.25),
        # Root (inside point)
        (AXLE_D / 2, 0),
    ]
)

tooth_path = (
    round2d(r=0.1)(tooth_path)
    .linear_extrude(TEETH_WIDTH)
    .translateZ(FEEDER_LENGTH - TEETH_WIDTH - 0.25)
)

teeth_count = 10

for i in range(teeth_count):
    feeder += tooth_path.rotateZ(i * 360 / teeth_count)


# Export
feeder = feeder.color("white")
feeder.save_as_scad("feeder.scad")

feeder_rubber = feeder_rubber.color("dimgray")
feeder_rubber.save_as_scad("feeder_rubber.scad")

(feeder + feeder_rubber.translateZ(0.25)).save_as_scad("feeder_assembly.scad")
