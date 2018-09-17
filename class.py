#class name :
  #  def main():
 #       x=input("enter the name")
#        print(x)



        #multi level inhertence
class base():
    def main1(self):
        x=1
        y=2
        z=x+y
        print(z)
class child1(base):
    def main2(self):
        a=z+x
        print(a)
class child2(child1):
    def main3(self):
        b=a+z+x
        print(b)



d=child2()
d.main1()
d.main2()
d.main3()

