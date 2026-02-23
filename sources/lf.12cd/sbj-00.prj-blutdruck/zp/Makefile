# This file is part of the Open Source project 'proTironeComputatri'
# (c) 2025 Karsten Reincke (https://github.com/pro-tirone-computatri/protico.ltx)
# It is distributed under the terms of the creative commons license
# CC-BY-4.0 (= https://creativecommons.org/licenses/by/4.0/)

AUX_EXTS=url bbl blg aux dvi toc log lof nlo nls ilg ils ent out log bcf xml nav snm vrb json tmp
RES_EXTS=ps pdf 

TFL=texfiles.tmp

help:
	echo "make | make YOURFILE.pdf"

texFiles:
	@ if [ -f ${TFL} ]; then rm ${TFL}; fi
	@ ls *.tex | grep -v inc-image-list.tex | while read f; do echo $$f; echo $$f >> ${TFL}; done

.SUFFIXES: .tex .pdf

.tex.pdf:
	@ echo "### `date +'%Y%m%dT%H%M%S'`"
	@ echo "### (1) collecting relevant tex files"
	@ make texFiles
	@ echo "### (2) computing the image reference"
	@ bash ../../../bin/collect-img-meta-data.sh `cat ../../td.lf`
	@ python3 ../../../bin/write-img-meta-data-list.py > inc-image-list.tex
	@ echo "### (2) converting $< to $@"
	@ pdflatex -shell-escape $<
	@ biber `basename $< .tex`
	@ pdflatex -shell-escape $<
	@ pdflatex -shell-escape $<
	@ make clear

clear:
	$(foreach EXT, ${AUX_EXTS}, if [ ! "x`ls *.${EXT} 2>/dev/null`" = "x" ]; then rm *.${EXT}; fi;)

clean:	clear
	$(foreach EXT, ${RES_EXTS}, if [ ! "x`ls *.${EXT} 2>/dev/null`" = "x" ]; then rm *.${EXT}; fi;)
	@ if [ -f ./inc-image-list.tex ]; then rm ./inc-image-list.tex; fi 
	

