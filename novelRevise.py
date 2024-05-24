# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 15:53:59 2019

@author: shenlei
"""

import os

CHARSET = 'utf-8'

def changeToDoubleQuotationInLine(lineStr, replacedStr):
    destStr = lineStr
    posi = destStr.find(replacedStr)
    count = 0
    lenOfReplacedStr = len(replacedStr)
    while posi >= 0:
        if count % 2 == 0:
            destStr = destStr[:posi] + "“" + destStr[posi + lenOfReplacedStr:]
        else:
            destStr = destStr[:posi] + "”" + destStr[posi + lenOfReplacedStr:]
        posi = destStr.find(replacedStr, posi+1)
        count += 1
    return destStr


def changeToDoubleQuotation(srcFileName, replacedList):
    dstFileName = srcFileName[:-4] + "(revise).txt"
    srcFile = open(srcFileName, "r", encoding=CHARSET)
    dstFile = open(dstFileName, "w", encoding='utf-8')
    line = srcFile.readline()
    while line:
        if len(line.strip()) == 0:
            line = srcFile.readline()
            continue
        for replacedStr in replacedList:
            line = changeToDoubleQuotationInLine(line, replacedStr)
        dstFile.write(line + '\n')
        line = srcFile.readline()
    srcFile.close()
    dstFile.close()
    return


def removeRubbishLine(srcFileName, rubbishList):
    dstFileName = srcFileName[:-4] + "(revise).txt"
    srcFile = open(srcFileName, "r", encoding=CHARSET)
    dstFile = open(dstFileName, "w", encoding='utf-8')
    line = srcFile.readline()
    while line:
        if len(line.strip()) == 0:
            line = srcFile.readline()
            continue
        rubbishFlag = False
        for rubbishStr in rubbishList:
            if line.find(rubbishStr) >= 0:
                rubbishFlag = True
                # print(line)
                break
        if not rubbishFlag:
            dstFile.write(line + '\n')
        line = srcFile.readline()
    srcFile.close()
    dstFile.close()
    return


def removeRepetitionLine(srcFileName):
    dstFileName = srcFileName[:-4] + "(revise).txt"
    srcFile = open(srcFileName, "r", encoding=CHARSET)
    dstFile = open(dstFileName, "w", encoding='utf-8')
    line = srcFile.readline()
    oldLine = 'just begin......'
    while line:
        if len(line.strip()) == 0:
            line = srcFile.readline()
            continue
        if len(line.strip()) > 30:
            dstFile.write(oldLine + '\n')
        else:
            if line.replace(' ', '').find(oldLine.replace(' ', '')) < 0:
                dstFile.write(oldLine + '\n')
        oldLine = line
        line = srcFile.readline()
    dstFile.write(oldLine + '\n')
    srcFile.close()
    dstFile.close()
    return
srcFileName = "e:\\workspace\\txt\\aaaa.txt"
replacedList = ["\""]

#changeToDoubleQuotation(srcFileName, replacedList)
rubbishList = ["大风小说为你提供"]
srcFileName = "d:\\workspace\\txt\\aaaa.txt"
removeRubbishLine(srcFileName, rubbishList)
#srcFileName = "e:\\workspace\\txt\\test.txt"
#removeRepetitionLine(srcFileName)
