import os
import fnmatch
import re
from textwrap import TextWrapper
from functools import partial
from verse import Verse
from utils import *

def decorate_facory(phrase, pre, post):
    def _subber(m):
        return pre + m.group(0) + post
    return partial(re.compile(phrase, re.IGNORECASE).sub, _subber)

def my_decorator(func):
    def wrapped_func(*args, **kwargs):
        d = decorate_search(*args, **kwargs)
        return func(d)
    return wrapped_func


#Beginning of search
verses = []
with open('newTestament') as f:
    for line in f:
        line = line[0:-2] #takes the ~ off each line
        line = line.split("|")
        verses.append(Verse(line[0], line[1], line[2], line[3]))

# for i in range(0,len(verses) - 1):
#     print(verses[i].toString())
loop = True
while loop:
    search = input("Enter word or phrase to search: ").lower()
    decorate_search = decorate_facory(search, colors.OKBLUE, colors.NORMAL)
    nprint = my_decorator(print)
    results = []
    for entry in verses:
        if search in entry.text.lower():
            results.append(entry)

    for i in range(len(results)):
        print("[" + str(i + 1) + "]", end= " ")
        nprint(results[i].toString())

    selection = input("Make choice to view chapter('q' for quit, 'n' for new search): ")
    if selection == 'q':
        loop = False
    elif selection == 'n':
        loop = True
    else:
        selVerse = results[int(selection) - 1]
        chapter = []
        for entry in verses:
            if selVerse.book == entry.book and selVerse.chapter == entry.chapter:
                chapter.append(entry)

        clear()

        for entry in chapter:
            nprint(entry.toString())

        valid = False
        while not valid:
            selection = input("('q' for quit, 'n' for new search): ")
            if selection == 'q':
                loop = False
                valid = True
            elif selection == 'n':
                loop = True
                valid = True
            else:
                valid = False
                continue
