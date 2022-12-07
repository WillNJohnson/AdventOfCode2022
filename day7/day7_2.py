directory = {}

with open('data.txt', 'r') as f:
    cwd = []
    for line in f:
        line_list = line.split()
        if 'ls' in line_list:
            for line in f:
                listing_list = line.split()

                # no longer is ls mode
                if '$' in listing_list: 
                    line_list = listing_list
                    break

                # directory listing can contain either a DIRECTORY or a FILE
                if 'dir' in listing_list:
                    dirname = '-'.join(cwd) + '-' + listing_list[1]

                    # current working directory contains a directory
                    directory['-'.join(cwd)]['dirs'].append(dirname)

                    # on a subdirectory, update up-level directories to contain that subdirectory
                    # if not already included
                    for i in range(len(dirname)-1):
                        if (dirname[i] == '-'):
                            dirname_level = dirname[0:i]
                            if dirname not in directory[dirname_level]['dirs']:
                                directory[dirname_level]['dirs'].append(dirname)
                else:
                    filename, filesize = listing_list[1], int(listing_list[0])

                    # current working directory contains a file and corresponding filesize
                    directory['-'.join(cwd)]['files'].append(filename)
                    directory['-'.join(cwd)]['filesizes'].append(filesize)

        if 'cd' in line_list:
            # cd can either go up directory or visit a subdirectory inside cwd
            if line_list[2] == '..':
                cwd.pop()
            else:
                cwd.append(line_list[2])

                # create a dictionary for the newly-appended directory, if dictionary hasn't already been added
                if not '-'.join(cwd) in directory:
                    directory['-'.join(cwd)] = {'dirs': [], 'files': [], 'filesizes': [], 'totalsize': 0}

# calculate total size for each directory
for k, v in directory.items():
    totalsize = sum(v['filesizes'])

    for subdir in v['dirs']:
        totalsize += (sum(directory[subdir]['filesizes']))
    
    v['totalsize'] = totalsize

# free up a directory so that there is 'required_unused_space' amount of unused space
total_available_disk_space, required_unused_space = 70000000, 30000000
minimum_space_to_free = required_unused_space - (total_available_disk_space - directory['/']['totalsize'])
smallest_to_free = total_available_disk_space

# find the smallest space to free up by checking totalsize of each directory in root '/'
for dir in directory['/']['dirs']:
    dir_size = directory[dir]['totalsize']
    if minimum_space_to_free <= dir_size < smallest_to_free:
            smallest_to_free = dir_size

print(f'Total size of directory that can free up enough space on the filesystem to run the update: {smallest_to_free}')