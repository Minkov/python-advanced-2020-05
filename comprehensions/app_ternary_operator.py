# print 'even' if the number is even,
# and 'odd' if the number is odd

x = int(input())

even_message = 'The number is even'
odd_message = 'The number is odd'

if x % 2 == 0:
    print(even_message)
else:
    print(odd_message)

result = even_message \
    if x % 2 == 0 \
    else odd_message

print(result)
