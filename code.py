# -*- coding: utf-8 -*-
"""
Created on Sat May 21 10:52:50 2022

@author: Angel
"""

def f1(an_int):
    n = 1
    i = 0
    while n <= an_int:
        n = n*3
        i = i+1
    return n/3

def f2(an_int):
    if an_int >= 3600:
        hh = (an_int // 3600)
        an_int = an_int - hh*3600
        if an_int > 60:
            mm = an_int // 60
            an_int = an_int - mm*60
            ss = an_int
        else:
            mm = 0
            ss = an_int
    elif an_int > 60:
        hh = 0
        mm = an_int // 60
        an_int = an_int - mm*60
        ss = an_int
    else:
        hh = 0
        mm = 0
        ss = an_int
    return '''{:02d}:{:02d}:{:02d}'''.format(hh,mm,ss)

def f3(a_list):
    if a_list[0] < a_list[1]:
        minobj = a_list[1]
        mintot = a_list[0]
        indtot = 0
        indobj = 1
    else:
        minobj = a_list[0]
        mintot = a_list[1]
        indtot = 1
        indobj = 0
    if len(a_list) > 2:
        for i in range(2,len(a_list)):
            if a_list[i] < mintot:
                minobj = mintot
                mintot = a_list[i]
                indobj = indtot
                indtot = i
            elif a_list[i] < minobj:
                minobj = a_list[i]
                indobj = i
    return (indobj,minobj)
    
def f4(a_list1, a_list2, an_int):
    total = 0
    for i in range(len(a_list2)):
        n = 0
        for j in range(len(a_list1)):
            if a_list1[j] == a_list2[i]:
                n = n+1
        if n>= an_int:
            total = total + 1
    return total

def f5(a_list):
    l=[]
    for i in range(len(a_list)):
           l.append(a_list[0:i+1])
    return l
    
def f6(a_str):
    import string
    st = ''
    for i in a_str:
        if i not in string.ascii_letters and i not in string.digits:
            st=st+i
    return st

def f7(a_str):
    l = a_str.split()
    d = {}
    for i in range(len(l)):
        if l[i] not in d.keys():
            n = 0
            for j in range(i,len(l)):
                if l[j] == l[i]:
                    n=n+1
            d[l[i]]=n
    return d

def f8(a_str):
    import string
    new=''
    for i in a_str:
        if i not in string.ascii_letters:
            new=new+i
    new1 = new.split('\n')
    l = []
    for i in range(len(new1)):
        if new1[i] != '':
            l.append(new1[i])
    total = 0
    cont = 0
    for i in range(len(l)):
            total = total + float(l[i])
            cont = cont + 1
    media = total/cont
    return media
        