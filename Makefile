all: pull executable

executable: redirect.py
	chmod +x redirect.py

pull:
	git pull