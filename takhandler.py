import os
import datetime as dt

pd = dt.date.today()
print(pd)

#initializing the folder
parent_dir = os.path.dirname(os.path.realpath(__file__))
new_dir = "taskfolder"

try:
    fulldir = os.mkdir(f"{parent_dir}/{new_dir}")
except OSError :
    print("already exists")




todo = []
ask = input('would you like to add task YES/NO:') 

#asking various inputs 
while ask.upper() == "YES":
        addedtask = input('what are your goals(to cancel say NO )--')
        if addedtask.lower() == "no":
            break
        else:
            description =input('please add some info for task(leave empty for none) -- ')
            if description.lower()=="no":
                break
            else:
                todo.append(f"{addedtask}\n\n about:{description}") 
                           

else: 
    print("opaii!")



file = open(f"{parent_dir}/{new_dir}/{pd}.txt","w")


for x in todo :
    print(f" ->{x}")
    file.write(f" ->{x}")

else:
    print("those were daily tasks\n\n")


# here i am playing with list stuff
print(f"\n\n\ntotal tasks are {len(todo)}\n\n\n")

