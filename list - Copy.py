
marks = [10, 20, 30, 40]
print(marks)
print(type(marks))
print(marks[0])
print(marks[1])
marks[2] = 25
print(marks) #list are mutable as we chnage the values
student = [10, "Arti", 90.00, True] # in list diff datatype are allowed
print(student)
print(student[1:3])
print(student[0:])
print(student[-1])
print(student[-4:-1])

#list method
marks.append(50)#add element at last
print(marks) 
list.sort(marks) #sort the list
print(marks)
#list.sort(reverse = True(marks)) #sort in descending order
#print(marks)
list.reverse(marks)
print(marks)
marks.insert(2, 35) #insert element at specific index
print(marks)
marks.remove(25)
print(marks)

#WAP to check list is palindrom or not
list = [10, 20, 30, 20, 30]
list_copy = list.copy()
list_copy.reverse()
if(list == list_copy):
    print("list is palindrom")
else:
    print("list is not palindrom")

#WAP to sort the list
list = ["A", "B", "C", "A", "D", "A"]
print(list.sort())
print(list)


#WAP to ask user to enter names of 3 movie and store them in list
"""movies = []
movie1 = input("Enter 1st movie name")
movie2 = input("Enter 2nd movie name")
movie3 = input("Enter 3rd movie name")
movies.append(movie1)
movies.append(movie2)
movies.append(movie3)
print(movies)"""
