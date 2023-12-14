print('salary module start')
from datetime import datetime as dt
from application.clear_db import delete_db


def calculate_salary():
    today = dt.now().strftime('%d-%m-%Y')
    print('salary calculated: ', today)


if __name__ == '__main__':
    calculate_salary()
    delete_db()

print('salary module finish')