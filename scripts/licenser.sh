#!/bin/bash

NumberOfFiles="$#"
let FileCount=0
args=("$@")

while [ ${NumberOfFiles} -gt 0 ]
do
	FileName=${args[$FileCount]}
	cat license_header.txt| cat - ${FileName}  > /tmp/out && mv /tmp/out ${FileName}
	let  FileCount=FileCount+1
	let  NumberOfFiles=NumberOfFiles-1
done
exit 0
