name = input('What is your name? ')

words = name.split(" ")

for word in words:
    lastindex = len(word) -1
    for index in range (lastindex, -1, -1):
        print(word[index], end='')
    print(end=' ')
print(end='\n')


name = input('What is your name? ')

first, last = name.split()
print(first[::1], last[::-1])
