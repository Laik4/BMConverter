#!/usr/bin/env python3
from PIL import Image, ImageDraw
from pyzbar.pyzbar import decode
import sys
import re
from os import path

def get_option(args):
    res = []
    for arg in args:
        if(re.match(r'\-\w', arg)):
            res.append(arg)
    return set(res)

def convert(filename, padding=2, size=5, rev=False):

    if not path.isfile(filename):
        print('No such file or directory: \'{}\''.format(filename))
        exit(0)

    with open(filename, 'r') as f:
        data = f.read()

        h, w = 0, 0
        H, W = 2000, 2000

        bk_col = (0, 0, 0)
        wt_col = (255, 255, 255)
        draw = Image.new('RGB', (size, size))
        draw_d = ImageDraw.Draw(draw)
        if rev:
            bg_col = bk_col
            fill_col = wt_col
        else:
            fill_col = bk_col
            bg_col = wt_col
        draw_d.rectangle((0, 0, size ,size), fill=fill_col)

        image = Image.new('RGB', (H, W), bg_col)

        x, y = 0, 0
        for pixel in data:
            if pixel == '1':
                x += 1
            elif pixel == '0':
                image.paste(draw, (padding+x*size, padding+y*size))
                x += 1
            elif pixel == '\n':
                y += 1
                h += 1
                w = max(w, x)
                x = 0


        return image.crop((0, 0, 2*padding+w*size, 2*padding+h*size))




if __name__ == '__main__':

    args = sys.argv
    filename = args[0]
    outfilename = None
    for i, opt in enumerate(args):
        if opt == '-o':
            outfilename = args[i+1]
            break

    im = convert(filename, padding=10)
    if outfilename:
        im.save('{}.png'.format(outfilename))
    else:
        im.show()
