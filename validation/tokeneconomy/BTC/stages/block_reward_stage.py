
import numpy as np
from ..constants import constants

"""
    'block_reward': {
        'policies': {
        },
        'variables': {
            'V': update_V,
            'M': update_M,
            'W': update_W,
        }
    },
"""

"""
User Policies
"""

"""
State Updates
"""
def update_V(_g, step, sL, s, _input):
    revenue = s['P'] * s['Q'] + s['B']
    cost = max(1, s['C'] * s['Q'])
    return ('V', revenue / cost)

def update_M(_g, step, sL, s, _input):
    return ('M', s['M'] + s['B'])

def update_W(_g, step, sL, s, _input):
    return ('W', s['W'] - s['B'])
