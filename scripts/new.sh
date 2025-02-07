#!/bin/bash

create_problem() {
    PROBLEM_NUMBER=$1
    PROBLEM_NAME=$2
    LANGUAGE=$3

    # create the main problem folder
    MAIN_FOLDER="${PROBLEM_NUMBER}-${PROBLEM_NAME}"
    mkdir -p "$MAIN_FOLDER"

    # create a subfolder for the language
    LANGUAGE_FOLDER="${MAIN_FOLDER}/${LANGUAGE}"
    mkdir -p "$LANGUAGE_FOLDER"

    # create the extension
    if [ "$LANGUAGE" = "cpp" ]; then
        EXTENSION="cpp"
    elif [ "$LANGUAGE" = "python" ]; then
        EXTENSION="py"
    elif [ "$LANGUAGE" = "c" ]; then
        EXTENSION="c"
    else
        echo "Unsupported language: $LANGUAGE"
        exit 1
    fi

    # create the solution file
    SOLUTION_FILE="${LANGUAGE_FOLDER}/${PROBLEM_NAME}.${EXTENSION}"
    touch "$SOLUTION_FILE"

    # create a description file
    DESC_FILE="${MAIN_FOLDER}/desc.md"
    touch "$DESC_FILE"
    if [ "$LANGUAGE" = "cpp" ]; then
        echo "#include <iostream>" >> "$SOLUTION_FILE"
        echo "" >> "$SOLUTION_FILE"
        echo "using namespace std;" >> "$SOLUTION_FILE"
        echo "" >> "$SOLUTION_FILE"
        echo "" >> "$SOLUTION_FILE"
    fi

    echo "Folder structure created for problem ${PROBLEM_NUMBER}-${PROBLEM_NAME} in ${LANGUAGE}"
}

echo "Enter problem number:"
read PROBLEM_NUMBER

echo "Enter problem name:"
read PROBLEM_NAME

echo "Enter language (e.g. cpp, python):"
read LANGUAGE

create_problem "$PROBLEM_NUMBER" "$PROBLEM_NAME" "$LANGUAGE"
