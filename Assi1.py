
file_name =input("enter the name of file")
file = open(file_name,'r')

lines =0
words=0
characters =0

for line in file:
	wordcount =line.split()
	lines=lines +1
	words = words + len(wordcount)
	characters = characters +len(line)

print(lines);
print(words);
print(characters);