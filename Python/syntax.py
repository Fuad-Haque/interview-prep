"""Algorithm Name: Frequency Counting (Hash Map/Dictionary Counting)"""

#1 word count:
def word_count(text: str) -> dict[str, int]:
    counts = {}
    words = text.lower().split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1
    return counts
print(word_count("Hello my Name is Fuad hello"))

#2 character count:
def char_count(text: str) -> dict[str, int]:
    countss = {}
    for char in text.lower():
        if char.isalpha():
            countss[char] = countss.get(char, 0) + 1
    return countss
print(char_count("Hello myyy naame is Fuad"))

#3 vowel count:
def vowel_count_per_word(sentence: str) -> dict[str, int]:
    vowels = set('aieou')
    countsss = {}
    for word in sentence.lower().split():
        countsss[word] = sum(1 for char in word if char in vowels)
    return countsss
print(vowel_count_per_word("Fuuuaaad"))
