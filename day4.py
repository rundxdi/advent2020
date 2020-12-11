# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 14:01:45 2020

@author: rundx
"""
import sys

f = open('day4.txt','r')

passports = []
temp = []
for line in f:
    
    if len(line.rstrip()) > 0:
        temp += line.rstrip().split()
    if len(line.rstrip()) == 0:
        passports.append(temp)
        temp = []



passdict = {}
i=0

for passport in passports:
    passdict[i] = dict()
    for entry in passport:
        tentry = entry.split(':')
        passdict[i][tentry[0]] = tentry[1]
    i+=1

valids = 0
for passport in passdict:
    flag = 0
    if 'byr' in passdict[passport]:
        flag +=1
    if 'iyr' in passdict[passport]:
        flag +=1
    if 'eyr' in passdict[passport]:
        flag +=1
    if 'hgt' in passdict[passport]:
        flag +=1
    if 'hcl' in passdict[passport]:
        flag +=1
    if 'ecl' in passdict[passport]:
        flag +=1
    if 'pid' in passdict[passport]:
        flag +=1
    if flag == 7:
        valids += 1
        
print(valids)


valids2 = 0
valcols = ['amb','blu','brn','gry','grn','hzl','oth']

for passport in passdict:
    byr = passdict[passport].get('byr')
    iyr = passdict[passport].get('iyr')
    eyr = passdict[passport].get('eyr')
    hgt = passdict[passport].get('hgt')
    hcl = passdict[passport].get('hcl')
    ecl = passdict[passport].get('ecl')
    pid = passdict[passport].get('pid')
    try:
        byr = int(byr)
        iyr = int(iyr)
        eyr = int(eyr)
        if len(pid) != 9:
            continue
        pid = int(pid)
        #print(hgt)
        #print(pid)
        
        if byr < 1920 or byr > 2002:
            continue
        if iyr <2010 or iyr > 2020:
            continue
        if eyr <2020 or eyr > 2030:
            continue
        if hgt[-2:] != 'cm' and hgt[-2:] != 'in':
            continue
        elif hgt[-2:] == 'cm':
            hgt = int(hgt[:-2])
            if hgt < 150 or hgt > 193:
                continue
        elif hgt[-2:] == 'in':
            hgt = int(hgt[:-2])
            if hgt < 59 or hgt > 76:
                continue
        if len(hcl) != 7 or hcl[0] != '#':
            continue
        for char in hcl:
            if ord(char) < 48 or ord(char) > 102:
                continue
            elif ord(char) > 57 and ord(char) < 97:
                continue
        if ecl not in valcols:
            continue
    except:
        continue
        print(passport)
        sys.exit()
    print('no')
    valids2 += 1
        
print(valids2)