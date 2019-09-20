import numpy as np
from ..constants import constants

"""
    'update_signals': {
        'policies': {
            'new_B': decide_new_B,
        },
        'variables': {
            'B': record_B,
            'lambda_S': update_lambda_S,
            'lambda_D': update_lambda_D,
            'KPI_prev': record_KPI_prev,
            'KPI': update_KPI,
        }
    }
"""

"""
User Policies
"""
def decide_new_B(_g, step, sL, s):
    new_B = s['B'] * constants['decay_rate'] if s['W'] > 0.1 else 0
    return {'new_B': new_B}

"""
State Updates
"""
def record_B(_g, step, sL, s, _input):
    return ('B', _input['new_B'])

def update_lambda_S(_g, step, sL, s, _input):
    # scale_factor = max(min(s['R'] / s['R_prev'], 1.6), 0.75)
    scale_factor = s['R'] / s['R_prev']
    return ('lambda_S', s['lambda_S'] * scale_factor)

def update_lambda_D(_g, step, sL, s, _input):
    scale_factor = s['P_prev'] / s['P']
    scaled_lambda_D = s['lambda_D'] * scale_factor
    return ('lambda_D', scaled_lambda_D)
