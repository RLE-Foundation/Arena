import gradio as gr

# 假设的Benchmark和Environment数据
benchmarks = {
    "Benchmark A": ["Environment 1", "Environment 2"],
    "Benchmark B": ["Environment 3", "Environment 4"],
    "Benchmark C": ["Environment 5", "Environment 6"]
}

def update_environments(benchmark):
    # 根据选择的 Benchmark 返回对应的 Environment 列表
    if benchmark in benchmarks:
        print(f"Updating environments for {benchmark}: {benchmarks[benchmark]}")
        return gr.update(choices=benchmarks[benchmark], value=None)  # 更新选项，并重置值为 None
    else:
        print("No environments found for the selected benchmark")
        return gr.update(choices=[], value=None)  # 如果没有匹配的 Benchmark，清空选项

def submit_model(github_username, benchmark, environment, training_steps, code_link):
    # 这里可以添加提交模型的逻辑
    return f"Submitted by {github_username}:\nBenchmark: {benchmark}\nEnvironment: {environment}\nTraining Steps: {training_steps}\nCode Link: {code_link}"

def clear_form():
    # 清空所有输入组件
    return [None, None, None, None, None]

with gr.Blocks(theme=gr.themes.Soft()) as demo:
    gr.Markdown("<center><h1 style='font-size: 40px;'>⚔️Reinforcement Learning Agent Arena⚔️</h1></center>")
    gr.Markdown("""
                # 📜📜📜 The workflow of RLArena
                # 🏆🏆🏆 Visit the leaderboard
                - Accelerate your RL research with the well-organized benchmark scores.
                # 💪💪💪 Submit your agent now!
                """)
    with gr.Row():
        with gr.Column():
            benchmark = gr.Dropdown(label="Benchmark", choices=list(benchmarks.keys()), info="Please select a benchmark.")
            environment = gr.Dropdown(label="Environment", choices=[], value=None, info="Please select an environment.")  # 初始化为空列表，值为 None
    
            training_steps = gr.Number(label="Training Steps", precision=0, info="Please enter the training steps.")
            code_link = gr.Textbox(label="Code Link", info="Example: https://github.com/username/repo")
            with gr.Row():
                submit_button = gr.Button("Submit", variant="primary")  # 使用 Soft 主题的主色调
                clear_button = gr.Button("Clear", variant="secondary")
        with gr.Column():
            output = gr.Textbox(label="Evaluation Result")
    
    # 监听 Benchmark 的变化，并更新 Environment 下拉菜单
    benchmark.change(
        fn=update_environments,  # 调用的函数
        inputs=benchmark,        # 输入是 Benchmark 的值
        outputs=environment      # 输出是 Environment 的下拉菜单
    )

    submit_button.click(submit_model, inputs=[benchmark, environment, training_steps, code_link], outputs=output)
    
    with gr.Row():
        # add multiple images with html
        html_images = """
        <div><br><br></div>

        # 🔥🔥🔥 Powered by
        <div style="display: flex; flex-wrap: wrap; gap: 10px; justify-content: left;">
          <div style="flex: 0 0 calc(25% - 10px); display: flex; justify-content: center; align-items: center;">
            <img src="/file=static/logo_polyu.png" alt="Image 1" style="max-width: 100%; height: auto;">
          </div>
          <div style="flex: 0 0 calc(25% - 10px); display: flex; justify-content: center; align-items: center;">
            <img src="/file=static/logo_sjtu.png" alt="Image 2" style="max-width: 100%; height: auto;">
          </div>
          <div style="flex: 0 0 calc(25% - 10px); display: flex; justify-content: center; align-items: center;">
            <img src="/file=static/logo_eias.png" alt="Image 3" style="max-width: 100%; height: auto;">
          </div>
          <div style="flex: 0 0 calc(25% - 10px); display: flex; justify-content: center; align-items: center;">
            <img src="/file=static/logo_idt.png" alt="Image 4" style="max-width: 100%; height: auto;">
          </div>
          <div style="flex: 0 0 calc(25% - 10px); display: flex; justify-content: center; align-items: center;">
            <img src="/file=static/logo_ustc.png" alt="Image 5" style="max-width: 100%; height: auto;">
          </div>
          <div style="flex: 0 0 calc(25% - 10px); display: flex; justify-content: center; align-items: center;">
            <img src="/file=static/logo_purdue.png" alt="Image 6" style="max-width: 100%; height: auto;">
          </div>
        </div>
        """
        gr.Markdown(html_images)
        
        
demo.launch(allowed_paths=["./"])