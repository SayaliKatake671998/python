Python 3.12.0 (tags/v3.12.0:0fb18b0, Oct  2 2023, 13:03:39) [MSC v.1935 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
dict1={1:"one",2:"two"}
print(dict1)
{1: 'one', 2: 'two'}
clear dict1
SyntaxError: incomplete input
dict1.clear()
print(dict1)
{}
dict1={1:"one",2:"two"}

print(dict1)
{1: 'one', 2: 'two'}
del dict1
print(dict1)
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    print(dict1)
NameError: name 'dict1' is not defined. Did you mean: 'dict'?
>>> 
>>> dict1={1:"one",2:"two"}
... 
>>> dict1.get(2)
'two'
>>> dict1.get(3)
>>> dict1.get(5:"not found")
SyntaxError: invalid syntax
>>> dict1.get(5,"not found")
'not found'
>>> 1 in dict1
True
>>> 3 in dict1
False
>>> 5 in dict1
False
>>> dict1.items()
dict_items([(1, 'one'), (2, 'two')])
>>> dict1.keys()
dict_keys([1, 2])
>>> print(len(dict1))
2
>>> s=len(dict2)
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    s=len(dict2)
NameError: name 'dict2' is not defined. Did you mean: 'dict1'?
>>> s=len(dict1)
>>> print(s)
2
>>> dict2={2:"two",3:"Three",4:"four"}
>>> dict1.update(dict2)
>>> print(dict1)
{1: 'one', 2: 'two', 3: 'Three', 4: 'four'}
>>> print(dict2)
{2: 'two', 3: 'Three', 4: 'four'}
>>> dict2.values()
dict_values(['two', 'Three', 'four'])
