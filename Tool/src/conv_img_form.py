import argparse
import re

def conv_img_form(path, width, height):
    with open(path, 'r') as f:
        lines = f.readlines()

    f = open(path, 'w')
    for i, line in enumerate(lines):
        candidates = re.findall('!\[\]\(.*?\)', line)
        if not candidates:
            f.write(line)
            continue

        for c in candidates:
            img_path = re.findall('h.*[a-zA-Z]', c)[0]
            c_changed = """<img src="{}" width={} height={}>""".format(img_path, width, height)
            line = line.replace(c, c_changed)

        f.write(line)

    f.close()

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

        conv_img_form(path, width, height)
    except IndexError as e:
        print('파일 경로를 명시해주세요!! (Ex./hsyang/seminar/rl/test.md)')