import io
import json

filename = 'packages/data/ega_tests_redacted.json'


def make_tests():
    with io.open(filename, encoding='utf-8') as f:
        tests_datas = json.load(f)

    answers = []

    for answer in tests_datas.keys():
        if answer.find('|') > -1:
            answer_splited = answer.split('|')
            answers.append(answer_splited[1])
        else:
            answers.append(answer.lower())

    tasks = []
    for text in tests_datas.values():
        for text_line in text:
            text[text.index(text_line)] = text_line.strip()
        tasks.append(text)

    tests = {}

    for answer in answers:
        tests[tuple(tasks[answers.index(answer)])] = answer

    tests_index = {}
    n = 0
    for test in tests.items():
        tests_index[n] = test
        n += 1

    return tests_index
