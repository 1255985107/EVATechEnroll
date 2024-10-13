#!/bin/bash
# author: jerryhzy

search() {
    local directory=$1
    local extension=$2
    local count=0

    while IFS= read -r -d '' file; do # find folders
        echo "${file/#$HOME/\~}"
        let "count++"
    done < <(find "$directory" -type f -name "*.$extension" -print0)
    echo "Total $count files."
}

show_help() {
    cat << EOF
USAGE: search_file.sh [OPTIONS]
search_file.sh is a script to search files in a particular directory.
OPTIONS:
    --extension EXT    Specify the file extension to search for.
    --directory DIR    Specify the directory to search in.
    --interactive      Run in interactive mode.
    --help             Display this help and exit.
EOF
}

while [[ "$#" -gt 0 ]]; do
    case $1 in
        --extension) extension=$2; shift;;
        --directory) directory=$2; shift;;
        --interactive) interactive=1;;
        --help) show_help; exit;;
        *) echo "Unknown option: $1"; show_help; exit 1;;
    esac
    shift
done
if [[ -n $interactive ]]; then # interactive
    while true; do
        read -p "Please input file extension (q to quit): " extension
        if [[ "$extension" == "q" ]]; then
            break
        fi
        read -p "Please input directory to search (q to quit): " directory
        if [[ "$directory" == "q" ]]; then
            break
        fi
        search "$directory" "$extension"
    done
else # not interactive
    if [[ -z "$extension" || -z "$directory" ]]; then
        echo "Error: Both --extension and --directory must be specified."
        show_help
        exit 1
    fi
    search "$directory" "$extension"
fi