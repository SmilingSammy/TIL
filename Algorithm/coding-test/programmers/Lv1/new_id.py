import re


def solution(new_id):
    # step1
    new_id = new_id.lower()
    # step2
    new_id = re.sub("[^a-z0-9\-\_\.]", "", new_id)
    # step3
    new_id = re.sub("\.+", '.', new_id)
    # step4
    new_id = new_id.strip('.')

    # step5
    if not new_id:
        new_id = 'a'

    # step6
    if len(new_id) >= 16:
        new_id = new_id[:15]
        if new_id[-1] == '.':
            new_id = new_id[:-1]

    # step7
    if len(new_id) <= 2:
        new_id = new_id + (3 - len(new_id)) * new_id[-1]

    return new_id