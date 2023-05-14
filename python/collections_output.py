Python 3.9.5 (tags/v3.9.5:0a7dcbd, May  3 2021, 17:27:52) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> st = "python Narayana"
>>> print(st)
python Narayana
>>> st = [8:11]
SyntaxError: invalid syntax
>>> st[8:12]
'aray'
>>> st[-7:4]
''
>>> st[5:-9]
'n'
>>> st[20:30]
''
>>> st[12:-8]
''
>>> st[1:4]
'yth'
>>> st[11:]
'yana'
>>> st[2:]
'thon Narayana'
>>> st[:]
'python Narayana'
>>> st[3::4]
'hNy'
>>> st[4::-3]
'oy'
>>> st[-3::-6]
'a p'
>>> st[-1::-1]
'anayaraN nohtyp'
>>> st[-1::-1]
'anayaraN nohtyp'
>>> st1 = "python"
>>> st2 = "developer"
>>> st = st1+st2
>>> print(st)
pythondeveloper
>>> 
>>> st = "python"
>>> n = 3
>>> st1 = st * n
>>> print(st1)
pythonpythonpython
>>> 
>>> x = 'a'
>>> y = 'b'
>>> z = 'c'
>>> st = x+y+z
>>> print(st)
abc
>>> st1 = ''.join(x+y+z)
>>> print(st1)
abc
>>> st = ' '.join(x+y+z)
>>> print(st)
a b c
>>> st = ','.join(x+y+z)
>>> print(st)
a,b,c
>>> st = '*'.join(x+y+z)
>>> print(st)
a*b*c
>>> st = 'python'
>>> st = a,b,c,d,e,f
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    st = a,b,c,d,e,f
NameError: name 'a' is not defined
>>> a,b,c,d,e,f = st
>>> print(st)
python
>>> print(a)
p
>>> print)b)
SyntaxError: unmatched ')'
>>> print(b)
y
>>> 
>>> st = "sadfsahfkjsahfkjsahfjksadhfjhsajkfhaskjfhqeruyyf"
>>> print(st)
sadfsahfkjsahfkjsahfjksadhfjhsajkfhaskjfhqeruyyf
>>> len(st)
48
>>> count(st)
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    count(st)
NameError: name 'count' is not defined
>>> count(st('a'))
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    count(st('a'))
NameError: name 'count' is not defined
>>> st.count('a')
7
>>> st.count('j')
6
>>> st.count('as')
1
>>> st.index('j')
9
>>> st.lower()
'sadfsahfkjsahfkjsahfjksadhfjhsajkfhaskjfhqeruyyf'
>>> st.upper()
'SADFSAHFKJSAHFKJSAHFJKSADHFJHSAJKFHASKJFHQERUYYF'
>>> st.swapcase()
'SADFSAHFKJSAHFKJSAHFJKSADHFJHSAJKFHASKJFHQERUYYF'
>>> st1 = 'PYTHON narayana'
>>> st1.swapcase()
'python NARAYANA'
>>> st = 'python'
>>> st.islower()
True
>>> st.isupper()
False
>>> st1='PYTHON'
>>> st1.islower()
False
>>> st1.isupper()
True
>>> st2 = "python developer in hyderabad"
>>> st2.title()
'Python Developer In Hyderabad'
>>> st2.captitalize()
Traceback (most recent call last):
  File "<pyshell#70>", line 1, in <module>
    st2.captitalize()
AttributeError: 'str' object has no attribute 'captitalize'
>>> st2.capitalize()
'Python developer in hyderabad'
>>> 
>>> 
>>> st = "python"
>>> st.startswith('p')
True
>>> st.endswith('er')
False
>>> st = "python developer in hyderabada"
>>> st.split()
['python', 'developer', 'in', 'hyderabada']
>>> st = "python developer in hyderabada"
>>> st.split('n')
['pytho', ' developer i', ' hyderabada']
>>> st = "python,developer,in,hyderabada"
>>> st.split(',')
['python', 'developer', 'in', 'hyderabada']
>>> print(type(st))
<class 'str'>
>>> st = "laxman"
>>> st.replace('a','_')
'l_xm_n'
>>> st.replace('a','_',1)
'l_xman'
>>> st/replace('a','_',2)
Traceback (most recent call last):
  File "<pyshell#87>", line 1, in <module>
    st/replace('a','_',2)
NameError: name 'replace' is not defined
>>> st.replace('a','_',2)
'l_xm_n'
>>> lst = [10,20,30,40,50,60,70,80,90]
>>> lst[:]
[10, 20, 30, 40, 50, 60, 70, 80, 90]
>>> lst[1:-1]
[20, 30, 40, 50, 60, 70, 80]
>>> lst[-1:-1]
[]
>>> lst[-1::-1]
[90, 80, 70, 60, 50, 40, 30, 20, 10]
>>> lst[-4:5]
[]
>>> lst[-4:8]
[60, 70, 80]
>>> lst[:]
[10, 20, 30, 40, 50, 60, 70, 80, 90]
>>> lst[2::3]
[30, 60, 90]
>>> lst[2::-2}
SyntaxError: closing parenthesis '}' does not match opening parenthesis '['
>>> lst[4::-2]
[50, 30, 10]
>>> lst[5::-9]
[60]
>>> lst1=[1,2,3]
>>> lst2=[2,3,4]
>>> lst3=lst1+lst2
>>> print(lst1)
[1, 2, 3]
>>> lst4=[5,6,7]
>>> lst5=[8,9,10]
>>> lst6=lst4+lst5
>>> print(lst6)
[5, 6, 7, 8, 9, 10]
>>> n= 3
>>> ls = lst * n
>>> print(ls)
[10, 20, 30, 40, 50, 60, 70, 80, 90, 10, 20, 30, 40, 50, 60, 70, 80, 90, 10, 20, 30, 40, 50, 60, 70, 80, 90]
>>> 
>>> 
>>> 
>>> lst = [10,20,true,1,'a',False,true]
Traceback (most recent call last):
  File "<pyshell#115>", line 1, in <module>
    lst = [10,20,true,1,'a',False,true]
NameError: name 'true' is not defined
>>> lst = [10,20,true,1,0,false,true]
Traceback (most recent call last):
  File "<pyshell#116>", line 1, in <module>
    lst = [10,20,true,1,0,false,true]
NameError: name 'true' is not defined
>>> lst = [10,20,True,1,0,'a',True,False]
>>> lst.count(1)
3
>>> lst.count(0)
2
>>> lst.count(True)
3
>>> lst.(False)
SyntaxError: invalid syntax
>>> lst.count(False)
2
>>> lst.index('a')
5
>>> lst.index(10)
0
>>> lst.index(1)
2
>>> lst.index(x)
5
>>> lst = [10,20,30]
>>> lst(max)
Traceback (most recent call last):
  File "<pyshell#128>", line 1, in <module>
    lst(max)
TypeError: 'list' object is not callable
>>> max(lst)
30
>>> min(lst)
10
>>> sum(lst)
60
>>> 
>>> lst = [10,20,30]
>>> lst.append(4)
>>> print(lst)
[10, 20, 30, 4]
>>> lst.append(100,200)
Traceback (most recent call last):
  File "<pyshell#136>", line 1, in <module>
    lst.append(100,200)
TypeError: list.append() takes exactly one argument (2 given)
>>> lst.append(90)
>>> print(lst)
[10, 20, 30, 4, 90]
>>> lst.extend([100,200])
>>> print(lst)
[10, 20, 30, 4, 90, 100, 200]
>>> lst.extend(100,200,300)
Traceback (most recent call last):
  File "<pyshell#141>", line 1, in <module>
    lst.extend(100,200,300)
TypeError: list.extend() takes exactly one argument (3 given)
>>> lst.extend([100,200,300])
>>> print(lst)
[10, 20, 30, 4, 90, 100, 200, 100, 200, 300]
>>> lst.inser(3,'laxman')
Traceback (most recent call last):
  File "<pyshell#144>", line 1, in <module>
    lst.inser(3,'laxman')
AttributeError: 'list' object has no attribute 'inser'
>>> lst.insert([3,'laxman'])
Traceback (most recent call last):
  File "<pyshell#145>", line 1, in <module>
    lst.insert([3,'laxman'])
TypeError: insert expected 2 arguments, got 1
>>> lst.insert(0,True)
>>> print(lst)
[True, 10, 20, 30, 4, 90, 100, 200, 100, 200, 300]
>>> lst.insert(2,'a')
>>> print(lst)
[True, 10, 'a', 20, 30, 4, 90, 100, 200, 100, 200, 300]
>>> lst.insert([2,'b'],[4,'c'])
Traceback (most recent call last):
  File "<pyshell#150>", line 1, in <module>
    lst.insert([2,'b'],[4,'c'])
TypeError: 'list' object cannot be interpreted as an integer
>>> lst = [10,20,30]
>>> lst.remove(10)
>>> print(lst)
[20, 30]
>>> lst.pop(2)
Traceback (most recent call last):
  File "<pyshell#154>", line 1, in <module>
    lst.pop(2)
IndexError: pop index out of range
>>> lst1 = [10,20,20,30,50]
>>> lst1.pop(3)
30
>>> print(lst)
[20, 30]
>>> t = 10,10,20,20
>>> print(t)
(10, 10, 20, 20)
>>> type(t)
<class 'tuple'>
>>> s = {10,20,10,20,40,50,70}
>>> print(s)
{50, 20, 70, 40, 10}
>>> type(s)
<class 'set'>
>>> 
>>> 
>>> lst = [10,20,30,10,40,50,50,60]
>>> lst2 = list(set(lst))
>>> print(lst2)
[40, 10, 50, 20, 60, 30]
>>> type(lst2)
<class 'list'>
>>> 
>>> 
>>> t = (10,10,20,30,40,50,20,20,30,40,50)
>>> t2 = tuple(set(t))
>>> print(t2)
(40, 10, 50, 20, 30)
>>> type(t2)
<class 'tuple'>
>>> 
>>> 
>>> 
>>> st = "laxman"
>>> st2 = ''.join(set(st))
>>> print(st2)
xlanm
>>> print(st2)
xlanm
>>> type(st2)
<class 'str'>
>>> 
>>> 
>>> a = 10
>>> b = 'a'
>>> c = True
>>> d = 1.5
>>> s = {a,b,c,d}
>>> print(S)
Traceback (most recent call last):
  File "<pyshell#191>", line 1, in <module>
    print(S)
NameError: name 'S' is not defined
>>> print(s)
{'a', 10, True, 1.5}
>>> type(s)
<class 'set'>
>>> s = {10,20,20,30,40,50,40,50}
>>> len(s)
5
>>> s.count(10)
Traceback (most recent call last):
  File "<pyshell#196>", line 1, in <module>
    s.count(10)
AttributeError: 'set' object has no attribute 'count'
>>> s = {10,20,30}
>>> s1=s.add(10)
>>> print(s1)
None
>>> s2=s.add{50}
SyntaxError: invalid syntax
>>> s2=s.add(50)
>>> print(s2)
None
>>> 
>>> 
>>> 
>>> 
>>> s = {10,20,30,50}
>>> s.remove(10)
>>> print(s)
{20, 50, 30}
>>> s.remove(60)
Traceback (most recent call last):
  File "<pyshell#210>", line 1, in <module>
    s.remove(60)
KeyError: 60
>>> s.discard(60)
>>> print(s)
{20, 50, 30}
>>> 
>>> 
>>> emp = {'eno':'101','ename':'laxman','sal':'10000'}
>>> print(emp)
{'eno': '101', 'ename': 'laxman', 'sal': '10000'}
>>> type(emp)
<class 'dict'>
>>> emp['salary'] = 40000
>>> print(emp)
{'eno': '101', 'ename': 'laxman', 'sal': '10000', 'salary': 40000}
>>> emp['ename'] =  'bangaru laxman'
>>> print(emp)
{'eno': '101', 'ename': 'bangaru laxman', 'sal': '10000', 'salary': 40000}
>>> 
>>> 
>>> 
>>> emp['eno'] = '100'
>>> print(emp)
{'eno': '100', 'ename': 'bangaru laxman', 'sal': '10000', 'salary': 40000}
>>> 
>>> emp.pop('eno')
'100'
>>> print(emp)
{'ename': 'bangaru laxman', 'sal': '10000', 'salary': 40000}
>>> emp.popitem()
('salary', 40000)
>>> print(emp)]
SyntaxError: unmatched ']'
>>> print(emp)
{'ename': 'bangaru laxman', 'sal': '10000'}
>>> len(emp)
2
>>> emp = {'eno':'101','ename':'laxman','sal':'20000'}
>>> print(emp)
{'eno': '101', 'ename': 'laxman', 'sal': '20000'}
>>> emp.keys()
dict_keys(['eno', 'ename', 'sal'])
>>> emp.values()
dict_values(['101', 'laxman', '20000'])
>>> 
>>> emp1 = {'company':'mphasis','loc':'hyd'}
>>> emp1.update(emp)
>>> print(emp)
{'eno': '101', 'ename': 'laxman', 'sal': '20000'}
>>> print(emp1)
{'company': 'mphasis', 'loc': 'hyd', 'eno': '101', 'ename': 'laxman', 'sal': '20000'}
>>> 
>>> t = (10,20,30,40)
>>> d = {}.fromkeys(t,0)
>>> print(d)
{10: 0, 20: 0, 30: 0, 40: 0}
>>> st = "bangaru laxman"
>>> d = {}.fromkeys(st,0)
>>> print(d)
{'b': 0, 'a': 0, 'n': 0, 'g': 0, 'r': 0, 'u': 0, ' ': 0, 'l': 0, 'x': 0, 'm': 0}
>>> 
>>> 
>>> 