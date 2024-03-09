#encoding:utf8
import jieba
import re


class TextProcessor:
    re_alphabet = "[a-zA-Z]+"
    re_digit = "[0-9]+"

    def __init__(self):
        self.tokenizer = jieba.Tokenizer()

    def tokenize_words(self, text):
        tokenized_words = self.tokenizer.tokenize(text)

        words = []
        for token in tokenized_words:
            if len(token) < 2:
                continue
            if re.match(self.re_digit, token):
                continue
            if re.match(self.re_alphabet, token):
                continue
            words.append(token)
        return words

    def split_sentences(self, text):
        return re.split("。|！|？", text)
