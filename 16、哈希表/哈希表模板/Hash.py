hash = {}

# ��
hash['kk'] = 90
hash['gg'] = 3
hash['tt'] = 6
hash['zz'] = 8
print(hash)

# ɾ

hash.pop('tt')
print(hash)

# ��
hash['gg'] += 1
print(hash)

# ��
print( hash.get('kk', 0) )