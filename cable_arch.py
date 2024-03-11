from solid2 import *
from solid2.extensions.bosl2 import *

set_global_fn(180)

pillar = zcyl(h=15, d=20, anchor=BOTTOM)

arch = hull()(pillar, pillar.translateX(60))

cube_hole = cube(11, anchor=BOTTOM).translateZ(-1)

arch -= cube_hole
arch -= cube_hole.translateX(60)

arch_hole = ycyl(h=22, d=20)

arch -= hull()(arch_hole.translateX(20), arch_hole.translateX(40))

arch.save_as_scad("cable_arch.scad")
