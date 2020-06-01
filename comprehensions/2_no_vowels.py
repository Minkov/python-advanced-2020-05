text = input()

vowels = {'a', 'o', 'u', 'e', 'i', 'A', 'O', 'U', 'E', 'I'}

no_vowels_text = [ch for ch in text if ch not in vowels]
print(''.join(no_vowels_text))
