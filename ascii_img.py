from cv2 import cv2
import numpy as np

import sys



def toASCII(img, cols = 70, rows = None, CHAR_LIST='@%#8*+=-:. '):
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
    #print(rows, cols)
    for i in range(rows):
        for j in range(cols):
            gray = np.mean(
                img[int(i * cell_height):min(int((i + 1) * cell_height), height),
                    int(j * cell_width):min(int((j + 1) * cell_width), width)]
                )
            result += grayToChar(gray, CHAR_LIST)
        result += '\n'
    return result


def grayToChar(gray, CHAR_LIST):
    num_chars = len(CHAR_LIST)
    return CHAR_LIST[ min(int(gray * num_chars / 255), num_chars - 1) ]



if __name__=="__main__":
    img_file = sys.argv[1]
    txt_file = sys.argv[2]
    if len(sys.argv)>3:
        nb_cols = int(sys.argv[3])
    else:
        nb_cols = 80

    img = cv2.imread(img_file)
    ascii_txt = toASCII(img, nb_cols)

    f = open(txt_file, 'w')
    f.write(ascii_txt)
    f.close()



