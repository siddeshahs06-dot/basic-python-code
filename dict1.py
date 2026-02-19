dict={}
for i in range(0,2):
    student=input("enter a student ID")
    dict1={}
    for j in range(0,2):
        key=input("enter a key")
        value=input("enter a value")
        dict1[key]=value
    dict[student]=dict1    
print(dict)    