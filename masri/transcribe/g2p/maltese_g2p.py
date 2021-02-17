#-*- coding: utf-8 -*- 
#############################################################################################
#g2p_cw_rules.py

#Author: Carlos Daniel Hernandez Mena
#Location: University of Malta
#Date: July 2019

#Presentation:

#This file contains the g2p_cw_rules() that applies the CrimsonWing Grapheme-to-Phoneme
#rules. 

#The main strategy is to apply a "find and replace" command to every rule specified
#by CrimsonWing. This is possible because CrimsonWing demands that its rules have
#to be applied in the same order they are numbered.

#As this is the simplest way to apply the rules, this is also probably the fastest. About
#28,000 words are transcribed in about 2 minutes.

#UPDATES:

#Carlos Mena. 28-March-2020. === I modified the g2p_cw_rules() function to be able
#to handle full sentences instead of taking only one word at a time.

#############################################################################################
#############################################################################################
#GLOBAL VARIABLES

ALL_VOWELS = ['ί','a','e','i','o','u','ϊ','ä','ë','ï','ö','ü','ɐ','ɛ','ɪ','ɔ','ʊ','à','è','ì','ò','ù']

ALL_CONSONANTS = ['b','ċ','d','f','g','ġ','h','ħ','j','k','l','m','n','p','q','r','s','t','v','w','x','z','ż','c','y','ʔ','ʦ','ʧ','ǳ','ʤ','ʃ','ʒ']

#############################################################################################
#############################################################################################
#GLOBAL FUNCTIONS

#Fuctions from 1 to 8 work in a similar way. In fact, they are combinations of sets of
#consonants and vowels surrounding a grapheme. For example:

#C grapheme C
#C grapheme V
#V grapheme C
#V grapheme V
#C grapheme
#grapheme C
#V grapheme
#grapheme V

#'C' is in reality the list of consonants ALL_CONSONANTS and V is ALL_VOWELS. To
#implement for example the function "ApplyRule_CgraphV()" that corresponds to the
#combination "C grapheme V" the pseudocode is 

#	1:	for every_consonant in C:
#	2:		for every_vowel in V:
#	3:			combination = C+grapheme+V
#	4:			if combination is in the current word:
#	5:				replace the combination for the phoneme. Note tha the combiation is 
# 										 the grapheme you want to convert.

#This pseudocode is valid for functions from 1 to 8.
#-------------------------------------------------------------------------------------------#

#1. Function ApplyRule_CgraphC()

def ApplyRule_CgraphC(word,graph_in,graph_out):
	for C_Left in ALL_CONSONANTS:
		for C_Right in ALL_CONSONANTS:
			cadena_in = C_Left + graph_in  + C_Right
			cadena_out = C_Left + graph_out + C_Right				
			word = word.replace(cadena_in,cadena_out)
		#ENDFOR
	#ENDFOR
	return word
#ENDDEF

#############################################################################################
#2. Function ApplyRule_VgraphV()

def ApplyRule_VgraphV(word,graph_in,graph_out):
	for V_Left in ALL_VOWELS:
		for V_Right in ALL_VOWELS:
			cadena_in = V_Left + graph_in  + V_Right
			cadena_out = V_Left + graph_out + V_Right			
			word = word.replace(cadena_in,cadena_out)
		#ENDFOR
	#ENDFOR
	return word
#ENDDEF

#############################################################################################
#3. Function ApplyRule_CgraphV()

def ApplyRule_CgraphV(word,graph_in,graph_out):
	for C_Left in ALL_CONSONANTS:
		for V_Right in ALL_VOWELS:
			cadena_in = C_Left + graph_in  + V_Right
			cadena_out = C_Left + graph_out + V_Right				
			word = word.replace(cadena_in,cadena_out)
		#ENDFOR
	#ENDFOR
	return word
#ENDDEF

#############################################################################################
#4. Function ApplyRule_CgraphV()

def ApplyRule_VgraphC(word,graph_in,graph_out):
	for V_Left in ALL_VOWELS:
		for C_Right in ALL_CONSONANTS:
			cadena_in  = V_Left + graph_in  + C_Right
			cadena_out = V_Left + graph_out + C_Right				
			word = word.replace(cadena_in,cadena_out)
		#ENDFOR
	#ENDFOR
	return word
#ENDDEF


#############################################################################################
#5. Function ApplyRule_CgraphC()

def ApplyRule_Cgraph(word,graph_in,graph_out):
	for C_Left in ALL_CONSONANTS:
		cadena_in = C_Left + graph_in
		cadena_out = C_Left + graph_out			
		word = word.replace(cadena_in,cadena_out)
	#ENDFOR
	return word
#ENDDEF


#############################################################################################
#6. Function ApplyRule_graphC()

def ApplyRule_graphC(word,graph_in,graph_out):
	for C_Right in ALL_CONSONANTS:
		cadena_in  = graph_in + C_Right
		cadena_out = graph_out	+ C_Right		
		word = word.replace(cadena_in,cadena_out)
	#ENDFOR
	return word
#ENDDEF

#############################################################################################
#7. Function ApplyRule_graphV()

def ApplyRule_graphV(word,graph_in,graph_out):
	for V_Right in ALL_VOWELS:
			cadena_in  = graph_in  + V_Right
			cadena_out = graph_out + V_Right				
			word = word.replace(cadena_in,cadena_out)
	#ENDFOR
	return word
#ENDDEF

#############################################################################################
#8. Function ApplyRule_graphV()

def ApplyRule_Vgraph(word,graph_in,graph_out):
	for V_Left in ALL_VOWELS:
			cadena_in  = V_Left + graph_in
			cadena_out = V_Left + graph_out
			word = word.replace(cadena_in,cadena_out)
	#ENDFOR
	return word
#ENDDEF

#############################################################################################
#############################################################################################
#MAIN FUCTION: g2p_cw_rules()

import string
import re

def g2p_cw_rules(cadena):

	#We save the original string (Just in case)
	org = cadena

	#We have to be sure that the input string is a string
	cadena = str(cadena)

	#The input string is processed in lowercase
	cadena = cadena.lower()

	#Saving the dash with an innocuous character
	cadena = cadena.replace('-','ŵ')

	#Remove the apostrophe
	cadena = cadena.replace("\'","")

	#Eliminating punctuation marks
	cadena = cadena.translate(str.maketrans('','', string.punctuation))

	#Eliminating the extra spaces
	cadena = re.sub('\s+',' ',cadena)

	#Eliminating the extra espaces at the end and at the begining of the string (trim)
	cadena = cadena.strip()

	#Restoring the dash
	cadena = cadena.replace('ŵ','-')

	#Letters "c" and "y" are not part of the Maletse alphabet, so
	#these substitutions seems to help.
	cadena = cadena.replace("y","ɪ")
	cadena = cadena.replace("ca","ka")
	cadena = cadena.replace("ce","se")
	cadena = cadena.replace("ci","si")
	cadena = cadena.replace("co","ko")
	cadena = cadena.replace("cu","su")
	
	#Replace the two symbols of the vowel "ie" for just one symbol "ί"
	cadena = cadena.replace("ie","ί")

	#Insert word boundaries
	cadena = "#"+cadena+"#"
	cadena = cadena.replace(' ','#')

	#-----------------------------------------------------------------------------------#
	#Diphthongs
	#Rule 001
	cadena = cadena.replace("għu","ɔʊ")
	#Rule 002
	cadena = cadena.replace("għi","ɛɪ")
	#Rule 003
	cadena = cadena.replace("aj","ɐɪ")
	#Rule 004
	cadena = cadena.replace("aw","ɐʊ")
	#Rule 005
	cadena = cadena.replace("ej","ɛɪ")
	#Rule 006
	cadena = cadena.replace("ew","ɛʊ")
	#Rule 007
	cadena = cadena.replace("iw","ɪʊ")
	#Rule 008
	cadena = cadena.replace("oj","ɔɪ")
	#Rule 009
	cadena = cadena.replace("ow","ɔʊ")

	#-----------------------------------------------------------------------------------#
	#Vowels and vowel lengthening rules

	#Rule 010
	cadena = cadena.replace("ίgħe","ίjë")
	#Rule 011
	cadena = cadena.replace("agħa","ä")
	#Rule 012
	cadena = cadena.replace("egħe","ë")
	#Rule 013
	cadena = cadena.replace("ogħo","ö")

	#Rule 014
	cadena = ApplyRule_CgraphC(cadena,'ehi','ëhi')
	cadena = ApplyRule_CgraphC(cadena,'egħi','ëgħi')

	#Rule 015
	#cadena = ApplyRule_Cgraph(cadena,'a#','ä#')
	##cadena = ApplyRule_graphCgraph(cadena,'#','#','a#','ä#')

	#Rule 016
	#cadena = ApplyRule_Cgraph(cadena,'e#','ë#')
	##cadena = ApplyRule_graphCgraph(cadena,'#','#','e#','ë#')

	#Rule 017
	#cadena = ApplyRule_Cgraph(cadena,'o#','ö#')
	##cadena = ApplyRule_graphCgraph(cadena,'#','#','o#','ö#')

	#Rule 018
	#cadena = ApplyRule_Cgraph(cadena,'u#','ü#')
	##cadena = ApplyRule_graphCgraph(cadena,'#','#','u#','ü#')

	#Rule 019
	cadena = cadena.replace("aha","ä")

	#Rule 020
	cadena = cadena.replace("aho","ö")

	#Rule 021
	cadena = cadena.replace("ehe","ë")

	#Rule 022
	cadena = cadena.replace("għa","għä")

	#Rule 023
	cadena = cadena.replace("agħ","ägħ")

	#Rule 024
	cadena = cadena.replace("għe","għë")

	#Rule 025
	cadena = cadena.replace("egħ","ëgħ")

	#Rule 026
	cadena = cadena.replace("għo","għö")

	#Rule 027
	cadena = cadena.replace("ogħ","ögħ")

	#Rule 028
	cadena = cadena.replace("ha","hä")

	#Rule 029
	cadena = cadena.replace("ah","äh")

	#Rule 030
	cadena = cadena.replace("he","ëh")

	#Rule 031
	cadena = cadena.replace("eh","ëh")

	#Falta Rule 032

	cadena = ApplyRule_graphC(cadena,'ίgħ','ëgħ')

	#Rule 033
	cadena = cadena.replace("ί","ϊ")

	#Rule 034
	cadena = cadena.replace("iħ","ïħ")
	cadena = cadena.replace("igħ","ïgħ")
	cadena = cadena.replace("ih","ïh")
	cadena = cadena.replace("iq","ïq")

	#Rule 035
	cadena = cadena.replace("a","ɐ")

	#Rule 036
	cadena = cadena.replace("e","ɛ")

	#Rule 037
	cadena = cadena.replace("i","ɪ")

	#Rule 038
	cadena = cadena.replace("o","ɔ")

	#Rule 039
	cadena = cadena.replace("u","ʊ")

	#-----------------------------------------------------------------------------------#
	#Consonants

	#Rule 040
	cadena = cadena.replace("bċ","pċ")
	cadena = cadena.replace("bf","pf")
	cadena = cadena.replace("bħ","pħ")
	cadena = cadena.replace("bk","pk")
	cadena = cadena.replace("bp","pp") #--------------
	cadena = cadena.replace("bq","pq")
	cadena = cadena.replace("bs","ps")
	cadena = cadena.replace("bt","pt")
	cadena = cadena.replace("bx","px")
	cadena = cadena.replace("bz","pz")
	cadena = cadena.replace("b#","p#")

	#Rule 041
	#b = b

	#Rule 042
	cadena = cadena.replace("ċb","ʤb")
	cadena = cadena.replace("ċd","ʤd")
	cadena = cadena.replace("ċġ","ʤġ")
	cadena = cadena.replace("ċg","ʤg")
	cadena = cadena.replace("ċv","ʤv")
	cadena = cadena.replace("ċż","ʤż")

	#Rule 043
	cadena = cadena.replace("ċ","ʧ")

	#Rule 044

	cadena = ApplyRule_Vgraph(cadena,'dx','ʧx')
	cadena = ApplyRule_Vgraph(cadena,'ddx','ʧdx')
	cadena = ApplyRule_Vgraph(cadena,'dtx','ʧtx')

	#Rule 045

	cadena = ApplyRule_Vgraph(cadena,'ds','ʦs')
	cadena = ApplyRule_Vgraph(cadena,'dds','ʦds')

	#Rule 046
	cadena = cadena.replace("ndn","nnn")

	#Rule 047
	cadena = cadena.replace("dċ","tċ")
	cadena = cadena.replace("df","tf")
	cadena = cadena.replace("dħ","tħ")
	cadena = cadena.replace("dk","tk")
	cadena = cadena.replace("dp","tp")
	cadena = cadena.replace("dq","tq")
	cadena = cadena.replace("ds","ts")
	cadena = cadena.replace("dt","t") #--------------
	cadena = cadena.replace("dx","tx")
	cadena = cadena.replace("d#","t#")

	#Rule 048
	#d = d

	#Rule 049
	cadena = cadena.replace("fb","vb")
	cadena = cadena.replace("fd","vd")
	cadena = cadena.replace("fġ","vġ")
	cadena = cadena.replace("fg","vg")
	cadena = cadena.replace("fv","v") #--------------
	cadena = cadena.replace("fż","vż")

	#Rule 050
	#f = f

	#Rule 051
	
	cadena = ApplyRule_VgraphV(cadena,'għh','Hh') # see rule 66


	#Rule 052
	cadena = ApplyRule_VgraphV(cadena,'għ','')

	#Rule 053
	cadena = ApplyRule_CgraphV(cadena,'għ','')
	cadena = ApplyRule_VgraphC(cadena,'għ','')

	#Rule 054
	cadena = cadena.replace("#għ","#")

	#Rule 055
	cadena = cadena.replace("għ#","h#")

	#Rule 056
	cadena = cadena.replace("ġċ","ʧċ")
	cadena = cadena.replace("ġf","ʧf")
	cadena = cadena.replace("ġħ","ʧħ")
	cadena = cadena.replace("ġk","ʧk")
	cadena = cadena.replace("ġp","ʧp")
	cadena = cadena.replace("ġq","ʧq")
	cadena = cadena.replace("ġs","ʧs")
	cadena = cadena.replace("ġt","ʧt")
	cadena = cadena.replace("ġx","ʧx")
	cadena = cadena.replace("ġ#","ʧ#")

	#Rule 057
	cadena = cadena.replace("ġ","ʤ")

	#Rule 058
	cadena = cadena.replace("gċ","kċ")
	cadena = cadena.replace("gf","kf")
	cadena = cadena.replace("għ","kħ")
	cadena = cadena.replace("gk","kk")
	cadena = cadena.replace("gp","kp")
	cadena = cadena.replace("gq","kq")
	cadena = cadena.replace("gs","ks")
	cadena = cadena.replace("gt","kt")
	cadena = cadena.replace("gx","kx")
	cadena = cadena.replace("g#","k#")

	#Rule 059
	#g = g

	#Rule 060
	cadena = cadena.replace("#h","#")

	#Rule 061
	cadena = cadena.replace("h#","H#") #See rule 66

	#Rule 062
	cadena = ApplyRule_CgraphV(cadena,'h','')


	#Rule 063
	cadena = ApplyRule_graphV(cadena,'ih','ij')
	cadena = ApplyRule_graphV(cadena,'ïh','ïj')
	cadena = ApplyRule_graphV(cadena,'ίh','ίj')
	cadena = ApplyRule_graphV(cadena,'ϊh','ϊj')

	#Rule 064
	cadena = cadena.replace("ʊhί","ʊwί")
	cadena = cadena.replace("ʊhɐ","ʊwɐ")
	cadena = cadena.replace("ʊhɪ","ʊwɪ")
	cadena = cadena.replace("ʊhɔ","ʊwɔ")
	cadena = cadena.replace("ʊhʊ","ʊwʊ")

	cadena = cadena.replace("ʊhϊ","ʊwϊ")
	cadena = cadena.replace("ʊhä","ʊwä")
	cadena = cadena.replace("ʊhï","ʊwï")
	cadena = cadena.replace("ʊhö","ʊwö")
	cadena = cadena.replace("ʊhü","ʊwü")


	cadena = cadena.replace("ühί","ʊwί")
	cadena = cadena.replace("ühɐ","ʊwɐ")
	cadena = cadena.replace("ühɪ","ʊwɪ")
	cadena = cadena.replace("ühɔ","ʊwɔ")
	cadena = cadena.replace("ühʊ","ʊwʊ")

	cadena = cadena.replace("ühϊ","ʊwϊ")
	cadena = cadena.replace("ühä","ʊwä")
	cadena = cadena.replace("ühï","ʊwï")
	cadena = cadena.replace("ühö","ʊwö")
	cadena = cadena.replace("ühü","ʊwü")

	#Rule 065

	cadena = ApplyRule_VgraphV(cadena,'h','')

	#Rule 066
	cadena = cadena.replace("h","")
	cadena = cadena.replace("H","h") #This is not a rule

	#Rule 067
	cadena = cadena.replace("ħ","h")

	#Rule 068
	#j = j

	#Rule 069
	cadena = cadena.replace("kb","gb")
	cadena = cadena.replace("kd","gd")
	cadena = cadena.replace("kġ","gġ")
	cadena = cadena.replace("kg","gg") #--------------
	cadena = cadena.replace("kv","gv")
	cadena = cadena.replace("kż","gż")

	#Rule 070
	#k = k

	#Rule 071
	#l = l

	#Rule 072
	#m = m

	#Rule 073
	cadena = cadena.replace("nb","mb")
	cadena = cadena.replace("np","mp")

	#Rule 074
	cadena = cadena.replace("ɪnl","ɪll")
	cadena = cadena.replace("ϊnl","ϊll")

	#Rule 075
	cadena = cadena.replace("ɪnm","ɪmm")
	cadena = cadena.replace("ϊnm","ϊmm")

	#Rule 076
	cadena = cadena.replace("ɪnr","ɪrr")
	cadena = cadena.replace("ϊnr","ϊrr")

	#Rule 077
	#m = m

	#Rule 078
	cadena = cadena.replace("pb","bb") #--------------
	cadena = cadena.replace("pd","bd")
	cadena = cadena.replace("pġ","bġ")
	cadena = cadena.replace("pg","bg")
	cadena = cadena.replace("pv","bv")
	cadena = cadena.replace("pż","bż")

	#Rule 079
	#p = p

	#Rule 080
	cadena = cadena.replace("q","ʔ")

	#Rule 081
	#r = r

	#Rule 082
	cadena = ApplyRule_Vgraph(cadena,'ss-x','ssʃ')

	#Rule 083
	cadena = ApplyRule_Vgraph(cadena,'sx#','sʃ#')
	cadena = cadena.replace("ssx#","ssʃ#")

	#Rule 084
	cadena = cadena.replace("sb","Zb")
	cadena = cadena.replace("sd","Zd")
	cadena = cadena.replace("sġ","Zġ")

	cadena = cadena.replace("sʤ","Zʤ")
	cadena = cadena.replace("sg","Zg")
	cadena = cadena.replace("sv","Zv")
	cadena = cadena.replace("sż","Zż")



	#Rule 085
	#s = s

	#Rule 086
	cadena = cadena.replace("tb","db")
	cadena = cadena.replace("td","dd")
	cadena = cadena.replace("tġ","dġ")
	cadena = cadena.replace("tʤ","dʤ")
	cadena = cadena.replace("tg","dg")
	cadena = cadena.replace("tv","dv")
	cadena = cadena.replace("tż","dż")

	#Rule 087
	cadena = ApplyRule_Vgraph(cadena,'tx','ʧx')

	#Rule 088
	cadena = ApplyRule_Vgraph(cadena,'ts','ʦs')

	#Rule 089
	#t = t

	#Rule 090
	cadena = cadena.replace("vċ","fċ")
	cadena = cadena.replace("vf","ff")
	cadena = cadena.replace("vħ","fħ")
	cadena = cadena.replace("vk","fk")
	cadena = cadena.replace("vp","fp")
	cadena = cadena.replace("vq","fq")
	cadena = cadena.replace("vs","fs")
	cadena = cadena.replace("vt","ft")
	cadena = cadena.replace("vx","fx")
	cadena = cadena.replace("vz","fz")
	cadena = cadena.replace("v#","f#")

	#Rule 091
	#v = v

	#Rule 091
	#w = w

	#Rule 093
	cadena = cadena.replace("xb","ʒb")
	cadena = cadena.replace("xd","ʒd")
	cadena = cadena.replace("xġ","ʒġ")
	cadena = cadena.replace("xg","ʒg")

	#Rule 094
	cadena = ApplyRule_VgraphV(cadena,'x','ʒ')

	#Rule 095
	#cadena = cadena.replace("x","ʃ")
	cadena = cadena.replace("x","X")

	#Rule 096
	cadena = ApplyRule_VgraphV(cadena,'zz','ǳ ')

	#Rule 097
	cadena = cadena.replace("z","ʦ")

	#Rule 098
	cadena = ApplyRule_Vgraph(cadena,'żż-X','zsʃ') ## Trampa

	#Rule 100
	cadena = cadena.replace("żżx#","żzx#")
	cadena = cadena.replace("żżX#","żzX#")
	cadena = cadena.replace("żż-","żz-")

	#Rule 101
	cadena = cadena.replace("żċ","sċ")
	cadena = cadena.replace("żf","sf")
	cadena = cadena.replace("żħ","sħ")
	cadena = cadena.replace("żk","sk")
	cadena = cadena.replace("żp","sp")
	cadena = cadena.replace("żq","sq")
	cadena = cadena.replace("żs","ss")
	cadena = cadena.replace("żt","st")
	cadena = cadena.replace("żx","sx")
	cadena = cadena.replace("żX","sX")
	cadena = cadena.replace("ż#","s#")

	#Rule 102
	cadena = cadena.replace("ż","z")

	#-----------------------------------------------------------------------------------#
	#Accented vowels
	
	#Rule 103
	#à = à

	#Rule 104
	#è = è

	#Rule 105
	#ì = ì

	#Rule 106
	#ò = ò

	#Rule 107
	#ù = ù

	#-----------------------------------------------------------------------------------#
	#Last transformations
	cadena = cadena.replace("#"," ")
	cadena = cadena.strip()
	cadena = cadena.replace("-","")
	cadena = cadena.replace("\'","")

	cadena = cadena.replace("Z","z")
	cadena = cadena.replace("X","ʃ")

	cadena = cadena.replace("ä","ɐː")
	cadena = cadena.replace("ë","ɛː")
	cadena = cadena.replace("ï","iː")
	cadena = cadena.replace("ί","ɪː")
	cadena = cadena.replace("ϊ","ɪː")
	cadena = cadena.replace("ö","ɔː")
	cadena = cadena.replace("ü","ʊː")

	#Fair substitutions
	cadena = cadena.replace("ʦ","ts")
	#cadena = cadena.replace("ʧ","tʃ")
	cadena = cadena.replace("ǳ ","dz")

	#Returning the resulting transcription
	return cadena

#ENDDEF
#############################################################################################
#############################################################################################

