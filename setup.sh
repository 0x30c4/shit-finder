#!/bin/bash

if [ ! -f "shit_finder.py" ]; then
    wget https://raw.githubusercontent.com/0x30c4/shit-finder/master/shit_finder.py
fi

chmod +x shit_finder.py

mv shit_finder.py shit_finder

cp shit_finder ~/.local/bin

echo 
echo "------------------------------Shit-Finder-------------------------------"
echo   Shit-Finder is installed successfully!!!!
<<<<<<< HEAD
printf "To use shit_finder type 'shit_finder --help'\n\n"
=======
printf "To use shit-finder restart your terminal and then type 'findshit --help'\n\n"
>>>>>>> e212361d79d85d7850483d26d4aba3ecb583658a
