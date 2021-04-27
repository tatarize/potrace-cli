
# Installing

`pip install potrace-cli`

# Command Line Usage

This installs an entrypoint for the script `potracer` which does similar and parallel things to `potrace`.

```
usage: potracer [-h] [-v] [-l] [-o OUTPUT] [-b {svg,jagged-svg}]
               [-z {black,white,left,right,minority,majority,random}]
               [-t TURDSIZE] [-a ALPHAMAX] [-n] [-O OPTTOLERANCE] [-C COLOR]
               [-i] [-k BLACKLEVEL] [-s SCALE] [-1]
               [filename]

positional arguments:
  filename              an input file

optional arguments:
  -h, --help            show this help message and exit
  -v, --version         prints version info and exit
  -l, --license         prints license info and exit
  -o OUTPUT, --output OUTPUT
                        write all output to this file
  -b {svg,jagged-svg}, --backend {svg,jagged-svg}
                        select backend by name
  -z {black,white,left,right,minority,majority,random}, --turnpolicy {black,white,left,right,minority,majority,random}
                        how to resolve ambiguities in path decomposition
  -t TURDSIZE, --turdsize TURDSIZE
                        suppress speckles of up to this size (default 2)
  -a ALPHAMAX, --alphamax ALPHAMAX
                        corner threshold parameter
  -n, --longcurve       turn off curve optimization
  -O OPTTOLERANCE, --opttolerance OPTTOLERANCE
                        curve optimization tolerance
  -C COLOR, --color COLOR
                        set foreground color (default Black)
  -i, --invert          invert bitmap
  -k BLACKLEVEL, --blacklevel BLACKLEVEL
                        invert bitmap
```

# Requirements
* PIL/Pillow is required for image loading and modifications.
* Potracer for potracing.

# License
This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 2, or (at your option) any later version.

Furthermore, this is permitted to be relicensed under any terms the Peter Selinger's original Potrace is licensed under. If he broadly publishes the software under a more permissive license this port should be considered licensed as such as well. Further, if you purchase a proprietary license for inclusion within commercial software under his Dual Licensing program your use of this software shall be under whatever terms he permits for that. Any contributions to this port must be made under equally permissive terms.

"Potrace" is a trademark of Peter Selinger.
