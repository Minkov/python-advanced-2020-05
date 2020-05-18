from collections import deque


def solve(people, tosses_count):
    people = deque(people)

    while people:
        people.rotate(-tosses_count + 1)
        person = people.popleft()

        if people:
            print(f'Removed {person}')
        else:
            print(f'Last is {person}')


# solve(
#     'George Peter Michael William Thomas'.split(' '),
#     10
# )
solve(
    input().split(' '),
    int(input())
)
