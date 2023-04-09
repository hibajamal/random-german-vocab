# -*- coding: utf-8 -*-
import random

f = open('foundations.txt', encoding='utf-8')

print("Level: Foundations.")
words = f.readlines()
random.shuffle(words)

print("Words:", len(words))

score = 0
total = 0

for line in words:
	total += 1

	l = line.split(',')
	print(total, ". Word:", l[0])
	m = input("Meaning? ")
	if m == 'EXIT' or len(m) == 0:
		print("You either exited the game or did not respond. Bye.")
		print("BTW the meaning of this word was \'{}\'".format(l[1].strip()))
		break
	elif m.strip() in l[1]:
		score += 1
	msg = 'Correct! Meaning was \''+l[1].strip()+'\'\n' if m.strip() in l[1] else 'Incorrect! Meaning was \''+l[1].strip()+'\'\n'
	print(msg)
	if len(l)>2:
		print("Example: ", l[2])

total = 1 if total == 1 else total-1

print("\nYour score:", score, 'out of', total, 'correct.', round((score/total)*100,2), '%')
f.close()