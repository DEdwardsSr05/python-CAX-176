numbers = list(range(1, 21))
multiples_of_three = []

for num in numbers:
    if num % 3 == 0:
        multiples_of_three.append(num)

print(multiples_of_three)