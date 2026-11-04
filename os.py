import os


print("Current Directory:", os.getcwd())


os.chdir(r"C:\Users\PACE COMPUTERS\PycharmProjects\PythonProject3")
print("New Directory:", os.getcwd())


print("\nDirectory Contents:")
print(os.listdir())


if not os.path.exists("PythonPractice"):
    os.mkdir("PythonPractice")
    print("\nDirectory Created Successfully!")


os.makedirs("Project/Data/2026", exist_ok=True)
print("Nested Directories Created!")


print("\nPath Exists:", os.path.exists("PythonPractice"))


print("Is File:", os.path.isfile("main.py"))

print("Is Directory:", os.path.isdir("PythonPractice"))


path = os.path.join("Project", "Data", "2026")
print("\nJoined Path:", path)

print("Base Name:", os.path.basename(path))


print("\nUsername:", os.getenv("USERNAME"))



if os.path.isfile("test.txt"):
    os.remove("test.txt")
    print("\nFile Deleted!")

# 16. Remove an Empty Directory
if os.path.isdir("EmptyFolder") and not os.listdir("EmptyFolder"):
    os.rmdir("EmptyFolder")
    print("Empty Directory Deleted!")