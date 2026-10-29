#usr/bin/bash

filenames_doc="tmp.txt"
input_dir_start="../content/"

# usage instructions
usage() { echo "Usage: $0 -i INPUT_DIRECTORY" 1>&2; exit 1; }

printf "##########################################\n"
printf "#            CDN Upload Script           #\n"
printf "##########################################\n\n\n"

# get command line arguments
while getopts "i:w" opts; do
    case "${opts}" in
        i)
            search_dir=${OPTARG}
            ;;
        w)
            wet_run=1
            ;;
        *)
            usage
            wet_run=0
            ;;
    esac
done
shift $((OPTIND-1))

# check command line arguments
if [ -z "${search_dir}" ]; then
    printf "No search dir provided\n"
    usage
elif [[ $search_dir != $input_dir_start* ]]; then
    printf "Input directory must start with '${input_dir_start}' instead got ${search_dir}\n"
    usage
fi

printf "Searching ${search_dir} for files...\n\n\n"
find ${search_dir} -name "*" > ${filenames_doc}

# upload files to storage bucket
while IFS="" read -r line || [ -n "$line" ]
do
    if [ -f "$line" ]; then
        s3_filename=${line/$input_dir_start/}
        if [ "$wet_run" == 1 ]; then
            aws s3 cp ${line} s3://media/${s3_filename} --profile fastly-us-west-1
        else
            echo "Would've uploaded ${s3_filename}"
        fi
    # else
    #     echo "Skipping $line. It is not a file"
    fi
done < ${filenames_doc}
printf "\n\n\n"
printf "Cleaning up...\n"
rm ${filenames_doc}
