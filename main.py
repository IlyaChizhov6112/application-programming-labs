
import argparse
import re
import datetime



def get_file() -> str:
    parser = argparse.ArgumentParser()
    parser.add_argument('file', type=str, help='name of the file')
    args = parser.parse_args()
    return args.file
def read(file: str) -> str:
    with open(file, "r", encoding="utf-8") as file:
        return file.read()
def find(text: str) -> int:
    pattern=r"\d{2}.\d{2}.\d{4}"
    numbers = re.findall(pattern, text)
    count=0
    for i in numbers:
        birthday = datetime.datetime.now() - datetime.datetime.strptime(i, "%d.%m.%Y")
        if 30 <= (birthday.days / 365) <= 40:
            count += 1
    return count
def main():
    file=get_file()
    try:
        text=read(file)
        print(f"Количество людей от 30 до 40:",  find(text))
    except FileNotFoundError:
        print(f"Файл не найден")
if __name__ == "__main__":
    main()
