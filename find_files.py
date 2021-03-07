import os


# execute the find ~/ function in terminal
# select with command a, paste into text file
# copy path

def list_to_string(liste, seperator=''):
    return seperator.join(liste)

# paste path            here
terminal_list = open('/Users/erikpreuss/Desktop/clash/princess.txt', 'r')
terminal_string = terminal_list.read().replace('\n', '')
terminal_list.close()
terminal_string = terminal_string.split('/')
path = []
for i in terminal_string:
    # write here the file/folder you want to find
    if i == 'User':
        place = terminal_string.index(i) - 1
        while terminal_string[place] != 'Users':
            path.append(terminal_string[place] + '/')
            place -= 1
        path.append('/Users/')
        path = path[::-1]
        path.append(i)
        print(list_to_string(path))
        path = []
