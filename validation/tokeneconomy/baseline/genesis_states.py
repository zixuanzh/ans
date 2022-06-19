from .initial_values import initial_values

genesis_states = {
    # initial states of the economy
    'D': float(10000),
    'S': float(10000),
    'P': float(0),
    'P_prev': float(0),
    'Q': float(0),
    'Q_prev': float(0),
    'U': float(1),
    'U_prev': float(1),
    'C': float(1),
    'B': initial_values['B'],
    'V': float(0),
    'R': float(0),
    'R_prev': float(0),
    'M': initial_values['B'],
    'W': initial_values['W'],
    'K': initial_values['K'],
    'K_prev': initial_values['K'],
    # decision variables
    'delta_D': float(0),
    'delta_S': float(0),

    # signals for decisions
    'lambda_D': initial_values['lambda_D'],
    'lambda_S': initial_values['lambda_S'],
    'timestamp': '2019-01-01 00:00:00',
}
