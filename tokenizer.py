import os
import tensorflow as tf

from transformers import pipeline, RobertaTokenizerFast, TFRobertaForTokenClassification
from divide_chapters import _PREPROCESSED_PATH

if __name__ == '__main__':
    ner_pipe = pipeline('ner', grouped_entities=True)

    for book in os.scandir(_PREPROCESSED_PATH):
        for chapter in os.scandir(book.path):
            with open(chapter.path, 'r') as chpt_file:
                chpt_text = chpt_file.read()

            # bert tokenization
            test = ner_pipe(chpt_text)
            breakpoint()
