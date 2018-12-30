import os

filename = os.path.join(os.path.dirname(__file__), "umlaute.txt")

with open(filename, "r", encoding= "utf-8") as file:
    for line in file:
        print(line)

filename = os.path.join(os.path.dirname(__file__), "umlaute_out.txt")
with open(filename, "w", encoding= "utf-8") as file:
    file.write("Über")
