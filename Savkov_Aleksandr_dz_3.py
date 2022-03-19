numbers = {
    'one' : 'один',
    'two' : 'два',
    'three' : 'три',
    'four' : 'четыре',
    'five' : 'пять',
    'six' : 'шесть',
    'seven' : 'семь',
    'eight' : 'восемь',
    'nine' : 'девять',
    'ten' : 'десять'
}

def num_translate (number):
    return numbers.get(number)

print(num_translate('one'))
print(num_translate('eleven'))


def thesaurus(*names):
    result = dict()
    for name in names:
        result.setdefault(name[0], [])
        result[name[0]].append(name)
    return result

print(thesaurus("Иван", "Мария", "Петр", "Илья"))



import random

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

def get_jokes(num):
    joke_list = []
    for i in range(num):
        from_nouns = random.choice(nouns)
        from_adverbs = random.choice(adverbs)
        from_adjectives = random.choice(adjectives)
        joke_list.append(f'{from_nouns} {from_adverbs} {from_adjectives}')
    return joke_list


print(get_jokes(1))
print(get_jokes(2))


