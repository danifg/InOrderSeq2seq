import sys

def tree(acts,words,pos):
	btree = []
	openidx = []
	wid = 0

	previous_act = 'N'

	size_tree = 0
	max_size_tree = len(words)

	for act in acts:
		if act[0] == 'S':
			if len(words) != 0:
				btree.append("("+pos[0]+" "+words[0]+")")
				del words[0]
				del pos[0]
				wid += 1
			previous_act = 'S'
			size_tree += 1

		elif act[0] == 'N':
			btree.insert(-1,"("+act[1:])
			openidx.append(len(btree)-2)
			previous_act = 'N'
		else:#REDUCE

			if len(openidx)>0:
				tmp = " ".join(btree[openidx[-1]:])+")"
				btree = btree[:openidx[-1]]
				btree.append(tmp)
				openidx = openidx[:-1]
			previous_act = 'R'


	if len(openidx)>0:
		tope = len(openidx)
		for i in range(tope):
			tmp = " ".join(btree[openidx[-1]:])+")"
			btree = btree[:openidx[-1]]
			btree.append(tmp)
			openidx = openidx[:-1]

	if len(btree)>1:
		print '(S',
		for i in range(len(btree)):
				print btree[i], 
		print ')'	
	else:
		print btree[0]




if __name__ == "__main__":
	allpos = []
	pos = []
	for line in open(sys.argv[3]):
		line=line.strip()
		if line != 	"":
			ws = line.split(" ")
			for i in range(len(ws)):
				pos.append(ws[i])
			allpos.append(pos)
			pos = []

	text = []
	words = []
	for line in open(sys.argv[2]):
		line=line.strip()
		if line != 	"":
			ws = line.split(" ")
			for i in range(len(ws)):
				words.append(ws[i])
			text.append(words)
			words = []
	allactions = []
	actions = []
	
	sent = 0
	for line in open(sys.argv[1]):
		line=line.strip()
		if line != "":
			trans = line.split(" ")
			num_shift = 0
			num_nt = 0
			num_reduce = 0
			for i in range(len(trans)):
				actions.append(trans[i])
				if trans[i][0] == 'S': num_shift=num_shift+1
				if trans[i][0] == 'N': num_nt=num_nt+1
				if trans[i][0] == 'R': num_reduce=num_reduce+1

			if len(text[sent])>num_shift:
				faltan = len(text[sent])-num_shift
				actions.append("NTS")				
				for i in range(faltan):
					actions.append("S")
					
				actions.append("RS")
		
		
			allactions.append(actions)
			actions=[]
			sent = sent + 1
		else:
			if sent < len(text):
				actions.append("S")
				actions.append("NS")
				for i in range(len(text[sent]-1)):
					actions.append("S")
				
				actions.append("RS")
				allactions.append(actions)
				actions=[]
				sent = sent + 1
		

	for i in range(len(text)):
		tree(allactions[i], text[i], allpos[i]);
		
		
