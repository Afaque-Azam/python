import os

# directory_path = r"C:\Users\afaqu\OneDrive\Desktop\project"

directory_path = r"C:\Users\afaqu\Videos\movie"


contents = os.listdir(directory_path)
for item in contents:
    print(item)