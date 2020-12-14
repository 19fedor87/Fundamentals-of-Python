# Создать текстовый файл (не программно), сохранить в нем несколько
# строк, выполнить подсчет количества строк, количества слов в каждой строке.

my_list = ['Здравствуйте\n', 'Пока\n', 'Очень хорошо\n']
with open("test_1.txt", 'w+') as f_obj:
    f_obj.writelines(my_list)
with open("test_1.txt") as f_obj:
    lines = 0
    letters = 0
    for line in f_obj:
        lines += line.count("\n")
        letters = len(line)-1
        print(f"{letters} letters in line")
    print(f"String count is {lines}")