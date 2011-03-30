#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
Si collega alla pagina del centro maree di Venezia e vede se ci sarà acqua alta
"""

import sys
import datetime
import time
import locale
from strutturadati import clsMarea
import connessione
#import twitter
#import shutil
#import os
#import time
#import math
#from array import array

class clsAcquaAlta(object):

	_SOGLIA_PERICOLO = 105 # 105cm
	_TAG_PERICOLO = "[ATTENZIONE]"
	
	_objURL = None
	_cBuffer = None
	_aLista = None
	_dDataOdierna = None

	def __init__(self):
		isinstance(self._dDataOdierna, datetime.datetime)

		""" Costruttore della classe """

		# Imposta il locale sulla lingua italiana
		locale.setlocale(locale.LC_ALL, 'it_IT')

		self._dDataOdierna = datetime.datetime.today()
		#try:
		self._objURL = connessione.clsConnessione()
		self._aLista = self._objURL.cercaValori()
		#except Exception:
		#	sys.exit(-1)

	def __getValori(self, P_lValoriMassimi, P_nGiornoDiPartenza = 0, P_nRisultati = 2):
		""" Restituisce i prossimi valori massimi o minimi di marea """
		
		objRiga = clsMarea()
		objRisultati = []
		isinstance(objRisultati, clsMarea)
		
		cOutput = ""
		nConto = 0
		dDataCercata = datetime.datetime.combine(datetime.date.today(), datetime.time(0, 0, 0))
		if (P_nGiornoDiPartenza > 0): dDataCercata += datetime.timedelta(days=P_nGiornoDiPartenza)

		lGiaScritto = False
		for objRiga in self._aLista:                
			if ((objRiga.massimo == P_lValoriMassimi) 
			    and (objRiga.data >= dDataCercata)
			    and (nConto < P_nRisultati)):
				objRisultati.append(objRiga)
				nConto += 1
		return objRisultati

	def __getValoriMassimi(self, P_nGiornoDiPartenza = 0, P_nRisultati = 2):
		""" Restituisce i prossimi massimi di marea """		
		return self.__getValori(True, P_nGiornoDiPartenza, P_nRisultati)
		
	def __getValoriMinimi(self, P_nGiornoDiPartenza = 0, P_nRisultati = 2):
		""" Restituisce i prossimi minimi di marea """
		return self.__getValori(False, P_nGiornoDiPartenza, P_nRisultati)

	def getPrevisioneOggi(self):
		""" Esegue una previsione """
		
		#cFirma = "[AquaBot]"
		aLista = self.__getValoriMassimi()
		isinstance(aLista, clsMarea)

		cOutput = ""
		
		if (len(aLista) > 1): 
			if ((aLista[0].valore >= self._SOGLIA_PERICOLO) or 
			    (aLista[1].valore >= self._SOGLIA_PERICOLO)): cOutput += self._TAG_PERICOLO + " "
			cOutput += "I prossimi massimi di marea sono previsti "
			cGiorno1 = aLista[0].getGiorno()
			cGiorno2 = aLista[0].getGiorno()
			cOutput += "{1} alle {0} a {2}cm e {4}alle {3} a {5}cm.".format(
			     aLista[0].data.strftime("%H:%M"),
			     cGiorno1, 
			     aLista[0].valore,
			     aLista[1].data.strftime("%H:%M"),
			     cGiorno2 + " " if(cGiorno1 != cGiorno2) else "", 
			     aLista[1].valore)
		else: 
			if (aLista[0].valore >= self._SOGLIA_PERICOLO): cOutput += self._TAG_PERICOLO + " "
			cOutput += "Il prossimo massimo di marea e' previsto "
			cOutput += "alle {0} {1} a {2}cm.".format(
			     aLista[0].data.strftime("%d %B"),
			     aLista[0].getGiorno(), 
			     aLista[0].valore)			     

		return cOutput

	def getPrevisioneDomani(self):
		""" Esegue una previsione per domani """

		"""cFirma = "[AquaBot]"
		cOutput = "Domani " + self.__getProssimoMassimo(1)
		if (cOutput != ""): 
			cOutput += " " + self.__getProssimoMinimo(1)
			if ((len(cOutput) + len(cFirma) + 1) < 140):
				cOutput += " " + cFirma
		return cOutput"""

	def __str__(self):
		""" Scrive l'elenco completo delle maree previsto dal centro 
		(override della funzione __str__ standard) """

		cOutput = ""
		objMarea = clsMarea()
		
		for objMarea in self._aLista:
			""" Visualizza la linea solo se la previsione si riferisce
			ad una data non passata """
			if (objMarea.data >= self._dDataOdierna):
				cMaxMin = "massimo" if (objMarea.massimo) else "minimo"
				cOutput += "Il {0} e' previsto un {1:7} di {2:-3}cm alle {3}\n".format(
				     objMarea.data.strftime("%d %B"),
				     cMaxMin,
				     objMarea.valore,
				     objMarea.data.strftime("%H:%M"))
		return cOutput