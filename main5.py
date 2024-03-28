# for loops in python

fruits =["apple" , "bnana" , "orange" , "grapes"]
for fruits in fruits:
    print(f"processing{fruits}")


#example 2: iterating over a range of nnumber
    print("\nexample2")


for i in range(1,6):
    print(f"square of {i}: {i**2}")

# example 3: iterating over a string
    print("\example3")
    word = "python"
    for sam in word:
        print(f"character:{sam}")    

name = "sam"
for i in name:
    print(i)
    if(i =="b"):
      print("this is something we have")        