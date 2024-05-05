import shutil
shutil.copy('63.py', 'main2.py')
shutil.copytree('test', 'newfolder')
shutil.copy2('63.py', 'main3.py')
shutil.move('test/file.py', 'file.py')
shutil.rmtree('test')

import os
os.remove('file.py')
