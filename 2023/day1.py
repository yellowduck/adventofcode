"""
--- Day 1: Trebuchet?! ---

https://adventofcode.com/2023/day/1
"""
import re

textnums = {
    "one":"1",  "1":"1",
    "two":"2",  "2":"2",
    "three":"3",  "3":"3",
    "four":"4",  "4":"4",
    "five":"5",  "5":"5",
    "six":"6",  "6":"6",
    "seven":"7",  "7":"7",
    "eight":"8",  "8":"8",
    "nine":"9",  "9":"9",
}

def text_to_num(match):
    return textnums.get(match,"")

# def extract_numbers(line):

def problem(part=1, input=None):
    if not input:
        data = open("day1.input", "rt").read().split()
    else:
        data = input.split("\n")

    if part==1:
        pattern = r"\d"
    else:
        # detect overlapping using neagtive look behind
        # re.findall(pattern, "oneight")
        pattern = r"(?<![eont])one|two|three|four|five|six|seven|eight|nine|\d"
        # pattern = r"one|two|three|four|five|six|seven|eight|nine|\d"

    calibration = 0
    # Part 1
    # for line in data:
    #     n = re.findall(r"\d", line)
    #     if len(n) == 1:
    #         n.append(n[0])
    #     calibration += int(n[0]+n[-1])

    for line in data:
        n = list(map(text_to_num, re.findall(pattern, line)))
        # n = re.sub(pattern, text_to_num, line)
        if len(n) == 1:
            n.append(n[0])
        calibration += int(n[0]+n[-1])
        print(f"{n[0]}{n[-1]}:{line=} {n=} {calibration=}")

    return calibration

if __name__ == '__main__':

    # test="1abc2\npqr3stu8vwx\na1b2c3d4e5f\ntreb7uchet"
    # assert problem(1, test)==142

    # print(f"Part 1: {problem(1)}")
    # assert problem(1)==54916

    # # check that last entry is used
    # test="two1nine\neightwothree\nabcone2threexyz\nxtwone3four\n4nineeightseven2\nzoneight234\n7pqrstsixteen"
    # assert problem(2, test)==281

    print(f"Part 2: {problem(2)}")
    # 547002 too low
    # 54812 too high
