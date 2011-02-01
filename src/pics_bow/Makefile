HGID:=$(shell hg tip --template "\\def\\HgNode\{{node|short}}\n\\def\\HgDate\{{date|shortdate}}\n\\def\\HgAuthor\{{author|person}}\n" )

all: hgid.tex noresults results pics_bow.tex 

limited: hgid.tex noresults pics_bow.tex 

noresults:
	pygmentize -f latex Makefile     > Makefile.tex	
	echo '' > assign.tex 
	echo '' > classif.tex 	
	echo '' > kmeans.tex 
	echo '' > surfs.tex 

results:
	pygmentize -f latex assign.py  > assign.tex
	pygmentize -f latex classif.py > classif.tex
	pygmentize -f latex kmeans.py  > kmeans.tex 
	pygmentize -f latex surfs.py   > surfs.tex


hgid.tex: dummy
	[ -f $@ ] || touch $@
	hg tip --template "\\def\\HgNode\{{node|short}}\n\\def\\HgDate\{{date|shortdate}}\n\\def\\HgAuthor\{{author|person}}\n\\def\\HgBranch\{{branches|nonempty}}\n\\def\\HgRev\{{rev}}\n"  >  $@

pics_bow.tex: dummy 
	pdflatex $@
	pdflatex $@ 

clean:
	-rm -f *.aux *.log *~ *.*~ *.pdf *.avi iter*.jpg *.pyc \#* 
	-rm -f Makefile.tex hgid.tex assign.tex classif.tex kmeans.tex surfs.tex
	

clean_data:
	-rm -f centroids moto plane moto_qv plane_qv moto_qv_tests plane_qv_tests

dataset:
	wget http://people.csail.mit.edu/torralba/code/spatialenvelope/spatial_envelope_256x256_static_8outdoorcategories.zip
	unzip spatial_envelope_256x256_static_8outdoorcategories.zip
	rm spatial_envelope_256x256_static_8outdoorcategories.zip
	python gists.py

dummy: ;


