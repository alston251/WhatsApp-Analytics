#!/usr/bin/python

import sys
import re

def find(parameter, str):
  result = re.findall(parameter, str)
  if result:
    return result
  else:
    return "not found"

def extract_names(filename):
    # dictionary to store output results
    names_count = {}

    # open file
    in_file = open(filename, "r")

    # read through each line
    for each_line in in_file:
        # use regex to find names
        name = find(r"\d\d: \w+ ?\w+:",each_line)

        if name != "not found":
            # convert from list to string
            name = name[0]
            # shorten name strings by 4 chars from left
            name = name[4:-1]

            # if name exists, increment counter
            # add name to dict if it doesn't exist
            if name in names_count:
                names_count[name] += 1
            else:
                names_count[name] = 1

    # convert dict to a list of tuples
    output = names_count.items()
    return output


def main():
    args = sys.argv[1:]

    if not args:
        print "usage: whatsApp_analytics.py [whatsApp _chat.txt file]"
        sys.exit(1)

    # get path of chat.txt file
    txt_file = args[0]

    def sort_tuple(each_word):
        return each_word[-1]

    # pass file to names extraction function
    result = extract_names(txt_file)
    result = sorted(result, key = sort_tuple, reverse = True)
    print result

    # create output file
    output_name = "output.csv"
    output_file = open(output_name, "w")

    for each in result:
        output_file.write(each[0] + "," + str(each[1]) + "\n")
    output_file.close()

    # output with matplotlib


if __name__ == '__main__':
    main()