def get_count_char(str_):
    k = {}
    str_=str_.lower()
    for i in str_:
        if i.isalpha() and i not in k:
            k[i] = str_.count(i)
    return k

main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
print(get_count_char(main_str))
l = get_count_char(main_str)
def poly_musor():
    a = 0
    for key in l:
        a += l[key]
    g = {}
    for v in l:
        g[v] = int(l[v]*100/a)
    return g
print(poly_musor())