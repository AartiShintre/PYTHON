# Values are stored in key-value pairs
my_dict = {
    "name": "Arti",
    "age": 21,
    "city": "Pune",
    "subject": ["Python", "Java", "C++"]
}

print(my_dict)
print(type(my_dict))  # dict is mutable; we can change the values
my_dict["name"] = "Aarya"
print(my_dict)
student = {
    "name" : "Shreeja",
    "Subject" : {
        "Python" : 80,
        "Java" : 70,
        "C++" : 60
    }
}
print(student)
print(student["Subject"]["Python"])

#methods
print(student.keys())
print(student.values())
print(student.items())
print(student.get("name"))
