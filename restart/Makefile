# Makefile for the kdd paper
# Most of the elements are shamelessly copied from the wikipedia page
# http://en.wikipedia.org/wiki/Make_%28software%29
# To generate the figures, you have to start openoffice or libreoffice with the command:
# ooffice "-accept=socket,host=localhost,port=2002,tcpNoDelay=1;urp;"


PAPER	= restart.pdf
SRC = restart.lyx
UNOCONV	= unoconv -f pdf 
PFIGS = $(wildcard presfigs-gen/*.pdf)
FIGS = $(wildcard figs-gen/*.pdf)


all: $(PAPER) open


lyx:
	/Applications/Lyx.app/Contents/MacOS/lyx --export pdf $(SRC)

restart.lyx: lyx

$(PAPER): figures presfigs $(SRC) 

clean:
	rm -f *~
	rm -f *pdf
	rm -f *log
	rm -f *aux
	rm -f *bbl
	rm -f *blg
	rm -f *tex

auxclean: clean
	rm -f *fls
	rm -f *fdb_latexmk
	rm -f *aux
	rm -f *bbl
	rm -rf *blg
	rm -rf *synctex.gz
	rm -rf *blg

figures: $(FIGS)


figs-gen/%.pdf: figures/%.odg
	echo "Making figure" $* ;\
	${UNOCONV} figures/$*.odg; \
	mv figures/$*.pdf figs-gen/$*.pdf

presfigs: $(PFIGS)


presfigs-gen/%.pdf: presfigs/%.odg
	echo "Making figure" $* ;\
	${UNOCONV} presfigs/$*.odg; \
	mv presfigs/$*.pdf presfigs-gen/$*.pdf

# works on mac
open:
	open $(PAPER)
	