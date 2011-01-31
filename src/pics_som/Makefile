all: hgid.tex python2latex pic_som.tex 

python2latex:
	pygmentize -f latex color_map.py > color_map.tex
	pygmentize -f latex gist_map.py  > gist_map.tex
	pygmentize -f latex gists.py     > gists.tex
	pygmentize -f latex kohonen.py   > kohonen.tex
	pygmentize -f latex Makefile     > Makefile.tex	

hgid.tex: dummy
	[ -f $@ ] || touch $@
	hg tip --template "\\def\\HgNode\{{node|short}}\n\\def\\HgDate\{{date|shortdate}}\n\\def\\HgAuthor\{{author|person}}\n\\def\\HgBranch\{{branches|nonempty}}\n\\def\\HgRev\{{rev}}\n"  >  $@

pic_som.tex: dummy 
	pdflatex $@
	pdflatex $@ 

clean:
	-rm -f *.aux *.log *~ *.*~ *.pdf *.avi iter*.jpg *.pyc
	-rm -f color_map.tex gist_map.tex gists.tex kohonen.tex hgid.tex

movie: 
	ffmpeg -r 25 -b 1000 -i iter_%08d.jpg -y movie.avi 

dataset:
	wget http://people.csail.mit.edu/torralba/code/spatialenvelope/spatial_envelope_256x256_static_8outdoorcategories.zip
	unzip spatial_envelope_256x256_static_8outdoorcategories.zip
	rm spatial_envelope_256x256_static_8outdoorcategories.zip
	python gists.py

dummy: ;


