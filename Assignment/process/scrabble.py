def scrabble_score(word):
    SCORES = {...}
    score = 0
    word = word.upper()
    for letter in word:
        if letter.isalpha():
            score += next(points for points, letters in SCORES.items() if letter in letters)
    return score