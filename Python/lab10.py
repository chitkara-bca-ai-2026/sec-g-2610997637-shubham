# Save your file as: lab10_text_processing.py

print("=========================================")
print("          TEXT PROCESSING TOOL          ")
print("=========================================")

# 1. Accept a sentence from the user
sentence = input("Enter a sentence: ")
print()
print("--- Processing Results ---")

# 2. Display a character at a specific position using string indexing
pos = int(input("Enter position for indexing: "))
print(f"Character at position {pos} : '{sentence[pos]}'")

# 3. Extract a portion of the sentence using string slicing
start = int(input("Enter start index for slicing : "))
end = int(input("Enter end index for slicing   : "))
print(f"Sliced string [{start}:{end}]          : '{sentence[start:end]}'")

# 4 & 5. Convert the sentence into uppercase and lowercase
print(f"Uppercase                    : {sentence.upper()}")
print(f"Lowercase                    : {sentence.lower()}")

# 6. Replace a specified word with another word
to_replace = input("Enter word to replace        : ")
replace_with = input("Enter replacement word       : ")
print(f"After replace                : {sentence.replace(to_replace, replace_with)}")

# 7. Find and display the length of the sentence
print(f"Length of sentence           : {len(sentence)}")
print()

print("=========================================")
print("Analysis Complete!")
print("=========================================")
