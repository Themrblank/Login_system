import sqlite3

conn = sqlite3.connect('registration.db')  
cursor = conn.cursor()
failed_attempts = 0  

conn.execute('''
    CREATE TABLE IF NOT EXISTS users(
             username TEXT,
             password TEXT
    )
''')

conn.commit()
conn.close()

def login_system():
    global failed_attempts
    action = input('Press l for login, r for register, x to exit: ')  
    if action == 'l':
        login()
    elif action == 'r':
        register()
    elif action == 'x':
        print('Goodbye!')  
        exit()
    else:
        print('Invalid action')
        login_system()

def register():
    conn = sqlite3.connect('registration.db')
    cursor = conn.cursor()
    username = input('What is your username? ')  
    password = input('Create a password: ')  
    conn.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, password))
    conn.commit()
    conn.close()

def login():
    global failed_attempts
    conn = sqlite3.connect('registration.db')
    cursor = conn.cursor()
    username = input('What is your username? ') 
    password = input('Enter your password: ')  
    cursor.execute('SELECT * FROM users WHERE username = ? AND password = ?', (username, password))
    user = cursor.fetchone()
    if user:
        print('Welcome!')
    else:
        failed_attempts += 1
        if failed_attempts < 3:
            print('Incorrect login!')
            login_system()  
        else:
            print('Too many failed attempts!')
            exit()
    conn.commit()
    conn.close()

login_system()
