def count_vowels_consonants(string):
    vowels="aeiouAEIOU"
    consonants="bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    vowels_counts=sum(1 for char in string if char in vowels)
    consonants_counts=sum(1 for char in string if char in consonants)
    return vowels_counts,consonants_counts
    
input_string=input()
vowels,consonants=count_vowels_consonants(input_string)
print(vowels)
print(consonants)