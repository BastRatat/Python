# VARIABLES

x = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
y = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]
print("Input a word to play scrabble")
word = input("")
game = Game(x, y, word)
letter_to_points = game.letter_to_point()
print(letter_to_points)
# CLASSES DECLARATION

class Game:

    def __init__(self, letters, points, word=None):
        self.letters = letters
        self.points = points
        self.word = word
        

    def letter_to_point(self):
        dictionary = {key:value for key, value in zip(self.letters, self.points)}
        dictionary.update({" ":0})
        return dictionary

    def __repr__(self):
        return "{}\r {}\r {}\r".format(self.letters,  self.points, self.word)

class Calculations(Game):

    def __init__(self, word):
        self.word = word

    def score_word(self):
        point_total = 0
        for letter in self.word:
            point_total += letter_to_points.get(letter, 0)
        return point_total 



# INSTANTIATIONS AND CALLS 
print("You chose to find out the how many points you'll get from {}".format(word))

# print(game) # returns the repr() method.

#print(letter_to_points)
test = Calculations(word)
print(test.score_word())