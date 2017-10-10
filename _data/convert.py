import bibtexparser

with open('publications.bib') as bibtex_file:
    bibtex_str = bibtex_file.read()

    bib_database = bibtexparser.loads(bibtex_str)
    # print (bib_database.entries[0])

    # print [key for key, value in bib_database.entries[0].items()]

    bib_ascii = [dict([(key.encode('ascii', 'ignore'), val.encode('ascii', 'ignore')) for (key, val) in entry.items()]) for entry in bib_database.entries ]
    print '[\n'
    print ',\n\n'.join(str(entry) for entry in bib_ascii) 
    print '\n]'
