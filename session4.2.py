def show_menu():
    print('\n1-Add')
    print('2-Remove')
    print('3-Search')
    print('4-Edit')
    print('5-Show_List')
    print('6-Buy')
    print('7-Exit')

def read_file():
    f=open('text.txt','r')
    for line in f:
        ls=line.split(',')
        d={'id':ls[0],'name':ls[1],'price':ls[2],'count':ls[3]}
        list.append(d)
    

def add():
    id=input('\nid: ')
    name=input('name: ')
    price=input('price: ')
    count=input('count: ')
    d={'id':id,'name':name,'price':price,'count':count+'\n'}
    list.append(d)
    

def remove():
    code=input("\nEnter the code: ")
    for dic in list:
        if dic['id']==code:
            list.remove(dic)
            print('\nThe desired product has been removed\n')
            for dic in list:
                print(dic)
            break
    else:
        print('\nThe desired product is not in the product list')
        
def search():
    key=input('\nEnter your code: ')
    for dic in list:
        if dic['id']==key or dic['name']==key:
            print(dic)
            break
    else:
        print('\nKey not found')

def edit():
    lable={'1':'name','2':'price','3':'count'}
    key=input('\nEnter your code: ')
    for dic in list:
        if dic['id']==key:
            print('\nWhich field to edit?')
            print('1-Name')
            print('2-Price')
            print('3-Count')
            field=input('\n')
            new_value=input('Enter the new value: ')
            dic[lable[field]]=new_value
            if field=='3':
                dic[lable[field]]=new_value+'\n'
            print('\nInformation has been updated\n\n',dic,)
            break
    else:
        print('Key not found')

def show_list():
    print('\n\tcode\t\tname\t\tprice\t\tcount\n')
    for dic in list:
        print('\t',dic['id'],'\t\t',dic['name'],'\t\t',dic['price'],'\t\t',dic['count'])
    
def buy():
    invoice=[]
    while True:
        name=input("\nEnter the product name or press the 'E' key to end buying: ")
        if name!='E':
            for dic in list:
                if dic['name']==name:
                    num=input('Enter the number of product: ')
                    if int(dic['count'])<int(num):
                        print('insufficient inventory')
                      
                    else:
                        dic['count']=str(int(dic['count'])-int(num))+'\n'
                        total_cost=int(num)*int(dic['price'])
                        
                        p={'name':name,'price':dic['price'],'total cost':total_cost}
                        invoice.append(p)
                        
                    break    
            else:
                print('Good not found')
        else:
            print('\n***Purchase Invoice***\n') 
            for dic in invoice :
                print(dic)
            break

def save_to_database():
    f=open('text.txt','w')
    for dic in list:
        string=dic['id']+','+dic['name']+','+dic['price']+','+dic['count']
        f.write(string)
    f.close()    


list=[]
read_file()
while True:
    
    show_menu()
    user_choice=int(input('Enter your choice: '))
    if user_choice==1:
        add()
    elif user_choice==2:
        remove()
    elif user_choice==3:
        search()
    elif user_choice==4:
        edit()
    elif user_choice==5:
        show_list()
    elif user_choice==6:
        buy()
    elif user_choice==7:
        save_to_database()  
        exit(0)
    else:
        print('\n invalid number')
