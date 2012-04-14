#! /usr/bin/env python

"""
    File to NIST mteval format XML

    USAGE: ./toxml.py <filename> [docid]

    (C) 2012 Elias Zeidan

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.    
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
