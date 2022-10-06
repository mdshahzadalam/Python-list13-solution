#10. Write a Python script to create a list, where each element of the list is a digit of a
#    given number.

test_list = [56, 72, 875, 9, 173]
print("The original list is : " + str(test_list))
K =int(input("Enter a number if you want to print in the list:-"))
res = [ele for ele in test_list if str(K) in str(ele)]
print(f"Elements with digit {K} : "+ str(res))