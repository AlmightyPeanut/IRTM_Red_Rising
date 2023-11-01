import os
import torch

from divide_chapters import _PREPROCESSED_PATH
from transformers import AutoTokenizer, AutoModel

if __name__ == '__main__':
    tokenizer = AutoTokenizer.from_pretrained("shtoshni/longformer_coreference_ontonotes")
    model = AutoModel.from_pretrained("shtoshni/longformer_coreference_ontonotes")

    for book in os.scandir(_PREPROCESSED_PATH):
        for chapter in os.scandir(book.path):
            with open(chapter.path, 'r') as chpt_file:
                chpt_text = chpt_file.read()

            # https://huggingface.co/docs/transformers/main/en/model_doc/longformer#transformers.LongformerModel
            # https://huggingface.co/shtoshni/longformer_coreference_joint
            # https://github.com/shtoshni/fast-coref/tree/99d5896d91bc1f9913db857ff8c8dcb961b7ad2e
            inputs = tokenizer(chpt_text, return_tensors='pt')
            tokens = inputs.tokens()

            outputs = model(**inputs)[0]
            predictions = torch.argmax(outputs, dim=2)

            for token, prediction in zip(tokens, predictions[0].numpy()):
                print(token, model.config.id2label[prediction])

            break
