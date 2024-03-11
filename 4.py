def genpromo(prod, date):
    '''Функция создает промокод по заданному алгоритму и возвращает его'''
    '''
    Атрибуты:
        prod - Название продукта
        date - Дата его поступления
    '''
    otv=''
    '''строю промокод'''
    otv+=prod[0].upper()+prod[1].upper()+str(date.split('.')[0])+prod[-2:][::-1].upper()+str(date.split('.')[1])[::-1]
    '''возвращаю строку'''
    return otv



'''открываю данный файл на чтение'''
fin=open('products.csv', 'r', encoding='utf-8')
'''открываю созданный файл для записи'''
fout=open('product_promo.csv', 'w', encoding='utf-8')


'''записываю названия столбцов в новую таблицу'''
print(fin.readline().strip(), 'promocode', sep=';', file=fout)
for s in fin:
    '''считываю данные из таблицы'''
    cat, prod, date, price, unit=s.strip().split(';')
    '''записываю данные из старой таблицы + искомую цену в новую таблицу'''
    print(cat, prod, date, price, unit, genpromo(prod, date), sep=';', file=fout)
