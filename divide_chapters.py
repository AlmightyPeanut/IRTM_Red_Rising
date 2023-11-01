import os
import re
from pathlib import Path

_PREPROCESSED_PATH = "text_data/preprocessed/"

if __name__ == '__main__':
    if not os.path.isdir(_PREPROCESSED_PATH):
        os.mkdir(_PREPROCESSED_PATH)

    with os.scandir("text_data/raw/") as directory:
        for file in directory:
            file_name = file.name
            with open(file.path, "r") as f:
                text = f.read()

            part_pattern = r'(PART I+V?.*)'
            chpt_pattern = r'(\d+\s+\t[\w+\s+’]+\t)'

            pc_pattern = re.compile(part_pattern + r'?' + chpt_pattern)
            part_pattern = re.compile(part_pattern)
            chpt_pattern = re.compile(chpt_pattern)
            if not re.findall(chpt_pattern, text):
                continue

            book_path = _PREPROCESSED_PATH + file_name[:-4] + '/'
            if not os.path.isdir(book_path):
                os.mkdir(book_path)

            chpt_title = ''
            for text_part in re.split(chpt_pattern, text):
                if re.match(part_pattern, text_part):
                    continue

                if re.match(chpt_pattern, text_part):
                    chpt_title = re.sub(r'\s+', '_', text_part.strip())
                    continue

                if chpt_title == '':
                    continue

                chapter_file_name = book_path + chpt_title + ".txt"
                if not os.path.isfile(chapter_file_name):
                    Path(chapter_file_name).touch()

                with open(chapter_file_name, "w") as chapter_file:
                    chapter_file.write(re.sub(r'[\s]+', ' ', text_part))
