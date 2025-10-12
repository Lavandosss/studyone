import module1
import module2
file = open("result.txt", "w")
for numbers in [module2.list1, module2.list2, module2.list3]:
    a, b = module1.find_two_smallest(numbers)
    file.write(str(a) + " " + str(b) + "\n")
file.close()
