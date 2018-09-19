# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

# coding=utf-8

import os

dir = [('dir_' + str(i + 1)) for i in range(9)]


def make_dir(paths):
    dir_path = os.path.join(os.getcwd(), paths)
    try:
        os.mkdir(dir_path)
    except:
        print(dir_path + ' - директория сужествует')


def rm_dir(paths):
    dir_path = os.path.join(os.getcwd(), paths)
    try:
        os.rmdir(dir_path)
    except:
        print(dir_path + ' - директории нет')


for c in dir:
     make_dir(c)

#print(c)

for r in dir:
     rm_dir(r)

#print(r)




# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.


# coding=utf-8

import os

list = os.listdir()

for l in list:
    print(l)





# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

# coding=utf-8

import os
import shutil
import sys

dir = os.getcwd()
script_name = sys.argv[0]
shutil.copyfile(script_name, 'script_name' + '_back' + '.py')


print(dir)
print(script_name)
