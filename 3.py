'''открываю данный файл на чтение'''
fin=open('products.csv', 'r', encoding='utf-8')
'''считываю первую строку чтобы не мешала'''
fin.readline()
w=dict()

for s in fin:
    '''считываю данные из таблицы'''
    cat, prod, date, price, unit=s.strip().split(';')
    '''добавляю все данные в словарь'''
    unit=float(unit)
    if cat in w:
        if prod in w[cat]:
            w[cat][prod]+=unit
        else:
            w[cat][prod]=unit
    else:
        w[cat]=dict()
        w[cat][prod]=unit

s=input()
while s!='молоко':
    if s not in w:
        print('Такой категории не существует в нашей БД')
    else:
        mi=10**9
        pr=''
        for el in w[s]:
            if w[s][el]<mi:
                mi=w[s][el]
                pr=el
        print("В категории: "+s+" товар: "+pr+" был куплен "+str(int(mi))+" раз")
    s=input()