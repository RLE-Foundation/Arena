import gymnasium as gym
import argparse

def run_env(action=None):
    env = gym.make("CartPole-v1")
    state = env.reset()
    # 
    while True:
        if action is None:
            action = int(input("Enter action (0 or 1): "))
        state, reward, done, trunc, info = env.step(action)
        print(f"State: {state}, Reward: {reward}, Done: {done}")
        if done:
            break

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="RL Environment")
    parser.add_argument("--action", type=int, help="Action to take (0 or 1)")
    args = parser.parse_args()
    run_env(action=args.action)