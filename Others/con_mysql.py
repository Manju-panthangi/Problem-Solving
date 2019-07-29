from __future__ import print_function
from datetime import date, datetime, timedelta
import mysql.connector

cnx = mysql.connector.connect(user='root', password='root')
cursor = cnx.cursor()

DB_NAME = 'emp123'
# cursor.execute("CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(DB_NAME))
cursor.execute("USE {}".format(DB_NAME))

# TABLES = {}
# TABLES['employees'] = (
#     "CREATE TABLE `employees` ("
#     "  `emp_no` int(11) NOT NULL AUTO_INCREMENT,"
#     "  `birth_date` date NOT NULL,"
#     "  `first_name` varchar(14) NOT NULL,"
#     "  `last_name` varchar(16) NOT NULL,"
#     "  `gender` enum('M','F') NOT NULL,"
#     "  `hire_date` date NOT NULL,"
#     "  PRIMARY KEY (`emp_no`)"
#     ") ENGINE=InnoDB")

# TABLES['salaries'] = (
#     "CREATE TABLE `salaries` ("
#     "  `emp_no` int(11) NOT NULL,"
#     "  `salary` int(11) NOT NULL,"
#     "  `from_date` date NOT NULL,"
#     "  `to_date` date NOT NULL,"
#     "  PRIMARY KEY (`emp_no`,`from_date`), KEY `emp_no` (`emp_no`),"
#     "  CONSTRAINT `salaries_ibfk_1` FOREIGN KEY (`emp_no`) "
#     "     REFERENCES `employees` (`emp_no`) ON DELETE CASCADE"
#     ") ENGINE=InnoDB")

# for table_name in TABLES:
#     table_description = TABLES[table_name]
#     cursor.execute(table_description)

# tomorrow = datetime.now().date() + timedelta(days=1)

# add_employee = ("INSERT INTO employees "
#                 "(first_name, last_name, hire_date, gender, birth_date) "
#                 "VALUES (%s, %s, %s, %s, %s)")
# add_salary = ("INSERT INTO salaries "
#                 "(emp_no, salary, from_date, to_date) "
#                 "VALUES (%(emp_no)s, %(salary)s, %(from_date)s, %(to_date)s)")

# data_employee = ('Geert', 'Vanderkelen', tomorrow, 'M', date(1977, 6, 14))

# # Insert new employee
# cursor.execute(add_employee, data_employee)
# emp_no = cursor.lastrowid

# # Insert salary information
# data_salary = {
#     'emp_no': emp_no,
#     'salary': 50000,
#     'from_date': tomorrow,
#     'to_date': date(9999, 1, 1),
# }
# cursor.execute(add_salary, data_salary)

# # Make sure data is committed to the database
# cnx.commit()

query = ("SELECT first_name, last_name, hire_date FROM employees "
            "WHERE hire_date BETWEEN %s AND %s")

hire_start = date(2019, 1, 1)
hire_end = date(2019, 12, 31)

cursor.execute(query, (hire_start, hire_end))
# cursor.execute(query)

for (first_name, last_name, hire_date) in cursor:
    print("{}, {} was hired on {:%d %b %Y}".format(last_name, first_name, hire_date))

cursor.close()
cnx.close()