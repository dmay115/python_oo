"""Word Finder: finds random words from a dictionary."""
class WordFinder:
    """Creates word list and prints number of words in created list"""
    def __init__(self, path):
        self.word_list = []
        self.line_count = 0
        self.fill_list(path)
        print(self.line_count)

    def fill_list(self, path):
        file = open(f"{path}", 'r')
        for line in file:
            trim_line = line.strip('\n')
            self.word_list.append(trim_line)
            self.line_count += 1
        file.close()

    # def random(self):
