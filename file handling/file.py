# string = """python programming"""
# f.write(string)
# f.close()
# print("contant added succesfully")

# w+ mode
f = open('sample.txt', 'w+')
# string = """Java programming"""
# f.write(string)
f.write('python')
content = f.readlines()
print(content)
f.close()
print("content added sucessfully")
