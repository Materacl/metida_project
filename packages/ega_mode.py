import io

filename = 'packages/data/ega_ex.txt'


def make_tests():
    with io.open(filename, encoding='utf-8') as f:
        tests_datas = f.readlines()

    answers = [answer.rstrip() for answer in tests_datas[5::6]]
    tasks = [task for task in tests_datas if task.rstrip() not in answers]

    tests = {}
    i = 0

    for answer in answers:
        tests[tuple(tasks[i:i + 5])] = answer
        i += 5

    tests_index = {}
    n = 0
    for test in tests.items():
        tests_index[n] = test
        n += 1
    return tests_index