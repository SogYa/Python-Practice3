def repetition(word_1, word_2):
    return len(word_1) == len(word_2) and all(letter_1 in word_2 for letter_1 in word_1)


number = int(input())
words = sorted(input().lower() for i in range(number))
used = list()
for i in range(len(words) - 1):
    anagrams = [words[i]]
    for j in range(i + 1, len(words)):
        if repetition(words[i], words[j]) and words[i] not in used and words[j] not in used:
            anagrams.append(words[j])
            used.append(words[j])
    if len(anagrams) > 1:
        print(*anagrams)
