class Verse(object):
    def __init__(self, book, chapter, verse, text):
        self.book = book
        self.chapter = chapter
        self.verse = verse
        self.text = text

    def toString(self):
        return self.book + " " + self.chapter + ":" + self.verse + " " + self.text