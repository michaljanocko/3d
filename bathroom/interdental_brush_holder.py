from solid2 import *
from solid2.extensions.bosl2 import *
from solid2.extensions.bosl2.rounding import *

BRUSH_LENGTH = 50.5
BRUSH_WIDTH = 8.25
BRUSH_THICKNESS = 1.9

set_global_fn(50)

number_of_brushes = CustomizerSliderVariable(
    name="Number_of_brushes", default_value=10, min_=5, max_=30
)


def brush(space: bool = False):
    HANDLE_LENGTH = 16.25

    # From the Geogebra drawing
    X = (9.683, 4.048)

    b = (
        ellipse(d=(HANDLE_LENGTH, BRUSH_WIDTH), anchor=LEFT)
        + circle(d=1.5).translateX(BRUSH_LENGTH)
        + polygon(
            [
                (X[0], X[1]),
                (BRUSH_LENGTH, 1.5 / 2),
                (BRUSH_LENGTH, -1.5 / 2),
                (X[0], -X[1]),
            ]
        )
    )

    rounding = os_circle(r=BRUSH_THICKNESS / 2 - 1 / 1000)
    b = convex_offset_extrude(BRUSH_THICKNESS, top=rounding, bottom=rounding)(b)

    if space:
        b = minkowski()(b, sphere(r=0.5))

    return b.color("Tomato")


holder_height = (BRUSH_THICKNESS + 0.1) * number_of_brushes

holder = cyl(h=holder_height + 2, d=15, center=False)

holder = hull()(holder, holder.translateX(BRUSH_LENGTH - 8)).translateX(5)

brush_space = brush(space=True)

holder -= hull()(
    brush_space.translateZ(2),
    brush_space.translateZ(2 + holder_height),
)

# A column hole used for seeing remaining brushes
column_hole = circle(r=1, anchor=[0, 1])
holder -= (
    convex_offset_extrude(15 / 2, top=os_circle(r=-1))(
        hull()(column_hole, column_hole.translateY(holder_height))
    )
    .rotate([90, 0, 0])
    .translate([15 / 2, -1 / 100, BRUSH_THICKNESS * 2 + 1])
)

# A hole through which one can pull out a new brush
feeder_hole = brush_space.translateZ(2)
holder -= hull()(feeder_hole, zrot(20, cp=[BRUSH_LENGTH + 1, 0, 0])(feeder_hole))

holder -= minkowski()(
    cube([5, BRUSH_WIDTH * 2, 2], anchor=BOTTOM),
    sphere(d=BRUSH_THICKNESS * 2 + 1),
)

holder -= (
    (regular_ngon(4, side=1, realign=True, anchor=RIGHT + BACK) - circle(r=1))
    .linear_extrude(2.5)
    .translate(
        [5 / 2 + BRUSH_THICKNESS + 0.5 + 1 - 1 / 100, -15 / 2 + 1 - 1 / 100, -0.5]
    )
)

model = holder

# Holders for brushes in use
round_edge = xcyl(h=12, r=1).translateZ(BRUSH_THICKNESS + 3)
in_use_holder = (
    hull()(
        cube([12, 24, 1], anchor=BOTTOM),
        round_edge.translateY(12 - 1),
        round_edge.translateY(-12 + 1),
    ).translateX(6)
    - brush_space.translate([-25, -6, 2])
    - brush_space.translate([-25, 6, 2])
)
in_use_holder = in_use_holder.rotate([90, 90, 0]).translate(
    [0, -15 / 2 + 1 / 100, holder_height + 2]
)

model += in_use_holder.translateX(30)

model.save_as_scad(__file__.replace(".py", ".scad"))
