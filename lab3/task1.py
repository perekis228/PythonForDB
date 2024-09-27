#python lab3/task1.py -d lab3/plates/train/dirty -oper flip
import os
import argparse
from skimage import io, transform, exposure
import numpy as np

def clockwise(img):
    return (transform.rotate(img, angle=-45, resize=True)*255).astype(np.uint8)

def counterclockwise(img):
    return (transform.rotate(img, angle=45, resize=True)*255).astype(np.uint8)

def flip(img):
    return img[::-1]

def swirl(img):
    return (transform.swirl(img, strength=10)*255).astype(np.uint8)

def gamma(img):
    return (exposure.adjust_gamma(img, gamma=0.5)*255).astype(np.uint8)

def complex(img):
    return gamma(swirl(flip(img)))

def main(input_dir, operation):
    operations = {'clockwise': clockwise,
                  'counterclockwise': counterclockwise,
                  'flip': flip,
                  'swirl': swirl,
                  'gamma': gamma,
                  'complex': complex}

    try:
        cur_oper = operations[operation]
    except KeyError:
        raise Exception(f'There is no such operation "{operation}"')

    next_num = int(os.listdir(input_dir)[-1][:4])+1
    str_num = ''

    for filename in os.listdir(input_dir):
        img = io.imread((input_dir + '/' + filename))
        res = cur_oper(img)
        for i in range(1, 5):
            if next_num < 10**i:
                str_num = '0'*(4-i) + str(next_num)
                break
        print(str_num+'.jpg')
        io.imsave(input_dir + f'/{str_num}.jpg', res)
        next_num += 1

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Thumbnail Viewer")
    parser.add_argument("-d", "--input_dir", type=str, help="Input directory path")
    parser.add_argument("-oper", "--operation", type=str, help="Operation")
    args = parser.parse_args()

    main(args.input_dir, args.operation)
