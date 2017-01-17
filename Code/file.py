import os

def delete():
    tdir = '../Data/Data/Profile_Data/'
    for fn in os.listdir(tdir):
        if fn.endswith('.txt'):
            os.remove(tdir + fn)

def copy(name):
    name = name.lower()
    sdir = '../Data/Data/All_Profile_Data/'
    tdir = '../Data/Data/Profile_Data/'
    for fn in os.listdir(sdir):
        name_segment = fn[fn.find('_') + 1 : fn.rfind('.')]
        if name_segment == name or name_segment == name + 'Compressed':
            fin = open(os.path.join(sdir, fn), 'rb')
            text = fin.read()
            tname = fin.name[fin.name.rfind('/') + 1:]
            fout = open(tdir + tname,'wt')
            fout.write(text)
            fin.close()
            fout.close()