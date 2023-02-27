import os
import os.path as path

working_path = './2-From-components-to-chip'

os.chdir(working_path)

files = os.listdir('.')
nbs = [f for f in files if f.endswith('.ipynb')]

for nb in nbs[:]:
    name = path.splitext(nb)[0]
    # os.renames(nb, name+'/'+nb)  # ❗Uncomment this line messes with files!
    print('Moved\t  ', nb, '\n\tto', name+'/'+nb)
