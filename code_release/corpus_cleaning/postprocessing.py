"""
=== DESCRIPTION
This file postprocesses english data, removing
noise like leading dashes, non-ascii characters, 
non-english examples, etc

=== USAGE
python postprocessing.py [en file] [ja file]
"""
import sys
from tqdm import tqdm


VALID_PUNCTUATION = '!#$%&(),.:;?\'[]{}'


def percent_english_words(l):
    l = ''.join(c for c in l if c not in string.punctuation)
    words = l.split(' ')
    en_count = 0.0
    i = 0
    for word in words:
        try:
            if dictionary.check(word.strip()):
                en_count += 1
        except:
            pass
        i += 1.0

    percent = en_count/i if i != 0 else 0
    return percent


def is_alpha(c):
    try:
        return c.encode('ascii').isalpha()
    except:
        return False


def safe(char):
    if is_alpha(char):
        return True

    if char in VALID_PUNCTUATION:
        return True

    if char == ' ':
        return True

    if char.isdigit():
        return True

    return False


en = open(sys.argv[1])
en_lines = en.readlines()

ja = open(sys.argv[2])
ja_lines = ja.readlines()


for en_l, ja_l in tqdm(zip(en_lines, ja_lines)):
    cleaned_line = en_l.strip('- ').lstrip('.)] ').rstrip(',([ ')
    cleaned_line = ''.join(c for c in en_l if safe(c)).strip().lstrip('.')
    cleaned_line = cleaned_line.replace('  ', ' ').lower()

    ja_cleaned = ja_l.lstrip('- ').strip()

    if len(cleaned_line) >= 2 and percent_english_words(cleaned_line) > 0.4:
        print '%s\t%s' % (cleaned_line, ja_cleaned)

