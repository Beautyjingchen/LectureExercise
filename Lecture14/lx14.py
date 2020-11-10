#!/usr/bin/python3
import os

def new_find_my_kmers(dna,ksize=2,minkfreq=2) :
   kmersfound = []
   kmerstarts = list(range(0,len(dna)))
   for base in kmerstarts:
       if (base+ksize) < len(dna)+1:
           seqout = (dna)[base:base+ksize]
           kmersfound = kmersfound + [seqout] 
   nrset = list(set(kmersfound))
   returnstuff = []
   for kfreqfind in nrset:
       if kmersfound.count(kfreqfind) > minkfreq :
           returnstuff.append(kfreqfind.upper()+": "+str(kmersfound.count(kfreqfind)))
   return returnstuff

