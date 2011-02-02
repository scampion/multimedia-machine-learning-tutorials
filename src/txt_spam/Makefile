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
	sed -i 's#,# #g' spambase.data

html:
	-mkdir html
	latex2html -html_version 4.0,unicode -dir html tp_spam_naives_classifier.tex 

weka:
	cp spambase.data /tmp/data
	dos2unix /tmp/data	
	sed -i 's/1$/spam/g' /tmp/data 
	sed -i 's/0$/ham/g' /tmp/data
	tail -n 58 spambase.names  | sed 's/^/@ATTRIBUTE\ /g' | sed 's/continuous\./REAL/g'  > /tmp/attrs
	
	echo '@RELATION spambase' > spambase.attrs
	cat /tmp/attrs >> spambase.attrs
	echo '@DATA' >> spambase.attrs
	cat /tmp/data >> spambase.attrs

dummy: ;


