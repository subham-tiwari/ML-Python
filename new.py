Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> print("computes the avag")
computes the avag
>>> print(" ")
 
>>> score1,score2=eval(input("enter the values of score 1 and score 2 "))
enter the values of score 1 and score 2 
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    score1,score2=eval(input("enter the values of score 1 and score 2 "))
  File "<string>", line 0
    
    ^
SyntaxError: unexpected EOF while parsing
>>> score1,score2=eval(input("enter the values of score 1 and score 2 "))
enter the values of score 1 and score 2 123
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    score1,score2=eval(input("enter the values of score 1 and score 2 "))
TypeError: cannot unpack non-iterable int object
>>> score1,score2=eval(input("enter the values of score 1 and score 2 "))
enter the values of score 1 and score 2 123 3445
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    score1,score2=eval(input("enter the values of score 1 and score 2 "))
  File "<string>", line 1
    123 3445
           ^
SyntaxError: unexpected EOF while parsing
>>> print("Computes the Avag")
print(" ")
score1,score2=eval(input("enter the values of Score 1 and Score 2"))
Avg=(score1+score2)/2
print("Avg is",Avg)
# you have to enter scores by using Commas in output 

SyntaxError: multiple statements found while compiling a single statement
>>> print("Computes the Avag")
print(" ")
score1,score2=eval(input("enter the values of Score 1 and Score 2"))
Avg=(score1+score2)/2
print("Avg is",Avg)
SyntaxError: multiple statements found while compiling a single statement
>>> score1,score2=eval(input("enter the values of Score 1 and Score 2"))
Avg=(score1+score2)/2
print("Avg is",Avg)
SyntaxError: multiple statements found while compiling a single statement
>>> score1,score2=eval(input("enter the values of Score 1 and Score 2"))
enter the values of Score 1 and Score 2123,345
>>> avg=((score1+score2)/2)
>>> print(avg)
234.0
>>> print("avg is : " avg)
SyntaxError: invalid syntax
>>> print("avg is : " ,avg)
avg is :  234.0
>>> class(avg)
SyntaxError: invalid syntax
>>> x=input("cide")
cide  343
>>> print(x
	  )
  343
>>> eval(cide)
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    eval(cide)
NameError: name 'cide' is not defined
>>> list_str"[3,4,5,5,5]"
SyntaxError: invalid syntax
>>> list_str="[3,4,5,5,5]"
>>> list_str=eval(list_str)
>>> print("Computes the Avag")
print(" ")
score1,score2=eval(input("enter the values of Score 1 and Score 2"))

SyntaxError: multiple statements found while compiling a single statement
>>> print("Computes the Avag")
Computes the Avag
>>> print("Computes the Avag")
print(" ")
Computes the Avag
SyntaxError: multiple statements found while compiling a single statement
>>> print(" ")

 
>>> score1,score2=eval(input("enter the values of Score 1 and Score 2"))

enter the values of Score 1 and Score 2123,46
>>> avg=(score1+score2)
>>> avg
169
>>> var1=10
>>> var2=55
>>> del var1
>>> var1
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    var1
NameError: name 'var1' is not defined
>>> print(var1)
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    print(var1)
NameError: name 'var1' is not defined
>>> str="hello word"
>>> print(Str)
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    print(Str)
NameError: name 'Str' is not defined
>>> print(str)
hello word
>>> print(str[0])
h
>>>     print (str [0])
SyntaxError: unexpected indent
>>> print (str [0])
h
>>> print (str [2:5])
llo
>>> print(str[0:4])
hell
>>> print(str[2:])
llo word
>>> print(str*2)
hello wordhello word
>>> print str*3
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(str*3)?
>>> print str*2
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(str*2)?
>>> print str + "TEST"
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(str + "TEST")?
>>> print str*2
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(str*2)?
>>> str1="hello"
>>> str2"mail"
SyntaxError: invalid syntax
>>> str2="mail"
>>> print(str1,str2)
hello mail
>>> str3="hello"
>>> str4="spam"
>>> print(str3,str4)
hello spam
>>> firstname=input("input your name")
input your name Subham
>>> print (firstname)
 Subham
>>> print("Hello" , firstname)
Hello  Subham
>>> cars = 100
 space_in_a_car = 4.0
 drivers = 30
 passengers = 90

SyntaxError: multiple statements found while compiling a single statement
>>> cars = 100
>>> space_in_a_car = 4.0
>>> drivers = 30
>>> passengers = 90
>>> carsnotdriven=cars-drivers
>>> carsdriven=drivers
>>> carpoolcap=carsdriven*space_in_a_car
>>> avgeragecar=passengers/carsdriven
>>> print("there are " ,cars,"available)
	  
SyntaxError: EOL while scanning string literal
>>> print("there are " ,cars,"available")
	  
there are  100 available
>>> print("there are only" , droven ,"drivers available")
	  
Traceback (most recent call last):
  File "<pyshell#76>", line 1, in <module>
    print("there are only" , droven ,"drivers available")
NameError: name 'droven' is not defined
>>> 
