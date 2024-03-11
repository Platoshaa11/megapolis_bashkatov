fin=open('products.csv', 'r', encoding='utf-8') '''открываю данный файл на чтение'''
fout=open('products_new.csv', 'w', encoding='utf-8') '''открываю созданный файл для записи'''

otv_sum=0
print(fin.readline().strip(), 'total', sep=';', file=fout) '''записываю названия столбцов в новую таблицу'''
for s in fin:
    cat, prod, date, price, unit=s.strip().split(';')
    print(cat, prod, date, price, unit, float(price)*float(unit), sep=';', file=fout) '''записываю данные из старой таблицы + искомую цену в новую таблицу'''