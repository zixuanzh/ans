import numpy as np
from ..constants import constants

"""    
    'offer_service': {
        'policies': {
            'new_delta_D': decide_new_delta_D,
            'new_delta_S': decide_new_delta_S,
        },
        'variables': {
            'delta_D': record_delta_D,
            'delta_S': record_delta_S,
            'D': update_D,
            'S': update_S,
        }
    },
"""

"""
User Policies
"""
def decide_new_delta_D(_g, step, sL, s):
    new_delta_D = np.random.poisson(s['lambda_D'])
    return {'new_delta_D': new_delta_D}

def decide_new_delta_S(_g, step, sL, s):
    new_delta_S = np.random.poisson(s['lambda_S'])
    return {'new_delta_S': new_delta_S}

"""
State Updates
"""

def record_delta_D(_g, step, sL, s, _input):
    return ('delta_D', _input['new_delta_D'])

def record_delta_S(_g, step, sL, s, _input):
    return ('delta_S', _input['new_delta_S'])

def update_D(_g, step, sL, s, _input):
    return ('D', s['D'] + _input['new_delta_D'] - constants['departure_D'])

def update_S(_g, step, sL, s, _input):
    return ('S', s['S'] + _input['new_delta_S'] - constants['departure_S'])