from conv_formula import convert_formula
from conv_img_form import conv_img_form
import argparse

if __name__ == '__main__':
    try:
        parser = argparse.ArgumentParser()
        parser.add_argument('--path', type=str, help="파일 경로")
        parser.add_argument('--width', default='50%', type=str, help="이미지 너비")
        parser.add_argument('--height', default='50%', type=str, help="이미지 높이")

        args = parser.parse_args()
        path = args.path
        width = args.width
        height = args.height

        convert_formula(path)
        conv_img_form(path, width, height)
    except IndexError as e:
        print('파일 경로를 명시해주세요!! (Ex./hsyang/seminar/rl/test.md)')



