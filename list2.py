Python 3.12.0 (tags/v3.12.0:0fb18b0, Oct  2 2023, 13:03:39) [MSC v.1935 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> l1=[10,20,30,40,50]
>>> l1
[10, 20, 30, 40, 50]
>>> l1.a
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    l1.a
AttributeError: 'list' object has no attribute 'a'
>>> l1.append(100)
>>> l1
[10, 20, 30, 40, 50, 100]
