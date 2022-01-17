def solution(s):
    text_ls = s.split(" ")
    answer_ls = []

    for text in text_ls:
        answer = ""
        for idx, elem in enumerate(text):
            if idx % 2 == 0:
                answer += elem.upper()
            else:
                answer += elem.lower()

        answer_ls.append(answer)

    return " ".join(answer_ls)