import time

def from_roman(number):
    for blank in number:
        if blank == " "
            pass
        else:
            output-1 = output-1 + blank
    for blank in output-1:
        if blank == 'i' or 'I':
            out_num = out_num + 1
        if blank == 'v' or 'V':
            out_num = out_num + 5
        if blank == 'x' or 'X':
            out_num = out_num + 10
    return out_num
def to_roman (number):
    done = False
    output = ''
    while done == False:
        while float(number) > 9:
            output = output + 'X'
        while float(number) > 4:
            output = output + 'V'
        while float(number) > 0:
            output = output + 'I'
        done = True
    return output