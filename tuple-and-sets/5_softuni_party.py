def input_to_list(lines_count):
    return [input() for _ in range(lines_count)]


def input_to_list_until_command(command):
    result = []

    while True:
        line = input()
        if line == command:
            break
        result.append(line)

    return result

def get_not_arrived_guests(guests, guests_arrived):
    # guests_set = set(guests)
    # [guests_set.remove(guest) for guest in guests_arrived]
    # return guests_set
    return set(guests) - set(guests_arrived)

def print_result(result):
    result = sorted(result)
    print(len(result))
    [print(guest) for guest in result if guest[0].isdigit()]
    [print(guest) for guest in result if not guest[0].isdigit()]


guests = input_to_list(int(input()))
guests_arrived = input_to_list_until_command('END')

print_result(
    get_not_arrived_guests(guests, guests_arrived)
)
