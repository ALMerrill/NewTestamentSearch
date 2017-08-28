import os

from verse import Verse

verses = []
with open('newTestament') as f:
    for line in f:
        line = line[0:-2] #takes the ~ off each line
        line = line.split("|")
        verses.append(Verse(line[0], line[1], line[2], line[3]))

# for i in range(0,len(verses) - 1):
#     print(verses[i].toString())

search = input("Enter word or phrase to search: ").lower()
results = []
for entry in verses:
    if search in entry.text.lower():
        results.append(entry)

for i in range(len(results)):
    print("[" + str(i + 1) + "]", end= " ")
    print(results[i].toString())

selection = int(input("Make choice to view chapter: "))
selVerse = results[selection - 1]
chapter = []
for entry in verses:
    if selVerse.book == entry.book and selVerse.chapter == entry.chapter:
        chapter.append(entry)

clear = lambda: os.system('cls')
clear()

for entry in chapter:
    print(entry.toString())