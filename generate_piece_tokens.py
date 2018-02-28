from math import *
from functools import reduce

version = "1.1"
layer = 5
fi = layer * 4
r = fi / 2
s = pi * r * r
spacing = fi * 2
corner_r = 0.75

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def add(self, that):
        return Vector(self.x + that.x, self.y + that.y)
    def sub(self, that):
        return Vector(self.x - that.x, self.y - that.y)
    def dot(self, that):
        return self.x * that.x + self.y * that.y
    def cross(self, that):
        return self.x * that.y - self.y * that.x
    def length(self):
        return sqrt(self.dot(self))
    def scaled(self, factor):
        return Vector(self.x * factor, self.y * factor)
    def from_radial(angle, radius):
        return Vector(cos(angle), -sin(angle)).scaled(radius)
    def to_svg(self):
        return f'{self.x :7.3f}, {self.y :7.3f}'
        
def merge(list, separator):
    return reduce(lambda x, y: x + separator + y, list)

def round_corners(polygon, radius):
    n = len(polygon)
    def corner(i):
        v = [polygon[(i + j) % n].sub(polygon[i]) for j in [-1, 1]]
        if v[0].cross(v[1]) < 0:
            return 'L ' + polygon[i].to_svg()
        l = [v[j].length() for j in range(2)]
        angle = acos(v[0].dot(v[1]) / l[0] / l[1])
        offset = 1 / tan(angle / 2) * radius
        p = [v[j].scaled(offset / l[j]).add(polygon[i]) for j in range(2)]
        return f'''L {p[0].to_svg()}
                A {radius :7.3f}, {radius :7.3f} 0 0 0 {p[1].to_svg()}'''
    p = polygon[-1].sub(polygon[0]).scaled(0.5).add(polygon[0])
    return f'''<path d="
                M {p.to_svg()}
                ''' + merge([corner(i) for i in range(n)], '''
                ''') + '''
                z
            "/>'''
    
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
    round_corners([Vector.from_radial(2 * pi * (i + 0.5) / 4, square_r) for i in range(4)], corner_r),
    round_corners([Vector.from_radial(2 * pi * (i / 3 + 0.25), triangle_r) for i in range(3)], corner_r),
    round_corners([Vector(cross_r * cos( pi * (a + 0.5) / 2) * (3 if (a % 2) * 2 == b     else 1),
                          cross_r * sin(-pi * (a + 0.5) / 2) * (3 if (a % 2) * 2 == 2 - b else 1))
                   for a in range(4) for b in range(3)], corner_r),
    round_corners([Vector.from_radial(2 * pi * (i / 10 + 0.25), star_r2 if i % 2 == 0 else star_r1) for i in range(10)], corner_r),
    f'''<path d="
                M {Vector.from_radial(-2 * pi * 0.25, clover_r).to_svg()}
                ''' + merge([f"A {clover_r : 7.3f}, {clover_r : 7.3f} 0 1 0 "
                    + Vector.from_radial(2 * pi * ((i + 1) / 3 - 0.25), clover_r).to_svg() for i in range(3)], '''
                ''') + '''
                z
            "/>'''
]

hole = '''<polygon fill="white" points="
                ''' + merge([Vector.from_radial(2 * pi * i / 4, layer / sqrt(2) * 1.1).to_svg()
                             for i in range(4)], '''
                ''') + f'''
            "/>'''

with open(f'piece_tokens_{layer}mm_v{version}.svg', 'w') as f:
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
