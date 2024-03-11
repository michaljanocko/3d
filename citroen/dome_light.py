from solid2 import *
from solid2.extensions.bosl2 import *
from solid2.extensions.bosl2 import rounding

set_global_fn(1)

MAX_WIDTH = 55.5
MIN_WIDTH = 51.9
WIDTH_OFFSET = (MAX_WIDTH - MIN_WIDTH) / 2

MAX_LENGTH = 96.7
MIN_LENGTH = 94
LENGTH_OFFSET = (MAX_LENGTH - MIN_LENGTH) / 2

CORNER_RADIUS = 6.75

base_ = [
    # Left
    (0, MAX_WIDTH / 2),
    (LENGTH_OFFSET / 4, WIDTH_OFFSET + MIN_WIDTH - CORNER_RADIUS * 2),
    (LENGTH_OFFSET, WIDTH_OFFSET + MIN_WIDTH - CORNER_RADIUS),
    (LENGTH_OFFSET + CORNER_RADIUS, WIDTH_OFFSET + MIN_WIDTH),
    (MAX_LENGTH / 4, MAX_WIDTH - WIDTH_OFFSET / 4),
    # Top
    (MAX_LENGTH / 2, MAX_WIDTH),
    (MAX_LENGTH / 4 * 3, MAX_WIDTH - WIDTH_OFFSET / 4),
    (MAX_LENGTH - LENGTH_OFFSET - CORNER_RADIUS, WIDTH_OFFSET + MIN_WIDTH),
    (MAX_LENGTH - LENGTH_OFFSET, WIDTH_OFFSET + MIN_WIDTH - CORNER_RADIUS),
    (MAX_LENGTH - LENGTH_OFFSET / 4, WIDTH_OFFSET + MIN_WIDTH - CORNER_RADIUS * 2),
    # Right
    (MAX_LENGTH, MAX_WIDTH / 2),
    (MAX_LENGTH - LENGTH_OFFSET / 4, WIDTH_OFFSET + CORNER_RADIUS * 2),
    (MAX_LENGTH - LENGTH_OFFSET, WIDTH_OFFSET + CORNER_RADIUS),
    (MAX_LENGTH - LENGTH_OFFSET - CORNER_RADIUS, WIDTH_OFFSET),
    (MAX_LENGTH / 4 * 3, WIDTH_OFFSET / 4),
    # Bottom
    (MAX_LENGTH / 2, 0),
    (MAX_LENGTH / 4, WIDTH_OFFSET / 4),
    (LENGTH_OFFSET + CORNER_RADIUS, WIDTH_OFFSET),
    (LENGTH_OFFSET, WIDTH_OFFSET + CORNER_RADIUS),
    (LENGTH_OFFSET / 4, WIDTH_OFFSET + CORNER_RADIUS * 2),
]

base = [(x, y, 0) for x, y in base_]

middle = [
    (
        x - 3.25 if x > MAX_LENGTH / 2 else x + 3.25 if x < MAX_LENGTH / 2 else x,
        y - 3.25 if y > MAX_WIDTH / 2 else y + 3.25 if y < MAX_WIDTH / 2 else y,
        11,
    )
    for x, y in base_
]

top = [
    (x, y, 22)
    for (x, y) in [
        (21, 21),
        (MAX_LENGTH - 21, 21),
        (MAX_LENGTH - 21, MAX_WIDTH - 21),
        (21, MAX_WIDTH - 21),
    ]
]

# for path in [base, base_top]:
#     path = path2d(path)
#     path = rounding.round_corners(path, closed=True, r=10)
#     path = rounding.offset_stroke(path, width=[0, -1.6], closed=True)

form = hull_points(base + middle + top)

hole = minkowski_difference()(form, sphere(r=1.6, anchor=CENTER)).translateZ(-1.6)

rim = minkowski_difference()(
    polygon(base_).linear_extrude(5.2), sphere(r=1.6 * 2, anchor=CENTER)
).translateZ(-5.2 / 2)

model = form - hole  # - rim

model.color("AntiqueWhite", alpha=0.5).save_as_scad("dome_light.scad")
