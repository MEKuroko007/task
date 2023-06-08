Automate push task of alx from terminal to github

first you need to clone your repo by using token and config name and email\n
	git clone https://{Token}@github.com/<username>/<repo.git>\n
	git config --global user.name "<name>"\n
	git config --global user.email "<email>"

before use this script make sure the python3 package installed on your terminal
	python3 -v

if not type this command :
	sudo apt install python3

after that use alias to be easy use :
	alias task='python3 task.py'

happy hacking :)
