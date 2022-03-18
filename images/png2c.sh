#!/bin/bash

png2c() {
file=$1
cfile="$(echo -n "$1" | rev | cut -f 2- -d '.' | rev).c"
cname=$(echo -n "$1" | sed -e 's/[^a-zA-Z0-9_]/_/')
echo "// Warning: This is a generated file, do not edit it!" >"$cfile"
echo "#include <stdint.h>" >>"$cfile"
echo "#include <stddef.h>" >>"$cfile"
echo "const char $cname[] = {" >>"$cfile"
xxd -i <"$file" >>"$cfile"
echo "};" >>"$cfile"
echo "const size_t ${cname}_len = sizeof($cname) / sizeof(char);" >>"$cfile"
}

for i in $*; do
	png2c "$i"
done
