from application.salary import calculate_salary
from application.people import get_employee
from datetime import datetime

if __name__ == '__main__':
    print(datetime.today())
    calculate_salary()
    get_employee()
