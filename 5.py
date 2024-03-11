'''открываю данный файл на чтение'''
fin=open('products.csv', 'r', encoding='utf-8')
'''открываю данный файл на запись'''
fout=open(' few_products.txt', 'w', encoding='utf-8')
'''считываю первую строку чтобы не мешала'''
fin.readline()
w=dict()

for s in fin:
    '''считываю данные из таблицы'''
    cat, prod, date, price, unit=s.strip().split(';')
    '''добавляю все данные в словарь'''
    unit=float(unit)
    w[cat]=w.get(cat, 0)+unit
k=0
for a, b in sorted(w.items(), key=lambda x:x[1]):
    if k==10:
        break
    print(a, b, file=fout)
    k+=1