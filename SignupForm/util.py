# -*- coding: utf-8 -*-

NUM_ZEN='０１２３４５６７８９'
NUM_HAN='0123456789'
HIRA_ZEN='あいうえおかきくけこさしすせそたちつてとなにぬねのはひふへほまみむめもやゆよらりるれろわをんっぁぃぅぇぉゃゅょがぎぐげござじずぜぞだぢづでどばびぶべぼぱぴぷぺぽ'
KANA_ZEN='アイウエオカキクケコサシスセソタチツテトナニヌネノハヒフヘホマミムメモヤユヨラリルレロワヲンッァィゥェォャュョガギグゲゴザジズゼゾダヂヅデドバビブベボパピプペポ'

ALPA_ZEN='ＡＢＣＤＥＦＧＨＩＪＫＬＭＮＯＰＱＲＳＴＵＶＷＸＹＺ'
alpa_ZEN='ａｂｃｄｅｆｇｈｉｊｋｌｍｎｏｐｑｒｓｔｕｖｗｘｙｚ'
ALPA_HAN='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
alpa_HAN='abcdefghijklmnopqrstuvwxyz'

NUM_ZEN2HAN_tbl = str.maketrans(NUM_ZEN, NUM_HAN)
ALPA_ZEN2HAN_tbl = str.maketrans(ALPA_ZEN + alpa_ZEN, ALPA_HAN + alpa_HAN)

def numZEN2HAN(str):
    return str.translate(NUM_ZEN2HAN_tbl)

def alpaZEN2HAN(str):
    return str.translate(ALPA_ZEN2HAN_tbl)
