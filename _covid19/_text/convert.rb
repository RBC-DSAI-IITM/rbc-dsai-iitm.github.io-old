require 'bibtex' 

BibTeX::Parser::Log = BibTeX.log
print BibTeX.open('ilds.bib').to_json
