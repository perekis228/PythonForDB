#python lab3/task1.py -d lab3/plates/train/dirty -oper flip
import os
import argparse
from skimage import io, transform, exposure

def clockwise(img):
    return transform.rotate(img, angle=-45, resize=True)

def counterclockwise(img):
    return transform.rotate(img, angle=45, resize=True)

def flip(img):
    return img[::-1]

def swirl(img):
    return transform.swirl(img, strength=10)

def gamma(img):
    return exposure.adjust_gamma(img, gamma=0.5)

def complex(img):
    return gamma(swirl(flip(img)))

def main(input_dir, operation):
    operations = {'clockwise': clockwise,
                  'counterclockwise': counterclockwise,
                  'flip': flip,
                  'swirl': swirl,
                  'gamma': gamma,
                  'complex': complex}

    cur_oper = operations[operation]
    for filename in os.listdir(input_dir):
        print(input_dir + '/' + filename)
        img = io.imread((input_dir + '/' + filename))
        res = cur_oper(img)
        io.imsave(input_dir + f'/new_{filename}', res.astype('uint8'))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Thumbnail Viewer")
    parser.add_argument("-d", "--input_dir", type=str, help="Input directory path")
    parser.add_argument("-oper", "--operation", type=str, help="Operation")
    args = parser.parse_args()

    main(args.input_dir, args.operation)