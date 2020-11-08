#!/usr/bin/env python3

# Usage:
# $ cd jiashengwu.github.io
# $ python update_thumbnail.py

import os
from pdf2image import convert_from_path
from PIL import Image

resume_name = 'Jiasheng_Wu_Resume_SDE'
sizes = [
	(1200, 627) # LinkedIn
]

curr_dir = os.path.split(os.path.realpath(__file__))[0]
pdf_path = os.path.join(curr_dir, '{}.pdf'.format(resume_name))

for size in sizes:
	png_path = '{}_{}x{}.png'.format(resume_name, size[0], size[1])
	png = convert_from_path(pdf_path, fmt='png', single_file=True, size=(size[0], None))[0]
	_, height = png.size
	png = png.crop((0, 0, size[0], size[1]))
	png.save(os.path.join(curr_dir, png_path))
