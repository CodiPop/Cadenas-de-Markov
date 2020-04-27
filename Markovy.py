
## Cada linea en el documento es una pagina del pdf source de donde se saco el txt.

a = input("K: ")
b = input("N: ")
file = open("gabo.txt", "r")
abc = file.read()
file.close
##Shows the entire txt as a String

##Creates a list of the words in the txt
Lw = abc.split()
print("********************************************************************************************************************************************")
##creates a list without duplicates
Lwnf = list(dict.fromkeys(Lw))
for i in Lw:
    print(i, end= " ")
