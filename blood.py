
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
    if(choice==2):
        print("view blooddonor")
    elif(choice==3):
        print('search blooddonor')
    elif(choice==4):
        print('update the blooddonor')
    elif(choice==5):
        print('delete the blooddonar')
    elif(choice==6):
        break  