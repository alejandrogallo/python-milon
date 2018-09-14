# -*- coding: utf-8 -*-
import os
from milon.dictionaries import *
from milon.transliteration import *


def test_data():
    assert(os.path.exists(data_dir))
    assert(os.path.exists(en_he_datapath))
    assert(os.path.exists(he_en_datapath))


def test_dictionaries_heen():
    d = DictionaryHeEn()
    assert(len(d.words) == 33001)

    results = d.lookup(u'כל')
    assert(results)
    assert(results[0]['translation'][0] == 'all')

    results = d.lookup_ascii('kl')
    assert(results)
    assert(results[0]['translation'][0] == 'all')

    results = d.lookup_ascii('$lwm')
    assert(results)
    assert(results[0]['translation'][0] == 'wellness')

    results = d.lookup_ascii('Any')
    assert(results)


def test_dictionaries_enhe():
    d = DictionaryEnHe()
    assert(len(d.words) == 60061)

    results = d.lookup('dream')
    assert(results)
    assert(unicode_to_sbl(results[0]['translation'][0]) == u'ḥălwōm')
