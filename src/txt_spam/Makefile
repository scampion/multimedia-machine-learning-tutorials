all:  dataset

clean:
	-rm *.aux *.log *.*~ *~ *.pdf \#* 
	-rm spam_naives_classifier.tex Makefile.tex hgid.tex
	-rm -Rf html
	-rm -Rf spambase.data  spambase.DOCUMENTATION  spambase.names

dataset:
	wget http://archive.ics.uci.edu/ml/machine-learning-databases/spambase/spambase.zip
	unzip spambase.zip 
	rm spambase.zip
	#replace comma , by a whitespace 
	sed -i -e 's#,# #g' spambase.data

html:
	-mkdir html
	latex2html -html_version 4.0,unicode -dir html tp_spam_naives_classifier.tex 

dummy: ;


