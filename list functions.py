Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> l=[1,2,3,4]
>>> l
[1, 2, 3, 4]
>>> dir(l)
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
>>> l.append([5,6,7])
>>> l
[1, 2, 3, 4, [5, 6, 7]]
>>> l.append([19,[23,54,67],234,[2343,678,97]])
>>> l
[1, 2, 3, 4, [5, 6, 7], [19, [23, 54, 67], 234, [2343, 678, 97]]]
>>> l[5]
[19, [23, 54, 67], 234, [2343, 678, 97]]
>>> l[5][2]
234
>>> l[5][1]
[23, 54, 67]
>>> l[5][1][2]
67
>>> l[5][1][3]
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    l[5][1][3]
IndexError: list index out of range
>>> l[5][1][0]
23
>>> print(l[5][1][0])
23
>>> l.contains[2]
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    l.contains[2]
AttributeError: 'list' object has no attribute 'contains'
>>> l.clear
<built-in method clear of list object at 0x0000000002DD0F08>
>>> l
[1, 2, 3, 4, [5, 6, 7], [19, [23, 54, 67], 234, [2343, 678, 97]]]
>>> l.Clear
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    l.Clear
AttributeError: 'list' object has no attribute 'Clear'
>>> l.clear
<built-in method clear of list object at 0x0000000002DD0F08>
>>> l
[1, 2, 3, 4, [5, 6, 7], [19, [23, 54, 67], 234, [2343, 678, 97]]]
>>> del l[:]
>>> l
[]
>>> l=[1,2,3,4]
>>> l.clear()
>>> l
[]
>>> l=[1,2,3,4]
>>> l
[1, 2, 3, 4]
>>> l.clear()
>>> copyl=l
>>> copyl
[]
>>> l=[1,2,3,4]
>>> copyl=l
>>> copyl
[1, 2, 3, 4]
>>> print(copyl)
[1, 2, 3, 4]
>>> l.count(1)
1
>>> l.count(2)
1
>>> l.count("2")
0
>>> list.count(l)
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    list.count(l)
TypeError: count() takes exactly one argument (0 given)
>>> l.count(2)
1
>>> l.count(3)
1
>>> l.count(2,3)
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    l.count(2,3)
TypeError: count() takes exactly one argument (2 given)
>>> l.extend("hello" , "fuck")
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    l.extend("hello" , "fuck")
TypeError: extend() takes exactly one argument (2 given)
>>> l.extend(["hello" , "fuck"])
>>> l
[1, 2, 3, 4, 'hello', 'fuck']
>>> list.insert(0,"the count starts from here ")
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    list.insert(0,"the count starts from here ")
TypeError: descriptor 'insert' requires a 'list' object but received a 'int'
>>> l.insert(0,"the count starts from here ")
>>> l
['the count starts from here ', 1, 2, 3, 4, 'hello', 'fuck']
>>> l.insert(0,'the count starts from here')
>>> l.clear(0)
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    l.clear(0)
TypeError: clear() takes no arguments (1 given)
>>> l.del[0]
SyntaxError: invalid syntax
>>> del l[1]
>>> l
['the count starts from here', 1, 2, 3, 4, 'hello', 'fuck']
>>> del l[0]
>>> l
[1, 2, 3, 4, 'hello', 'fuck']
>>> l.extend(0,'Numbers')
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    l.extend(0,'Numbers')
TypeError: extend() takes exactly one argument (2 given)
>>> l.insert(0,'Numbers')
>>> type[l]
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    type[l]
TypeError: 'type' object is not subscriptable
>>> type(l)
<class 'list'>
>>> l
['Numbers', 1, 2, 3, 4, 'hello', 'fuck']
>>> l.index('e')
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    l.index('e')
ValueError: 'e' is not in list
>>> l.index("e")
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    l.index("e")
ValueError: 'e' is not in list
>>> l..extend(["hello"])
SyntaxError: invalid syntax
>>> l.extend(["hello"])
>>> l
['Numbers', 1, 2, 3, 4, 'hello', 'fuck', 'hello']
>>> del.l[7]
SyntaxError: invalid syntax
>>> del l[7]
>>> l
['Numbers', 1, 2, 3, 4, 'hello', 'fuck']
>>> l.append(["hello ,"people"])
	      
SyntaxError: invalid syntax
>>> l.append(["hello","people"])
	      
>>> l
	      
['Numbers', 1, 2, 3, 4, 'hello', 'fuck', ['hello', 'people']]
>>> l.index("hello")
	      
5
>>> l.append(5)
	      
>>> l
	      
['Numbers', 1, 2, 3, 4, 'hello', 'fuck', ['hello', 'people'], 5]
>>> l.append("hello")
	      
>>> l
	      
['Numbers', 1, 2, 3, 4, 'hello', 'fuck', ['hello', 'people'], 5, 'hello']
>>> l.remove("hello")
	      
>>> lreve=l.reverse()
	      
>>> lreve
	      
>>> print(lereve)
	      
Traceback (most recent call last):
  File "<pyshell#78>", line 1, in <module>
    print(lereve)
NameError: name 'lereve' is not defined
>>> print(lreve)
	      
None
>>> print(l.reverse())
	      
None
>>> l.reverse()
	      
>>> print(l)
	      
['hello', 5, ['hello', 'people'], 'fuck', 4, 3, 2, 1, 'Numbers']
>>> lrev=print(l)
	      
['hello', 5, ['hello', 'people'], 'fuck', 4, 3, 2, 1, 'Numbers']
>>> lrev
	      
>>> print(lrev)
	      
None
>>> sortthelist<-sort(l)
	      
Traceback (most recent call last):
  File "<pyshell#86>", line 1, in <module>
    sortthelist<-sort(l)
NameError: name 'sortthelist' is not defined
>>> sortthelist=l.sort()
	      
Traceback (most recent call last):
  File "<pyshell#87>", line 1, in <module>
    sortthelist=l.sort()
TypeError: '<' not supported between instances of 'int' and 'str'
>>> l.sort()
	      
Traceback (most recent call last):
  File "<pyshell#88>", line 1, in <module>
    l.sort()
TypeError: '<' not supported between instances of 'int' and 'str'
>>> lsort=[1,23,44,5]
	      
>>> l.sort()
	      
Traceback (most recent call last):
  File "<pyshell#90>", line 1, in <module>
    l.sort()
TypeError: '<' not supported between instances of 'int' and 'str'
>>> l
	      
['hello', 5, ['hello', 'people'], 'fuck', 4, 3, 2, 1, 'Numbers']
>>> l.pop()
	      
'Numbers'
>>> l
	      
['hello', 5, ['hello', 'people'], 'fuck', 4, 3, 2, 1]
>>> l.pop()
	      
1
>>> 
