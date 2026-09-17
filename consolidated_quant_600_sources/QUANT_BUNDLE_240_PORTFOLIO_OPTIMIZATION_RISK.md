# ⚡ [QUANT-SOURCE-240] Consolidated Quant & Algo Trading Repositories
**Category**: `PORTFOLIO_OPTIMIZATION_RISK` | **Repositories in this Source**: 3
**Generated**: QUANT_BUNDLE_240_PORTFOLIO_OPTIMIZATION_RISK.md | **Target**: NotebookLM 290+ Quant Code Brain

---

## [1/3] Repository: portfolio-optimization (`PHASE4-QUANT-175`)
- **Full Name**: `PHASE4-QUANT-175_kvsnoufal__portfolio-optimization`
- **Description**: A python application, that demonstrates optimizing a portfolio using machine learning.
- **GitHub Stars**: 108
- **Source Pool**: `phase4_quant_wheels_100`

### Documentation & Overview (README.md)
# Portfolio Optimization using Reinforcement Learning
Experimenting with RL for building optimal portfolio of 3 stocks and comparing it with portfolio theory based Markowitz' approach



Pls checkout the [medium article](https://medium.com/@noufalsamsudin/portfolio-optimization-using-reinforcement-learning-1b5eba5db072) for a quick overview.


To train RL model:
```
python train.py
```

To download data: 
1. https://www.mediafire.com/file/xivks3xf64b83ph/cleaned_preprocessed.csv/file
2. https://www.mediafire.com/file/g05yja1uiilhfuu/cleaned.csv/file

Take a look at pre_process.py if you want to get an idea on how this file was cleaned and compiled.


## Problem Statement

I will be formulating this as a portfolio optimization problem : 
Given histories of 3 different stocks, how would we allocate a fixed amount of money between these stocks every day so that maximize the likelihood of returns. 

The objective is to develop of policy (strategy) for building a portfolio. The portfolio is essentially an allocation of available resources across various stocks. The policy then needs to restructure the portfolio over time as new information becomes available.


![Pic of Model](https://github.com/kvsnoufal/portfolio-optimization/blob/main/img/po_model.png)


## RL agent training

![Pic of training](https://github.com/kvsnoufal/portfolio-optimization/blob/main/img/training.png)

## Results


![Pic of results](https://github.com/kvsnoufal/portfolio-optimization/blob/main/img/compare.png)

### Core Implementation Code & Architecture
#### File: `policies.py`
```python
class MarkowitzPolicy:
    def __init__(self):
        self.portfolios = self.init_portfolios()

    def get_action(self,memory):
        df1 = memory.copy().reset_index(drop=True).tail(30)
        for i,row in df1.iterrows():
            for i2,row2 in self.portfolios.iterrows():
                df1.loc[i,f"p{i2} value"] = np.dot(row,row2)
        for i in range(NPORTS):
            df1[f"p{i} return"] = df1[f"p{i} value"].diff()
        
        df2 = df1.agg(["mean","std"])[[f"p{i} return" for i in range(NPORTS)]].T
        df2.loc[df2["std"].isnull(),"std"]=1e-8
        df2["sharpe"] = df2["mean"]/df2["std"]
        
        
        max_ = df2.sort_values("std").head(df2.shape[0]//4)["mean"].max()
        
        max_ = df2[df2["mean"]==max_].index[0].strip("p").strip(" return")
        max_ = int(max_)
        action = self.portfolios.loc[max_,:].values/100
        action = np.hstack((0,action))
        return action

    def init_portfolios(self):
        if FIXED_PORTFOLIO:
            ps = pd.read_csv("portfolios_sample.csv")
        else:
            portfolios = []
            for i in range(NPORTS):
                num1 = np.random.randint(100)
                num2 = np.random.randint(100-num1)
                num3 = 100-num1-num2
                portfolios.append([num1,num2,num3])

            ps = pd.DataFrame(portfolios,columns=COINS)
            # ps.to_csv("portfolios_sample.csv",index=None)
        return ps
```

#### File: `pre_process.py`
```python
import pandas as pd
FILE = "cleaned.csv"
COINS = ["DASH","LTC","STR"]
COLS = ['high', 'low', 'open', 'close', 'volume', 'quoteVolume','weightedAverage']
SCOLS = ["vh","vl","vc","open_s","volume_s","quoteVolume_s","weightedAverage_s"]
OBS_COLS = ['vh', 'vl', 'vc', 'open_s', 'volume_s', 'quoteVolume_s', 'weightedAverage_s', 'vh_roll_7', 'vh_roll_14', 'vh_roll_30', 'vl_roll_7', 'vl_roll_14', 'vl_roll_30', 'vc_roll_7', 'vc_roll_14', 'vc_roll_30', 'open_s_roll_7', 'open_s_roll_14', 'open_s_roll_30', 'volume_s_roll_7', 'volume_s_roll_14', 'volume_s_roll_30', 'quoteVolume_s_roll_7', 'quoteVolume_s_roll_14', 'quoteVolume_s_roll_30', 'weightedAverage_s_roll_7', 'weightedAverage_s_roll_14', 'weightedAverage_s_roll_30']
EPISODE_LENGTH = 500


df = pd.read_csv(FILE)

        
df["date"] = df["date"].apply(lambda x: pd.Timestamp(x, unit='s', tz='US/Pacific'))
df = df[df["coin"].isin(COINS)].sort_values("date")
df["vh"] = df["high"]/df["open"]
df["vl"] = df["low"]/df["open"]
df["vc"] = df["close"]/df["open"]
df["open_s"] = df.groupby("coin")["open"].apply(lambda x: x - x.shift(1))
df["volume_s"] = df.groupby("coin")["volume"].apply(lambda x: x - x.shift(1))
df["quoteVolume_s"] = df.groupby("coin")["quoteVolume"].apply(lambda x: x - x.shift(1))
df["weightedAverage_s"] = df.groupby("coin")["weightedAverage"].apply(lambda x: x - x.shift(1))

new_cols = []

for col in SCOLS:
    print(col)
    df[col+"_roll_7"] = df.groupby("coin")[col].apply(lambda x: x.rolling(7).mean().bfill())
    new_cols.append(col+"_roll_7")
    df[col+"_roll_14"] = df.groupby("coin")[col].apply(lambda x: x.rolling(14).mean().bfill())
    new_cols.append(col+"_roll_14")
    df[col+"_roll_30"] = df.groupby("coin")[col].apply(lambda x: x.rolling(30).mean().bfill())
    new_cols.append(col+"_roll_30")
    
SCOLS.extend(new_cols)
print(SCOLS)

df.to_csv("cleaned_preprocessed.csv")
```

#### File: `utils.py`
```python
import tensorflow as tf
import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt
from sklearn import preprocessing
from tqdm import tqdm
from tf_agents.environments import py_environment
from tf_agents.environments import tf_environment
from tf_agents.environments import tf_py_environment
from tf_agents.environments import utils
from tf_agents.specs import array_spec
from tf_agents.environments import wrappers
from tf_agents.environments import suite_gym
from tf_agents.trajectories import time_step as ts
from tf_agents.policies.policy_saver import PolicySaver
from tf_agents.agents.ddpg import actor_network
# import actor_network
from tf_agents.agents.ddpg import critic_network
from tf_agents.agents.ddpg import ddpg_agent

from tf_agents.agents.dqn import dqn_agent
from tf_agents.drivers import dynamic_step_driver
from tf_agents.environments import suite_gym
from tf_agents.environments import tf_py_environment
from tf_agents.eval import metric_utils
from tf_agents.metrics import tf_metrics
from tf_agents.networks import q_network
from tf_agents.policies import random_tf_policy
from tf_agents.replay_buffers import tf_uniform_replay_buffer
from tf_agents.trajectories import trajectory
from tf_agents.trajectories import policy_step
from tf_agents.utils import common
import logging

def compute_avg_return(environment, policy, num_episodes=10):
            
        total_return = 0.0
        for _ in range(num_episodes):

            time_step = environment.reset()
            episode_return = 0.0
            counter = 0
            while not time_step.is_last():
                action_step = policy.action(time_step)
                time_step = environment.step(action_step.action)
                episode_return += time_step.reward
                
                counter+=1
            total_return += episode_return
            # print("total reward",total_return)
        avg_return = total_return / num_episodes
        return avg_return.numpy()[0]
    
def collect_step(environment, policy, buffer):
        time_step = environment.current_time_step()
        action_step = policy.action(time_step)
        next_time_step = environment.step(action_step.action)
        traj = trajectory.from_transition(time_step, action_step, next_time_step)

        # Add trajectory to the replay buffer
        buffer.add_batch(traj)
def collect_data(env, policy, buffer, steps):
        for _ in range(steps):
            collect_step(env, policy, buffer)
```

#### File: `config.py`
```python
import tensorflow as tf
FILE = "cleaned_preprocessed.csv"
COINS = ["DASH","LTC","STR"]
COLS = ['high', 'low', 'open', 'close', 'volume', 'quoteVolume','weightedAverage']
SCOLS = ['vh', 'vl', 'vc', 'open_s', 'volume_s', 'quoteVolume_s', 'weightedAverage_s', 'vh_roll_7', \
    'vh_roll_14', 'vh_roll_30', 'vl_roll_7', 'vl_roll_14', 'vl_roll_30', 'vc_roll_7', 'vc_roll_14', 'vc_roll_30', \
        'open_s_roll_7', 'open_s_roll_14', 'open_s_roll_30', 'volume_s_roll_7', 'volume_s_roll_14', 'volume_s_roll_30', \
            'quoteVolume_s_roll_7', 'quoteVolume_s_roll_14', 'quoteVolume_s_roll_30', 'weightedAverage_s_roll_7', \
                'weightedAverage_s_roll_14', 'weightedAverage_s_roll_30']
OBS_COLS = ['DASH_vh', 'LTC_vh', 'STR_vh', 'DASH_vl', 'LTC_vl', 'STR_vl', 'DASH_vc', 'LTC_vc', 'STR_vc', \
    'DASH_open_s', 'LTC_open_s', 'STR_open_s', 'DASH_volume_s', 'LTC_volume_s', 'STR_volume_s', 'DASH_quoteVolume_s', \
        'LTC_quoteVolume_s', 'STR_quoteVolume_s', 'DASH_weightedAverage_s', 'LTC_weightedAverage_s', 'STR_weightedAverage_s', \
            'DASH_vh_roll_7', 'LTC_vh_roll_7', 'STR_vh_roll_7', 'DASH_vh_roll_14', 'LTC_vh_roll_14', 'STR_vh_roll_14', \
                'DASH_vh_roll_30', 'LTC_vh_roll_30', 'STR_vh_roll_30', 'DASH_vl_roll_7', 'LTC_vl_roll_7', 'STR_vl_roll_7', \
                    'DASH_vl_roll_14', 'LTC_vl_roll_14', 'STR_vl_roll_14', 'DASH_vl_roll_30', 'LTC_vl_roll_30', 'STR_vl_roll_30', \
                        'DASH_vc_roll_7', 'LTC_vc_roll_7', 'STR_vc_roll_7', 'DASH_vc_roll_14', 'LTC_vc_roll_14', 'STR_vc_roll_14', \
                            'DASH_vc_roll_30', 'LTC_vc_roll_30', 'STR_vc_roll_30', 'DASH_open_s_roll_7', 'LTC_open_s_roll_7', \
                                'STR_open_s_roll_7', 'DASH_open_s_roll_14', 'LTC_open_s_roll_14', 'STR_open_s_roll_14', 'DASH_open_s_roll_30', \
                                    'LTC_open_s_roll_30', 'STR_open_s_roll_30', 'DASH_volume_s_roll_7', 'LTC_volume_s_roll_7', 'STR_volume_s_roll_7', \
                                        'DASH_volume_s_roll_14', 'LTC_volume_s_roll_14', 'STR_volume_s_roll_14', 'DASH_volume_s_roll_30',\
                                             'LTC_volume_s_roll_30', 'STR_volume_s_roll_30', 'DASH_quoteVolume_s_roll_7', 'LTC_quoteVolume_s_roll_7', \
                                                 'STR_quoteVolume_s_roll_7', 'DASH_quoteVolume_s_roll_14', 'LTC_quoteVolume_s_roll_14', \
                                                     'STR_quoteVolume_s_roll_14', 'DASH_quoteVolume_s_roll_30', 'LTC_quoteVolume_s_roll_30', \
                                                         'STR_quoteVolume_s_roll_30', 'DASH_weightedAverage_s_roll_7', 'LTC_weightedAverage_s_roll_7', \
                                                             'STR_weightedAverage_s_roll_7', 'DASH_weightedAverage_s_roll_14', 'LTC_weightedAverage_s_roll_14',\
                                                                  'STR_weightedAverage_s_roll_14', 'DASH_weightedAverage_s_roll_30', 'LTC_weightedAverage_s_roll_30', 'STR_weightedAverage_s_roll_30']

OBS_COLS = ['DASH_vh','LTC_vh','STR_vh','DASH_vl','LTC_vl','STR_vl','DASH_vc','LTC_vc','STR_vc','DASH_open_s','LTC_open_s','STR_open_s','DASH_volume_s','LTC_volume_s','STR_volume_s','DASH_quoteVolume_s','LTC_quoteVolume_s','STR_quoteVolume_s','DASH_weightedAverage_s','LTC_weightedAverage_s','STR_weightedAverage_s','DASH_vh_roll_30','LTC_vh_roll_30','STR_vh_roll_30','DASH_vl_roll_30','LTC_vl_roll_30','STR_vl_roll_30','DASH_vc_roll_30','LTC_vc_roll_30','STR_vc_roll_30','DASH_open_s_roll_30','LTC_open_s_roll_30','STR_open_s_roll_30','DASH_volume_s_roll_30','LTC_volume_s_roll_30','STR_volume_s_roll_30','DASH_quoteVolume_s_roll_30','LTC_quoteVolume_s_roll_30','STR_quoteVolume_s_roll_30','DASH_weightedAverage_s_roll_30','LTC_weightedAverage_s_roll_30','STR_weightedAverage_s_roll_30']                                                                  

OBS_COLS_MIN = [-0.39,-0.39,-0.39,-52.92,-144.06,-159.81,-31.78,-19.57,-61.76,-87.7,-65.71,-130.35,-51.36,-51.09,-77.06,-0.03,-0.16,-74.55,-73.04,-73.72,-145.94,-0.77,-0.77,-0.77,-12.17,-14.24,-25.47,-15.64,-12.37,-12.73,-44.75,-25.01,-32.13,-39.2,-83.44,-74.04,-0.03,-0.2,-75.79,-44,-25,-32.25]
OBS_COLS_MAX = [53.16,69.71,90.97,0.4,0.4,0.4,39.31,24.4,85.49,114.25,66.32,130.35,55.72,60.25,66.09,0.04,0.18,96.32,67.32,73.63,145.94,9.96,17.79,53.89,0.81,0.81,0.81,7.58,9.9,14.93,41.44,16.35,32.11,34.64,82.48,59.62,0.03,0.2,78.16,38.94,16.29,32.24]
EPISODE_LENGTH = 1500
LOGDIR="LOGDIR"
MODEL_SAVE = "model_save"


NUM_ITERATIONS = 1000
COLLECT_STEPS_PER_ITERATION = 100
LOG_INTERVAL = 10
EVAL_INTERVAL = 4
MODEL_SAVE_FREQ = 12


REPLAY_BUFFER_MAX_LENGTH = 10000 #100000
BATCH_SIZE = 100
NUM_EVAL_EPISODES = 4

actor_fc_layers=(400, 300)
critic_obs_fc_layers=(400,)
critic_action_fc_layers=None
critic_joint_fc_layers=(300,)
ou_stddev=0.2
ou_damping=0.15
target_update_tau=0.05
target_update_period=5
dqda_clipping=None
td_errors_loss_fn=tf.compat.v1.losses.huber_loss
gamma=0.05
reward_scale_factor=1.0
gradient_clipping=None

actor_learning_rate=1e-4
critic_learning_rate=1e-3
debug_summaries=False
summarize_grads_and_vars=False
```

#### File: `train.py`
```python
import tensorflow as tf
import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt
from sklearn import preprocessing
from tqdm import tqdm
from tf_agents.environments import py_environment
from tf_agents.environments import tf_environment
from tf_agents.environments import tf_py_environment
from tf_agents.environments import utils
from tf_agents.specs import array_spec
from tf_agents.environments import wrappers
from tf_agents.environments import suite_gym
from tf_agents.trajectories import time_step as ts
from tf_agents.policies.policy_saver import PolicySaver
from tf_agents.agents.ddpg import actor_network
from tf_agents.agents.ddpg import critic_network
from tf_agents.agents.ddpg import ddpg_agent

from tf_agents.agents.dqn import dqn_agent
from tf_agents.drivers import dynamic_step_driver
from tf_agents.environments import suite_gym
from tf_agents.environments import tf_py_environment
from tf_agents.eval import metric_utils
from tf_agents.metrics import tf_metrics
from tf_agents.networks import q_network
from tf_agents.policies import random_tf_policy
from tf_agents.replay_buffers import tf_uniform_replay_buffer
from tf_agents.trajectories import trajectory
from tf_agents.trajectories import policy_step
from tf_agents.utils import common
import logging

import config
from  environments import CardGameEnv
from utils import *

tf.compat.v1.enable_v2_behavior()
os.makedirs(config.LOGDIR,exist_ok=True)
os.makedirs(config.MODEL_SAVE,exist_ok=True)
logging.basicConfig(filename=os.path.join(config.LOGDIR,'log.log'), 
level=logging.INFO, 
format='%(asctime)s | %(name)s | %(levelname)s | %(message)s')
if __name__=='__main__':
    train_py_env = CardGameEnv()
    eval_py_env = CardGameEnv()
    
    train_env = tf_py_environment.TFPyEnvironment(train_py_env)
    eval_env = tf_py_environment.TFPyEnvironment(eval_py_env)
    actor_fc_layers = config.actor_fc_layers
    critic_obs_fc_layers = config.critic_obs_fc_layers
    critic_action_fc_layers = config.critic_action_fc_layers
    critic_joint_fc_layers = config.critic_joint_fc_layers
    ou_stddev = config.ou_stddev
    ou_damping = config.ou_damping
    target_update_tau = config.target_update_tau
    target_update_period = config.target_update_period
    dqda_clipping = config.dqda_clipping
    td_errors_loss_fn = config.td_errors_loss_fn
    gamma = config.gamma
    reward_scale_factor = config.reward_scale_factor
    gradient_clipping = config.gradient_clipping

    actor_learning_rate = config.actor_learning_rate
    critic_learning_rate = config.critic_learning_rate
    debug_summaries = config.debug_summaries
    summarize_grads_and_vars = config.summarize_grads_and_vars
    
    global_step = tf.compat.v1.train.get_or_create_global_step()

    actor_net = actor_network.ActorNetwork(
            train_env.time_step_spec().observation,
            train_env.action_spec(),
            fc_layer_params=actor_fc_layers,
        )

    critic_net_input_specs = (train_env.time_step_spec().observation,
                            train_env.action_spec())

    critic_net = critic_network.CriticNetwork(
        critic_net_input_specs,
        observation_fc_layer_params=critic_obs_fc_layers,
        action_fc_layer_params=critic_action_fc_layers,
        joint_fc_layer_params=critic_joint_fc_layers,
    )

    tf_agent = ddpg_agent.DdpgAgent(
        train_env.time_step_spec(),
        train_env.action_spec(),
        actor_network=actor_net,
        critic_network=critic_net,
        actor_optimizer=tf.compat.v1.train.AdamOptimizer(
            learning_rate=actor_learning_rate),
        critic_optimizer=tf.compat.v1.train.AdamOptimizer(
            learning_rate=critic_learning_rate),
        ou_stddev=ou_stddev,
        ou_damping=ou_damping,
        target_update_tau=target_update_tau,
        target_update_period=target_update_period,
        dqda_clipping=dqda_clipping,
        td_errors_loss_fn=td_errors_loss_fn,
        gamma=gamma,
        reward_scale_factor=reward_scale_factor,
        gradient_clipping=gradient_clipping,
        debug_summaries=debug_summaries,
        summarize_grads_and_vars=summarize_grads_and_vars,
        train_step_counter=global_step)
    tf_agent.initialize()
    
    random_policy = random_tf_policy.RandomTFPolicy(train_env.time_step_spec(),
                                                    train_env.action_spec())

    replay_buffer = tf_uniform_replay_buffer.TFUniformReplayBuffer(
        data_spec=tf_agent.collect_data_spec,
        batch_size=train_env.batch_size,
        max_length=config.REPLAY_BUFFER_MAX_LENGTH)

    collect_data(train_env, random_policy, replay_buffer, steps=100)

    dataset = replay_buffer.as_dataset(
        num_parallel_calls=3, 
        sample_batch_size=config.BATCH_SIZE, 
        num_steps=2).prefetch(3)
    
    my_policy = tf_agent.collect_policy
    saver = PolicySaver(my_policy, batch_size=None)

    iterator = iter(dataset)
    tf_agent.train = common.function(tf_agent.train)

    # Reset the train step
    tf_agent.train_step_counter.assign(0)

    # Evaluate the agent's policy once before training.
    avg_return = compute_avg_return(eval_env, tf_agent.policy, \
                                    config.NUM_EVAL_EPISODES)
    returns = [avg_return]
    iterations=[0]
    for _ in tqdm(range(config.NUM_ITERATIONS),total=config.NUM_ITERATIONS):
            # Collect a few steps using collect_policy and save to the replay buffer.
            for _ in range(config.COLLECT_STEPS_PER_ITERATION):
                collect_step(train_env, tf_agent.collect_policy, replay_buffer)

            # Sample a batch of data from the buffer and update the agent's network.
            experience, unused_info = next(iterator)
            train_loss = tf_agent.train(experience).loss

            step = tf_agent.train_step_counter.numpy()

            if step % config.LOG_INTERVAL == 0:
                print('step = {0}: loss = {1}'.format(step, train_loss))

            if step % config.EVAL_INTERVAL == 0:
                avg_return = compute_avg_return(eval_env, tf_agent.policy, \
                                                config.NUM_EVAL_EPISODES)
                print('step = {0}: Average Return = {1}'.format(step, avg_return))
                logging.info('step = {0}: Average Return = {1}'.format(step, avg_return))
                returns.append(avg_return)
                iterations.append(step)
            if step % config.MODEL_SAVE_FREQ == 0:
                saver.save(os.path.join(config.MODEL_SAVE,f'policy_step_{step}_gamma.mdl'))
                
        # except:
        #     print("error_skipping")

    # iterations = range(0, num_iteratioens + 1, eval_interval)
    plt.plot(iterations, returns)
    plt.ylabel('Average Return')
    plt.xlabel('Iterations')
    plt.ylim(top=50)
    plt.show()
    plt.savefig("output_img_gamma.png")
    pd.DataFrame({"interations":iterations,"Return":returns}).to_csv(os.path.join(config.LOGDIR,"output_ar_gamma.csv"),index=None)
```

#### File: `environments.py`
```python
import tensorflow as tf
import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt
from sklearn import preprocessing
from tqdm import tqdm
from tf_agents.environments import py_environment
from tf_agents.environments import tf_environment
from tf_agents.environments import tf_py_environment
from tf_agents.environments import utils
from tf_agents.specs import array_spec
from tf_agents.environments import wrappers
from tf_agents.environments import suite_gym
from tf_agents.trajectories import time_step as ts
from tf_agents.policies.policy_saver import PolicySaver
from tf_agents.agents.ddpg import actor_network
from tf_agents.agents.ddpg import critic_network
from tf_agents.agents.ddpg import ddpg_agent
from tf_agents.agents.dqn import dqn_agent
from tf_agents.drivers import dynamic_step_driver
from tf_agents.environments import suite_gym
from tf_agents.environments import tf_py_environment
from tf_agents.eval import metric_utils
from tf_agents.metrics import tf_metrics
from tf_agents.networks import q_network
from tf_agents.policies import random_tf_policy
from tf_agents.replay_buffers import tf_uniform_replay_buffer
from tf_agents.trajectories import trajectory
from tf_agents.trajectories import policy_step
from tf_agents.utils import common
import logging

import config


tf.compat.v1.enable_v2_behavior()

class CardGameEnv(py_environment.PyEnvironment):

    def __init__(self):
        self._action_spec = array_spec.BoundedArraySpec(
            (len(config.COINS)+1,), np.float64, minimum=0, maximum=1, name='action')
        self._observation_spec = array_spec.BoundedArraySpec(
            shape=(len(config.OBS_COLS),), dtype=np.float64, minimum=config.OBS_COLS_MIN,\
                maximum=config.OBS_COLS_MAX,\
                     name='observation')
        self.reset()
        self._episode_ended = False
        


    def action_spec(self):
        return self._action_spec

    def observation_spec(self):
        return self._observation_spec

    def _reset(self):
        self.memory_return = pd.DataFrame(columns=[t+"_close" for t in config.COINS])
        self._episode_ended = False
        self.index = 0
        self.time_delta = pd.Timedelta(5,unit='m')
        self.init_cash = 1000
        self.current_cash = self.init_cash
        self.current_value = self.init_cash
        self.previous_price = {}
        self.old_dict_coin_price_1 = {}
        self.old_dict_coin_price_2 = {}

        self.money_split_ratio = np.zeros((len(config.COINS)+1))
        self.money_split_ratio[0] = 1

        self.df = pd.read_csv(config.FILE)
        self.scaler = preprocessing.StandardScaler()
        
        self.df["date"] = self.df["date"].apply(lambda x: pd.Timestamp(x, unit='s', tz='US/Pacific'))
        self.df = self.df[self.df["coin"].isin(config.COINS)].sort_values("date")
        self.scaler.fit(self.df[config.SCOLS].values)
        self.df = self.df.reset_index(drop=True)

        self.max_index = self.df.shape[0]
        start_point = (np.random.choice(np.arange(3,self.max_index - config.EPISODE_LENGTH))//3) *3
        end_point = start_point + config.EPISODE_LENGTH//3 *3
        self.df = self.df.loc[start_point:end_point+2].reset_index(drop=True)
        
        
        self.df = self.df.reset_index(drop=True)


        self.init_time = self.df.loc[0,"date"]
        self.current_time = self.init_time
        self.dfslice = self.df[(self.df["coin"].isin(config.COINS))&(self.df["date"]>=self.current_time)&(self.df["date"]<self.current_time+pd.Timedelta(5,unit='m'))].copy().drop_duplicates("coin")

        self.current_stock_num_distribution = self.calculate_actual_shares_from_money_split()
        self.previous_value = self.current_value
        self.current_stock_money_distribution,self.current_value  = self.calculate_money_from_num_stocks()
        self.money_split_ratio = self.normalize_money_dist()
        
        self.step_reward = 0
        
        info_ =  {"state":"state",\
                "money_split":self.money_split_ratio,"share_num":self.current_stock_num_distribution,\
                "value":self.current_value,"time":self.current_time,\
                "reward":self.step_reward,\
                # "raw_output":self.get_observations_unscaled(),
                "scaled_output":self.get_observations()}
        self._state = info_["scaled_output"][config.OBS_COLS].values.flatten()
        reward = info_["reward"]
        self._episode_ended = True if self.index==config.EPISODE_LENGTH//3 else False
        

        return ts.restart(self._state)

    def _step(self, action):
 
        if self._episode_ended:
 
            return self.reset()
        if sum(action)<=1e-3:
            self.money_split_ratio = [1/len(action) for t in action]
        else:
            self.money_split_ratio = action/sum(action)

        self.current_stock_num_distribution = self.calculate_actual_shares_from_money_split()
        self.step_time()
        self.index +=1

        info_ =  {"state":"state",\
                    "money_split":self.money_split_ratio,"share_num":self.current_stock_num_distribution,\
                    "value":self.current_value,"time":self.current_time,\
                    "reward":self.step_reward,\
                    "scaled_output":self.get_observations()}
 
        self._state = info_["scaled_output"][config.OBS_COLS].values.flatten()
        reward = info_["reward"]
        self._episode_ended = True if self.index==config.EPISODE_LENGTH//3 else False
        if self._episode_ended:
            reward = 0
            return ts.termination(self._state , reward)
        else:
            try:
                return ts.transition(
                    self._state, reward=reward, discount=1)
            except Exception as e:
                print("ERRORRRRRR!!!!!!!!!!!!!!!!")
                print(self._state)
                print(reward)
                print(self.step_reward, self.current_value, self.previous_value)
                print(self.current_stock_money_distribution)
                print(self.current_stock_num_distribution)
                print(action)
                print(self.index)
                print(self.dfslice)
                print(self.current_time)
                print(self.money_split_ratio )
                print(e)
                self.df.to_csv(os.path.join(LOGDIR,"error_df.csv"))
                
                raise ValueError

    def step_time(self):
        self.current_time += self.time_delta
        self.dfslice = self.df[(self.df["coin"].isin(config.COINS))&(self.df["date"]>=self.current_time)&(self.df["date"]<self.current_time+pd.Timedelta(5,unit='m'))].copy().drop_duplicates("coin")
        self.previous_value = self.current_value
        self.current_stock_money_distribution,self.current_value  = self.calculate_money_from_num_stocks()
        self.money_split_ratio = self.normalize_money_dist()
        self.step_reward = self.current_value - self.previous_value
        # self.step_reward = np.min([self.step_reward,0.25])


    def get_observations(self):
        dfslice = self.dfslice
        dfs = pd.DataFrame()
        for i,grp in dfslice.groupby("coin"):
            tempdf = pd.DataFrame(self.scaler.transform(grp[config.SCOLS].values))
            tempdf.columns = [i+"_"+c for c in config.SCOLS]
            if dfs.empty:
                dfs = tempdf
            else:
                dfs = dfs.merge(tempdf,right_index=True,left_index=True,how='inner')

        return dfs
    def get_observations_unscaled(self):
        dfslice = self.dfslice
        dfs = pd.DataFrame()
        for i,grp in dfslice.groupby("coin"):
            tempdf = pd.DataFrame(grp[config.COLS].values)
            tempdf.columns = [i+"_"+c for c in config.COLS]
            if dfs.empty:
                dfs = tempdf
            else:
                dfs = dfs.merge(tempdf,right_index=True,left_index=True,how='inner')
        
        self.memory_return = pd.concat([self.memory_return,dfs[[t+"_close" for t in config.COINS]]],ignore_index=True)
        
        return dfs
    def calculate_actual_shares_from_money_split(self):
        dict_coin_price = self.dfslice[["coin","open"]]\
                        .set_index("coin").to_dict()["open"]
        
        num_shares = []
        for i,c in enumerate(config.COINS):
            if c in dict_coin_price:
                num_shares.append( self.money_split_ratio[i+1]*self.current_value//dict_coin_price[c] )
            else:
                num_shares.append( self.money_split_ratio[i+1]*self.current_value//self.old_dict_coin_price_1[c] )
            
        self.current_cash = self.money_split_ratio[0]*self.current_value
        for c in dict_coin_price:
            self.old_dict_coin_price_1[c] = dict_coin_price[c]
        
        return num_shares
    def calculate_money_from_num_stocks(self):
        money_dist = []
        money_dist.append(self.current_cash)
        dict_coin_price = self.dfslice[["coin","open"]]\
                        .set_index("coin").to_dict()["open"]
        for i,c in enumerate(config.COINS):
            if c in dict_coin_price:
                money_dist.append(self.current_stock_num_distribution[i]*dict_coin_price[c])
            else:
                money_dist.append(self.current_stock_num_distribution[i]*self.old_dict_coin_price_2[c])
        
        for c in dict_coin_price:
            self.old_dict_coin_price_2[c] = dict_coin_price[c]
        return money_dist,sum(money_dist)
    def normalize_money_dist(self):
        normal = []
        
        for i,c in enumerate(self.current_stock_money_distribution):
            normal.append(c/self.current_value)
        return normal
```


==================================================


## [2/3] Repository: fortitudo.tech (`PHASE4-QUANT-170`)
- **Full Name**: `PHASE4-QUANT-170_fortitudo-tech__fortitudo.tech`
- **Description**: Entropy Pooling views and stress testing combined with Conditional Value-at-Risk (CVaR) portfolio optimization in Python.
- **GitHub Stars**: 310
- **Source Pool**: `phase4_quant_wheels_100`

### Documentation & Overview (README.md)
|Pytest| |Codecov| |Binder|

.. |Pytest| image:: https://github.com/fortitudo-tech/fortitudo.tech/actions/workflows/tests.yml/badge.svg
   :target: https://github.com/fortitudo-tech/fortitudo.tech/actions/workflows/tests.yml

.. |Codecov| image:: https://codecov.io/gh/fortitudo-tech/fortitudo.tech/graph/badge.svg?token=Z16XK92Gkl 
   :target: https://codecov.io/gh/fortitudo-tech/fortitudo.tech

.. |Binder| image:: https://mybinder.org/badge_logo.svg
   :target: https://mybinder.org/v2/gh/fortitudo-tech/fortitudo.tech/main?labpath=examples

Fortitudo Technologies Open Source
==================================

This package allows you to explore open-source implementations of some of our
fundamental methods, for example, Sequential Entropy Pooling (SeqEP), Conditional
Value-at-Risk (CVaR) as well as Conditional Maximum Loss (CML) optimization,
and Fully Flexible Resampling (FFR) in Python.

You can watch this `YouTube playlist <https://www.youtube.com/playlist?list=PLfI2BKNVj_b2rurUsCtc2F8lqtPWqcs2K>`_
for a walkthrough of the package's functionality and examples.

For a high-level introduction to the investment framework, watch this `YouTube video <https://youtu.be/4ESigySdGf8>`_
and `Substack post <https://antonvorobets.substack.com/p/fully-general-investment-framework>`_.

For a pedagogical and deep presentation of the investment framework and its methods,
see the `Portfolio Construction and Risk Management Book <https://antonvorobets.substack.com/p/pcrm-book>`_.

To build the deepest understanding of all the theories and methods, you can
complete the `Applied Quantitative Investment Management Course <https://antonvorobets.substack.com/t/course>`_.

Audience
--------

The package is intended for advanced users who are comfortable specifying
portfolio constraints and Entropy Pooling views using matrices and vectors.
This gives full flexibility in relation to working with these technologies.
Hence, input checking is intentionally kept to a minimum.

Installation Instructions
-------------------------

Installation can be done via pip::

   pip install -U fortitudo.tech

For best performance, we recommend that you install the package in a `conda environment
<https://conda.io/projects/conda/en/latest/user-guide/concepts/environments.html>`_
and let conda handle the installation of dependencies before installing the
package using pip. You can do this by following these steps::

   conda create -n fortitudo.tech -c conda-forge python scipy pandas matplotlib cvxopt
   conda activate fortitudo.tech
   pip install fortitudo.tech

The examples might require you to install additional packages, e.g., seaborn and
ipykernel/notebook/jupyterlab if you want to run the notebooks. Using pip to
install these packages should not cause any dependency issues.

You can also explore the examples in the cloud without any local installations using
`Binder <https://mybinder.org/v2/gh/fortitudo-tech/fortitudo.tech/main?labpath=examples>`_.
However, note that Binder servers have very limited resources and might not support
some of the optimized routines this package uses. If you want access to a stable
and optimized environment with persistent storage, please subscribe to our Data
Science Server.

Company
-------

Fortitudo Technologies offers novel investment software as well as quantitative
and digitalization consultancy to the investment management industry. For more
information, please visit our `website <https://fortitudo.tech>`_.

Disclaimer
----------

This package is completely separate from our proprietary solutions and therefore
not representative of the quality and functionality offered by the Investment Simulation
and Investment Analysis modules.

For a short presentation of which CVaR problems the Investment Analysis module can solve
and at what speed, see the
`cvar-optimization-benchmarks repository <https://github.com/fortitudo-tech/cvar-optimization-benchmarks>`_.

If you are a professional investor and want to experience how these methods
can be used for sophisticated analysis in practice, please request a demo by
sending an email to demo@fortitudo.tech.

### Core Implementation Code & Architecture
#### File: `.vscode/settings.json`
```python
{
    "flake8.args": [
        "--max-line-length=99",
        "--ignore=E123,E402,E741,F401,W503"
    ],
}
```

#### File: `fortitudo/__init__.py`
```python
# fortitudo.tech - Novel Investment Technologies.
# Copyright (C) 2021-2025 Fortitudo Technologies.

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
```

#### File: `fortitudo/tech/__init__.py`
```python
# fortitudo.tech - Novel Investment Technologies.
# Copyright (C) 2021-2025 Fortitudo Technologies.

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

from .data import load_pnl, load_parameters, load_risk_factors, load_time_series, plot_vol_surface
from .entropy_pooling import entropy_pooling
from .functions import (simulation_moments, covariance_matrix, correlation_matrix,
                        portfolio_cvar, portfolio_var, portfolio_vol, exposure_stacking)
from .optimization import cvar_options, MeanCVaR, MeanVariance
from .option_pricing import forward, call_option, put_option
from .simulation import FullyFlexibleResampling, exp_decay_probs, normal_exp_decay_calib
```

#### File: `tests/context.py`
```python
# fortitudo.tech - Novel Investment Technologies.
# Copyright (C) 2021-2025 Fortitudo Technologies.

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from fortitudo.tech import (
    entropy_pooling, MeanCVaR, cvar_options, MeanVariance, load_parameters,
    simulation_moments, covariance_matrix, correlation_matrix, portfolio_cvar,
    portfolio_var, portfolio_vol, load_pnl, load_risk_factors, load_time_series,
    plot_vol_surface, forward, call_option, put_option, FullyFlexibleResampling,
    exp_decay_probs, normal_exp_decay_calib, exposure_stacking)

from fortitudo.tech.functions import _simulation_check

R = load_pnl()
time_series = load_time_series()
```

#### File: `tests/test_data.py`
```python
# fortitudo.tech - Novel Investment Technologies.
# Copyright (C) 2021-2025 Fortitudo Technologies.

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import numpy as np
from pandas import DataFrame
from matplotlib.figure import Figure
from context import load_parameters, load_risk_factors, time_series, plot_vol_surface, R


def test_load_data():
    instrument_names, means, covariance_matrix = load_parameters()
    assert list(R.columns) == instrument_names
    I = R.shape[1]
    assert means.shape == (I,)
    assert covariance_matrix.shape == (I, I)


def test_load_risk_factors():
    risk_factors = load_risk_factors()
    assert type(risk_factors) is DataFrame
    assert risk_factors.shape == (5039, 82)


def test_time_series():
    assert time_series.shape == (5040, 79)
    assert np.all(time_series.values >= 0)


def test_plot_vol_surface():
    fig, _ = plot_vol_surface(0, time_series.values[:, 34:69])
    assert type(fig) is Figure
```

#### File: `pyproject.toml`
```python
[tool.poetry]
name = "fortitudo.tech"
version = "1.2.5"
description = "Entropy Pooling views and stress testing combined with Conditional Value-at-Risk (CVaR) portfolio optimization in Python."
authors = ["Fortitudo Technologies <software@fortitudo.tech>"]
license = "GPL-3.0-or-later"
readme = "README.rst"
homepage = "https://fortitudo.tech"
repository = "https://github.com/fortitudo-tech/fortitudo.tech"
documentation = "https://os.fortitudo.tech"
keywords = ["CVaR", "Efficient Frontier", "Entropy Pooling", "Quantitative Finance", "Portfolio Optimization"]
classifiers = [
    "Intended Audience :: Education",
    "Intended Audience :: Financial and Insurance Industry",
    "Intended Audience :: Science/Research",
    "Programming Language :: Python :: 3.13",
    "Programming Language :: Python :: 3.12",
    "Programming Language :: Python :: 3.11",
    "Programming Language :: Python :: 3.10",
    "Programming Language :: Python :: 3.9",
    "Topic :: Office/Business :: Financial",
    "Topic :: Office/Business :: Financial :: Investment",
    "Topic :: Scientific/Engineering :: Mathematics"]
packages = [
    { include = "fortitudo/tech" }
]

include = [
    "fortitudo/tech/data/pnl.csv", "fortitudo/tech/data/parameters.csv",
    "fortitudo/tech/data/risk_factors.csv", "fortitudo/tech/data/time_series.csv"]

[tool.poetry.urls]
"Issues" = "https://github.com/fortitudo-tech/fortitudo.tech/issues"

[tool.poetry.dependencies]
python = "^3.9, <3.15"
scipy = "^1.10"
cvxopt = "^1.3.0"
pandas = ">=1.3.4"
numpy = ">=2.0"
matplotlib = "^3.4"

[tool.poetry.dev-dependencies]
pytest-cov = "^3.0.0"
sphinx-rtd-theme = "^1.0.0"
sphinx-autodoc-typehints = "^1.12.0"
sphinxcontrib-bibtex = "^2.4.1"

[build-system]
requires = ["poetry-core>=1.0.0"]
build-backend = "poetry.core.masonry.api"
```


==================================================


## [3/3] Repository: deepfolio (`PHASE4-QUANT-176`)
- **Full Name**: `PHASE4-QUANT-176_jialuechen__deepfolio`
- **Description**: Quadratic Programming based Python Package for Portfolio Optimization
- **GitHub Stars**: 100
- **Source Pool**: `phase4_quant_wheels_100`

### Documentation & Overview (README.md)
# DeepFolio

DeepFolio is a Quadratic Programming-based Python library for large-scale portfolio optimization.

It implements a unified QP framework with an efficient OSQP-ADMM solver (featuring sparse LDL caching and warm starts), and provides full support for real-world constraints such as long/short limits, turnover bounds, and factor neutrality. DeepFolio pioneers ℓ₁+ℓ₂² regularization on mapped factor weights and integrates cutting-edge covariance estimators (AP-Trees, IPCA, RP-PCA, etc.), enabling single-core, high-precision optimization for portfolios with hundreds of assets across multiple rolling-window backtests.

---

## Features

- **Flexible data pipeline**: Resampling, feature engineering, and custom hooks
- **Portfolio Transformer model**: Attention-based allocation for multiple assets
- **Multiple loss functions**: Sharpe ratio, CVaR, and more
- **Cost models**: Linear, Almgren-Chriss transaction cost modeling
- **Portfolio constraints**: Gross exposure, leverage cap, and more
- **Scenario augmentation**: Monte Carlo simulation and scenario generation
- **Integrated backtesting**: Performance monitoring and evaluation
- **Auto re-training & hyperparameter tuning**

---

## Installation

```bash
pip install deepfolio
```

## Quickstart

```python
from deepfolio import Pipeline, PortfolioTransformer, MultiLossTrainer, Backtester

# 1. Data loading and preprocessing
pipe = Pipeline(hooks=[Pipeline.pct_return])
prices = pipe.load('prices.csv')  # Load your price data (CSV with datetime index and asset columns)
returns = prices.values           # Convert to numpy array

# 2. Build the model
model = PortfolioTransformer(n_assets=returns.shape[1])

# 3. Train the model with multiple objectives (e.g., maximize Sharpe, minimize CVaR)
trainer = MultiLossTrainer(model=model, losses=['sharpe', 'cvar'])
trainer.fit(returns, epochs=100, batch_size=32)

# 4. Generate portfolio weights for new data
weights = model.predict(returns[-20:])  # Predict weights for the last 20 periods

# 5. Backtest the strategy
backtester = Backtester(model)
results = backtester.run(returns)

# 6. Analyze results
```

## License

MIT

### Core Implementation Code & Architecture
#### File: `deepfolio/monitor.py`
```python
class Monitor:
    # TODO: implement
    pass
```

#### File: `deepfolio/autotrain.py`
```python
class AutoTrainer:
    # TODO: implement
    pass
```

#### File: `deepfolio/metrics.py`
```python
import numpy as np

class Metrics:
    # TODO: implement
    pass
```

#### File: `deepfolio/scenario.py`
```python
import torch

class ScenarioEngine:
    # TODO: implement
    pass
```

#### File: `deepfolio/backtest.py`
```python
import torch
import numpy as np

class Backtester:
    # TODO: implement
    pass
```

#### File: `tests/test_deepfolio.py`
```python
import pytest
import deepfolio

def test_version():
    assert hasattr(deepfolio, '__version__')
```


==================================================
