#encoding=utf-8
import os
import jieba
import jieba.posseg as pseg
import sys
import string
import codecs
import jieba.posseg as pseg

fileName = 'E:/aa0011/test/aaaa.txt'

resName = 'E:/aa0011/test/004.txt'
source = open(fileName, 'r')

result = codecs.open(resName, 'w', 'utf-8')
line = source.readline()
line = line.rstrip('\n')

while (line != ""):
    seg=pseg.cut(line)
    for i in seg:
        x = i.flag
        if(x == 'u')or(x == 'ule')or(x == 'uzhi')or(x == 'a')or(x == 'd')or(x == 'p'):
                result.write(i.word+ '\r\n')
        else:
            print(i.word + '\r\n')
    line = source.readline()
else:
    print('End file: ' )
    source.close()
    result.close()


print('End All')
