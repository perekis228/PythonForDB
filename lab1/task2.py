from pathlib import Path

dirpath = r'C:\PythonUniversity\PythonForDB\lab1\files'
if dirpath:
    root = Path(dirpath)
else:
    root = Path('.')
files = ['text1.txt', 'text3.txt', 'text4.txt', 'text5.txt']

for root2, dirs, root_files in root.walk(on_error=print):
    if files:
        files_exist = []
        files_not_exist = []
        for file in files:
            if file in root_files:
                files_exist.append(file)
            else:
                files_not_exist.append(file)

        print('Exist:')
        with open('Exist.txt', 'w') as exist_txt:
            for file in files_exist:
                print('\t', file)
                exist_txt.write(f'{file}\n')

        with open('Not_exist.txt', 'w') as not_exist_txt:
            print('Not exist:')
            for file in files_not_exist:
                print('\t', file)
                not_exist_txt.write(f'{file}\n')
    else:
        print(f'Files: {len(root_files)}\nDir size: {sum((root2 / file).stat().st_size for file in root_files)} bytes')