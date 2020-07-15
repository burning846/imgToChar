import os
import cv2
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('--input', type=str, default='input.png') 
parser.add_argument('--output', type=str, default='output.txt')
parser.add_argument('--width', type=int, default=-1)
parser.add_argument('--height', type=int, default=-1)

# char_list
ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")
# ascii_char = list("$@B%8&WM#*ZLCJUYunxrjft()1{}[]?-_+~<>;:,\"^`'. ")


def rgb2char(rgb):
    r,g,b = list(rgb)
    gray = 0.2126 * r + 0.7152 * g + 0.0722 * b

    return ascii_char[int(gray / 256.0 * len(ascii_char))]

if __name__ == '__main__':
    args = parser.parse_args()
    if not os.path.exists(args.input):
        print('ERROR: %s not found' % args.input)

    img = cv2.imread(args.input, cv2.IMREAD_COLOR)
    if args.width > 0 and args.height > 0:
        img = cv2.resize(img, (args.width, args.height))
    else:
        args.width = img.shape[1]
        args.height = img.shape[0]


    out_txt = ""

    for i in range(args.height):
        for j in range(args.width):
            out_txt += rgb2char(img[i, j])
        out_txt += '\n'

    print(out_txt)

    with open(args.output, 'w') as f:
        f.write(out_txt)
    