import requests

# 禁用代理
session = requests.Session()
session.trust_env = False  # 忽略系统代理

def download_gif(url, save_path):
    response = session.get(url)
    if response.status_code == 200:
        with open(save_path, 'wb') as file:
            file.write(response.content)
        print(f"GIF已成功下载并保存到 {save_path}")
    else:
        print(f"下载失败，状态码: {response.status_code}")

# # 示例链接
# gif_url = "https://ale.farama.org/_images/alien.gif"
# # 保存路径
# save_path = "alien.gif"

for env in ['bigfish', 'caveflyer', 'chaser', 'climber', 'dodgeball', 'fruitbot', 'heist', 'jumper', 'leaper', 'maze', 'miner', 'ninja', 'plunder', 'starpilot']:
    gif_url = f"https://github.com/openai/procgen/blob/master/screenshots/{env}.png"
    save_path = f"assets/images/procgen/{env}.png"
    download_gif(gif_url, save_path)

