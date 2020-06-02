from Hash_table.hash_table import MyHash

hash_table = MyHash(10)
hash_table.add_hash('Dmitry Kuznetsov', '888888888')
hash_table.add_hash('Ivan Ivanov', '9999999999')
hash_table.add_hash('Fedor', '55555555555')
hash_table.add_hash('Egor', '44444444444')
hash_table.add_hash('Oleg', '22222222222')

print(hash_table)
