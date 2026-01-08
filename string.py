str1 = "I am don"
str2 = 'I am don'
str3 = """I am don"""
print(str1)
print(str2)
print(str3)
str4 = "I am don.\nof my world"
print(str4)

# concatibnation
str = "hello"
str1 = "Arti"
final_str = str +" "+ str1
print(final_str)

#length function
print(len(final_str))

#indexing
print(final_str[0])
print(final_str[1])
print(final_str[-1])
print(final_str[-7])
#final_str[1] = 'a'
#print(final_str[1]) #strings are imutable means we can not change the value

#slicing
print(final_str[0:7])
print(final_str[6:10])
print(final_str[0:])
print(final_str[-1:-5])

#string functions
str5 = "I am Don"
print(str5.upper())
print(str5.lower())
print(str5.endswith("n"))
print(str5.capitalize())
print(str5.replace("Don", "Big Don"))
print(str5.find("am"))
print(str5.count("I"))
print(str5.count("i"))
