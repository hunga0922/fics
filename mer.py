#! /usr/bin/python3.6
# -*- coding: utf-8 -*-
# PYNQ DMA and Aurora test

import time
import numpy as np
import subprocess
import struct
import sys
import random
BLOCK=0.7
ficb= np.zeros((4,6))
j=0
while(j<4):
    i= 0
    while(i<6):
        if(BLOCK<random.random()):
            ficb[j][i] = 1
        else:
            ficb[j][i]=0
        i=i+1
    print(ficb)
    j=j+1

print("Busy matrix")
j=0
while(j<4):
    print(j,ficb[j][5],ficb[j][4],ficb[j][3],ficb[j][2],ficb[j][1],ficb[j][0])
    j=j+1

start=[0,0,0,0,0,0];
size=[0,0,0,0,0,0];
i=0
k=0
while(i<6):
    j=k
    while(j<4):
        if(ficb[j][i]==0) :
            print(i, "start find", j)
            tstart = j
            tsize=0
            break
        else:
            j=j+1
            if(j==4):
                tstart=3
                tsize=0
    k=j
    while(k<4):
        if(ficb[k][i]==0):
            tsize=tsize+1
            k=k+1
        else:
            if(size[i]<tsize): 
                start[i] = tstart
                size[i]=tsize
            break
    if(k>=4):
        if(size[i]<tsize): 
            start[i] = tstart
            size[i]=tsize
        i=i+1
        k=0

print("Start", start[5],start[4],start[3],start[2],start[1],start[0])
print("Size", size[5],size[4],size[3],size[2],size[1],size[0])

mer=[0,0,0,0,0,0];
sp=[0,0,0,0,0,0];
width=[0,0,0,0,0,0];
length=[0,0,0,0,0,0];
i=0
while(i<6):
    k=i+1
    tstart = start[i]
    twidth= size[i]
    tlength=1
    while(k<6):
        ttwidth = twidth
        ttstart = tstart
        if(start[k]>tstart):
            twidth = twidth -(start[k]-tstart)
            tstart = start[k]
        if(( start[k]+size[k]) < (tstart+twidth)):
            twidth = twidth - ( (tstart+twidth)-(start[k]+size[k]) )
        print(k,tstart,twidth)
        if(twidth<=0): 
            tstart = ttstart
            twidth = ttwidth
            break;
        k=k+1
    mer[i]= (k-i)*twidth
    if(mer[i]<size[i]) :
        mer[i]=size[i]
        sp[i]=start[i]
        width[i]=size[i]
        length[i]=1
    else:
        sp[i]=tstart
        width[i]=twidth
        length[i]=k-i
    i=i+1
print("MER  ", mer[5],mer[4],mer[3],mer[2],mer[1],mer[0])
print("Startp", sp[5],sp[4],sp[3],sp[2],sp[1],sp[0])
print("Width ", width[5],width[4],width[3],width[2],width[1],width[0])
print("Length", length[5],length[4],length[3],length[2],length[1],length[0])
