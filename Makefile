all: unexecutable pull executable

unexecutable: redirect.py
	chmod -x redirect.py

executable: redirect.py
	chmod +x redirect.py

pull:
	git pull
