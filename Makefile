SHELL := /bin/bash

start:
	python3 ~/pendulo/app.py 2>&1 | tee ~/pendulo/logs/app.log
	python3 ~/pendulo/logs.py

# Update git
git-update:
	git fetch
	git reset --hard origin/master

# Setup
install:
	make install-packages
	make install-reboot-script

install-packages:
	sudo apt update
	sudo apt install python3 idle3
	sudo apt install python3-pip
	sudo apt-get install python3-serial
	sudo apt-get install python-serial
	sudo pip3 install flask
	sudo pip3 install pyserial

install-reboot-script:
	sudo cp -rf start_web_app.sh /etc/init.d/
	sudo chmod +x /etc/init.d/start_web_app.sh
	sudo update-rc.d start_web_app.sh defaults
	crontab -l > file; echo "@reboot ~/pendulo/start_web_app.sh" >> file; crontab file; rm file
