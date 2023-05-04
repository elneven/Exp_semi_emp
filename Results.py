# -*- coding: utf-8 -*-
"""
Created on Thu May  4 11:14:12 2023

@author: elise
"""

from Model_Exp import Param
from Model_Exp import Inputs
from Model_Exp import Expander

"Initialize the model"

"Paramètres"
V_s = 0.0000863 #[m^3/rev]
rv_in = 2.3
m_dot_n = 0.26
N_n = 2000/60


AU_su_n = 1 #GUESSSS
A_leak=5E-7 #GUESSSS
AU_ex_n = 1 #-> GUESSSS
W_dot_loss_n = 1000
alpha_loss = 0.3
AU_amb = 24 #GUESSS
T_amb = 25 #GUESSS


params = Param(rv_in, V_s, m_dot_n, N_n, AU_su_n, A_leak, AU_ex_n, W_dot_loss_n, alpha_loss, AU_amb, T_amb)


"Inputs"
P_su_bar = 5.79 #[bar]
rp = 2.85
N_exp = 1350.9 
T_su_C = 76.85 #[°C]
Fluid = 'R1233zdE'

In = Inputs(P_su_bar, rp, N_exp, T_su_C, Fluid)


out = Expander(params, In)
out.solveSys()
