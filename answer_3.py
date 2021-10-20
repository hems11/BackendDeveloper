import sqlite3
import csv
from datetime import date

#question 1
def repair_order(arr):
    repair_time = 1 
    for x in arr:
        print(x)
a1 = [
        {'id':'f1', 'deadline':2, 'profit': 60 },
        {'id': 'f2', 'deadline': 1, 'profit': 100},
        {'id': 'f3', 'deadline': 3, 'profit': 20},
        {'id': 'f4', 'deadline': 2, 'profit': 40},
        {'id': 'f5', 'deadline': 1, 'profit': 20}
    ]
print("Answer of Question 1")    
repair_order(a1)

#question 2
def reconstruct_string(input_string):
    seen = input_string[0]
    ans = input_string[0]
    for i in input_string[1:]:
        if i != seen:
            ans += i
            seen = i
    return ans

string = "boooooo"
print("Answer of Question 2 \n",reconstruct_string(string))


#question 3
def create_db():
    conn = sqlite3.connect('emp.db') 
    c = conn.cursor()

    file_open = open("employee_info.csv")
    rows = csv.reader(file_open)
    
    c.execute('''CREATE TABLE IF NOT EXISTS employee(SL_NO int ,first_name text,last_name text,Gender text,birth_date date,annual_salary int)''')
    
    c.executemany("INSERT INTO employee VALUES (?, ?, ?, ?, ?, ?)", rows)

    c.execute(''' ALTER TABLE employee ADD COLUMN age int''')


    sql= "SELECT birth_date FROM employee"
    result = c.execute(sql)
    today = date.today()
    for x in result:
        age = today.year - x.year - ((today.month, today.day) < (x.month, x.day))
    

    conn.commit()
    conn.close()          
print("Answer of Question 3")
create_db()