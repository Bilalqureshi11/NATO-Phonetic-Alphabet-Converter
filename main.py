# import pandas

# # Read the CSV file
# data = pandas.read_csv('nato_phonetic_alphabet.csv')

# # Create a dictionary from the DataFrame
# phonetic_dict = {row.letter: row.code for (_, row) in data.iterrows()}

# # Get user input and convert to phonetic alphabet
# word = input('Enter a word: ').upper()

# try:
#     output_list = [phonetic_dict[letter] for letter in word]
# except KeyError:
#     print('Sorry, only letters in the alphabet are allowed.')
# else:
#     print(output_list)





import os

# Print current directory
print("Current Directory:", os.getcwd())

# Check if file exists
file_path = "nato_phonetic_alphabet.csv"

if os.path.exists(file_path):
    print("✅ File Found!")
else:
    print("❌ File NOT Found! Check the folder again.")

# Now try reading the file
import pandas
try:
    data = pandas.read_csv(file_path)
    print("✅ CSV Loaded Successfully!")
except Exception as e:
    print("❌ Error:", e)

