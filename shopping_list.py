shopping_list = []

print("What do you want to pick up at the store?")
print("Type 'DONE' to see your list.")

while True:
    newitem = input("> ")
    
    if newitem == "DONE":
        break
        
    shopping_list.append(newitem)
    print("Added! List has {} items".format(len(shopping_list)))
    continue
    
print("Here's your list:")    

for item in shopping_list:
    print(item)
        
        
    