import os
found = False
difficulty = "Easy"
name_song = "Pekorap Tropica"





#finding first folder of file
#os.listdir("") - listing files & directory in directory
for filename in os.listdir(r"C:\Users\Kosi\AppData\Local\osu!\Songs"):
    if name_song in filename:
        found = True
        print(filename)
        break
if found:
    print("YES")
else:
    print("No")



#combination of files
first_path = r"C:\Users\Kosi\AppData\Local\osu!\Songs"
secound_path = os.path.join(first_path, filename)


#difficulty finding
for filename2 in os.listdir(secound_path):
    if difficulty in filename2:
        print(filename2)


#extracting file data



