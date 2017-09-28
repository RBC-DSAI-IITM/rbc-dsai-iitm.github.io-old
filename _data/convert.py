import bibtexparser

with open('ilds.bib') as bibtex_file:
    bibtex_str = bibtex_file.read()

    bib_database = bibtexparser.loads(bibtex_str)
    #print(bib_database.entries)

    bib_ascii = [[(key.encode('ascii', 'ignore'), val.encode('ascii', 'ignore')) for (key, val) in entry] for entry in bib_database.entries ]

    print '\n\n'.join(str(entry) for entry in bib_ascii) 

