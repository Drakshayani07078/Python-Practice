rows = 4
col = 5
for i in range(rows):
    for j in range(col):
        print('*',end=' ')
    print()

print()
for i in range(rows):
    for j in range(i+1):
        print('*',end=' ')
    print()
print()
for i in range(rows):
    for j in range(i, rows):
        print('*',end=' ')
    print()

for i in range(rows):
    for j in range(i+1):
        print('*',end=' ')
    print()
for i in range(rows):
    for j in range(i, rows-1):
        print('*',end=' ')
    print()