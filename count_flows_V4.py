#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys,os
import argparse


parser=argparse.ArgumentParser(description='Flow Counter V4.0')
parser.add_argument("-in", dest="File", required=True, help=("Fasta file  [REQUIRED]"))
parser.add_argument("-out", dest="Out_name", required=True, help=("Output file name [REQUIRED]"))
parser.add_argument("-tech", dest="Tech_Type", required=True, help=("Pyrosequencing Technology (A=FLX Titanium, B=FLX+) [REQUIRED]"))

args=parser.parse_args()

while True:
    try:
        #fichier=str(raw_input("filename:"))
        fichier=args.File
        fichier=str(fichier)
        fasta = open(fichier, 'r')
    except IOError:
        print("ERROR, file %s does not exist"%(fichier))
        sys.exit()
    else:
        break

    
savefile = open(str(args.Out_name),'w')
colonne="Sequence_ID\tNb_flows\n"
savefile.write(colonne)
    
compteur=0
matrice=""
result={}

tech=str(args.Tech_Type)

if tech != 'A' and tech != 'B' and tech != 'a' and tech != 'b':
    print("ERROR, Technology Type %s not valid"%(tech))
    sys.exit()

if tech == "A" or tech == 'a':
    while compteur != 300:
        matrice += 'T'
        matrice += 'A'
        matrice += 'C'
        matrice += 'G'
        compteur += 1
        
if tech == "B" or tech == 'b':
    matrice="TACGTACGTACGATGTAGTCGAGCATCATCTGACGCAGTACGTGCATGATCTCAGTCAGCAGCTATGTCAGTGCATGCAGTGACTGATCGTCATCAGCTAGCATCGACTGCATAGATCGCATGACGATCGCATATCGTCAGTGCATGTAGTCGAGCATCATCTGACGCAGTACGTGCATGATCTCAGTCAGCAGCTATGTCAGTGCATGCATAGATCGCATGACGATCGCATATCGTCAGTGCAGTGACTGATCGTCATCAGCTAGCATCGACTGCATGTAGTCGAGCATCATCTGACGCAGTACGTGCATAGATCGCATGACGATCGCATATCGTCAGTGCATGATCTCAGTCAGCAGCTATGTCAGTGCATGCAGTGACTGATCGTCATCAGCTAGCATCGACTGCATGTAGTCGAGCATCATCTGACGCAGTACGTGCAGTGACTGATCGTCATCAGCTAGCATCGACTGCATAGATCGCATGACGATCGCATATCGTCAGTGCATGATCTCAGTCAGCAGCTATGTCAGTGCATGCATGTAGTCGAGCATCATCTGACGCAGTACGTGCATAGATCGCATGACGATCGCATATCGTCAGTGCAGTGACTGATCGTCATCAGCTAGCATCGACTGCATGATCTCAGTCAGCAGCTATGTCAGTGCATGCAGTGACTGATCGTCATCAGCTAGCATCGACTGCATAGATCGCATGACGATCGCATATCGTCAGTGCATGATCTCAGTCAGCAGCTATGTCAGTGCATGCATGTAGTCGAGCATCATCTGACGCAGTACGTGCATAGATCGCATGACGATCGCATATCGTCAGTGCATGATCTCAGTCAGCAGCTATGTCAGTGCATGCAGTGACTGATCGTCATCAGCTAGCATCGACTGCATGTAGTCGAGCATCATCTGACGCAGTACGTGCATGATCTCAGTCAGCAGCTATGTCAGTGCATGCATAGATCGCATGACGATCGCATATCGTCAGTGCATGTAGTCGAGCATCATCTGACGCAGTACGTGCAGTGACTGATCGTCATCAGCTAGCATCGACTGCATAGATCGCATGACGATCGCATATCGTCAGTGCATGTAGTCGAGCATCATCTGACGCAGTACGTGCATGATCTCAGTCAGCAGCTATGTCAGTGCATGCAGTGACTGATCGTCATCAGCTAGCATCGACTGCATGATCTCAGTCAGCAGCTATGTCAGTGCATGCAGTGACTGATCGTCATCAGCTAGCATCGACTGCATAGATCGCATGACGATCGCATATCGTCAGTGCATGTAGTCGAGCATCATCTGACGCAGTACGTGCATGATCTCAGTCAGCAGCTATGTCAGTGCATGCATGTAGTCGAGCATCATCTGACGCAGTACGTGCAGTGACTGATCGTCATCAGCTAGCATCGACTGCATAGATCGCATGACGATCGCATATCGTCAGTGCAGTGACTGATCGTCATCAGCTAGCATCGACTGCATGTAGTCGAGCATCATCTGACGCAGTACGTGCATAGATCGCATGACGATCGCATATCGTCAGTGCATGATCTCAGTCAGCAGCTATGTCAGTGCATGCAGTGACTGATCGTCATCAGCTAGCATCGACTGCATGTAGTCGAGCATCATCTGACGCAGTACGTGCATGATCTCAGTCAGCAGCTATGTCAGTGCATGCATAGATCGCATGACGATCGCATATCGTCAGTGCAGTGACTGATCGTCATCAGCTAGCATCGACTGCATGATCTCAGTCAGCAGC"
    
flow=0
lignes = fasta.readlines()
fasta.close

#print(matrice)
ambig=0
for ligne in lignes:
    if ligne[0]=='>':
        nomseq = ligne[1:]
        nomseq = nomseq[:-1]
        continue
    if ligne =='\n':
        break
    else:
        sequence=ligne
        x=0
        flow=0
        mat_cur=matrice[x]
        ambig=0
        for base in sequence:
            if base == 'N':
                #print("Séquence avec avec ambiguïté: %s"% (nomseq))
                resultat="%s\t%s\n"%(nomseq,"NA")
                savefile.write(resultat)
                ambig=1
                break      
            if base =='\n' or base=='' or base==' ':
                break
            if mat_cur==base and x !=0:
                continue
            else:
                while True:
                    mat_cur=matrice[x]
                    if base != mat_cur:
                        flow +=1
                        x+=1
                        continue
                    else:
                        break
        if ambig == 1:
            ambig=0
            continue
        else:
            resultat="%s\t%s\n"%(nomseq,flow+1)
            savefile.write(resultat)
savefile.close()
