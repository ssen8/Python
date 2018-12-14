#!/usr/bin/env python

import os
import rstr
import platform
import time

PLATFORM=platform.system()
REGEX=raw_input('Input regex : ')
RANGE=int(raw_input('Input Total number of strings : '))

f=open('Regex_pattern_wordlist.txt','a+')
time.sleep(1)
os.system('cls')
for i in range(RANGE):

     if (PLATFORM=='Windows'):
         print('\n .......... Generating wordlist .......... ')
         print('\n\t    OS - Windows\n\t    Printing {} of {} ...'.format(i,RANGE))
         time.sleep(0.1)
         os.system('cls')
     elif (PLATFORM=='Linux'):
         print('\n .......... Generating wordlist .......... ')
         print('\n\t    OS - Linux\n\t    Printing {} of {} ...'.format(i,RANGE))
         time.sleep(0.1)
         os.system('clear')
    
     a=rstr.xeger(r'{}'.format(REGEX))
     f.write(a+'\n')

f.close()


