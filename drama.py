from itertools import permutations

# Үгний үсгүүдийг тоонд хөрвүүлэх
def word_to_number(word, mapping):
    return sum(mapping[letter] * (10 ** (len(word) - idx - 1)) for idx, letter in enumerate(word))

# Бүх боломжит тоон хослолуудыг олох
def solve_equation():
    letters = 'drama' + 'drama' + 'teatr'
    unique_letters = set(letters)

    # Хэрэв давхар үсэг байгаа бол үсгийн тоо нь 10-оос их байж болохгүй
    if len(unique_letters) > 10:
        return None

    # Үсгүүдэд таарах тоон хослолыг олох
    for perm in permutations(range(10), len(unique_letters)):
        mapping = dict(zip(unique_letters, perm))

        # Эхний үсгүүдийн тоо 0 байхгүй байвал шалгах
        if mapping['d'] == 0 or mapping['t'] == 0:
            continue

        # Дээрх нөхцөлийг шалгах
        drama1 = word_to_number('drama', mapping)
        drama2 = word_to_number('drama', mapping)
        teatr = word_to_number('teatr', mapping)

        if drama1 + drama2 == teatr:
            return mapping  # Тухайн хослолыг буцаана

    return None

result = solve_equation()

if result:
    print(f"Тохирох тоон хослол: {result}")
else:
    print("Тохирох шийдэл олдсонгүй.")
