def encode(message):
    output = ""
    for blank in message:
        if blank == "q":
            output = output + "q"
        if blank == "w":
            output = output + "p"
        if blank == "e":
            output = output + "w"
        if blank == "r":
            output = output + "o"
        if blank == "t":
            output = output + "e"
        if blank == "y":
            output = output + "i"
        if blank == "u":
            output = output + "r"
        if blank == "i":
            output = output + "u"
        if blank == "o":
            output = output + "t"
        if blank == "p":
            output = output + "a"
        if blank == "a":
            output = output + "s"
        if blank == "s":
            output = output + "d"
        if blank == "d":
            output = output + "f"
        if blank == "f":
            output = output + "g"
        if blank == "g":
            output = output + "h"
        if blank == "h":
            output = output + "l"
        if blank == "j":
            output = output + "k"
        if blank == "k":
            output = output + "j"
        if blank == "l":
            output = output + "z"
        if blank == "z":
            output = output + "v"
        if blank == "x":
            output = output + "x"
        if blank == "c":
            output = output + "c"
        if blank == "v":
            output = output + "b"
        if blank == "b":
            output = output + "n"
        if blank == "n":
            output = output + "m"
        if blank == "m":
            output = output + "1"
        if blank == "Q":
            output = output + "3"
        if blank == "W":
            output = output + "2"
        if blank == "E":
            output = output + "4"
        if blank == "R":
            output = output + "6"
        if blank == "T":
            output = output + "5"
        if blank == "Y":
            output = output + "9"
        if blank == "U":
            output = output + "8"
        if blank == "I":
            output = output + "7"
        if blank == "O":
            output = output + "0"
        if blank == "P":
            output = output + "!"
        if blank == "A":
            output = output + "@"
        if blank == "S":
            output = output + "#"
        if blank == "D":
            output = output + "$"
        if blank == "F":
            output = output + "~"
        if blank == "G":
            output = output + "^"
        if blank == "H":
            output = output + "&"
        if blank == "J":
            output = output + "*"
        if blank == "K":
            output = output + "("
        if blank == "L":
            output = output + ")"
        if blank == "Z":
            output = output + "X"
        if blank == "X":
            output = output + "M"
        if blank == "C":
            output = output + "L"
        if blank == "V":
            output = output + "P"
        if blank == "B":
            output = output + "O"
        if blank == "N":
            output = output + "I"
        if blank == "M":
            output = output + "J"
        if blank == "1":
            output = output + "H"
        if blank == "2":
            output = output + "Y"
        if blank == "3":
            output = output + "T"
        if blank == "4":
            output = output + "G"
        if blank == "5":
            output = output + "B"
        if blank == "6":
            output = output + ","
        if blank == "7":
            output = output + "."
        if blank == "8":
            output = output + "/"
        if blank == "9":
            output = output + ";"
        if blank == "0":
            output = output + "]"
        if blank == " ":
            output = output + "_"
    return output


def decode(message):
    counter = 0
    output = ""
    for blank in message:
        if blank == "_":
            output = output + " "
        if blank == "q":
            output = output + "q"
        if blank == "p":
            output = output + "w"
        if blank == "w":
            output = output + "e"
        if blank == "o":
            output = output + "r"
        if blank == "e":
            output = output + "t"
        if blank == "i":
            output = output + "y"
        if blank == "r":
            output = output + "u"
        if blank == "u":
            output = output + "i"
        if blank == "t":
            output = output + "o"
        if blank == "a":
            output = output + "p"
        if blank == "s":
            output = output + "a"
        if blank == "d":
            output = output + "s"
        if blank == "f":
            output = output + "d"
        if blank == "g":
            output = output + "f"
        if blank == "h":
            output = output + "g"
        if blank == "l":
            output = output + "h"
        if blank == "k":
            output = output + "j"
        if blank == "j":
            output = output + "k"
        if blank == "z":
            output = output + "l"
        if blank == "v":
            output = output + "z"
        if blank == "x":
            output = output + "x"
        if blank == "c":
            output = output + "c"
        if blank == "b":
            output = output + "v"
        if blank == "n":
            output = output + "b"
        if blank == "m":
            output = output + "n"
        if blank == "1":
            output = output + "m"
        if blank == "3":
            output = output + "Q"
        if blank == "2":
            output = output + "W"
        if blank == "4":
            output = output + "E"
        if blank == "6":
            output = output + "R"
        if blank == "5":
            output = output + "T"
        if blank == "9":
            output = output + "Y"
        if blank == "8":
            output = output + "U"
        if blank == "7":
            output = output + "I"
        if blank == "0":
            output = output + "O"
        if blank == "!":
            output = output + "P"
        if blank == "@":
            output = output + "A"
        if blank == "-":
            output = output + "S"
        if blank == "#":
            output = output + "D"
        if blank == "~":
            output = output + "F"
        if blank == "$":
            output = output + "G"
        if blank == "=":
            output = output + "H"
        if blank == "%":
            output = output + "J"
        if blank == "+":
            output = output + "K"
        if blank == "^":
            output = output + "L"
        if blank == "A":
            output = output + "Z"
        if blank == "&":
            output = output + "X"
        if blank == "S":
            output = output + "C"
        if blank == "*":
            output = output + "V"
        if blank == "Q":
            output = output + "B"
        if blank == "(":
            output = output + "N"
        if blank == "W":
            output = output + "M"
        if blank == ")":
            output = output + "1"
        if blank == "Z":
            output = output + "2"
        if blank == "X":
            output = output + "3"
        if blank == "M":
            output = output + "4"
        if blank == "L":
            output = output + "5"
        if blank == "P":
            output = output + "6"
        if blank == "O":
            output = output + "7"
        if blank == "I":
            output = output + "8"
        if blank == "J":
            output = output + "9"
    return  output

def encodefile(file_name):
    f = open(file_name, "r")
    unincrypted_file = f.read()
    f = open(file_name, "w")
    f.write(encode(unincrypted_file))

def decodefile(file_name):
    f = open(file_name, "r")
    encrypted_file = f.read()
    f.close()
    f = open(file_name, "w")
    f.write(" ")
    f.write(decode(encrypted_file))
    f.close()
