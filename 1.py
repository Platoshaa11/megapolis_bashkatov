'''открываю данный файл на чтение'''
fin=open('products.csv', 'r', encoding='utf-8')
'''открываю созданный файл для записи'''
fout=open('products_new.csv', 'w', encoding='utf-8')

otv_sum=0
'''записываю названия столбцов в новую таблицу'''
print(fin.readline().strip(), 'total', sep=';', file=fout)
for s in fin:
    '''считываю данные из таблицы'''
    cat, prod, date, price, unit=s.strip().split(';')
    '''записываю данные из старой таблицы + искомую цену в новую таблицу'''
    print(cat, prod, date, price, unit, float(price)*float(unit), sep=';', file=fout)
    '''добавляю итоговую цену в сумму для ответа'''
    otv_sum+=float(price)*float(unit)
print(otv_sum)