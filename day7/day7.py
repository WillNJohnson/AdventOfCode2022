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

# calculate sum of files with total sizes that are at most 100,000
sum_at_most_size_100_000 = 0
for k, v in directory.items():
    if v['totalsize'] <= 100000:
        sum_at_most_size_100_000 += v['totalsize']

print(f'Sum of the total sizes of directories containing total size of 100,000 at most: {sum_at_most_size_100_000}')