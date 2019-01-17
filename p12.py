# -*- coding: utf-8 -*-


def load_blocked():
    with open('to.txt', encoding='utf-8') as f:
        blocked_words = [l.strip() for l in f.readlines() if l]
        # blocked_words = []
        # for l in f.readlines():
        #     if l:
        #         blocked_words.append(l.strip())
    return blocked_words


def words_filter(text, blocked, symbol='*'):
    for w in blocked:
        text = text.replace(w, symbol * len(w))
        # 这里用 w.decode(charset) 的长度，是为了将字符传转为 unicode 再计算长度
        # 否则一个中文字符的长度会是 2 或者 3，这里 charset 默认 utf-8，也可调用时指定
        # Python 3 没有这个问题了
    return text


if __name__ == '__main__':
    while True:
        textjudge = input('请输入一段文字（直接回车退出）：\n')
        if not textjudge:
            break
        print(words_filter(textjudge, load_blocked()))
