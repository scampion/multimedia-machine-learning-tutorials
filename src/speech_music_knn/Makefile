
all: hgid.tex python2latex tp_speech_music.tex 

python2latex:
	@echo Pygmentize latex 
	pygmentize -f latex grab.sh > grab.tex
	pygmentize -f latex query.sh > query.tex
	pygmentize -f latex speech_music.py > tp.tex


hgid.tex: dummy
	[ -f $@ ] || touch $@
	hg tip --template "\\def\\HgNode\{{node|short}}\n\\def\\HgDate\{{date|shortdate}}\n\\def\\HgAuthor\{{author|person}}\n\\def\\HgBranch\{{branches|nonempty}}\n\\def\\HgRev\{{rev}}\n"  >  $@

tp_speech_music.tex: dummy 
	pdflatex $@
	pdflatex $@ 

clean:
	-rm *.aux *.log *.*~ *.pdf 
	-rm grab.tex hgid.tex query.tex tp.tex

dummy: ;


