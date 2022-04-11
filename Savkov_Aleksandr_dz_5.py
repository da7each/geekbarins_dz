def odd_nums(m):
    n = 1
    while n <= m:
        yield n
        n += 2

odd_to_15 = odd_nums(15)
print(next(odd_to_15))
print(next(odd_to_15))
print(next(odd_to_15))
print(next(odd_to_15))
print(next(odd_to_15))
print(next(odd_to_15))
print(next(odd_to_15))
print(next(odd_to_15))
print(next(odd_to_15))

m2 = 15
odd_nums_gen = (n for n in range(1, m2, 2))
print(next(odd_nums_gen))
print(next(odd_nums_gen))
print(next(odd_nums_gen))
print(next(odd_nums_gen))
print(next(odd_nums_gen))
print(next(odd_nums_gen))
print(next(odd_nums_gen))
print(next(odd_nums_gen))
print(next(odd_nums_gen))

tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена']
klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']

dict_gen = ((tutors,klasses) for tutors, klasses in zip(tutors,klasses))
print(next(dict_gen))
print(next(dict_gen))
print(next(dict_gen))
print(next(dict_gen))
print(next(dict_gen))
print(next(dict_gen))
print(next(dict_gen))
print(next(dict_gen))


src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
new_list = [num for i, num in enumerate(src) if num > src[i - 1] and i != 0]
print(new_list)


src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
new_list = [num for num in src if src.count(num) == 1]
print(new_list)