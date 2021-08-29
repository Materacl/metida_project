import requests
from bs4 import BeautifulSoup as BS
import json

url = 'https://rus-ege.sdamgia.ru/test?theme=286&print=true'

text_to_replace = 'В одном из приведённых ниже предложений НЕВЕРНО употреблено выделенное слово. Исправьте лексическую ошибку, подобрав к выделенному слову пароним. Запишите подобранное слово.'


def main():
    r = requests.get(url)
    soup = BS(r.text, 'html.parser')
    print()

    tests_texts_raw = soup.find_all('div', class_='pbody')

    tests_texts = []
    for tests_text_raw in tests_texts_raw:
        task_lines_raw = tests_text_raw.find_all('p', class_='left_margin')
        print(task_lines_raw)

        if task_lines_raw[0].text != '':
            task_lines = task_lines_raw[0].text.replace(text_to_replace, '').split('.')

            for task_line in task_lines:
                if task_line == '':
                    task_lines.remove(task_line)
                elif len(task_line) < 10:
                    task_lines.remove(task_line)
                else:
                    task_line.strip()

            tests_texts.append(task_lines)

    tests_answers_raw = soup.find_all('div', class_='answer')

    tests_answers = []

    for tests_answer_raw in tests_answers_raw:
        tests_answers.append(tests_answer_raw.text.replace('Ответ: ', ''))

    print(tests_answers)
    print(tests_texts)

    tests = {}
    for tests_answer in tests_answers:
        tests[tests_answer] = tests_texts[tests_answers.index(tests_answer)]

    with open('data/ega_tests.json', 'w', encoding='utf8') as f:
        json.dump(tests, f, ensure_ascii=False)


if __name__ == '__main__':
    main()
