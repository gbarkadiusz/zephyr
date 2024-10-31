# Copyright: (c)  2024, Intel Corporation 
# Author: Arkadiusz Cholewinski <arkadiuszx.cholewinski@intel.com>
# MIT License, see (https://opensource.org/license/mit/)

class PowerShieldData:
    
    def __init__(self):
        self.data = []
        self.current_RMS = None
        self.power = None