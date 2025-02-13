#!/bin/bash

create_problem() {
    INPUT_TITLE=$1

    PROBLEM_NUMBER=$(echo "$INPUT_TITLE" | sed -E 's/([0-9]+)\..*/\1/')
    PROBLEM_NUMBER=$(printf "%04d" "$PROBLEM_NUMBER")

    PROBLEM_NAME=$(echo "$INPUT_TITLE" | sed -E 's/[0-9]+\.\s*(.*)/\1/' | tr '[:upper:]' '[:lower:]' | tr ' ' '-')

    MAIN_FOLDER="${PROBLEM_NUMBER}-${PROBLEM_NAME}"
    mkdir -p "$MAIN_FOLDER"

    for LANGUAGE in "cpp" "python"; do
        LANGUAGE_FOLDER="${MAIN_FOLDER}/${LANGUAGE}"
        mkdir -p "$LANGUAGE_FOLDER"

        if [ "$LANGUAGE" = "cpp" ]; then
            EXTENSION="cpp"
        elif [ "$LANGUAGE" = "python" ]; then
            EXTENSION="py"
        fi

        SOLUTION_FILE="${LANGUAGE_FOLDER}/${PROBLEM_NAME}.${EXTENSION}"
        touch "$SOLUTION_FILE"

        if [ "$LANGUAGE" = "cpp" ]; then
            cat <<EOF > "$SOLUTION_FILE"
#include <iostream>

using namespace std;

EOF
        fi
    done

    DESC_FILE="${MAIN_FOLDER}/desc.md"
    touch "$DESC_FILE"

    echo "Folder structure created for problem ${PROBLEM_NUMBER}-${PROBLEM_NAME}"
}

echo "Paste the problem title:"
read PROBLEM_TITLE

create_problem "$PROBLEM_TITLE"
