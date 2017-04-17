#!/bin/bash

# Change to the directory of pdf file
cd $(dirname "$1")
pdf=$(basename "$1")
pdf_data="${pdf%.*}""_data.txt"
bkFile="$2"

echo "Converting $bkFile to pdftk compatible format"
python3 booky.py < "$bkFile" > bookmarks-pdftk-compatible.txt

echo "Dumping pdf meta data..."
pdftk "$pdf" dump_data_utf8 output "$pdf_data"

echo "Clear dumped data of any previous bookmarks"
sed -i '/Bookmark/d' "$pdf_data"

echo "Inserting your bookmarks in the data"
sed -i '/NumberOfPages/r bookmarks-pdftk-compatible.txt' "$pdf_data"

echo "Creating new pdf with your bookmarks..."
pdftk "$pdf" update_info_utf8 "$pdf_data" output "${pdf%.*}""_new.pdf"

echo "Deleting leftovers"
rm bookmarks-pdftk-compatible.txt "$pdf_data"
