all:
	if [ -f .BACKEND_PID ]; then \
		make kill;\
		echo bye;\
	else \
		make run;\
		echo hi;\
	fi

run:
	python main.py & echo $$! > .BACKEND_PID
	echo PID of server process: `cat .BACKEND_PID`

kill:
	echo PID of server process: `cat .BACKEND_PID`
	kill `cat .BACKEND_PID`
	rm .BACKEND_PID