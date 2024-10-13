#!/bin/bash
# author: jerryhzy

function SearchFolder(){
	# DirectoryName = $1, FileExtensionName = $2
	sed "s|^$HOME|~|" $1

}

if [$1 = "--interactive"]
then
	echo "Please input file extension (q to quit):"
elif [$1 = "--extension"]
then
	FileExtensionName = $2
	if [$3 = "--directory"]
	then
		DirectoryName = $4
		SearchFolder ${DirectoryName} ${FileExtensionName}
	else
		echo "Invalid arguments. Please check your input."
		exit 0
	fi
elif [$1 = "--directory"]
then
	DirectoryName = $2
	if [$3 = "--extension"]
	then
		FileExtensionName = $4
		SearchFolder ${DirectoryName} ${FileExtensionName}
	else
		echo "Invalid arguments. Please check your input."
		exit 0
	fi

elif [$1 = "--help"]
then
	echo "
		Usage: search_file.sh [OPTION]... [FOLDER]...\n
		List all files in the given folder.
	"
else
	echo "Invalid arguments. Please check your input."
fi