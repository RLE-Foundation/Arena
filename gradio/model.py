import gradio as gr
import torch as th
import numpy as np
from benchmarks import build_env

def submit_model(github_username, 
                 benchmark, 
                 environment, 
                 version, 
                 training_steps, 
                 code_link,
                 model_uploader
                 ):
    avg_episode_rewards = 0
    success_msg = f"""
    INFO: Submitted by {github_username}:
    INFO: Benchmark: {benchmark}
    INFO: Environment: {environment}
    INFO: Version: {version}
    INFO: Training Steps: {training_steps}
    INFO: Code Link: {code_link}
    INFO: Final Score: {avg_episode_rewards}
    """
    username_error_msg = f"""
    ERROR: The GitHub username should be consistent with the code link!
    """

    model_none_error_msg = f"""
    ERROR: No model uploaded!
    """

    # check if username is valid
    if github_username.lower() not in code_link.lower():
        return username_error_msg
    if model_uploader is None:
        return model_none_error_msg
    
    episode_rewards = evaluate_model(model_uploader, benchmark, environment, version)
    avg_episode_rewards = np.mean(episode_rewards)

    return success_msg

def evaluate_model(model_uploader, benchmark, environment, version):
    env = build_env(benchmark, environment, version)
    print(env)

    episode_rewards = []

    obs, info = env.reset()
    while len(episode_rewards) < 100:
        # action = model_uploader.predict(obs)
        action = env.action_space.sample()
        obs, reward, terminated, truncated, info = env.step(action)
        print(reward)
        episode_rewards.append(reward)

        if terminated or truncated:
            obs, info = env.reset()

    return episode_rewards

