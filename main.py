def highest_even(li):
    evens = []
    for item in li:
        if item % 2 == 0:
            evens.append((item))
    return max(evens)

    pass

print(highest_even([10,2,3,4,8,11]))

a= 'hellooooooooooooooooooooo'
if (n :=len(a)>10):
    print(f'too long {n}')

while ((n := len((a))>1)):
    print(n)
    a= a [:-1]
