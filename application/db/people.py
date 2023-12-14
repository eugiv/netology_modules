print('people module start')
from datetime import datetime as dt


def get_employees():
    today = dt.now().strftime('%d-%m-%Y')
    print("I'm employee: ", today)


if __name__ == '__main__':
    get_employees()

print('people module finish')
