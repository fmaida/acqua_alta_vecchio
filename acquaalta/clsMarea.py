#!/usr/bin/python
# -*- coding: UTF-8 -*-

import datetime


class clsMarea(object):

	def __init__(self):
		self._dOggi = datetime.datetime.today()
		self._dData = None
		self._nValore = None
		self._lMassimo = None

	def getData(self):
		return self._dData
	def setData(self, P_dData):
		self._dData = P_dData
	data = property(getData, setData, None, "Data ed ora della marea")

	def getValore(self):
		return self._nValore
	def setValore(self, P_nValore):
		self._nValore = P_nValore
	valore = property(getValore, setValore, None, "Valore della marea in cm")

	def getMassimo(self):
		return self._lMassimo
	def setMassimo(self, P_lAssegnaMassimo):
		self._lMassimo = P_lAssegnaMassimo
	massimo = property(getMassimo, setMassimo, None, "Indica se il valore è un massimo o no")

	def getGiorno(self, P_lIncludiArticolo = False):
		#isinstance(P_dData, datetime.datetime)
		#isinstance(self._dDataOdierna, datetime.datetime)

		""" Restituisce l'indicazione sul giorno indicato

		Keyword arguments:
		P_dData -- Data indicata

		Returns:
		Una stringa contenente una data valida oppure l'indicazione se 
		accadrà oggi o domani"""

		cData = ""
		try:
			# Se la data è oggi
			if (self.data.date() == self._dOggi.date()):
				if (P_lIncludiArticolo): cData += "di "
				cData += "oggi"
			elif (self.data.date() == (self._dOggi.date() + datetime.timedelta(days=1))):
				if (P_lIncludiArticolo): cData += "di "                
				cData += "domani"                
			else:
				if (P_lIncludiArticolo): cData += "del "
				cData += P_dData.strftime("%d %B")
		except Exception:
			if (P_lIncludiArticolo): cData += "di "
			cData = "un giorno indefinito"
		return cData
	giorno = property(getGiorno)