#!/usr/bin/python

# whatsApp_analytics.py
# 01/01/2017
# Alston Cheung

import sys
import re
import matplotlib.pyplot as plt

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
        print "usage: [whatsApp _chat.txt] [--tocsv optional] [output file]"
        sys.exit(1)

    # get path of chat.txt file
    txt_file = args[0]

    # function for sorting list fo tuples by 2nd item
    def sort_tuple(each_word):
        return each_word[-1]

    # pass file path to extract_names function
    result = extract_names(txt_file)
    result = sorted(result, key = sort_tuple, reverse = True)

    # matplotlib chart parameters
    labels = []
    for each in result:
        labels.append(each[0] + " - " + str(each[1]))
    values = zip(*result)[1]

    # plot pie chart
    plt.pie(values, labels = labels, shadow = True)
    plt.axis('equal')
    plt.show()

    if len(args) > 1:
        if args[1] == '--tocsv':
            if len(args) < 3:
                print "error: not enough command args"
                sys.exit(1)

            # create output file
            output_name = args[2]
            output_file = open(output_name, "w")

            for each in result:
                output_file.write(each[0] + "," + str(each[1]) + "\n")
            output_file.close()

if __name__ == '__main__':
    main()