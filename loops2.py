a = int(input("Enter a number: "))
i =1
while i <= 10:
    print(a*i)
    i += 1

#WAP to store the squre of a no from 1 to 10
i = 1
while i <= 10:
    print(i*i)
    i += 1

#WAP to print all the list
list = [2, 3, 4, 5, 6, 7]
i =0
while i < len(list):
    print(list[i])
    i += 1
#WAP to search an element in the list
list = [2, 3, 4, 5, 6, 7]
i = 0
toSearch = 3

while i < len(list):
    if toSearch == list[i]:
        print("Found at index", i)
        break  # stop searching once found
    i = i + 1
else:
    print("Not found")