import os
import sys
inter_file  = []
new = set()
new_dict = {}
num = 0
def init(mini_file):
    num = len(mini_file)
    new_dict = {i: None for i in range(num)}

def writing_file(data,page):
	new_file = 'new_{0}.dat'.format(page)
	file = open(new_file,'w')
	file.write(data)
	file.close()
	inter_file.append(new_file)
def clear_file(rm_file):
    for i in range(len(rm_file)):
        os.remove(rm_file[i])
def select(ch2):
    pos  = -1
    pos_str = None
    for i in range(len(ch2)):
        if pos_str is None or ch2[i] < pos_str:
            pos = i 
        return pos

def dict(mini_file):  
    num = len(mini_file)  
    return {i: new_dict[i] for i in range(num) if i not in new}

def refresh():
     
    for i in range(num):
        if new_dict[i] is None and i not in new:
            new_dict[i] = mini_file[i].readline()
            if new_dict[i] == '':
                new.add(i)
            if len(new) == num:
                return False
            return True

def shift(pos1):
    print pos1
    val = new_dict[pos1]
    new_dict[pos1] = None 
    return val

def filemerger(filelist, output, temp_size):
    output_files = open(output, 'w', temp_size)
    mini_file = {}
    for i in range(len(filelist)):
        mini_file[i] = open(filelist[i], 'r', temp_size)
	init(mini_file)
    while refresh():
        pos = select(dict())
        output_files.write(shift(pos))
	#print mini_open
	

def reading_file():
	file_name = raw_input("=>")
	memory_ram = 	1024 *100 *4096 #4kb ram #4294967296 #for a 4gb ram 4 * 1024^3
	size_of = os.stat(file_name).st_size
	number_of_pages = (size_of / memory_ram)+1
	print size_of
	print "Number of page blocks that has to be handled" + str(number_of_pages)
	num_of_parts = memory_ram / size_of
	#pages_list = []
	i = 0
	file = open(file_name,'r')
	while True:
		data = file.readlines(memory_ram)
		if data == []:
			break
		else:
			data.sort()
		writing_file(''.join(data),i)
		i = i+1
        output_file = file_name + '.out'
        filemerger(inter_file, output_file, num_of_parts)
	clear_file(inter_file)



reading_file()

