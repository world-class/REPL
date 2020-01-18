#!/bin/bash

## Script to compress PDF Files using ghostscript incl. subdirs
## Copyright (C) 2016 Maximilian Fries - All Rights Reserved
## Contact: maxfries@t-online.de
## Last revised 2016-07-29

# Usage
# ./pdf-compress.sh [screen|ebook|prepress|default] [verbose]

# Variables and preparation
{
count=0
success=0
successlog=./success.tmp
gain=0
gainlog=./gain.tmp
pdfs=$(find ../../ -type f -name "*.pdf")
total=$(echo "$pdfs" | wc -l)
log=./log
verbose="-dQUIET"
mode="prepress"
echo "0" | tee $successlog $gainlog > /dev/null
}

# Are there any PDFs?
if [ "$total" -gt 0 ]; then

#Parameter Handling & Logging
{
  echo "-- Debugging for Log START --"
  echo "Number of Parameters: $#"
  echo "Parameters are: $*"
  echo "-- Debugging for Log END   --"
} >> $log

# Only compression-mode set
if [ $# -eq 1 ]; then
  mode="$1"
fi

# Also Verbose Level Set
if [ $# -eq 2 ]; then
  mode="$1"
  verbose=""
fi

echo "$pdfs" | while read -r file
do
  ((count++))
  echo "Processing File #$count of $total Files" | tee -a $log
  echo "Current File: $file "| tee -a $log
  gs -sDEVICE=pdfwrite -dCompatibilityLevel=1.4 -dPDFSETTINGS="/$mode" -dNOPAUSE \
  -dBATCH $verbose -sOutputFile="$file-new" "$file" | tee -a $log

  sizeold=$(wc -c "$file" | cut -d' ' -f1)
  sizenew=$(wc -c "$file-new" | cut -d' ' -f1)
  difference=$((sizenew-sizeold))

  # Check if new filesize is smaller
  if [ $difference -lt 0 ]
  then
    rm "$file"
    mv "$file-new" "$file"
    printf "Compression was successfull. New File is %'.f Bytes smaller\n" \
    $((-difference)) | tee -a $log
    ((success++)) 
    echo $success > $successlog
    ((gain-=difference))
    echo $gain > $gainlog
  else
    rm "$file-new"
    echo "Compression was not necessary" | tee -a $log
  fi

done

# Print Statistics
printf "Successfully compressed %'.f of %'.f files\n" $(cat $successlog) $total | tee -a $log
printf "Safed a total of %'.f Bytes\n" $(cat $gainlog) | tee -a $log

rm $successlog $gainlog

else
  echo "No PDF File in Directory"
fi
