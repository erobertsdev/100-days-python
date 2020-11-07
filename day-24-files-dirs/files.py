# file = open("my_file.txt")
# modes - r = read only, w = write, a = append
with open("my_file.txt", mode="r") as file: # as can be named anything
    contents = file.read()
    print(contents)
# file.close() # not needed when opened with "with"
with open("new_file.txt", mode="w") as file:
    file.write("\nNew text.")

