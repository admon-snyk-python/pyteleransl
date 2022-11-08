#!/bin/bash
meis="$(whoami)"

if [ "$meis" = "root" ]; then

	apt-get update
	apt-get install git python3 python3-pip pytesseract-ocr -y
	pip3 install -r requirements.txt

else
	echo "I need root persmissions! try 'sudo !!'"

fi

