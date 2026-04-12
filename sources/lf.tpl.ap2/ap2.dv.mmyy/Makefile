# This file is part of the Open Source project 'proTirone'
# (c) 2025 Karsten Reincke (https://github.com/protirone/protico.ltx)
# It is distributed under the terms of the creative commons license
# CC-BY-4.0 (= https://creativecommons.org/licenses/by/4.0/)

AUX_EXTS=tmp
RES_EXTS=pdf
DEL_FILE=exercises

LNX_TD="../.."
PTC_TD="../${LNX_TD}"
BLD=${PTC_TD}/built
MDHTMP=mdh.tmp


EVD="../../3ps/eisvogel"

help:
	echo "make [ help | lesson | lesson-ort | oraltrack ] "

lessons: lesson

lesson: lesson-ort

# recreates oraltrack document, releases it into the lesson directory tree
lesson-ort: oraltrack
	@ WD=`pwd` && SJN=`basename $${WD}` && LFN=`cat ../td.lf` && \
	  TGD="${BLD}/$${LFN}" && mkdir -p $${TGD} && \
    mv oraltrack.pdf $${TGD}/$${SJN}-solutions.pdf	
	@ tree ${BLD}

ort: oraltrack

oraltrack:
	make oraltrack.pdf

.SUFFIXES: .md .pdf 

.md.pdf:
	@ echo "### `date +'%Y%m%dT%H%M%S'`"
	@ echo "### converting $< to $@"
	@ MYD=`date +'%Y-%m-%d'` && cat header.md | sed "s/PTCDATE/$${MYD}/" >${MDHTMP} 
	@ pandoc ${MDHTMP} $< -o $@ --from markdown --template ${EVD}/eisvogel.latex --listings -V lang=de-DE
	@ make clear

clear:
	$(foreach EXT, ${AUX_EXTS}, if [ ! "x`ls *.${EXT} 2>/dev/null`" = "x" ]; then rm *.${EXT}; fi;)

clean:	clear
	find . -name "*.pdf" ! -name "*solution.*" | while read f; do rm $$f; done

