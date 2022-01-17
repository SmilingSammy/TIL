import re
import sys

def convert_formula(file_path):
    with open(file_path, 'r') as f:
        lines = f.readlines()

    f = open(file_path, 'w')
    for line in lines:
        candidates = re.findall('\\$.*\\$', line)
        if not candidates:
            f.write(line)
            continue

        for c in candidates:
            c_changed = '$`{}`$'.format(c[1:-1])
            line = line.replace(c, c_changed)

        f.write(line)

    f.close()

if __name__ == '__main__':
    try:
        file_path = sys.argv[1]
        convert_formula(file_path)
    except IndexError as e:
        print('파일 경로를 명시해주세요!! (Ex./hsyang/seminar/rl/test.md)')
