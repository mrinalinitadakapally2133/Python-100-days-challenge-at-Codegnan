import csv


try:
    with open('contacts.csv', 'a+') as f:
        values = ['name' , number], ['ravi' , 6302514144] 
        data =  csv.writer(f)
        print(data)
        print(list(data))
except Exception as e:
    print(f"File not found:{e}")