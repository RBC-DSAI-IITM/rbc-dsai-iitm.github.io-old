f = open('rawPeople2.txt')
lines = f.readlines()
f.close()

# print len(lines)
for i in range(len(lines)):
	i*=4
	print i
	# (name, designation) = tuple(lines[i].strip().split(','))
	data = lines[i].split(',')
	name, designation = data[0], lines[i][len(data[0])+1:].strip()
	email = lines[i+1].strip()
	bio = lines[i+2].strip()
	# areas = lines[i+3].strip()[20:]
	# root = email[:email.find('@')]
	# image = root + '.jpg'
	# filename = root + '.html'

	# with open(filename, 'w') as w:
	with open(str(i)+'.html', 'w') as w:
		w.write('---\n')
		w.write('layout : ' + 'default\n')
		w.write('name : ' + name + '\n')
		w.write('designation : ' + designation + '\n')
		w.write('email : ' + email + '\n')
		# w.write('areas : ' + areas + '\n')
		# w.write('image : ' + image + '\n')
		w.write('bio : ' + bio + '\n')
		w.write('---\n')

	# i+=5 