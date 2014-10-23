# -*- coding: utf-8 -*-

import os
import csv

def tree_walker(directory):
    """
    input:  directory -- string of directory you want to traverse
    output: files     -- list of strings containing all filenames
            owner     -- owner of the files, string
            sizes     -- list of strings containing file sizes for each file
            times     -- list of strings containing timestamps of last mod. for each file
            
    """
    
    # like os.listdir, but traverses directory trees
    stack = [directory]   # create a list containing the input directory
    files = []            # create an empty list for the full filename strings
    owner = 'Tim'         # set owner string, hardcoded in
    sizes = []            # create an empty list for the sizes of each file in files, as strings
    times = []            # create an empty list for the Unix timestamp for each file in files, as strings
    
    while stack:          # while the stack isn't empty
        
        directory = stack.pop()                      # pop the last element out of stack (i.e. last directory in the list)
        
        for file in os.listdir(directory):           # loop over all files in the directory
            
            fullname = os.path.join(directory, file) # get the full name of the file
            st = os.stat(fullname)                   # get the stats of the file
            size = str(st.st_size)                   # extract the size of the file from st
            time = str(st.st_mtime)                  # get the last mod. time of file
            
            # append the right values into the appropriate output lists
            files.append(fullname)                   
            sizes.append(size)                      
            times.append(time)
            
            if os.path.isdir(fullname) and not os.path.islink(fullname): # if the 'file' name turns out to be a directory
                stack.append(fullname)                                   # append it to the stack 
    
    
    return files,owner,sizes,times # output the lists of strings


def tree_to_csv(files,owner,sizes,times):
    """
    inputs:  files     -- list of strings containing all filenames
             owner     -- owner of the files, string
             sizes     -- list of strings containing file sizes for each file
             times     -- list of strings containing timestamps of last mod. for each file
    output: .csv file, arranged by column in the order listed in inputs
            named 'my_files.csv' by default
            
    """
    
    with open('my_files.csv','wb') as csvfile:
        file_writer = csv.writer(csvfile,delimiter=',')
        for i in range(len(files)):
            file_writer.writerow([files[i],owner,sizes[i],times[i]])
        
    
            
        
    
    
