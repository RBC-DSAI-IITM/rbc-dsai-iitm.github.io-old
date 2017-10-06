import glob

for filename in glob.glob('../_collaborators/Test*.yml'):

	f = open(filename)
	lines = f.readlines()
	f.close()

	lines.append(lines[-1])
	lines[len(lines)-2] = 'type: collaborator\n'

	with open(filename, 'w') as w:
		for line in lines:
			# print line
			w.write(line) 
