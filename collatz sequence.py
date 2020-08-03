
def collatz_rule(number):
    if number % 2 == 0:
        number = number / 2
    else:
        number = (3*number) + 1
    return number

def collatz_sequence(n):
    q = []
    q.append(n)
    while n != 1:
        n = collatz_rule(n)
        q.append(n)
    return len(q)

longest = 0
for i in range(1, 1000000):
    a = collatz_sequence(i)
    if longest < a:
        longest = a
        print("starting num: ", i, " length: ", a)
