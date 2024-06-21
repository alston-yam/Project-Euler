
words = {
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen",
    20: "twenty",
    30: "thirty",
    40: "forty",
    50: "fifty",
    60: "sixty",
    70: "seventy",
    80: "eighty",
    90: "ninety",
    100: "hundred",
    1000: "thousand"
}

number = 0

for i in range(1, 10):
    number += len(words[i])

number += 70

for i in range(20, 100):
    a = i % 10
    b = int((i - i%10)/10)
    if a == 0:
        number += len(words[i])
    else:
        number += len(words[b * 10]) + len(words[a])

for i in range(100, 1000):
    # cba
    a = i%10
    b = int((i-a)/10)%10
    c = (i - b*10 - a)/100
    if a == 0 and b == 0:
        number += len(words[c]) + len(words[100])
    elif b == 1:
        number += len(words[c]) + len(words[100]) + len("and") + len(words[b*10 + a])
    elif a == 0:
        number += len(words[c]) + len(words[100]) + len("and") + len(words[b*10])
    elif b == 0:
        number += len(words[c]) + len(words[100]) + len("and") + len(words[a])
    else:
        number += len(words[c]) + len(words[100]) + len("and") + len(words[b*10]) + len(words[a])

number += len("onethousand")
print(number)

