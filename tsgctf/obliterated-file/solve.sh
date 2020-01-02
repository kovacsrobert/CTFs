#!/bin/bash

set -e
shopt -s nullglob extglob

cd "`git rev-parse --git-path objects`"

# loose objects
for o in [0-9a-f][0-9a-f]/*([0-9a-f]) ; do
	printf "\n************************************************* $o\n\n"
	git cat-file -p ${o/\/}
	printf "\n"
done