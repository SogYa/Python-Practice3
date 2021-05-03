def check_rhythm(phrases):
    russian_vowels = ['а', 'о', 'э', 'и', 'у', 'ы', 'е', 'ё', 'ю', 'я']
    number_of_vowels_in_phrases = [len([c for c in phrase if c in russian_vowels]) for phrase in phrases]
    if max(number_of_vowels_in_phrases) == min(number_of_vowels_in_phrases):
        return 'Парам пам-пам'
    else:
        return 'Пам парам'


print(check_rhythm(input().split(' ')))
