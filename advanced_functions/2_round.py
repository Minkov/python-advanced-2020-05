def to_round_list(values):
    return [round(x) for x in values]

print(
    to_round_list(map(float, input().split(' ')))
)