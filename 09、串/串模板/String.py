# 创建
s = ''

# 拼接
s = s + 'hello'
print(s)
s += ' world'
print(s)

# 获取长度
print(len(s))

# 查
idx = s.find('world')
print(idx)

idx = s.find('World')
print(idx)

# 索引
print(s[3])

# 切片
print(s[3:5])
print(s[:5])
print(s[3:])
print(s[:])
print(s[:-1])

# 比较
t = "hello world"
print(t == s)

# 拷贝
t = "x"
s = t
print(s)