from datetime import datetime
import os, sqlite3

def writeToStorage(myinput, myoutput):
    path = os.getcwd()

    if not os.path.exists(path+'/storage/'):
        os.mkdir(path+'/storage/')
    
    time_now = datetime.now().strftime('%Y.%m.%d-%H.%M.%S')
    filename = path+'/storage/'+time_now+'.txt'

    with open(filename, 'w+') as f:
        f.write('INPUT:\n')
        f.write(str(myinput))
        f.write('\nOUTPUT:\n')
        f.write(str(myoutput))



def writeToDatabase(myinput, myoutput):
    path = os.getcwd()

    if not os.path.exists(path+'/database/'):
        os.mkdir(path+'/database/')

    # create database if first time
    # columns: id, input, output
    if not os.path.isfile(path+'/database/hoover_db.db'):
        connection = sqlite3.connect(path+'/database/hoover_db.db')
        cursor = connection.cursor()
        sql_command = 'CREATE TABLE data (id INTEGER PRIMARY KEY AUTOINCREMENT, input VARCHAR(500), output VARCHAR(50));'
        cursor.execute(sql_command)
    else:
        connection = sqlite3.connect(path+'/database/hoover_db.db')
        cursor = connection.cursor()

    parameters = (str(myinput), str(myoutput))
    cursor.execute('INSERT INTO data VALUES (NULL, ?, ?)', parameters)

    connection.commit()
    connection.close()



def printFromDatabase(filename = '../database/hoover_db.db', command='SELECT * FROM data ORDER BY id'):

    if os.path.isfile(filename):
        connection = sqlite3.connect(filename)
        cursor = connection.cursor()
        
        for row in cursor.execute(command):
            print(row)

        connection.close()
    else:
        print('Cannot find database ' + filename + '!')
    