from math import sqrt

from solid2 import *
from solid2.extensions.bosl2 import *
from solid2.extensions.bosl2 import threading

set_global_fn(72)

lens_width = CustomizerSliderVariable("Lens_width", 11, min_=1, max_=15)
lens_rim = CustomizerSliderVariable("Lens_rim", 1.25, min_=0.5, max_=2.5, step=0.05)
lens_thickness = CustomizerSliderVariable(
    "Lens_thickness", 1.25, min_=0.75, max_=2, step=0.05
)
focal_length = CustomizerSliderVariable("Focal_length", 31, min_=15, max_=75)
aperture = CustomizerSliderVariable("Aperture", 11, min_=2.8, max_=13, step=0.1)


e_mount = import_stl("e_mount.stl").rotateX(-90).translateZ(-3)


LENS_NUT_WIDTH = 32.5
LENS_NUT_HEIGHT = 1.5


def lens_nut():
    angle = 225

    lens_rail_end = zcyl(
        h=LENS_NUT_HEIGHT + lens_thickness + 0.2, d=lens_width + 2.2, anchor=BOTTOM
    ).rotateZ(180 - angle / 2)

    lens_rail_side = zcyl(
        h=LENS_NUT_HEIGHT + lens_thickness + 1.2, d=lens_width + 0.2, anchor=BOTTOM
    )

    lens_rail = lens_rail_end - lens_rail_side

    width = LENS_NUT_WIDTH - 0.5
    diaphragm = focal_length / aperture

    return zcyl(d=width, h=LENS_NUT_HEIGHT, anchor=BOTTOM) + lens_rail & cube(
        [width, width / sqrt(2), LENS_NUT_HEIGHT + 5], anchor=BOTTOM
    ) - zcyl(h=LENS_NUT_HEIGHT + 2, d=diaphragm, anchor=BOTTOM,).translateZ(-1) - zcyl(
        h=LENS_NUT_HEIGHT, d=lens_width - lens_rim, anchor=BOTTOM
    ).translateZ(
        0.6
    ) - zrot_copies(
        n=2
    )(
        zcyl(h=LENS_NUT_HEIGHT + 2, d=3, anchor=BOTTOM).down(1).left(lens_width / 2 + 3)
    )


FRONT_THICKNESS = 3

focus_threading = lambda is_ring: threading.threaded_rod(
    d=61 - 2 * (FRONT_THICKNESS - (1 if is_ring else 0.75)),
    l=10,
    pitch=2,
    blunt_start1=not is_ring,
    blunt_start2=is_ring,
    left_handed=True,
    internal=True,
    anchor=BOTTOM,
) & cube([61, 61, 7], anchor=BOTTOM)


def focus_ring():
    nut_lock_height = LENS_NUT_HEIGHT + lens_thickness + 1.2 + 0.05

    base = zcyl(d=61, h=10, chamfer2=1, anchor=BOTTOM) - zcyl(
        d=61 - 2 * FRONT_THICKNESS, h=10, anchor=BOTTOM
    ).down(3)

    lens_hole = zcyl(
        d1=lens_width - lens_rim - 2,
        d2=lens_width - lens_rim + 2 + FRONT_THICKNESS,
        h=2 + FRONT_THICKNESS,
        anchor=BOTTOM,
    )

    nut_lock = (
        zcyl(
            h=9 - nut_lock_height + 1,
            d=LENS_NUT_WIDTH + 4,
            chamfer=1,
            anchor=BOTTOM,
        )
        - zcyl(
            h=9 - nut_lock_height + 1 + 2,
            d=LENS_NUT_WIDTH,
            anchor=BOTTOM,
        ).down(1)
    ).up(8 - nut_lock_height - 1.4) + (
        zcyl(d=LENS_NUT_WIDTH + 4, h=1, chamfer1=1, anchor=BOTTOM)
        - cube([LENS_NUT_WIDTH / sqrt(2), 61, 3], center=True)
    ).up(
        2.6
    )

    notch = zcyl(h=9, d=2, anchor=BOTTOM, rounding=1, _fn=24)

    return (
        base
        - focus_threading(is_ring=True)
        - lens_hole.up(10 - 3 - 1)
        + nut_lock
        + zrot_copies(n=60, d=61)(notch)
    )


def mount():
    return (
        e_mount
        + focus_threading(is_ring=False)
        - zcyl(h=9, d=48, chamfer2=-2, anchor=BOTTOM).down(1)
    )


lens_nut().save_as_scad("single/lens_nut.scad")
focus_ring().save_as_scad("single/focus_ring.scad")
mount().down(15).save_as_scad("single/mount.scad")

(lens_nut() + focus_ring() + mount()).save_as_scad("single.scad")
