import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',password='',database='bloodbankdb')
mycursor = mydb.cursor()
while True:
    print("select an option from the menu")
    print('1 add blooddonar detail')
    print('2 view blooddonar details')
    print('3 search  blooddonor details')
    print('4 update blooddonor details')
    print('5 delete blooddonors details ')
    print('6 exit')
    
    choice=int(input('enter the option:'))
    if(choice==1):
        print("add  blooddonor")
        name=input('enter the name:')
        address=input("enter address:")
        phoneno=input('enter phone number:')
        bloodgroup=input("enter blood group:")
        sql='INSERT INTO `bloodbank`(`name`, `address`, `phoneno`, `bloodgroup`) VALUES (%s,%s,%s,%s)'
        data=(name,address,phoneno,bloodgroup)
        mycursor.execute(sql,data)
        mydb.commit()
        print("view student")
    if(choice==2):
        print("view blooddonor")
        sql='SELECT * FROM `bloodbank`' 
        mycursor.execute(sql)
        result=mycursor.fetchall()
        for i in result:
            print(i)
    elif(choice==3):
        print('search blooddonor')
        phoneno=input("enter phoneno:")
        sql='SELECT `id`, `name`, `address`, `phoneno`, `bloodgroup` FROM `bloodbank` WHERE `phoneno`='+phoneno
        mycursor.execute(sql)
        result=mycursor.fetchall()
        print(result)
    elif(choice==4):
        print('update the blooddonor')
    elif(choice==5):
        print('delete the blooddonar')
    elif(choice==6):
        break  