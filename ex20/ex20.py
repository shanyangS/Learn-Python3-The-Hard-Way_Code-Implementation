from sys import argv

script, input_file = argv

def print_all(f):
    print(f.read()) #open的一个方法

def rewind(f):
    f.seek(0) #将文件指针移动到文件的开始位置

def print_a_line(line_count, f):
    print(line_count, f.readline())

current_file = open(input_file)

print("First let's print the whole file:\n")

print_all(current_file)

print("Now let's rewind, kind of like a tape.")

rewind(current_file) #为了让文件接下来调用readline方法从头开始读取

print("Let's print three lines:")

current_line = 1
print_a_line(current_line, current_file) #一次默认读取一行

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)