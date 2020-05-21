n = int(input())
names = {input() for _ in range(n)}
[print(name) for name in names]