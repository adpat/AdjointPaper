
PAPER	= restart.pdf
SRC = restart.lyx
UNOCONV	= unoconv -f pdf 
PFIGS = $(wildcard presfigs-gen/*.pdf)
FIGS = $(wildcard figs-gen/*.pdf)
TEX_FOLDER=tex
ZIPFILE=paper.tar.gz


all: $(PAPER)


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
	rm -rf *gz

auxclean: clean
	rm -f *fls
	rm -f *fdb_latexmk
	rm -f *aux
	rm -f *bbl
	rm -rf *blg
	rm -rf *synctex.gz
	rm -rf *blg

tex: figures presfigs
	/Applications/Lyx.app/Contents/MacOS/lyx --export pdflatex $(SRC) $(TEX_FOLDER)

zip: tex
	tar -zcvf $(ZIPFILE) ./


dumpzip: zip
	rsync $(putswitches) $(switches) $(ZIPFILE) $(remoteuser)@$(remotehost):$(remotedir)$(sd)/

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


syncfileLocal     = restart.pdf
remoteuser   = jreilly
remotehost   = kepler.berkeley.edu
remotedir    = ~/public_html/reports/
switches     = --checksum -rlvzu --exclude ".*" --exclude "*.tgz*" --exclude "Makefile.*"
putswitches  = --exclude "logs"
putmessage   = Updating server with newer files from local site mirror...
sd = $(patsubst %/,%,$(tdir))

put:
	@echo "$(putmessage)"
	rsync $(putswitches) $(switches) $(syncfileLocal) $(remoteuser)@$(remotehost):$(remotedir)$(sd)/
	@echo

.PHONY: put

checkpoint: figures presfigs git

git:
	git commit -a -m 'standard checkpoint'
	git push