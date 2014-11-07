# -*- coding: utf-8 -*-

import sys
import os
import csv

def tree_walker(directory):
    """Function to walk a directory tree and returns pertinent tree information.
    
    Walks a directory tree and prints out directory and file information.
    Used for outputting to .csv files and pandas
    
    Args: 
        directory: directory name, string
    
    Returns:
        dirnames: list of directory names
       # dirlevels: list of directory levels, strings #
        dirsizes: list of directory sizes, strings
        filenames: list of file names
        filelevels: list of levels pertaining to directory level, string
        filesizes: list of file sizes, strings
        filetimes: list of Unix timestamps of last mod
        owner: file owner, hardcoded as 'Tim'
            
    """
    
    # determine platform and associated directory slash
    if 'win' in sys.platform:
        delimit = '\\'
    else:
        delimit = '/'
        
    # like os.listdir, but traverses directory trees
    # initialize arrays to hold information on directories and files
    dirnames = []
    dirlevels = []
    dirsizes = []
    filenames = []
    filelevels = []
    filesizes = []
    filetimes = []
    
    stack = [directory]   # create a list containing the input directory
    owner = 'Tim'         # set owner string, hardcoded in
    top_levels = directory.count(delimit) # to take of directories above the first one
    while stack:          # while the stack isn't empty
        
        directory = stack.pop()  # pop the last element out of stack (i.e. last directory in the list)
        #dirnames.append(directory) # append dir names and levels to arrays
        dir_level = directory.count(delimit)+1-top_levels
        dirlevels.append(str(dir_level))
        dir_size = 0  # initialize accumulator to find total dir size
        
        for file in os.listdir(directory):           # loop over all files in the directory
            
            fullname = os.path.join(directory, file) # get the full name of the file
            st = os.stat(fullname)                   # get the stats of the file
            size = st.st_size               # extract the size of the file from st
            time = str(st.st_mtime)                  # get the last mod. time of file
            
            # append the right values into the appropriate output file lists
            filenames.append(os.path.split(fullname)[1])       
            filelevels.append(str(dir_level))            
            filesizes.append(str(size))              
            filetimes.append(time)
            dirnames.append(os.path.split(fullname)[0])
            
            dir_size = dir_size + size # add file size to accumulator
            
            if os.path.isdir(fullname) and not os.path.islink(fullname): # if the 'file' name turns out to be a directory
                stack.append(fullname)  # append it to the stack 
            #else: # if it's a file
                
               
                
        dirsizes.append(str(dir_size)) # append accumulator to size list
    return dirnames,dirlevels,dirsizes,filenames,filelevels,filesizes,filetimes,owner # output the lists 




def tree_to_csv(dirnames,filenames,owner,filelevels,filesizes,filetimes):
    """Function to create a .csv file with directory tree information.
    
    Creates a .csv file with file names, directory levels, file sizes, 
    mod times, and owner.
    
    Args: 
        dirnames: list of directory names
        filenames: list of file names
        owner: file owner, hardcoded as 'Tim'
        filelevels: list of levels pertaining to directory level, string
        filesizes: list of file sizes, strings
        filetimes: list of Unix timestamps of last mod
  
    Returns:
        none
            
    """
    
    with open('my_files.csv','wb') as csvfile:
        file_writer = csv.writer(csvfile,delimiter=',')
        for i in range(len(dirnames)):
            file_writer.writerow([dirnames[i],filenames[i],owner,filelevels[i],filesizes[i],filetimes[i]])
        
if __name__ == "__main__":
# import everything that's necessary
    import pandas
    
    dirnames,dirlevels,dirsizes,filenames,filelevels,filesizes,filetimes,owner=tree_walker('.\\folder_l1_0')
    tree_to_csv(dirnames,filenames,owner,filelevels,filesizes,filetimes)

    data = pandas.read_csv('my_files.csv') # get the dataframe
    data.columns = ['Dir','File','Owner','Dir Level','Size (bytes)','Unix Timestamp'] # edit headers
    
    # set up spaces
    spaces4 = '    '
    maxlevels = int(max(dirlevels))
    indents = [spaces4*x for x in range(1,maxlevels+1)]   
    
    print('\nlevel {} directory ({} bytes)'.format(dirlevels[0],dirsizes[0]))
    
    dir_list = []
    file_list = []
    level_list = []
    
    for (Dir,File,Level), group_data in data.groupby(["Dir", "File", "Dir Level"]):
        dir_list.append(Dir)
        file_list.append(File)
        level_list.append(Level)
        print('{}level {} {}'.format(indents[Level-1],Level,File))   
        
        
        
        
        
    
    
