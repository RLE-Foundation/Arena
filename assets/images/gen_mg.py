import gymnasium as gym

import minigrid
from minigrid.wrappers import RGBImgObsWrapper
from PIL import Image
# register new environments

from gymnasium.envs.registration import register

tasks = [
    "MultiRoom-N7-S4",
    # "MultiRoom-NoisyTV-N7-S4",
    "KeyCorridor-S3-R3",
    "MultiRoom-N10-S10",
    "MultiRoom-N7-S8",
    "MultiRoom-N10-S4",
    "ObstructedMaze-2Dlh",
    "MultiRoom-N12-S10"
]
# register all tasks
register(
    id="MiniGrid-MultiRoom-N7-S4-v0",
    entry_point="minigrid.envs:MultiRoomEnv",
    kwargs={"minNumRooms": 7, "maxNumRooms": 7, "maxRoomSize": 4},
)

register(
    id="MiniGrid-MultiRoom-NoisyTV-N7-S4-v0",
    entry_point="minigrid.envs:MultiRoomEnv",
    kwargs={"minNumRooms": 7, "maxNumRooms": 7, "maxRoomSize": 4, "noise": True},
)

register(
    id="MiniGrid-KeyCorridor-S3-R3-v0",
    entry_point="minigrid.envs:KeyCorridorEnv",
    kwargs={"room_size": 3, "num_rows": 3},
)

register(
    id="MiniGrid-MultiRoom-N10-S10-v0",
    entry_point="minigrid.envs:MultiRoomEnv",
    kwargs={"minNumRooms": 10, "maxNumRooms": 10, "maxRoomSize": 10},
)

register(
    id="MiniGrid-MultiRoom-N7-S8-v0",
    entry_point="minigrid.envs:MultiRoomEnv",
    kwargs={"minNumRooms": 7, "maxNumRooms": 7, "maxRoomSize": 8},
)

register(
    id="MiniGrid-MultiRoom-N10-S4-v0",
    entry_point="minigrid.envs:MultiRoomEnv",
    kwargs={"minNumRooms": 10, "maxNumRooms": 10, "maxRoomSize": 4},
)


# register(
#     id="MiniGrid-ObstructedMaze-2Dlh-v0",
#     entry_point="minigrid.envs:ObstructedMazeEnv",
#     kwargs={"length": 2, "width": 2, "num_rows": 2, "num_cols": 2},
# )


register(
    id="MiniGrid-MultiRoom-N12-S10-v0",
    entry_point="minigrid.envs:MultiRoomEnv",
    kwargs={"minNumRooms": 12, "maxNumRooms": 12, "maxRoomSize": 10},
)

for task in tasks:
    env = gym.make(f'MiniGrid-{task}-v0')
    print(task, env.action_space)
    env = RGBImgObsWrapper(env, tile_size=128)
    obs, _ = env.reset()
    img = Image.fromarray(obs['image'])
    img.save(f'minigrid/{task}.png')
    env.close()
