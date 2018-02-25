from math import *
from functools import reduce

layer = 5
spacing = layer * 6
base_stroke = 0.3
	
with open(f'piece_base_{layer}mm.svg', 'w') as f:
	f.write(f'''\
<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" version="1.1" width="{spacing * 3 :.0f}mm" height="{spacing :.0f}mm" viewBox="0 0 {spacing * 3 :.0f} {spacing :.0f}">
	<g fill="gray" stroke="black" stroke-width="{base_stroke / (layer / 2) :7.3f}" transform="translate(0, {spacing / 2 :.0f}) scale({layer / 2 :7.3f})">
		<g id="0" transform="translate(6, 0)">
			<polygon points="
				 4,  4
				 1,  4
				 1,  3
				-1,  3
				-1,  4
				-2,  4
				-4,  2
				-4,  1
				-3,  1
				-3, -1
				-4, -1
				-4, -2
				-2, -4
				-1, -4
				-1, -3
				 1, -3
				 1, -4
				 2, -4
				 4, -2
				 4, -1
				 3, -1
				 3,  1
				 4,  1
			"/>
			<polygon fill="white" points="
				 3,  3
				 2,  3
				 2,  2
				 3,  2
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
				 3,  2
				 3,  0
				 4,  0
				 4,  4
				 2,  6
				 1,  6
				 1,  4
				-1,  4
				-1,  6
				-2,  6
				-4,  4
				-4,  0
				-3,  0
				-3,  2
			"/>
		</g>
		<g id="2" transform="translate({24 + 6 + 4}, 0) rotate(90)">
			<polygon points="
			     1,  4
				 1,  2
				 3,  2
				 3,  0
				 4,  0
				 4,  4
				 2,  6
				 1,  6
				 1, 12
				-1, 12
				-1,  6
				-2,  6
				-4,  4
				-4,  0
				-3,  0
				-3,  2
				-1,  2
				-1,  4
			"/>
		</g>
	</g>
</svg>
''')
