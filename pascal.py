#!/bin/python
import shutil
from math import factorial

# print pascal's triangle

# SGR color constants
# rene-d 2018


colours = {
    "black": "\033[0;30m",
    "red": "\033[0;31m",
    "green": "\033[0;32m",
    "brown": "\033[0;33m",
    "blue": "\033[0;34m",
    "purple": "\033[0;35m",
    "cyan": "\033[0;36m",
    "light_gray": "\033[0;37m",
    "dark_gray": "\033[1;30m",
    "light_red": "\033[1;31m",
    "light_green": "\033[1;32m",
    "yellow": "\033[1;33m",
    "light_blue": "\033[1;34m",
    "light_purple": "\033[1;35m",
    "light_cyan": "\033[1;36m",
    "light_white": "\033[1;37m",
    "bold_black": "\033[0;90m",
    "bold_red": "\033[0;91m",
    "bold_green": "\033[0;92m",
    "bold_brown": "\033[0;93m",
    "bold_blue": "\033[0;94m",
    "bold_purple": "\033[0;95m",
    "bold_cyan": "\033[0;96m",
    "bold_light_gray": "\033[0;97m",
    "bold_dark_gray": "\033[1;90m",
    "bold_light_red": "\033[1;91m",
    "bold_light_green": "\033[1;92m",
    "bold_yellow": "\033[1;93m",
    "bold_light_blue": "\033[1;94m",
    "bold_light_purple": "\033[1;95m",
    "bold_light_cyan": "\033[1;96m",
    "bold_light_white": "\033[1;97m",
}

used_colours = [
    "bold_red",
    "bold_green",
    "bold_blue",
    "bold_purple",
    "bold_cyan",
    "bold_light_red",
    "bold_light_green",
    "bold_yellow",
    "bold_light_blue",
    "bold_light_purple",
    "bold_light_cyan",
]
used_colours = ["light_white", "bold_light_gray"]

termwidth = shutil.get_terminal_size().columns

greek = [
    chr(int(x, base=16))
    for x in [
        "0x03b1",  # alpha
        "0x03b2",  # beta
        "0x03b3",  # gamma
        "0x03b4",  # delta
        "0x03b5",  # epsilon
        "0x03b6",  # zeta
        "0x03b7",  # eta
        "0x03b8",  # theta
        "0x03b9",  # iota
        "0x03ba",  # kappa
        "0x03bb",  # lambda
        "0x03bc",  # mu
        "0x03be",  # xi
        "0x03c0",  # pi
        "0x03c1",  # rho
        "0x03c3",  # sigma
        "0x03c4",  # tau
        "0x03c6",  # phi
        "0x03c8",  # psi
        "0x03c9",  # omega
        "0x0393",  # capital gamma
        "0x0394",  # capital delta
        "0x0398",  # capital theta
        "0x039b",  # capital lambda
        "0x039e",  # capital xi
        "0x03a0",  # capital pi
        "0x03a3",  # capital sigma
        "0x03a6",  # capital phi
        "0x03a9",  # capital omega
    ]
]

cyrillic = [
    chr(int(x, base=16))
    for x in [
        "0x0431",  # be
        "0x0434",  # de
        "0x0436",  # zhe
        "0x0437",  # ze
        "0x0438",  # i
        "0x043b",  # el
        "0x0446",  # tse
        "0x0447",  # che
        "0x0448",  # sha
        "0x0449",  # shcha
        "0x044a",  # hard sign
        "0x044b",  # yery
        "0x044c",  # soft sign
        "0x044d",  # e
        "0x044e",  # yu
        "0x044f",  # ya
        "0x0411",  # capital be
    ]
]


def digit_to_string(digit):
    if digit < 10:
        return str(digit)
    elif digit < 36:
        return chr(ord("a") + digit - 10)
    elif digit < 62:
        return chr(ord("A") + digit - 36)
    elif digit < 62 + len(greek):
        return greek[digit - 62]
    elif digit < 62 + len(greek) + len(cyrillic):
        return cyrillic[digit - 62 - len(greek)]


base = int(input(f"Enter base (maximum {62 + len(greek) + len(cyrillic)}): "))


def tobase(n, base):
    if n == 0:
        return "0"
    digits = []
    while n:
        digits.append(int(n % base))
        n //= base
    return "".join([digit_to_string(x) for x in digits[::-1]])


i = 0
linewidth = 0
lines = []
last_linewidth = 0
while linewidth < termwidth - len(str(i)) - 1:
    line = []
    for k in range(0, i + 1):
        val = int(factorial(i) / (factorial(k) * factorial(i - k)))
        line.append(tobase(val, base))
    last_linewidth = linewidth
    linewidth = sum([len(x) for x in line]) + len(line) - 1
    if linewidth < termwidth - len(str(i)) - 1:
        lines.append(line)
    i += 1

termwidth -= len(str(i)) + 1

offset = int((termwidth - last_linewidth) / 2)
output = [" " * offset + " ".join(lines[-1])]
poss = [
    offset + sum([len(x) for x in lines[-1][: j + 1]]) + j
    for j in range(len(lines[-1]))
]
for i, line in enumerate(lines[-2::-1]):
    new_poss = []
    cursor = 0
    output_line = ""
    endpoint = poss[0]
    for j, val in enumerate(line):
        centrepoint = poss[j]
        startpoint = centrepoint - len(val) // 2
        new_poss.append(endpoint + (startpoint - endpoint) // 2)
        endpoint = startpoint + len(val)
        output_line += " " * (startpoint - cursor)
        output_line += val
        cursor = startpoint + len(val)
    output.append(output_line)
    poss = new_poss[1:]
    offset += 1
print(
    "\n".join(
        [
            colours[used_colours[i % len(used_colours)]] + str(i) + " " + x
            for i, x in enumerate(output[::-1])
        ]
    )
)
