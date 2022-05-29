

"""'''''''

x=8
i=3

#list
my_list = [1, 3, 5, 7, ['abba']]
my_list.append(x)
my_list.insert(i, x)
my_list.remove(x)
my_list.index(x,[start], [end])
my_list.sort()

print(type(my_list))
#---------------------------
# dict
my_dict = {"1":1, "2":2, "3":3, "4":4, "5":5}
my_dict.get(key)
my_dict.items()
my_dict.values()
my_dict.keys()
my_dict.update(other_dict)

#---------------------------
# set
my_set = set()
my_set.add(x)
my_set.discard(x)
my_set.union(set2, ...)
my_set.intersection(set2, ...)
my_set.issubset(set2, ...)

#---------------------------
# str
my_str = "Welcome there!"
new_str = my_str.format(args, kwargs)
new_str = my_str.isdigit()
new_str = my_str.find(sstr)    #sstr has type str
new_str = my_str.split(symb)   #symb has type str
new_str = my_str.replace(templ, replstr [, maxcount])   #templ replstr have hype str, maxcount - integer





stro = "hello world!"
#print(stro[:6])
#print(stro[6:])
#print(stro[2:-2])

var_len = len(stro)
print(stro.upper(), var_len)

print("Wor" in stro)

info ="Name: {}, age: {}".format(stro, var_len)
print(info)

info = f"Name: {stro}, age: {var_len}"
print(info)


friends = ["Max", "Alex", "Kate"]
print(friends[1], friends[-1])
friends.append("paul")

friends.insert(2, "Maria")
print(friends)

friends.remove("Maria")
print(friends)

friends[3] = "Leonid"
print(friends)
del friends[3]
print(friends)

friends.sort()
print(friends)
friends.reverse()
print(friends)

friends = ("Max","Kate", "John", "Leo")
print(type(friends))

friend = {
    "name" : "Max",
    "age" : 20,
    "has_car" : True
}

print(friend["age"])
print("age" in friend)

friend["has_wofe"] = False
print(friend)
friend["has_wofe"] = True
print(list(friend.keys()))
print(list(friend.values()))
print(list(friend.items()))
print("Max" in friend.values())


friends = ["Eve","Dave","Bob","Joy","Hat"]
for friend in friends:
    hello = f"Hello {friend}"
    print(hello)

friend = "Ivanov Ivan"
for letter in friend:
    print(letter)

friend = {
    "name" : "Max",
    "age" : 20,
    "has_car" : True
}
for key, val in friend.items():
    print(key)
    print(val)

name, age, has_car = ("max", 23, True)
print(name, age, has_car)

result = range(1, 1000, 5)
print(list(result))


office = {"one", "two", "one", "three", "four"}
freelance = {"one", "three", "six"}
print(office-freelance)
print(freelance-office)
print(freelance&office)
print(freelance|office)

for item in office:
    print(item)

print("int: {0:d};  hex: {0:x};  oct: {0:o};  bin: {0:b}".format(42))
print("int: {0:d};  hex: {0:#x};  oct: {0:#o};  bin: {0:#b}".format(42))

S = "abcdef"
print(S.index("cde"))
"""