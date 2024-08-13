from pathlib import Path
import os
import pypinyin

# Install dependencies
os.system('pip install -r requirements.txt')

# Search pypinyin dict
pypinyin_dir = Path(os.path.dirname(pypinyin.__file__))
pypinyin_dict_files = list(pypinyin_dir.glob('**/*.json'))

# Generate pyinstaller spec
os.system(f'pyi-makespec main.py -w -n text-elementalizer \
                                 --add-data={pypinyin_dict_files[0]}:pypinyin \
                                 --add-data={pypinyin_dict_files[1]}:pypinyin \
                                 --icon=src/icon.ico \
                                 ')