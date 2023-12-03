"""
--- Day 1: Trebuchet?! ---

https://adventofcode.com/2023/day/1

try 1 & 2 used regex to try and match the words
findall does not perform overlapping matches which complicates things
trying with lookahead (?) did not produce the required effect, probably
because of the use of digits as well

lookahead needed to be around the whole search and not at beginning
as per the examples i was using

second attempt was very clunky by looking backwards into the string

"""
import re
textnums = [
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
]

def text_to_num(t):
    """If in list return index value otherwise assume a digit
    """
    if t in textnums:
        return str(textnums.index(t)+1)
    else:
        return t

def problem(part=1, input=None):
    if not input:
        data = open("day1.input", "rt").read().split()
    else:
        data = input.split("\n")

    calibration = 0

    if part==1:
        pattern = r"\d"
    else:
        pattern = f"(?=({'|'.join(textnums)}|\\d))"

    for line in data:
        f = list(map(text_to_num, (re.findall(pattern, line))))
        calibration += int(f[0]+f[-1])
        # print(f"{n[0]}{n[-1]}:{line=} {n=} {calibration=}")

    return calibration

if __name__ == '__main__':

    test="1abc2\npqr3stu8vwx\na1b2c3d4e5f\ntreb7uchet"
    assert problem(1, test)==142

    print(f"Part 1: {problem(1)}")
    assert problem(1)==54916

    # check that last entry is used
    test="two1nine\neightwothree\nabcone2threexyz\nxtwone3four\n4nineeightseven2\nzoneight234\n7pqrstsixteen"
    assert problem(2, test)==281

    print(f"Part 2: {problem(2)}")
    assert problem(2)==54728
    # 547002 too low
    # 54812 too high
