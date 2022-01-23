from datetime import datetime
def solution(a, b):
    return datetime(2016, a, b).strftime(format="%A")[:3].upper()