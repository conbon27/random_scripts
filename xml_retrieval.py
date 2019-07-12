# set file directory
# identify all files called metadata.xml in that directory
# copy each of those files to another folder
# rename them as you go
# re-encode xml files to remove forbidden characters (double http)
# https://stackoverflow.com/questions/38679463/python-script-to-find-and-move-files

import os
import shutil

RootDir1 = r'C:\Users\aconway\Downloads\envirogeo'
TargetFolder = r'C:\Users\aconway\Downloads\environconvert'
i = 0

# Walk through all files in the directory that contains the files to copy
for root, dirs, files in os.walk(RootDir1):

    for filename in files:
        if filename == 'metadata.xml':
            base = os.path.join(os.path.abspath(root))
            # Get current name
            old_name = os.path.join(base, filename)
            # Get parent folder
            parent_folder = os.path.basename(base)
            # New name based on parent folder
            new_file_name = 'environmental ' + \
                parent_folder + ' ' + str(i) + '.xml'
            new_abs_name = os.path.join(base, new_file_name)
            # Rename to new name
            os.rename(old_name, new_abs_name)
            i = i+1

for root, dirs, files in os.walk((os.path.normpath(RootDir1)), topdown=False):
    for name in files:
        if name.startswith('environmental'):
            print('identified metadata: ' + str(i))
            i = i + 1
            SourceFolder = os.path.join(root, name)
            shutil.copy2(SourceFolder, TargetFolder)

for root, dirs, files in os.walk(TargetFolder):

replacement = "http://www.isotc211.org/2005/inspire/imd"
original = "http://http://www.isotc211.org/2005/inspire/imd"
for dname, dirs, files in os.walk(TargetFolder):
    for fname in files:
        fpath = os.path.join(dname, fname)
        with open(fpath, errors='ignore') as f:
            s = f.read()
            s = s.replace(original, replacement)
        with open(fpath, "w") as f:
            f.write(s)
