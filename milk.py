# -*- coding: utf-8 -*-
"""
Created on Sun Feb 11 13:39:33 2018

@author: jpmul
"""

from iapws import IAPWS95, IAPWS97

def rho_bf(t):
    sg = 0.96666 - 0.001334 * t
    return sg

def rho_snf(t):
    sg = 1.635 - 0.0026 * t + 0.00002 * t**2.0
    return sg
    
def rho_water95(t):
    sg = IAPWS95(T=t + 273.15, P=0.101325).rho / 1000.0
    return sg

def rho_water97(t):
    sg = IAPWS97(T=t + 273.15, P=0.101325).rho / 1000.0
    return sg

def rho_milk(xsnf, xbf, t):
    

    xwater = 1.0 - xsnf - xbf
    
    xsnf, xbf, xwater = (xsnf*100.0, xbf*100.0, xwater*100.0)
    
    snf = rho_snf(t)
    bf = rho_bf(t)
    water = rho_water95(t)
    
    rho = 100.0 / ( xsnf/snf + xbf/bf + xwater/water )
    
    return rho
    
t = 4
bf = 0.055
snf = 0.150 - bf

print(t, rho_milk(snf, bf, t))
    
t = 4.4444444444
bf = 0.03928
snf = 0.39221

print(t, rho_milk(snf, bf, t), rho_milk(snf, bf, t)*8.34)
    
print(rho_bf(4.4444444))  



    