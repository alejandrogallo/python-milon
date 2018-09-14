#!/usr/local/bin/python
# -*- coding: utf-8 -*-
# Adapted from
# https://github.com/charlesLoder/hebrewTransliteration
from six import u as unicode


_unicode_to_sbl_chars = {
    # preserves white space
    u' ': u' ',
    # consonants
    u'א': u'ʾ',
    u'\uFB2E': u'ʾa',
    u'\uFB2F': u'ʾā',
    u'\uFB30': u'ʾ9',
    u'ב': u'b',
    u'\uFB31': u'b9',
    u'\uFB4C': u'b',
    u'ג': u'g',
    u'\uFB32': u'g9',
    u'ד': u'd',
    u'\uFB33': u'd9',
    u'ה': u'h',
    u'\uFB34': u'h9',
    u'ו': u'w',
    u'\uFB35': u'w9',
    u'\uFB4B': u'ô',
    u'ז': u'z',
    u'\uFB36': u'z9',
    u'ח': u'ḥ',
    u'ט': u'ṭ',
    u'\uFB38': u'ṭ9',
    u'י': u'y',
    u'\uFB39': u'y9',
    u'כ': u'k',
    u'\uFB3B': u'k9',
    u'\uFB4D': u'k',
    u'ך': u'k',
    u'\uFB3A': u'k9',
    u'ל': u'l',
    u'\uFB3C': u'l9',
    u'מ': u'm',
    u'\uFB3E': u'm9',
    u'ם': u'm',
    u'נ': u'n',
    u'\uFB40': u'n9',
    u'ן': u'n',
    u'ס': u's',
    u'\uFB41': u's9',
    u'ע': u'ʿ',
    u'פ': u'p',
    u'\uFB44': u'p9',
    u'\uFB4E': u'p',
    u'ף': u'p',
    u'\uFB43': u'p9',
    u'צ': u'ṣ',
    u'\uFB46': u'ṣ9',
    u'ץ': u'ṣ',
    u'ק': u'q',
    u'\uFB47': u'q9',
    u'ר': u'r',
    u'\uFB48': u'r9',
    u'ש': u'š',
    u'\u05C1': u'8',
    u'\u05C2': u'7',
    u'\uFB2A': u'š',  # ligature for שׁ
    u'\uFB2C': u'š9',
    u'\uFB2B': u'ś',  # ligature for שׂ
    u'\uFB2D': u'š9',
    u'ת': u't',
    u'\uFB4A': u't9',
    # vowels
    u'\u05B0': u'ǝ',  # shewa
    u'\u05B1': u'ĕ',  # hataf segol
    u'\u05B2': u'ă',  # hataf patach
    u'\u05B3': u'ŏ',  # hataf qamats
    u'\u05B4': u'i',  # hiriq
    u'\u05B5': u'ē',  # tsere
    u'\u05B6': u'e',  # segol
    u'\u05B7': u'a',  # patach
    u'\u05B8': u'ā',  # qamats
    u'\u05B9': u'ō',  # holam
    # this is the codepoint for a holam on a const waw, but it is rarely used
    u'\u05BA': u'ō',
    u'\u05BB': u'u',  # qibbuts
    u'\u05BC': u'9',  # dagesh
    u'\u05BD': u'',  # metheg
    u'\u05BE': u'-',  # maqqef
    u'\u05BF': u'',  # rafe
    # qamets hatuf/qatan. Not used often, most use a qamats instead
    u'\u05C7': u'o',
    # extra marks and cantillations
    u'\u0591': u'',  # athna
    u'\u0592': u'',
    u'\u0593': u'',
    u'\u0594': u'',
    u'\u0595': u'',
    u'\u0596': u'',
    u'\u0597': u'',
    u'\u0598': u'',
    u'\u0599': u'',
    u'\u059A': u'',
    u'\u059B': u'',
    u'\u059C': u'',
    u'\u059D': u'',
    u'\u059E': u'',
    u'\u059F': u'',
    u'\u05A0': u'',
    u'\u05A1': u'',
    u'\u05A2': u'',
    u'\u05A3': u'',
    u'\u05A4': u'',
    u'\u05A5': u'',
    u'\u05A6': u'',
    u'\u05A7': u'',
    u'\u05A8': u'',
    u'\u05A9': u'',
    u'\u05AA': u'',
    u'\u05AB': u'',
    u'\u05AC': u'',
    u'\u05AD': u'',
    u'\u05AE': u'',
    u'\u05AF': u'',
    u'\u05C3': u'',
}

unicode_no_vowels_to_simple_ascii_chars = {
    u' ': u' ',
    u'א': u'A',
    u'ב': u'b',
    u'ג': u'g',
    u'ד': u'd',
    u'ה': u'h',
    u'ו': u'w',
    u'ז': u'z',
    u'ח': u'H',
    u'ט': u'T',
    u'י': u'y',
    u'כ': u'k',
    u'ך': u'K',
    u'ל': u'l',
    u'מ': u'm',
    u'ם': u'M',
    u'נ': u'n',
    u'ן': u'N',
    u'ס': u'S',
    u'ע': u'\'',
    u'פ': u'p',
    u'ף': u'P',
    u'צ': u'c',
    u'ץ': u'C',
    u'ק': u'q',
    u'ר': u'r',
    u'ש': u'$',
    u'ת': u't',
}

hebrew_letters_no_vowels = unicode_no_vowels_to_simple_ascii_chars.keys()
simple_ascii_letters = unicode_no_vowels_to_simple_ascii_chars.values()
unicode_no_vowels_to_simple_ascii_table = dict(
    zip([ord(l) for l in simple_ascii_letters], hebrew_letters_no_vowels)
)

hebrew_letters = _unicode_to_sbl_chars.keys()
sbl_letters = _unicode_to_sbl_chars.values()
unicode_to_sbl_table = dict(zip([ord(l) for l in hebrew_letters], sbl_letters))

hebrew_special_signs = set(hebrew_letters) - set(hebrew_letters_no_vowels)
remove_vowels_table = dict(zip(
    [ord(l) for l in
        list(hebrew_letters_no_vowels) + list(hebrew_special_signs)],
    list(hebrew_letters_no_vowels) + [u''] * len(hebrew_special_signs)
))


def unicode_to_sbl(unicode_string):
    return unicode_string.translate(unicode_to_sbl_table)


def ascii_to_unicode(ascii_string):
    return unicode(ascii_string).translate(
        unicode_no_vowels_to_simple_ascii_table
    )


def remove_vowels(unicode_string):
    return unicode_string.translate(remove_vowels_table)
