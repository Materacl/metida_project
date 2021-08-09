import io
filename = 'data/ega_ex.txt'

with io.open(filename, encoding='utf-8') as f:
    tests_datas = f.readlines()

answers = [answer.rstrip() for answer in tests_datas[5::6]]
tasks = [task for task in tests_datas if task.rstrip() not in answers]

tests = {}
i = 0

for answer in answers:
    tests[tuple(tasks[i:i+5])] = answer
    i += 5


