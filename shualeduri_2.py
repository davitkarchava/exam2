# სავარჯიშო_1

import sqlite3


def db_connection(file):
    return sqlite3.connect(file)


def moc_2(conn):
    cursor = conn.cursor()
    count = cursor.execute("SELECT COUNT(*) FROM students WHERE SelfStudyHour < 2 ")
    for i in count:
        print(i)


def moc_3(conn):
    device = input("მოწყობილობა: ")
    age = int(input("ასაკი: "))
    cursor = conn.cursor()
    count = cursor.execute("SELECT COUNT(*) FROM students WHERE Device = ? and Age = ?", (device, age))
    for i in count:
        print(i)


def moc_4(conn):
    cursor = conn.cursor()
    cursor.execute("""INSERT INTO students(AGE,
    OnlineClassTime, Device, SelfStudyHour,
    FitnessTime, Sleep, SocialMedia, SocialMediaPlatform)
    VALUES (18, 20, "phone", 5, 4, 8, 7, "google");
    """)
    conn.commit()


def mpc_5(conn):
    cursor = conn.cursor()
    cursor.execute("UPDATE students SET  SocialMediaPlatform = 'data' WHERE age <> 21")
    conn.commit()


def main():
    conn = db_connection("survey.sqlite")
    moc_2(conn)
    moc_4(conn)
    moc_3(conn)
    mpc_5(conn)
    conn.close()


main()

# სავარჯიშო_2


import json


with open('sample (1).json') as user_file:
    file_contents = user_file.read()
user_file.close()
print(file_contents)

parsed_json = json.loads(file_contents)
print(parsed_json["person"]["address"])

for i in range(len(parsed_json["person"]["friends"])):
    print(parsed_json["person"]["friends"][i]["name"])

