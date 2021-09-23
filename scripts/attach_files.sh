#!/bin/bash

# 1st arg: txt file
# 2nd arg: dataset id

for i in `cat $1`
do
	dataset=${i%%/*}
	filename=${i##*/}
	if [[ $filename =~ "coordinates" ]]
	then
		imagename=${filename%%\.coordinates*}
	else
		imagename=${filename%%\.csv*}
	fi
	image=`python /uod/idr/metadata/idr-utils/scripts/annotate/find_images.py $imagename Dataset:$2`
	python /uod/idr/metadata/idr-utils/scripts/annotate/attach_file.py /uod/idr/filesets/idr0108-sabinina-nuclearporecomplex/20210426-Globus/$i $image
done
