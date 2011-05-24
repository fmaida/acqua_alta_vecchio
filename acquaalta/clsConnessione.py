#!/usr/bin/python
# -*- coding: UTF-8 -*-

import urllib2
import string
import datetime
import time
from clsMarea import clsMarea

class clsConnessione(object):
	
	""" Questa variabile indica l'indirizzo URL a cui collegarsi """
	_cURL = "http://www.comune.venezia.it/flex/cm/pages/ServeBLOB.php/L/IT/IDPagina/1748"	
	_cBuffer = None
	
	def __init__(self, P_cURL = None):
		if (P_cURL != None): self._cURL = P_cURL
		self._cBuffer = ""
		self.__apriURL()

	def __apriURL(self):
		""" Apre un'URL """

		try:
			filehandle = urllib2.urlopen(self._cURL)
			self._cBuffer = ""
			lCopia = False
			for cLinea in filehandle.readlines():
				if (string.find(cLinea, "<tbody") >= 0):
					lCopia = True
				if (lCopia):
					self._cBuffer += cLinea
					if (string.find(cLinea, "</tbody") >= 0):
						lCopia = False
						filehandle.close()
			
		except Exception:
			raise("Impossibile collegarsi al centro maree.")

	def __cercaTag(self, P_cTag, P_nPartenza = 0):
		""" Cerca il contenuto fra un tag di apertura e uno di chiusura
		returns: Una tupla con indice e valore trovati
		"""

		cOutput = ""
		nPos3 = -1
		nPos1 = string.find(self._cBuffer, "<" + P_cTag, P_nPartenza)
		if (nPos1 >= 0):
			nPos2 = string.find(self._cBuffer, ">", nPos1 + 1)
			nPos3 = string.find(self._cBuffer, "</" + P_cTag, nPos2 + 1)
			if (nPos3 >= 0):
				cOutput = self._cBuffer[nPos2 + 1:nPos3]
				return {"posizione": nPos3, "contenuto": cOutput}
	
	def cercaValori(self):
		""" Cerca le indicazioni delle maree nel file HTML 
		e restituisce una lista di istanze clsMarea """

		aLista = []
		nPos = 0
		objTrovato = self.__cercaTag("th", nPos)
		while(objTrovato != None):
			objRiga = clsMarea()
			"""            
			Cerca la data
			"""
			cFormatoData = "%d/%m/%Y %H:%M"
			dData = datetime.datetime.fromtimestamp(time.mktime(time.strptime(objTrovato["contenuto"], cFormatoData)))
			objRiga.data = dData
			nPos = objTrovato["posizione"] + 1
			# Cerca se è un massimo o minimo
			objTrovato = self.__cercaTag("td", nPos)
			if(objTrovato["posizione"] >= 0): 
				if (objTrovato["contenuto"] == "massimo"): 
					objRiga.massimo = True
				else:
					objRiga.massimo = False
				nPos = objTrovato["posizione"] + 1
			else:
				objRiga.massimo = False
			# Cerca quant'è il valore
			objTrovato = self.__cercaTag("td", nPos)
			if(objTrovato["posizione"] >= 0): 
				try:
					objRiga.valore = int(objTrovato["contenuto"])
				except Exception:
					objRiga.valore = 0
				nPos = objTrovato["posizione"] + 1
			else:
				objRiga.valore = 0
			aLista.append(objRiga)
			# Passa al successivo
			nPos = objTrovato["posizione"] + 1
			objTrovato = self.__cercaTag("th", nPos)
			
		return aLista