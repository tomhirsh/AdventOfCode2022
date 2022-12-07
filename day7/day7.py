from collections import defaultdict
import pdb
import os
import numpy as np

def add_to_sys_dir(sys_dir, current_path, next_file, dir_or_size):
    cur_loc = sys_dir
    for loc in current_path:
        cur_loc = cur_loc[loc]
    
    if dir_or_size == 'dir':
        cur_loc[next_file] = defaultdict()
    else:
        cur_loc[next_file] = int(dir_or_size)
    
    return sys_dir


def rec(name, cur_item, dirs_sizes=[], max_allowed_dir_size=100000):
    if type(cur_item) == int: # size. we are handling a file
        return cur_item, []

    # we are handling a dir
    dir_size = sum([rec(name, next_item, dirs_sizes, max_allowed_dir_size=max_allowed_dir_size)[0] for name, next_item in cur_item.items()])
    
    if dir_size <= max_allowed_dir_size:
        dirs_sizes.append(dir_size)
    dirs_sizes.append(dir_size)

    return dir_size, dirs_sizes


if __name__ == "__main__":
    current_path = []
    sys_dir = {'/': defaultdict()}

    with open(os.path.join('day7','data.txt'), 'r') as f:
        for line in f:
            line_splitted = line.strip().split()
            if line_splitted[0] == '$': #command
                if line_splitted[1] == 'cd':
                    next_dir = line_splitted[2]
                    if next_dir == '..':
                        current_path.pop()
                    elif next_dir == '/':
                        current_path = ['/']
                    else:
                        current_path.append(next_dir)
                else: # ls
                    continue
            else: # in ls
                add_to_sys_dir(sys_dir, current_path, line_splitted[1], dir_or_size=line_splitted[0])

    total_size, dirs_sizes = rec('/', sys_dir['/'], max_allowed_dir_size=100000)
    print(sum(dirs_sizes)) # part 1

    total_size, dirs_sizes = rec('/', sys_dir['/'], max_allowed_dir_size=np.inf)
    needed_space = 30000000 - (70000000 - dirs_sizes[-1])
    print(np.min([dir_size for dir_size in dirs_sizes if dir_size >= needed_space])) # part 2