#script for computing Lavenstein distance using dot-bracket file
def levenshtein(chars):
	d=[]
	cost=0
	for i in range(len(chars[0])):
		x=[]
		x.append(i)
		d.append(x)
	for j in range(1,len(chars[1])):
		d[0].append(j)

	for i in range(1,len(chars[0])):
		for j in range(1, len(chars[1])):
			if chars[0][i] == chars[1][j]:
				cost=0
			else:
				cost=1
			x= min(d[i-1][j]+1, d[i][j-1]+1, d[i-1][j-1]+cost)
			d[i].append(x)
	return d[len(chars[0])-1][len(chars[1])-1]


bases=[]
chars=[]
f= open("dot-brackets//RNAfold2.dbn","r")
bases.append(f.readline())
chars.append(f.readline())
f.close()

f= open("dot-brackets//FoldRNAs2.dbn","r")
bases.append(f.readline())
chars.append(f.readline())
f.close()


print(bases[0])
print(chars[0])
print()

print(bases[1])
print(chars[1])
print()

distance=levenshtein(chars)
print("Lavenshtein distance: {}".format(distance))

