import pandas

# Read the CSV file
data = pandas.read_csv('nato_phonetic_alphabet.csv')

# Create a dictionary from the DataFrame
phonetic_dict = {row.letter: row.code for (_, row) in data.iterrows()}

# Get user input and convert to phonetic alphabet
word = input('Enter a word: ').upper()

try:
    output_list = [phonetic_dict[letter] for letter in word]
except KeyError:
    print('Sorry, only letters in the alphabet are allowed.')
else:
    print(output_list)





