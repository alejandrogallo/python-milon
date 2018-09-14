# -*- coding: utf-8 -*-
import os
import re
import json
from milon.transliteration import ascii_to_unicode, remove_vowels


data_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data')
en_he_datapath = os.path.join(data_dir, 'enhe.json')
he_en_datapath = os.path.join(data_dir, 'heen.json')


class DictionaryEnHe:

    def __init__(self, limit=20):
        self.limit = limit
        with open(en_he_datapath) as fd:
            self.words = json.load(fd)

    def lookup(self, word):
        results = []
        for w in self.words:
            if re.match(word, w.get('translated')):
                results.append(w)
            if len(results) > self.limit:
                return results
        return results


class DictionaryHeEn:

    def __init__(self, limit=20):
        self.limit = limit
        with open(he_en_datapath) as fd:
            self.words = json.load(fd)

    def lookup(self, unicode_word):
        results = []
        for w in self.words:
            if re.match(
                remove_vowels(unicode_word), remove_vowels(w.get('translated'))
            ):
                results.append(w)
            if len(results) > self.limit:
                return results
        return results

    def lookup_ascii(self, word):
        uni_word = ascii_to_unicode(word)
        return self.lookup(uni_word)
