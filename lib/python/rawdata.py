#!/usr/lib/env python

import sys
from filterbank import FilterbankFile
from psrfits import PsrfitsFile

def initialize_rawdata(fn):
    if fn.endswith(".fil"):
        class RawData(FilterbankFile):
            def __init__(self, fin):
                self.fin=fin
                self.datatype="filterbank"
                self.N=0
                FilterbankFile.__init__(self, fin)
                self.N=self.nspec

    elif fn.endswith(".fits"):
        class RawData(PsrfitsFile):
            def __init__(self, fin):
                self.fin=fin
                self.datatype="psrfits"
                PsrfitsFile.__init__(self, fin)
                #Pull values out of subclass
                self.df=self.specinfo.df
                self.N=self.specinfo.N

    return RawData(fn)
