#!/usr/local/bin/python3
"""This module does nothing"""
import re
import os


def increment_pagenum(mystr, num):
    """input: (string, counter) / output: replaced string """
    regex_pattern = re.search(r",\s*(\d+)", mystr)
    if regex_pattern == None:
        return mystr
    else:
        print("regex_pattern.group(1) is", regex_pattern.group(1))
        new_page = int(regex_pattern.group(1))+num
        replace_pattern = r'\g<1>'+re.escape(str(new_page))
        print("replace_pattern -> value:", replace_pattern)
        #new_str = re.sub(r'(.*,\s*)\d+', r'\1 %s' % str(new_page), mystr)
        #new_str = re.sub(r'(.*,\s*)\d+', r"\1 {}".format(str(new_page)), mystr) # not working
        #new_str = re.sub(r'(.*,)\s*\d+', r'\1 %s' % str(new_page), mystr)
        #new_str = re.sub(r'(.*,)\s*\d+', replace_pattern, mystr) # progressing...
        #new_str = re.sub(r'(.*,)\s*\d+', r'\g<1>%s' % str(new_page), mystr) # This works!!!
### three lines come together ###
        replace_pattern = r'\g<1>'+re.escape(str(new_page))
        print("replace_pattern -> value:", replace_pattern)
        new_str = re.sub(r'(.*,)\s*\d+', replace_pattern, mystr) # and this also works!!!
### ###


        return new_str



def main():
    """ main """
    bmf = open(os.path.expanduser("~/booky/mybookmarks.txt"), "r")
    lines = bmf.readlines()
    #for i in range(len(lines)):
        #print("i -> value:", i)
        #print("lines[i]'s value:", lines[i])
        #lines[i] = lines[i].strip()
        #print("lines[i]'s value:", lines[i])
    print("lines's value:", lines)
    for i in range(len(lines)):
        print("i -> value:", i)
        lines[i] = increment_pagenum(lines[i],1)
        print("lines[", i, "]'s value:", lines[i])
    for line in lines:
        print(line)
    new_bmf = open(os.path.expanduser("~/booky/mynewbookmarks.txt"), "w")
    new_bmf.writelines(lines)

main()

