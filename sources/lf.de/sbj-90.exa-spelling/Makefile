# This file is part of the Open Source project 'proTirone'
# (c) 2025 Karsten Reincke (https://github.com/protirone/protico.ltx)
# It is distributed under the terms of the creative commons license
# CC-BY-4.0 (= https://creativecommons.org/licenses/by/4.0/)

AUX_EXTS=tmp
RES_EXTS=pdf
DEL_FILE=exercises

LNX_TD=../..
PTC_TD=../${LNX_TD}
BLD=${PTC_TD}/built
MDHTMP=mdh.tmp

EXACORE=dict
EXADICTA=${EXACORE}-antiqua.pdf
EXADICTD=${EXACORE}-suetterlin
EXADICTS=${EXADICTD}.pdf

EVD="../../3ps/eisvogel"

help:
	echo "make [ help | lessons | lesson-exc | exercises | lesson-ort | oraltrack | lesson-zpr | zenprese ] "

# recreates all sbj documents and releases them into the lesson directory tree
lessons: lesson-exa 

# --- SECTION EXAMEN  ---
# recreates oraltrack document, releases it into the lesson directory tree
lesson-exa: bld exa
	@ WD=`pwd` && SJN=`basename $${WD}` && LFN=`cat ../td.lf` && \
	  TGD="${BLD}/$${LFN}" && mkdir -p $${TGD} && \
        mv ${EXADICTA} $${TGD}/$${SJN}-${EXADICTA} && \
        mv ${EXADICTS} $${TGD}/$${SJN}-${EXADICTS}
	@ tree ${BLD}

exa:
	make ${EXADICTA}
	( cd ${EXADICTD} && make  ${EXADICTS} && mv ${EXADICTS} ../ )

bld:
	mkdir -p ${BLD}


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
	$(foreach EXT, ${RES_EXTS}, @if [ ! "x`ls *.${EXT} 2>/dev/null`" = "x" ]; then rm *.${EXT}; echo "removing existing .${EXT}-target-files"; fi;)
	$(foreach BNA, ${DEL_FILE}, @if [ ! "x`ls ${BNA}.* 2>/dev/null`" = "x" ]; then rm ${BNA}.*; echo "removing existing derivated ${BNA}.*"; fi;)

