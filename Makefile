# Makefile for the kdd paper
# Most of the elements are shamelessly copied from the wikipedia page
# http://en.wikipedia.org/wiki/Make_%28software%29
# To generate the figures, you have to start openoffice or libreoffice with the command:
# ooffice "-accept=socket,host=localhost,port=2002,tcpNoDelay=1;urp;"


PAPER	= adjointPaper.pdf
# All the tex files
TEX	= $(wildcard *.tex)
UNOCONV	= unoconv -f pdf 


all: $(PAPER)

$(PAPER): $(TEX) figures plots
	pdflatex article.tex ;\
	bibtex article
	pdflatex article.tex ;\
	pdflatex article.tex ;\
	mv article.pdf $(PAPER)

clean:
	rm -f *~
	rm -f *pdf
	rm -f *log	

figures: 

plots: 

figs-gen/%.pdf: figures/%.odg
	echo "Making figure" $* ;\
	${UNOCONV} figures/$*.odg; \
	mv figures/$*.pdf figs-gen/$*.pdf

figs-plots/%.pdf: figs-plots-tmp/%.pdf
	cp figs-plots-tmp/$*.pdf figs-plots/$*.pdf

# works on mac
open:
	open $(PAPER)

allmac: all open
