money=int(input("введите сумму "))
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
diposit1 = money * per_cent['ТКБ'] / 100
diposit2 = money * per_cent['СКБ'] / 100
diposit3 = money * per_cent['ВТБ'] / 100
diposit4 = money * per_cent['СБЕР'] / 100
deposit= []
deposit.append(diposit1)
deposit.append(diposit2)
deposit.append(diposit3)
deposit.append(diposit4)
print(deposit)
print(('Максимальная сумма, которую вы можете заработать-') , (max(deposit)))
