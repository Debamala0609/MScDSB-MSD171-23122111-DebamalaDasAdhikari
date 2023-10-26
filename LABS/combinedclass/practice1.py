# create a petstore class where youn have the details of pets available and their details 
#the clas will  have methods 
#store a new pet details 
#search for pet 
#sell a pet 
#LIST all pets 
# importing your petstore class,create a petstormain file,where you will implement a menue driven program from admin - who will manage the store & user will see the pets and buy pets 


class petStore:
    def __init__(self,Name,Age,Gender):
        self.Name= Name
        self.Age= Age
        self.Gender=Gender
    def printpetStore(self):
        print(self.Name,self.Age,self.Gender)
    pet = {
       { "pet1":" German Spheard",
        "age" : 2,
        "gender":"female"
       },
       {
           "pet2":"Golden Retriver",
           "age":3 ,
           "gender":"male"
       },
       {
           "pet3":"Corgi",
           "age":3,
           "gender":"male"
       }
      } 
pets=[]
def add_pet():
    Name =input("Enter a new breed")
    Age = input ("enter the age ")
    Gender=input("enter the age ")
    pet= petStore(Name,Age,Gender)
    pets.append(pet)
    print("updated sucessfully")
    
def searchName(pets):
 for Name in pets:
    print(Name)

