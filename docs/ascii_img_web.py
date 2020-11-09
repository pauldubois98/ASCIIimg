from cv2 import cv2
import numpy as np

import sys

img = cv2.imread("pic.jpg")


def toASCII(img, cols = 70, rows = None):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    height, width = img.shape
    cell_width = width / cols
    if rows is None:
        cell_height = 2.25 * cell_width
        rows = int(height / cell_height)
        
    else:
        cell_height = height / rows
    
    if cols > width or rows > height:
        raise ValueError('Too many cols or rows.')
    result = ""
    print(rows, cols, rows/cols)
    for i in range(rows):
        for j in range(cols):
            gray = np.mean(
                img[int(i * cell_height):min(int((i + 1) * cell_height), height),
                    int(j * cell_width):min(int((j + 1) * cell_width), width)]
                )
            result += grayToChar(gray)
        result += '\n'
    return result


def grayToChar(gray):
    CHAR_LIST = ' .:-=+*8#%@'
    CHAR_LIST = '@%#8*+=-:. '
    num_chars = len(CHAR_LIST)
    return CHAR_LIST[ min(int(gray * num_chars / 255), num_chars - 1) ]



def build_page(cols):
    pre = open('pre_pic.html', 'r')
    post = open('post_pic.html', 'r')
    html = pre.read()
    for col in cols:
        html += '\n<h2>{} columns</h2>'.format(col)
        html += '\n<pre id="img{}" style="font-size: {}em;">\n'.format(col,
                                                                       80/col)
        html += toASCII(img, col)
        html += '\n</pre>\n'
    html += post.read()
    post.close()
    pre.close()

    f = open('picture.html', 'w')
    f.write(html)
    f.close()



build_page([80, 100, 200, 400, 800][::-1])



