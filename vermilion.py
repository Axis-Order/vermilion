import sys


args = sys.argv


def encode(text):
    counter = 0
    w = ''
    with open("compressed.txt", "w") as wf:
        now_char = text[0]
        for c in text:
            if now_char == c:
                counter += 1
                now_char = c
            else:
                w += "+" + str(counter) + ":" + now_char + ';'
                now_char = c
                counter = 1
        w += "+" + str(counter) + ":" + now_char + ';'
        wf.write(w)
    return


def decode(text):
    now_char = ''
    tmp = ''
    is_digit = False
    is_char = False
    counter = 0
    num = 0
    wtext = ''
    is_convert = False
    print(text)
    with open("decode.txt", "w") as wf:
        for c in text:
            if c == '+':
                is_digit = True
                continue
            elif is_char:
                wtext = wtext + c * num
                is_char = False
                continue
            elif is_digit:
                if c == ':':
                    is_digit = False
                    is_char = True
                    counter = 0
                    num = int(tmp)
                    tmp = ''
                    continue
                tmp += c
                counter += 1
        wf.write(wtext)
    return




if __name__ == '__main__':
    src = input()
    if args[1] == 'c':
    #if False:
        with open(src, 'r') as f:
            text = f.read()
            encode(text)
    elif args[1] == 'x':
    #elif True:
        with open(src, 'r') as f:
            text = f.read()
            decode(text)

