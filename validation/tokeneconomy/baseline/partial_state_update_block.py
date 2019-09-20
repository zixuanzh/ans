from .stages.offer_service_stage import *
from .stages.transact_service_stage import *
from .stages.block_reward_stage import *
from .stages.tok_price_stage import *
from .stages.update_signals_stage import *

partial_state_update_block = {
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
    'transact_service': {
        'policies': {
            'new_P': decide_new_P,
            'new_Q': decide_new_Q,
            'new_U': decide_new_U,
        },
        'variables': {
            'P_prev': record_P_prev,
            'P': record_P,
            'Q_prev': record_Q_prev,
            'Q': record_Q,
            'U_prev': record_U_prev,
            'U': record_U,
            'C': update_C,
        }
    },
    'block_reward': {
        'policies': {},
        'variables': {
            'V': update_V,
            'M': update_M,
            'W': update_W,
        }
    },
    'tok_price': {
        'policies': {
            'new_K': decide_new_K,
        },
        'variables': {
            'K_prev': record_K_prev,
            'K': record_K,
            'R_prev': record_R_prev,
            'R': update_R,
        }
    },
    'update_signals': {
        'policies': {
            'new_B': decide_new_B,
        },
        'variables': {
            'B': record_B,
            'lambda_S': update_lambda_S,
            'lambda_D': update_lambda_D,
        }
    }
}