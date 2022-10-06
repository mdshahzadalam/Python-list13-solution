#4. Write a python script to Change the values "SQL" and "Reactnative" with the values
#    "NoSQL" and "Flutter" (List is thislist = ["Java", "SQL", "C", "Reactnative",
#    "Javascript", "Python"]

list = ["Java", "SQL", "C", "Reactnative","Javascript", "Python"]
del(list[1])
list.insert(1,"NoSql")
del(list[3])
list.insert(3,"Flutter")
print(list)
