#def greet(name):
 #   print("hello" + name+ " Good morning")


#CALLING BY 2 ARGUMENTS

#def greet(name , age) :
 #    print("Hi"+name+" and my age is  "+age)

 #DEFAULT ARGUMENTS
 
#def greet(name , age="23") :
 #   print("Hi",name+" and my age is  "+age)


#PYTHON KEYWORD ARGUMENTS

#def greet(name="subham" , age="23") :
 #   print("Hi",name+" and my age is  "+age)

#ERROR
#def greet("subham",age="23") :
 #   print("Hi",name+" and my age is  "+age)


#PYTHON PASSING MORE ARGUMENT IN A SINGLE FUNCTION WITH HELP OF *

#def greet(*names):

     #for name in names :
#the number of arguments you pass
      #   print("Hello" ,name)
         
#PASS BY VLAUE AND REFERENCE
#dictonary
employee={"subham":23 , "ashwin":20 , "bal":45 ,"neeraja":40}

def test(employee):
    employee={"bitti":8 ,"baba":7}
    print("inside " ,employee)
    return

test(employee)
print("outside",employee)
