# contents = ["in the name of god",
#             "my name is Alikhani",
#             "welcome to python course",
#             "this is our first tutorial"]
#
#
# filenames = ["doc.txt", "report.txt", "presentation.txt"]
#     file = open(f"{}")

# تمرین3
# temperatures = [10, 12, 14]
# file = open("file.txt", 'w')
# temperatures = [str(i)+"\n" for i in temperatures]
# file.writelines(temperatures)

# تمرین 4
# numbers = [10.1, 12.3, 14.7]
# numbers = [int(number) for number in numbers]
# print(numbers)
#
# with open("file.txt", 'r') as file:
#     print(file.read())
#     print(len(file.read()))

with open("file.txt", 'r') as file:
    content = file.read()
    print(content)
    print(len(content))

