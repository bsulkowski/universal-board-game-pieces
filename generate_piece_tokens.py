from math import *
from functools import reduce

layer = 5
fi = layer * 4
r = fi / 2
s = pi * r * r
spacing = fi * 2

def merge(list, separator):
    return reduce(lambda x, y: x + separator + y, list)

def coords(range, angle):
    return f"{range * cos(2 * pi * angle) : >7.3f}, {range * sin(-2 * pi * angle) : >7.3f}"

circle_r = r

square_a = sqrt(s)
square_r = square_a / sqrt(2)

triangle_a = sqrt(s / (sqrt(3) / 4))
triangle_r = triangle_a / sqrt(3)

cross_a = sqrt(s / 5)
cross_r = cross_a / sqrt(2)

star_a = 2 * sqrt(s / 5 / (1 / tan(pi * 0.2) - 1 / tan(pi * 0.3)))
star_r2 = (star_a / 2) / sin(pi * 0.2)
star_r1 = s / 5 / (star_a / 2)

clover_r = sqrt(s / (2 * pi + 6 * sqrt(3) / 4))

shapes = [
    f'<circle cx="0" cy="0" r="{circle_r :.3f}"/>',
    '''<polygon points="
                ''' + merge([coords(square_r, (i + 0.5) / 4) for i in range(4)], '''
                ''') + '''
            "/>''',
    '''<polygon points="
                ''' + merge([coords(triangle_r, i / 3 + 0.25) for i in range(3)], '''
                ''') + '''
            "/>''',
    '''<polygon points="
                ''' + merge([
                    f'{cross_r * cos(pi * (a + 0.5) / 2) * (3 if (a % 2) * 2 == b else 1) : 7.3f}, '
                    f'{cross_r * sin(-pi * (a + 0.5) / 2) * (3 if (a % 2) * 2 == 2 - b else 1) : 7.3f}'
                    for a in range(4) for b in range(3)], '''
                ''') + '''
            "/>''',
    '''<polygon points="
                ''' + merge([coords(star_r2 if i % 2 == 0 else star_r1, i / 10 + 0.25) for i in range(10)], '''
                ''') + '''
            "/>''',
    f'''<path d="
                M {coords(clover_r, 0 - 0.25)}
                ''' + merge([f"A {clover_r : 7.3f}, {clover_r : 7.3f} 0 1 0 " + coords(clover_r, (i + 1) / 3 - 0.25) for i in range(3)], '''
                ''') + '''
                z
            "/>'''
]

hole = '''<polygon fill="white" points="
                ''' + merge([coords(layer / sqrt(2) * 1.1, i / 4) for i in range(4)], '''
                ''') + f'''
            "/>'''

with open(f'piece_tokens_{layer}mm.svg', 'w') as f:
    f.write(f'''\
<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" version="1.1" width="{spacing * 6 :.0f}mm" height="{spacing :.0f}mm" viewBox="0 0 {spacing * 6 :.0f} {spacing :.0f}">
    <g fill="gray" stroke="black" stroke-width="0.3">
        ''' +
        merge([f'''<g id="{i}" transform="translate({spacing * (i + 0.5) :.0f}, {spacing / 2 :.0f})">
            {shapes[i]}
            {hole}        
        </g>''' for i in range(6)], '''
        ''') + f'''
    </g>
</svg>
''')
