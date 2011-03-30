import sys
#from acquaalta import clsAcquaAlta
from acquaalta import clsAcquaAlta

if (__name__ == "__main__"):
	objAcqua = clsAcquaAlta()
	cPrevisione = objAcqua.getPrevisioneOggi()
	if (cPrevisione != ""): print(cPrevisione)
	#cPrevisione = objAcqua.getPrevisioneDomani()
	#if (cPrevisione != ""): print("\n" + cPrevisione)
	print("\n\n")    
	print(objAcqua)