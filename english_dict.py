import sqlite3

MENU = """
########## SHELL DICTIONAY ##########
1 -> Search from the beggining of the word
2 -> Search from the end of the word
3 -> Search for any match
4 -> Search for exact match
5 -> Search on definition
9 -> Change limit
0 -> EXIT
"""

LIM=10

DB_FILE = 'dictionary.db'

def beggining_match(word, lim=10):
    word_list = []
    conn = sqlite3.connect(DB_FILE)
    crsr = conn.cursor()
    sql_command = f"SELECT * FROM entries WHERE word like '{word}%' LIMIT {lim}"
    crsr.execute(sql_command)
    data = crsr.fetchall()
    return data

def end_match(word, lim=10):
    word_list = []
    conn = sqlite3.connect(DB_FILE)
    crsr = conn.cursor()
    sql_command = f"SELECT * FROM entries WHERE word like '%{word}' LIMIT {lim}"
    crsr.execute(sql_command)
    data = crsr.fetchall()
    return data

def any_match(word, lim=10):
    word_list = []
    conn = sqlite3.connect(DB_FILE)
    crsr = conn.cursor()
    sql_command = f"SELECT * FROM entries WHERE word like '%{word}%' LIMIT {lim}"
    crsr.execute(sql_command)
    data = crsr.fetchall()
    return data

def exact_match(word, lim=10):
    word_list = []
    conn = sqlite3.connect(DB_FILE)
    crsr = conn.cursor()
    sql_command = f"SELECT * FROM entries WHERE word = '{word}' LIMIT {lim}"
    crsr.execute(sql_command)
    data = crsr.fetchall()
    return data

def definition_match(definition, lim=10):
    word_list = []
    conn = sqlite3.connect(DB_FILE)
    crsr = conn.cursor()
    sql_command = f"SELECT * FROM entries WHERE definition = '{definition}' LIMIT {lim}"
    crsr.execute(sql_command)
    data = crsr.fetchall()
    return data

while True:
    print(MENU)

    option = input('>')

    if option == '1':
        pattern = input('Word : ')
        words = beggining_match(pattern, LIM)
        print(f"########## Occurences : {len(words)} ##########")
        for i in words:
            print('Word -> ', i[0], f'({i[1]}) \n {i[2]} \n')

    elif option == '2':
        pattern = input('Word : ')
        words = end_match(pattern, LIM)
        print(f"########## Occurences : {len(words)} ##########")
        for i in words:
            print('Word -> ', i[0], f'({i[1]}) \n {i[2]} \n')

    elif option == '3':
        pattern = input('Word : ')
        words = any_match(pattern, LIM)
        print(f"########## Occurences : {len(words)} ##########")
        for i in words:
            print('Word -> ', i[0], f'({i[1]}) \n {i[2]} \n')

    elif option == '4':
        pattern = input('Word : ')
        words = exact_match(pattern, LIM)
        print(f"########## Occurences : {len(words)} ##########")
        for i in words:
            print('Word -> ', i[0], f'({i[1]}) \n {i[2]} \n')

    elif option == '5':
        pattern = input('Definition contains : ')
        words = exact_match(pattern, LIM)
        print(f"########## Occurences : {len(words)} ##########")
        for i in words:
            print('Word -> ', i[0], f'({i[1]}) \n {i[2]} \n')

    elif option == '9':
        l = input('New limit : ')
        if l.isdigit():
            LIM = int(l)
        else:
            print(f"Value {l} isn't a valid limit, please insert a number next.")


    elif option == '0':
        break

    else:
        print("*** This option doesn't exists ***")
