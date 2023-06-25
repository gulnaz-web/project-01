import sqlite3;

# ------------------ создание таблицы Students ------------------
# connection = sqlite3.connect('teachers.db')
# cursor = connection.cursor()
# query = """
#     CREATE TABLE Students (
#         Student_Id INTEGER,
#         Student_Name TEXT,
#         School_Id INTEGER PRIMARY KEY
#     );
# """
# cursor.execute(query)
# connection.commit()
# connection.close()



# ------------------ заполнение таблицы Students ------------------
# connection = sqlite3.connect('teachers.db')
# cursor = connection.cursor()
# query = """
#     INSERT INTO Students (Student_Id, Student_Name, School_Id) 
#     VALUES
#     (201, 'Иван', 1),
#     (202, 'Петр', 2),
#     (203, 'Анастасия', 3),
#     (204, 'Игорь', 4);
# """
# cursor.execute(query)
# connection.commit()
# connection.close()



# ------------------ получение информации о школе и студенте  ------------------
# ------------------ 1 способ (не связаны вместе) ------------------
# def get_connection():
#     connection = sqlite3.connect('teachers.db')
#     return connection

# def close_connection(connection): 
#     if connection:
#         connection.close()

# def get_student(student_id):
#     try:
#         connection = get_connection()
#         cursor = connection.cursor()
#         query = '''
#             SELECT * FROM Students
#             WHERE Student_id = ?
#         '''
#         cursor.execute(query, (student_id,))
#         records = cursor.fetchall()
        
#         for row in records:
#             print(f'ID Студента: {row[0]}')
#             print(f'Имя студента школы: {row[1]}')
#         close_connection(connection)
#     except (Exception, sqlite3.Error) as error:
#         print(f'Ошибка в получении данных {error}')
# get_student(201)

# def get_school(school_id):
#     try:
#         connection = get_connection()
#         cursor = connection.cursor()
#         query = '''
#             SELECT * FROM School
#             WHERE School_id = ?
#         '''
#         cursor.execute(query, (school_id,))
#         records = cursor.fetchall()
        
#         for row in records:
#             print(f'ID школы: {row[0]}')
#             print(f'Название школы: {row[1]}')
#         close_connection(connection)
#     except (Exception, sqlite3.Error) as error:
#         print(f'Ошибка в получении данных {error}')
# get_school(3)

# ------------------ 2 способ (связаны) ------------------
def get_connection():
    connection = sqlite3.connect('teachers.db')
    return connection

def close_connection(connection): 
    if connection:
        connection.close()

def get_school(school_id):
    try:
        connection = get_connection()
        cursor = connection.cursor()
        query = '''
            SELECT * FROM School
            WHERE School_id = ?
            '''
        cursor.execute(query, (school_id,))
        records = cursor.fetchall()
        for school in records:
            return school[1]
        close_connection(connection)
    except (Exception, sqlite3.Error) as error:
        print(f'Ошибка в получении данных {error}')

def get_student(student_id):
    try:
        connection = get_connection()
        cursor = connection.cursor()
        query = '''
            SELECT * FROM Students
            WHERE Student_id = ?
            '''
        cursor.execute(query, (student_id,))
        records = cursor.fetchall()
        for row in records:
            print(f'ID Студента: {row[0]}')
            print(f'Имя студента школы: {row[1]}')
            print(f'ID школы: {row[2]}')
            print(f'Название школы: {get_school(row[2])}')
        close_connection(connection)
    except (Exception, sqlite3.Error) as error:
        print(f'Ошибка в получении данных {error}')

get_student(202)
