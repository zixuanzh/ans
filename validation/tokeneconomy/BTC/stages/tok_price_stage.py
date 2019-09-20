from ..constants import constants

"""
    'K_price': {
        'policies': {
            'new_K': decide_new_K,
        },
        'variables': {
            'K_prev': record_K_prev,
            'K': record_K,
            'R': update_R,
        }
    },
"""
"""
User Policies
"""
def decide_new_K(_g, step, sL, s):
    return {'new_K': constants['gamma_K'] * (1.0 / s['V'])\
			+ (1 - constants['gamma_K']) * s['U']} 

"""
State Updates
"""
def record_K_prev(_g, step, sL, s, _input):
	return ('K_prev', s['K'])

def record_K_delta(_g, step, sL, s, _input):
    return ('K_delta', _input['new_K'] / s['K'])

def record_K(_g, step, sL, s, _input):
    return ('K', _input['new_K'])

def record_R_prev(_g, step, sL, s, _input):
    R_prev = s['R'] if s['R'] else _input['new_K'] * s['V']
    return ('R_prev', R_prev)

def update_R(_g, step, sL, s, _input):
    return ('R', _input['new_K'] * s['V'])
