import sys
from acquaalta.clsAcquaAlta import clsAcquaAlta

if (__name__ == "__main__"):
	objAcqua = clsAcquaAlta()
	cPrevisione = objAcqua.getPrevisioneOggi()
	if (cPrevisione != ""): print(cPrevisione)
	#cPrevisione = objAcqua.getPrevisioneDomani()
	#if (cPrevisione != ""): print("\n" + cPrevisione)
	print
	print(objAcqua)