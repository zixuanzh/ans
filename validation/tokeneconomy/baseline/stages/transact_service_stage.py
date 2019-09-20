import numpy as np
import pandas as pd
from ..constants import constants

"""
    'transact_service': {
        'policies': {
            'new_P': decide_new_P,
            'new_Q': decide_new_Q,
            'new_U': decide_new_U,
        },
        'variables': {
            'P_prev': record_P_prev,
            'P': record_P,
            'Q': record_Q,
            'U': record_U,
            'C': update_C,
        }
    },
"""

"""
User Policies
"""
def decide_new_P(_g, step, sL, s):
    return {'new_P': s['D']/s['S']}

def decide_new_Q(_g, step, sL, s):
    return {'new_Q': min(s['D'], s['S'])}



def compute_supply_reduction(s):
    # upcoming Bs in the next 6 months
    upcoming_Bs = [s['B'] * (constants['decay_rate']**x) for x in range(0, 25)]
    Bdiff = [(upcoming_Bs[i-1] - upcoming_Bs[i]) / upcoming_Bs[i-1] for i in range(1, len(upcoming_Bs)) ]
    Bema = max(pd.ewma(np.array(Bdiff), span=len(Bdiff)))
    return Bema

# speculative value
def decide_new_U(_g, step, sL, s):
    sign = 1 if np.random.rand() > 0.45 else -1
    delta = s['U'] * np.random.uniform(high=0.1) * sign + (np.random.uniform(high=compute_supply_reduction(s)) * s['U'])
    new_U = s['U'] + delta 
    compute_supply_reduction(s)
    return {'new_U': constants['momentum_U'] * new_U\
            + (1 - constants['momentum_U']) * s['U']}
"""
State Updates
"""
def record_P_prev(_g, step, sL, s, _input):
    P_prev = s['P'] if s['P'] else _input['new_P']
    return ('P_prev', P_prev)

def record_P(_g, step, sL, s, _input):
    return ('P', max(0.0001, _input['new_P']))

def record_Q_prev(_g, step, sL, s, _input):
    return ('Q_prev', s['Q'])

def record_Q(_g, step, sL, s, _input):
    return ('Q', _input['new_Q'])

def record_U_prev(_g, step, sL, s, _input):
    return ('U_prev', s['U'])

def record_U(_g, step, sL, s, _input):
    return ('U', _input['new_U'])

def update_C(_g, step, sL, s, _input):
    new_C = (1 + np.random.normal(0, 0.1)) * s['C']
    return ('C', constants['alpha_C'] * s['C']\
            + (1 - constants['alpha_C'] * new_C))
