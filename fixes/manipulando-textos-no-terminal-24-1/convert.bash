encoding_list=$(iconv -l | tr " " "\n")
if grep -iq WINDOWS-1252 <<< "$encoding_list"; then
	windows_encoding="WINDOWS-1252"
else
	windows_encoding="CP1252"
fi

filepaths=$(find ./machado -name *.txt | grep .txt)
for filepath in $filepaths; do
	file_format=$(file $filepath | cut -d: -f2)
	echo $file_format

	if [ "$file_format" = "ISO-8859 text" ]; then
		input_encoding="ISO-8859-1"
	else
		input_encoding=$windows_encoding
	fi

	iconv -f $input_encoding -t UTF-8 $filepath > $filepath.utf8
	rm $filepath
	mv $filepath.utf8 $filepath
done