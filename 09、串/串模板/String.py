# ����
s = ''

# ƴ��
s = s + 'hello'
print(s)
s += ' world'
print(s)

# ��ȡ����
print(len(s))

# ��
idx = s.find('world')
print(idx)

idx = s.find('World')
print(idx)

# ����
print(s[3])

# ��Ƭ
print(s[3:5])
print(s[:5])
print(s[3:])
print(s[:])
print(s[:-1])

# �Ƚ�
t = "hello world"
print(t == s)

# ����
t = "x"
s = t
print(s)