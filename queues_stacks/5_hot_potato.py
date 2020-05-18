from collections import deque


def solve(people, tosses_count):
    people = deque(people)
    index = 0

    while people:
        index += 1
        person = people.popleft()
        if index == tosses_count:
            if people:
                index = 0
                print(f'Removed {person}')
            else:
                print(f'Last is {person}')
        else:
            people.append(person)


# solve(
#     'George Peter Michael William Thomas'.split(' '),
#     10
# )
solve(
    input().split(' '),
    int(input())
)
