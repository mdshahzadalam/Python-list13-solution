#9. Write a Python script to create a list of city names taken from the user.

print("How many cities you want to add:-")
n=int(input())
print("Enter cities name:-")
l1=[]
i=1
while i<n:
    l1.append((input()))
    i+=1
print(l1)
