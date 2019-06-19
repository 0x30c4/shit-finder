#!/bin/bash
mkdir .Shit-finder
cp shit_finder.py ~/.Shit-finder
echo alias findshit=\"python3 ~/.Shit-finder/shit_finder.py\" >> ~/.bashrc

echo 
echo "------------------------------Shit-Finder-------------------------------"
echo   Shit-Finder is installed successfully!!!!
printf "To use shit-finder restart your terminal and then type 'findshit --help'\n\n"
