# Extract files
find . -depth -name '*.bz2' -exec bzip2 -n {} \; -exec rm {} \;

#Remove lines starting with <...
find . -name "*" -exec  sed -i '/^</ d' "{}" \;


