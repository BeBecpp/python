# Үгсийг тооны утгатай харьцуулах
def word_to_number(word):
    # Үгийн урт, утга болон бүтэцтэй тохирох тоо
    word_dict = {
        'd': 1,
        'r': 2,
        'a': 3,
        'm': 4,
        't': 5,
        'e': 6
    }
    
    return sum(word_dict.get(letter, 0) for letter in word)

# Жишээ
word1 = "drama"
word2 = "drama"
word3 = "teatr"

result1 = word_to_number(word1)
result2 = word_to_number(word2)
result3 = word_to_number(word3)

print(f"Drama + Drama = {result1 + result2}")
print(f"Teatr = {result3}")
