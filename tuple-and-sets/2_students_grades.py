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


def count_student_marks(values):
    students_marks = {}

    for value in values:
        (student, mark) = value.split(' ')
        if student not in students_marks:
            students_marks[student] = []
        students_marks[student].append(float(mark))

    return students_marks


def avg(values):
    return sum(values) / len(values)


def print_result(students_marks):
    for (student_name, marks) in students_marks.items():
        avg_mark = avg(marks)
        marks_string = ' '.join(f'{mark:.2f}' for mark in marks)
        print(f'{student_name} -> {marks_string} (avg: {avg_mark:.2f})')

# test_input = [
#     'Peter 5.20',
#     'Mark 5.50',
#     'Peter 3.20',
#     'Mark 2.50',
#     'Alex 2.00',
#     'Mark 3.46',
#     'Alex 3',
# ]

test_input = input_to_list(int(input()))

print_result(count_student_marks(test_input))
