# This file is part of the Open Source project 'proTironeComputatri'
# (c) 2025 Karsten Reincke (https://github.com/pro-tirone-computatri/protico.ltx)
# It is distributed under the terms of the creative commons license
# CC-BY-4.0 (= https://creativecommons.org/licenses/by/4.0/)
#

BLD=../../built/lf.09
CCL=curriculum-check-list
TCL=topic-check-list

lessons: checklists 
	find . -maxdepth 1 -type d -name "sbj-*" | while read d; \
		do echo $$d; \
		( cd $$d; \
		  make lessons; \
			make clean; \
		) \
	done


clean:
	find . -maxdepth 1 -type d -name "sbj-*" | while read d; \
		do echo $$d; \
		( cd $$d; \
		  make clean; \
		) \
	done
	if [ -f ${CCL}.pdf ]; then rm ${CCL}.pdf; fi
	if [ -f ${TCL}.pdf ]; then rm ${TCL}.pdf; fi

checklists:  
	( cd sbj-00.curriculum && make ../${CCL}.pdf && make ../${TCL}.pdf)
	mkdir -p ${BLD}
	mv ${CCL}.pdf ${TCL}.pdf ${BLD}/
	cp ${CCL}.md ${TCL}.md ${BLD}/

	
