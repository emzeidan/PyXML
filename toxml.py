#! /usr/bin/env python

"""
    File to NIST mteval format XML

    
"""

import os, sys, re

def makefile(filename, docid=str(sys.argv[2]), tsr="s", ext=".xml"):
    inputfilename = filename + ".txt"
    inputfile = open(inputfilename, "r+")
    
    name = filename + ext
    # put opening lines in document
    xml = open(name, "w+")
    xml.write("<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<!DOCTYPE mteval SYSTEM \"ftp://jaguar.ncsl.nist.gov/mt/resources/mteval-xml-v1.6.dtd\">\n<mteval>\n")
    # source? test? reference?
    if tsr=="s":
        xml.write("\t<srcset setid=\"plan\" srclang=\"English\">\n")
        xml.write("\t<doc docid=\"%s\" genre=\"\">\n"%docid) 
    elif tsr=="t":
        xml.write("\t<tstset setid=\"plan\" trglang=\"French\" srclang=\"English\" sysid=\"EliasPlan\">\n")
        xml.write("\t<doc docid=\"%s\" genre=\"\">\n"%docid) 
    elif tsr=="r":
        xml.write("\t<refset setid=\"plan\" trglang=\"French\" srclang=\"English\" refid=\"plan\">\n")
        xml.write("\t<doc docid=\"%s\" genre=\"\">\n"%docid) 

    endPunct = re.compile("[.!?\n]")
    sentence = endPunct.split(inputfile.read())
    num = 0
    for i in range(len(sentence)-1):
        num += 1
        xml.write("\t<seg id=\"%d\">%s</seg>\n" %(num, sentence[i]))

    if tsr=="s":
        xml.write("\t</doc>\n") 
        xml.write("\t</srcset>\n")

    elif tsr=="t":
        xml.write("\t</doc>\n") 
        xml.write("\t</tstset>\n")

    elif tsr=="r":
        xml.write("\t</doc>\n") 
        xml.write("\t</refset>\n")


    xml.write("</mteval>\n") 

if __name__ == "__main__":
    makefile(sys.argv[1])
