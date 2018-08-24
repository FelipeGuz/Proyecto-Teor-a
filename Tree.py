negacion = "~"
conectoresB = ["Y", "O", "->", "<->"]
#Class
class Tree(object):
	def __init__(self, Label, Left, Right):
		self.Label = Label
		self.Left = Left
		self.Right = Right
	def getLabel(self):
		return self.Label
	def getRight(self):
		return self.Right
	def getLeft(self):
		return self.Left
	def toString(self):
		if (self.Right != None and self.Left != None):
			return self.Left.toString()+self.Label+self.Right.toString()
		elif (self.Right != None and self.Left == None):
			return self.Label+self.Right.toString()
		elif (self.Right == None and self.Left == None):
			return self.Label
#set of Atoms
def Atoms(arb):
	if (arb.Label == negacion):
		return Atoms(arb.Right)
	elif (arb.Label in conectoresB):
		return Atoms(arb.Left)|Atoms(arb.Right)
	else:
		return {arb.Label}
#Interpretations
letrasProposicionales = ["p", "q", "r"]
interps = []
aux = {}
for a in letrasProposicionales:
	aux[a] = 1
interps.append(aux)
for a in letrasProposicionales:
	interps_aux = [i for i in interps] 
	for i in interps_aux:
		aux1 = {} 
		for b in letrasProposicionales:
			if a == b:
				aux1[b] = 1 - i[b]
			else:
				aux1[b] = i[b]
		interps.append(aux1)
#Trees
P = Tree("p", None, None)
R = Tree("r", None, None)
Q = Tree("q", None, None)
A1 = Tree("Y", Tree("p", None, None), Tree("O", Tree("q", None, None), Tree("r", None, None)))
A2 = Tree("O", Tree("Y", P, Q), Tree("Y", P, R))
D1 = Tree("->", P, Q)
D2 = Tree("O", Tree("~", None, P), Q)
arb = Tree("Y", Q, R)
print arb.toString()

