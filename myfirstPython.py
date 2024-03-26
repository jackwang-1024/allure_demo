name = "xiaoming"
print(name.center(40,'*'))
age = 18
print('My name is %s, %d years old' % (name, age))
print(('hello %s' % name).capitalize())

print(f'Nice to meet you,{name}')
print(f'Nice to meet you,{1 + 2}')
print(f'Nice to meet you,{name}:{age}')
x = 1
print(f'{x+1=}')

a = "{1} {0} {1}".format("hello", "world")
print(a)

b = '''
CREATE TABLE users (  
login VARCHAR(8), 
uid INTEGER,
prid INTEGER)
'''
print(b)
