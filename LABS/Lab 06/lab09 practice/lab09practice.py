class petStore:
   def __init__(self):
    self.pets= {
         "dogs":[],
         "cats":[],
         "rabbits":[],
         "parrots":[]
         }
   def storePet(self,type,breedname,price,age):
        temp = {
        "breedname":breedname,
        "price": price,
        "age":age,
        }
        self.pets[type].append(temp)

pets = petStore()  # to call class we need to define object 
print(pets.pets) #  for printing class call the object . name of the class 
pets.storePet('dogs','abc',12000,3)
pets.storePet('cats','ijk',8000,2)
print(pets.pets)
for pet in pets.pets:
  # print(pet)
  # print(pets.pets[pet])
   for item in pets.pets[pet]:
       #print(item)
       print(item['breedname'])



