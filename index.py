# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 12:24:59 2021

@author: Rodrigo
"""

import re
import pandas as pd
import capturando_tickers as tk

busca = tk.busca_filtrada()

fundamentus = busca

fundamentus = tk.remover_papeis_repetidos(fundamentus)


fundamentus = fundamentus.sort_values(by="EV/EBIT", ascending=True)
fundamentus = fundamentus.reset_index(drop=True)

lista = tk.remover_seguradoras_e_rj(fundamentus)



