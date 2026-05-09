# csv file reading as dictionary
# import csv
# try:
#     with open('students.csv', 'r') as file:
#         reader = csv.reader(file)
#         #print (reader)
#         #print(list(reader))
#         for row in reader:
#             print(row)

# except Exception as e:
#     print (e)









# import csv
# try:
#     with open('students.csv', 'r') as file:
#         reader = csv.DictReader(file)
#         #print (reader)
#         #print(list(reader))
#         for row in reader:
#             print(row)

# except Exception as e:
#     print (e)




# # writting data into csv files
# import csv
# try:
#     with open('students.csv', 'a',newline ='') as file:
#         writer = csv.DictWriter(file, fieldnames = ['roll','Name','age','class'])
#         data = [{'roll' : 108, 'Name' : 'Shiva', 'age' : 11, 'class' : 10},
#                 {'Name' : 'sai', 'roll' : 109, 'class' : 6, 'age' : 12}]
#         writer.writerows(data)
# except Exception as e:
#     print(e)




# writting data into csv files
import csv
try:
    with open('students1.csv', 'w',newline ='') as file:
        writer = csv.DictWriter(file, fieldnames = ['roll','Name','age','class'])
        data = [{'roll' : 108, 'Name' : 'Shiva', 'age' : 11, 'class' : 10},
                {'Name' : 'sai', 'roll' : 109, 'class' : 6, 'age' : 12}]
        writer.writeheader()
        writer.writerows(data)
except Exception as e:
    print(e)