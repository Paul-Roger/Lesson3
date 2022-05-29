

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

"""