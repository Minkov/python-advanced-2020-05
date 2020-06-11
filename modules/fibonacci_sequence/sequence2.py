def generate_sequence(n):
    sequence = [0, 1]
    for i in range(2, n):
        sequence.append(sequence[i - 2] + sequence[i - 1])
    return sequence


def create_sequence(n):
    current_sequence = sequence[:n - 1]
    print(' '.join(str(x) for x in current_sequence))


def locate(number):
    if number in sequence:
        print(f'The number - {number} is at index {sequence.index(number)}')
    else:
        print(f'The number {number} is not in the sequence')


sequence = generate_sequence(1000)

