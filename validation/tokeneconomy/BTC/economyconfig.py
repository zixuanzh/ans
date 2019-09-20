import math
from decimal import Decimal
from datetime import timedelta
import numpy as np
from typing import Dict, List

from cadCAD.configuration import append_configs
from cadCAD.configuration.utils import bound_norm_random, ep_time_step, config_sim
from .constants import constants
from .initial_values import initial_values
from .genesis_states import genesis_states
from .partial_state_update_block import partial_state_update_block

# dummy for parameter sweep
g: Dict[str, List[int]] = {
    'alpha': [1],
}

sim_config = {
    'N': 100,
    # 'N': 1,
    'T': range(1040),
    'M': g,
}

seeds = {
    'p': np.random.RandomState(26042019),
}
env_processes = {}

"""
Exogenous Processes
update price, timestamp, block
"""
ts_format = '%Y-%m-%d %H:%M:%S'
t_delta = timedelta(days=7, minutes=0, seconds=0)

def time_model(_g, step, sL, s, _input):
    x = ep_time_step(s, dt_str=s['timestamp'], fromat_str=ts_format, _timedelta=t_delta)
    return ('timestamp', x)

raw_exogenous_states = {
    'timestamp': time_model
}

env_processes = {}

append_configs(
    sim_configs=sim_config,
    initial_state=genesis_states,
    seeds=seeds,
    raw_exogenous_states=raw_exogenous_states,
    env_processes=env_processes,
    partial_state_update_blocks=partial_state_update_block
)
