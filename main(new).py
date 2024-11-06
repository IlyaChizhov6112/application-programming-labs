import argparse
import datetime
import re


def get_file() -> str:
    """
    Функция, которая получает имя файла из аргументов командной строки
    :return: имя файла
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('file', type = str, help = 'name of the file')
    args = parser.parse_args()
    return args.file


def read(file: str) -> str:
    """
    Функция, которая читает содержимое файла
    :param: file: имя файла
    :return: содержимое файла
    """
    with open(file, "r", encoding = "utf-8") as file:
        return file.read()


def find_dates(text: str) -> list:
    """
    Функция, которая находит даты рождения
    :param: text: содержимое файла
    :return: даты рождения
    """
    pattern = r"\d{2}.\d{2}.\d{4}"
    numbers = re.findall(pattern, text)
    return numbers


def counting (text: str) -> int:
    """
    Функция, которая считает сколько людей возраста от 30 до 40

    :param: text: содержимое файла
    :return: число человек возрастом от 30 до 40
    """
    numbers = find_dates(text)
    count = 0
    for i in numbers:
        age = datetime.datetime.now() - datetime.datetime.strptime(i, "%d.%m.%Y")
        if 30 <= (age.days / 365) <= 40:
            count += 1
    return count


def main():
    file = get_file()
    try:
        text=read(file)
        print(f"Количество людей от 30 до 40:", counting(text))
    except FileNotFoundError:
        print(f"Файл не найден")


if __name__ == "__main__":
    main()
