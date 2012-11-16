#!/bin/bash

scriptDir=`dirname $0`
outpathUI="$scriptDir/../views/"
suffixUI="UI.py"
outpathRC="$scriptDir/../../"
suffixRC="_rc.py"
for file in $scriptDir/*
do
    if [ -f $file ]; then
        ext=${file##*.}
        if [ $ext = "ui" ]; then
            echo $file
            outfilename=`basename "$file" ".$ext"`
            outfile="$outpathUI$outfilename$suffixUI"
            pyuic4 $file -o $outfile
        fi
        if [ $ext = "qrc" ]; then
            echo $file
            outfilename=`basename "$file" ".$ext"`
            outfile="$outpathRC$outfilename$suffixRC"
            pyrcc4 $file -o $outfile
        fi
    fi
done

