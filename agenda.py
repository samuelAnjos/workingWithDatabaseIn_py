import os
import sqlite3
from sqlite3 import Error

#making connection

def bankConnection():
    way = "D:\\1_python\\bd\\agenda.db"
    connection = None

    try:
        connection = sqlite3.connect(way)
    except Error as ex:
        print(ex)
    return connection

variableConnection = bankConnection()

#database request functions (Insert, Udpate, Delete)
def queryInsertUpdateDelete(connection, sql):
    try:
        temp = connection.cursor()
        temp.execute(sql)
        connection.commit()
    except Error as ex:
        print(ex)
    finally:
        print('Successful Operation')
        #connection.close()

#database request functions (Query)
def queryConsult(connection, sql):
    temp = connection.cursor()
    temp.execute(sql)
    response = temp.fetchall()
    #connection.close()
    return response




def mainFunctionMenu():
    os.system("cls")
    os.system("cls")
    print('1 - Insert New Record')
    print('2 - Delete Record')
    print('3 - Update Record')
    print('4 - See All Registration')
    print('5 - See Registration by Name')
    print('6 - Exit')

def consultByName():
    name  = input('Enter the name')
    variableSQL = "SELECT * FROM TB_CONTATOS WHERE T_NOMECONTATO LIKE '%"+name+"%'"
    record = queryConsult(variableConnection, variableSQL)
    limit = 10
    count = 0
    for r in record:
        print("ID:{0:_<3} Name:{1:_<30} Telephone:{2:_<14} E-mail:{3:_<30}".format(r[0], r[1], r[2], r[3]))
        #print(f"ID:{record[0]} Name:{record[1]} Telephone:{record[2]} E-mail:{record[3]}")

        count += 1
        if count >= limit:
            count = 0
            os.system("pause")
            os.system("cls")
    print('End of list')

def consultAll():
    variableSQL = "SELECT * FROM TB_CONTATOS"
    record = queryConsult(variableConnection, variableSQL)
    limit = 10
    count = 0
    for r in record:
        print("ID:{0:_<3}    Name:{1:_<8}    Telephone:{2:_<14}     E-mail:{3:_<8}".format(r[0], r[1], r[2], r[3]))
        #print(f"ID:{r[0]} Name:{r[1]} Telephone: {r[2]} E-mail: {r[3]}")

        count += 1
        if count >= limit:
            count = 0
            os.system("pause")
            os.system("cls")
    print('End of list')

def update():
    os.system("cls")
    id = input('Enter the ID of the record to be updated:')
    record = queryConsult(variableConnection, "SELECT * FROM TB_CONTATOS WHERE N_IDCONTATO=" + id)

    #receive data from the bank
    recordNome = record[0][1]
    recordTelefone= record[0][2]
    recordEmail = record[0][3]

    name = input('Enter the name: ')
    telephone = input('Enter the teleprhone')
    email = input('Enter the email')

    #checks if something has been entered by the user
    if(len(name) == 0):
        name = recordNome
    if (len(telephone) == 0):
        telephone = recordTelefone
    if (len(email) == 0):
        email = recordEmail

    variableSQL = "UPDATE TB_CONTATOS SET T_NOMECONTATO = '"+name+"', T_TELEFONECONTATO = '"+telephone+"', T_EMAILCONTATO = '"+email+"' WHERE N_IDCONTATO=" + id
    queryInsertUpdateDelete(variableConnection, variableSQL)


def delete():
    os.system("cls")
    id = input('Enter the ID of the record to be deleted: ')
    variableSQL = "DELETE FROM TB_CONTATOS WHERE N_IDCONTATO=" + id
    queryInsertUpdateDelete(variableConnection, variableSQL)

def insert():
    os.system("cls")
    name = input('Enter the name: ')
    telephone = input('Enter the teleprhone')
    email = input('Enter the email')
    variableSQL = "INSERT INTO TB_CONTATOS (T_NOMECONTATO, T_TELEFONECONTATO, T_EMAILCONTATO) VALUES ('"+name+"','"+telephone+"','"+email+"')"
    queryInsertUpdateDelete(variableConnection, variableSQL)

option = 0
while option != 6:
    mainFunctionMenu()
    option = int(input('Enter an Option: '))

    if option == 1:
        insert()
    elif option == 2:
        delete()
    elif option == 3:
        update()
    elif option == 4:
        consultAll()
    elif option == 5:
        consultByName()
    elif option == 6:
        os.system("cls")
        print('Finished Program')
    else:
        os.system("cls")
        print('Invalid Option!')
        os.system("pause")

variableConnection.close()
os.system("pause")


