class Trie:
    def __init__(self, name):
        self.name = name
        self.weight = 1
        self.children = []
    def find(self, name):
        # finds a child or returns false
        for t in self.children:
            if t.name == name:
                return t
                break
        else:
            return False
    def add(self, name):
        # adds a child or increases the weight of it if it already exists
        t = self.find(name)
        if t:
            t.weight += 1
        else:
            t = Trie(name)
            self.children.append(t)
        return t
    def sorted(self):
        return sorted(self.children, key = lambda x: x.weight, reverse = True)
    def findr(self, arr):
        # arr is a one-dimensional array of items to find one-by-one
        if arr != []:
            t = self.find(arr[0])
            if t:
                return t.findr(arr[1:])
            else:
                return False
        else:
            return self
    def addr(self, arr):
        # arr is a one-dimensional array of items to add one-by-one
        if not arr == []:
            return [self] + self.add(arr[0]).addr(arr[1:])
        else:
            return [self]
    def sortedr(self):
        if self.children == []:
            return [self]
        else:
            return [self] + self.sorted()[0].sortedr()

class Predictor:
    def __init__(self, file):
        # file is the history to read
        file = open(file, 'r', encoding = 'utf8', errors = 'ignore')
        data = file.read().lower().split('\n')
        file.close()

        terms = [i.split() + [''] for i in data]
        words = []
        for term in data:
            for word in term.split():
                words.append(list(word) + [''])

        self.children = [Trie('^') for _ in range(2)]

        self.populate(0, words)
        self.populate(1, terms)
    def populate(self, index, arr):
        # index is the trie to add to
        # arr is a two-dimensional array of items that end in ''
        for item in arr:
            self.children[index].addr(item)
    def predict(self, index, string):
        string = list(string)
        prediction = self.children[index].findr(string)
        if prediction:
            guesses = []
            for i in range(5):
                try:
                    guesses.append(string + [i.name for i in prediction.sorted()[i].sortedr()])
                except IndexError:
                    break
            return guesses
        else:
            return False
    def search(self, string):
        string = string.split()
        word = self.predict(0, list(string[-1]))
        if word:
            word = word[0]
            terms = string[:-1] + [''.join(word)]
            prediction = self.predict(1, terms)
            if prediction:
                return [' '.join(i[:-1]) for i in prediction]
            else:
                return [' '.join(terms)]
        else:
            return False
    def searchr(self, p = True):
        if p:
            print('Search for:')
        string = input('>>> ')
        if string != 'exit()' and string != '':
            guesses = self.search(string)
            if guesses:
                for guess in guesses:
                    print('... ' + guess)
            else:
                print('... No guesses!')
            self.searchr(False)

t = Predictor('history.txt')
t.searchr()