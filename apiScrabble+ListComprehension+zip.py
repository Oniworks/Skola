#zip ir ka ravejsledzejs
#ltp = zip(letters, points)
#print(list(ltp))

#List Comprehension
#dictionary = {a : b for a, b in zip(letters, points)}
#print(dictionary)

letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]
point_dictionary = {a : b for a,b in zip(letters, points)}
point_dictionary[""] = 0

def score_word(word, point_dictionary):
    score = 0
    for letter in word:
        score += point_dictionary[letter.upper()]
    return score

player_to_word = {"player1" : ["blue", "Tennis", "Exit"], "wordNerd" : ["Earth", "Eyes", "Machine"], "Lexi Con" : ["Eraser", "Belly", "Husky"], "Prof Reader" : ["Zap", "Coma", "Period"]}

for player in player_to_word:
    player_score = 0
    for word in player_to_word[player]:
        player_score += score_word(word, point_dictionary)
    print(f"{player} scored {player_score}")