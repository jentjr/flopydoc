"""
Simple script to help create files needed to make a sphinx documentation
website of the flopy project.  The script will read through all of the
flopy modules and create the sphinx autodoc rst (restructured text) files.

"""

import os

#print current working directory
print os.getcwd()

#look through the following subdirectories, and grab all of the
#modules that should be added to the sphinx documentation.
flopypth = os.path.join('..', '..', '..', 'flopy3.git', 'flopy')
pthlist = ['modflow', 'mt3d', 'seawat', 'utils', 'plot']
namelist = []
for pth in pthlist:
    dirpth = os.path.join(flopypth, pth)
    filelist = os.listdir(dirpth)
    for filename in filelist:
        if '.pyc' in filename:
            continue
        if '__init__' in filename:
            continue
        if '.py' in filename:
            prefix = filename.strip().split('.')[0]
            nm = 'flopy.' + pth + '.' + prefix
            print nm
            namelist.append(nm)


fnamelist = open('fnamelist.txt', 'w')

for name in namelist:

    fnamelist.write('   ' + name + '\n')
    prefix = name.strip().split('.')[2]
    fname = prefix + '.rst'
    if not os.path.exists(fname):
        f = open(fname, 'w')
        s = name + ' Module'
        f.write(s + '\n')
        s = len(s) * '='
        f.write(s + '\n\n')
        s = '.. automodule:: ' + name
        f.write(s + '\n')
        s = '   :members:'
        f.write(s + '\n')
        s = '   :inherited-members:'
        f.write(s + '\n')
        f.close()
    
fnamelist.close()
