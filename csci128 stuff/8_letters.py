# Roman Rodriguez
# CSCI 128 - Section J
# Assessment 8
# References: no one
# Time: 30 minutes

import helper_library

def get_input_grids():
    grid = []
    for i in range(5):
        newRow = input(f"ROW{i + 1}> ")
        if newRow == "DONE":
            return -1
        grid.append(newRow.split())

    return grid

def split_input_grids(inputGrids:list):
    letters = []
    try:
        x = inputGrids[0][0]
    except:
        return []
    amtLetters = (len(inputGrids[0]) // 6) + 1
    for i in range(len(inputGrids)):
        for j in range(len(inputGrids[i])):
            if inputGrids[i][j] != "0" and inputGrids[i][j] != "1":
                return -1
    
    startInd = 0
    for i in range(amtLetters):
        oneLetter = []
        for row in inputGrids:
            letLine = row[startInd:(startInd + 6)]
            for i in range(len(letLine)):
                letLine[i] = int(letLine[i])
            if len(letLine) > 5:
                letLine.pop()
            oneLetter.append(letLine)
        letters.append(oneLetter)
        startInd += 6

    return letters

def compute_scores(templates, letter_grid):
    scores = []
    toTry = len(templates)
    for trying in templates:
        score = 0
        for row in range(len(trying)):
            for col in range(len(trying[row])):
                if trying[row][col] == letter_grid[row][col]:
                    score += 1
        scores.append(score)

    return scores

def extract_letter(letters, computed_scores):
    highest = -1
    ind = 0
    for score in range(len(computed_scores)):
        if computed_scores[score] > highest:
            highest = computed_scores[score]
            ind = score
    
    return letters[ind]

if __name__ == "__main__":
    word = ""
    userIn = get_input_grids()
    if userIn == -1:
        print("OUTPUT ERROR: Invalid grid entered")
    elif split_input_grids(userIn) == -1:
        print("OUTPUT ERROR: Invalid pixel value encountered")
    else:
        numLetters = len(split_input_grids(userIn))
        print(f"OUTPUT {numLetters} Letters entered")
        templates = helper_library.get_grids()
        baseLetters = helper_library.get_letters()
        theLetters = split_input_grids(userIn)
        for i in range(numLetters):
            matchScores = compute_scores(templates, theLetters[i])
            word = word + str(extract_letter(baseLetters, matchScores))
        print(f"OUTPUT {word}")
