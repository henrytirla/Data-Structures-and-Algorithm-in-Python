"""A common punishment for school children is to write out a sentence multiple
times. Write a Python stand-alone program that will write out the
following sentence one hundred times: “I will never spam my friends
again.” Your program should number each of the sentences and it should
make eight different random-looking typos."""

import random

sentence = 'I will never spam my friends again.'
EightTypos = []
for i in range(8):
    EightTypos.append(sentence)
i = 0
while i < 8:
    s = ' '
    while s == ' ':
        num = random.randint(0, 8 * len(sentence))
        row = num // len(sentence)
        colum = num % len(sentence) - 1
        s = EightTypos[row][colum]

    ch = chr(random.choice(range(97, 123)))
    while ch == s:
        ch = chr(random.choice(range(97, 123)))
    EightTypos[row] = EightTypos[row][0:colum] + ch + EightTypos[row][colum + 1:len(sentence)]
    i += 1

for i in range(100 - 8):
    EightTypos.append(sentence)

random.shuffle(EightTypos)