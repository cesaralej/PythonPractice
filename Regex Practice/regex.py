import re

hand = open('actual.txt')
tex = ''

for line in hand:
  tex += line

numbs = re.findall('[0-9]+', tex)
sum = 0

for numb in numbs:
  sum += int(numb)

print(sum)

print( sum( [ int(i) for i in re.findall('[0-9]+', open('actual.txt').read()) ] ) )