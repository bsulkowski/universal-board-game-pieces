from math import *
from functools import reduce

version = "2.2"
layer = 5
spacing = layer * 6
base_stroke = 0.3

def merge(list, separator):
    return reduce(lambda x, y: x + separator + y, list)

def mirror(points):
    return points + [(-x, y) for (x, y) in reversed(points)]

fancy_edge = [
    (4,  0),
    (3.5, 1),
    (2.5, 1.5),
    (2, 2.5),
    (2, 3.5),
    (3, 5.5),
    (2,  6)
]
    
with open(f'piece_base_{layer}mm_v{version}.svg', 'w') as f:
    f.write(f'''\
<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" version="1.1" width="{spacing * 3.5 :.0f}mm" height="{spacing :.0f}mm" viewBox="0 0 {spacing * 3.5 :.0f} {spacing :.0f}">
    <g fill="gray" stroke="black" stroke-width="{base_stroke / (layer / 2) :7.3f}" transform="translate(0, {spacing / 2 :.0f}) scale({layer / 2 :7.3f})">
        <g id="0" transform="translate(6, 0)">
            <polygon points="
                 4,  4
                 1,  4
                 1,  3
                -1,  3
                -1,  4
                -3,  3
                -4,  1
                -3,  1
                -3, -1
                -4, -1
                -3, -3
                -1, -4
                -1, -3
                 1, -3
                 1, -4
                 3, -3
                 4, -1
                 3, -1
                 3,  1
                 4,  1
            "/>
            <polygon fill="white" points="
                 1.1,  1.1
                -1.1,  1.1
                -1.1, -1.1
                 1.1, -1.1
            "/>
        </g>
        <g id="1" transform="translate({12 + 6 + 2}, 0) rotate(90)">
            <polygon points="
                 ''' + merge([f'{x}, {y}' for (x, y) in mirror([
                 (1.1,  2),
                 (1.1,  0),
                 (3,  0),
                 (3, -1.9),
                 (4, -1.9)
                 ] + fancy_edge + [
                 (1.1,  6),
                 (1.1,  3.9)
                 ])], '''
                 ''') + f'''
            "/>
        </g>
        <g id="2" transform="translate({24 + 6 + 8}, 0) rotate(90)">
            <polygon points="
                 ''' + merge([f'{x}, {y}' for (x, y) in mirror([
                 (1.1,  4),
                 (1.1,  0),
                 (3,  0),
                 (3, -1.9),
                 (4, -1.9)
                 ] + fancy_edge + [
                 (1,  6),
                 (1, 14)
                 ])], '''
                 ''') + f'''
            "/>
        </g>
    </g>
</svg>
''')
