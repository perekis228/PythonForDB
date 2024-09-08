from pathlib import Path

root_str = r'C:\PythonUniversity\PythonForDB\lab1\files'
if root_str:
    root = Path(root_str)
else:
    root = Path('.')

for root2, dirs, files in root.walk(on_error=print):
    good_files = list(file for file in files if (root2 / file).stat().st_size <= 2048)
    if len(good_files):
        print(good_files)
        (root2/'small').mkdir()
        for file in good_files:
            (root2/file).replace(Path(root2/'small'/file))
    else:
        print('No data')