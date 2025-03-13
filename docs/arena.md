---
hide:
#   - toc
  - navigation
---
# **Arena**

⚠️⚠️⚠️ Read the guidelines below before submitting your agent!

<!-- - Select a benchmark, an environment, and a specific version;
- Enter your github username and the link to your code;
- Click "Submit" to evaluate your agent and get a unique ID; -->

<!-- <iframe
	src="https://rle-foundation-arena.hf.space"
	frameborder="0"
	width="100%"
	height="800px"
	style="padding: 0;"
></iframe> -->

<!-- ## ⚠️⚠️⚠️ Notice -->

<!-- # **Submission Guidelines** -->

<!-- ## **Step 1: Create a python file for model description**

- Write an `agent.py` to describe the model architecture, and make sure the model has an `.act()` function that accepts observations and generates actions. Please refer to [CleanRL](https://github.com/vwxyzjn/cleanrl/blob/master/cleanrl/ppo_atari.py) to create a simple and elegant model architecture.
``` py
# The code is from https://github.com/vwxyzjn/cleanrl/blob/master/cleanrl/ppo_atari.py
import torch
import torch.nn as nn

def layer_init(layer, std=np.sqrt(2), bias_const=0.0):
    torch.nn.init.orthogonal_(layer.weight, std)
    torch.nn.init.constant_(layer.bias, bias_const)
    return layer


class Agent(nn.Module):
    def __init__(self, envs):
        super().__init__()
        self.network = nn.Sequential(
            layer_init(nn.Conv2d(4, 32, 8, stride=4)),
            nn.ReLU(),
            layer_init(nn.Conv2d(32, 64, 4, stride=2)),
            nn.ReLU(),
            layer_init(nn.Conv2d(64, 64, 3, stride=1)),
            nn.ReLU(),
            nn.Flatten(),
            layer_init(nn.Linear(64 * 7 * 7, 512)),
            nn.ReLU(),
        )
        self.actor = layer_init(nn.Linear(512, envs.single_action_space.n), std=0.01)
        self.critic = layer_init(nn.Linear(512, 1), std=1)

    def get_value(self, x):
        return self.critic(self.network(x / 255.0))

    # the function directly outputs actions
    def act(self, x):
        hidden = self.network(x / 255.0)
        logits = self.actor(hidden)
        probs = Categorical(logits=logits)
        
        return probs.mode
```
- At least **⚠️3⚠️** trained models need to be submitted for evaluation, please name the `state_dict` file as:
``` sh
agent_0.pth
agent_1.pth
agent_2.pth
```


## **Step 2: Create a ZIP file**
Compress the `agent.py` and the models into an `agent.zip` file.

## **Step 3: Model upload**
- Fill out the submission form;
- Click the `Submit` button and wait for the result. -->
