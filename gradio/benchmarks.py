import gradio as gr
import gymnasium as gym

benchmarks = {
    "Arcade Learning Environment": {
        'env': ['Breakout', 'Pong', 'Qbert', 'Seaquest', 'SpaceInvaders'],
        'version': ['NoFrameskip-v4'],
    },
    "Procgen": {
        'env': ['BigFish', 'BossFight', 'Chaser', 'Climber', 'CaveFlyer', 'CoinRun', 'Dodgeball', 'FruitBot',  
                'Heist', 'Jumper', 'Leaper', 'Maze', 'Miner', 'Ninja', 'Plunder', 'Starpilot'],
        'version': ['Easy', 'Hard'],
    },
    'DeepMind Control Suite': {
        'env': ['Humanoid_Stand', 'Humanoid_Walk', 'Humanoid_Run'],
        'version': ['State-based', 'Image-based'],
    },
}

def update_environments(benchmark):
    if benchmark in benchmarks:
        print(f"Updating environments for {benchmark}: {benchmarks[benchmark]}")
        return gr.update(choices=benchmarks[benchmark]['env'], value=None), gr.update(choices=benchmarks[benchmark]['version'], value=None)
    else:
        print("No environments found for the selected benchmark")
        return gr.update(choices=[], value=None), gr.update(choices=[], value=None)

def build_env(benchmark, environment, version):
    # if benchmark == "Arcade Learning Environment":
    #     env = gym.make(f"{environment}-{version}")
    # elif benchmark == "Procgen":
    #     env = gym.make(f"{environment}-{version}")
    return gym.make("CartPole-v1")
