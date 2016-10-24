def ransom_note(magazine, rasom):

    def create_words_dict(words):
        words_dict = dict()
        for word in words:
            if word in words_dict:
                words_dict[word] += 1
            else:
                words_dict[word] = 1
        return words_dict

    magazine_dict = create_words_dict(magazine)
    rasom_dict = create_words_dict(rasom)

    for word in rasom:
        if word not in magazine_dict or magazine_dict[word] < rasom_dict[word]:
            return False
    return True

m, n = map(int, input().strip().split(' '))
magazine = input().strip().split(' ')
ransom = input().strip().split(' ')
answer = ransom_note(magazine, ransom)
if (answer):
    print("Yes")
else:
    print("No")


