# -*- coding: utf-8 -*-
from milon.transliteration import *


def test_unicode_to_sbl():
    assert(unicode_to_sbl(u'שלום') == u'šlwm')


def test_ascii_to_unicode():
    assert(ascii_to_unicode('$lwM') == u'שלום')
    assert(ascii_to_unicode('br$yt brh AlwhyM At') == u'ברשית ברה אלוהים את')


def test_remove_vowels():
    no_vowels = remove_vowels(
        u'וְהָאָרֶץ הָיְתָה תֹהוּ וָבֹהוּ וְחֹשֶׁךְ עַל־פְּנֵי תְהֹום וְרוּחַ אֱלֹהִים מְרַחֶפֶת עַל־פְּנֵי הַמָּֽיִם׃'
    )
    result = u'והארץ היתה תהו ובהו וחשך עלפני תהום ורוח אלהים מרחפת עלפני המים'
    assert(no_vowels == result)
