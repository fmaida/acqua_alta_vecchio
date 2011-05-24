#!/usr/bin/python
# -*- coding: UTF-8 -*-

import datetime

class clsMarea(object):
    """
    Classe che gestisce la struttura dei dati sulle maree
    """

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
        """
        Restituisce il valore della marea espresso in centimetri
        @param self: Riferimento all'istanza della classe
        @return: Restituisce un valore intero con l'altezza in centimetri della marea
        """
        return self._nValore

    def setValore(self, P_nValore):
        self._nValore = P_nValore

    valore = property(getValore, setValore, None, "Valore della marea in cm")

    def getMassimo(self):
        """
        Restituisce se il valore è un massimo di marea (True) oppure no
        @param self: Riferimento all'istanza della classe
        @return: Restituisce un booleano per indicare se il valore è un massimo di marea
        """
        return self._lMassimo

    def setMassimo(self, P_lAssegnaMassimo):
        self._lMassimo = P_lAssegnaMassimo

    massimo = property(getMassimo, setMassimo, None, "Indica se il valore è un massimo o no")

    def getGiorno(self, P_lIncludiArticolo=False):
        """
        Restituisce l'indicazione sul giorno indicato
        @param P_lIncludiArticolo:  Indica se includere nel testo l'uso dell'articolo (di, del, ...)
                                    quando si riferisce ad una data
        @return Una stringa contenente una data valida oppure l'indicazione se accadrà oggi o domani
        """
        
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