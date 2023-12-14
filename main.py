print('start main.py')
import requests

import application.db.people as ppl
import application.salary as slr
from application.clear_db import delete_db  # import is safe because 'if __name__...'
# contains delete_db call in clear_db.py

resp = requests.get('https://netology.ru/')
print("'Main' module level process result: ", resp.status_code)


def calculate_salary():
    print('Wrong salary calculation')
    delete_db()


if __name__ == '__main__':
    slr.calculate_salary()
    ppl.get_employees()

print('main.py closed')
