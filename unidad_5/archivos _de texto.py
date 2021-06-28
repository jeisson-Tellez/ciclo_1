
data = ["jose", "plablo", "Línea 3", "Línea 4", "Línea 5"]

fic = open("text_1.txt", "w")

for line in data:
    print(line, file=fic)
    print(line)
    
fic.close()
