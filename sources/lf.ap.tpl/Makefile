# This file is part of the Open Source project 'proTirone'
# (c) 2025 Karsten Reincke (https://github.com/protirone/protico.ltx)
# It is distributed under the terms of the creative commons license
# CC-BY-4.0 (= https://creativecommons.org/licenses/by/4.0/)
#


lessons:
	find . -maxdepth 1 -type d -name "ap2*" | while read d; \
		do echo $$d; \
		( cd $$d; \
		  make lessons; \
			make clean; \
		) \
	done

clean:
	find . -maxdepth 1 -type d -name "ap2*" | while read d; \
		do echo $$d; \
		( cd $$d; \
		  make clean; \
		) \
	done


