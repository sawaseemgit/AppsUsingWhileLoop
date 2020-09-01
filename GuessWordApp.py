import random as r

print('Welcome to the Guess My Word App')
game_dict = {
    'sports': ['basketball', 'baseball', 'soccer', 'football', 'tennis', 'cricket'],
    'colors': ['red', 'yellow', 'pink', 'white', 'purple', 'violet'],
    'fruits': ['apple', 'mango', 'banana', 'watermelon', 'peach', 'strawberry'],
    'classes': ['english', 'history', 'science', 'mathematics', 'arts', 'music']
}
game_keys = []
for key in game_dict.keys():
    game_keys.append(key)

game_category = game_keys[r.randint(0, len(game_keys) - 1)]
game_word = game_dict[game_category][r.randint(0, len(game_dict[game_category]) - 1)]

blank_word = []
for letter in game_word:
    blank_word.append('-')
guess_count = 0
guess = ''
print(f'Enter a {len(game_word)} word from "{game_category}" category: ')
while guess != game_word:
    print(''.join(blank_word))
    guess = input('Enter your guess letter: ').lower().strip()
    guess_count += 1
    if guess == game_word:
        print(f'Thats Correct. You guess the word in {guess_count} guesses.')
    else:
        print('Thats not right. let us reveal a letter to help you.')
        swap = True
        while swap:
            letter_index = r.randint(0, len(game_word) - 1)
            if blank_word[letter_index] == '-':
                blank_word[letter_index] = game_word[letter_index]
                swap = False

choice = input('Would you like to play again?(Yes/No): ').lower().strip()
if choice.startswith('n'):
    repeat = False
    print('Thank you for playing the game. Good bye.!')