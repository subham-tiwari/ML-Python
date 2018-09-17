class Animal:   
    def eat(self):
        x=1
        y=2
        global z
        z=x+y
        print ("Eating...",z)
class Dog(Animal):  
   def bark(self):
           global a
           a=z
           print ('Barking...',+a ) 
class BabyDog(Dog):  
    def weep(self):  
        print('Weeping...')  
d=BabyDog()  
d.eat()  
d.bark()  
d.weep() 
