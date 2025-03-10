import gradio as gr

# 假设的Benchmark和Environment数据
benchmarks = {
    "Benchmark A": ["Environment 1", "Environment 2"],
    "Benchmark B": ["Environment 3", "Environment 4"],
    "Benchmark C": ["Environment 5", "Environment 6"]
}

def update_environments(benchmark):
    return gr.Dropdown.update(choices=benchmarks.get(benchmark, []))

def submit_model(github_username, benchmark, environment, training_steps, code_link):
    # 这里可以添加提交模型的逻辑
    return f"Submitted by {github_username}:\nBenchmark: {benchmark}\nEnvironment: {environment}\nTraining Steps: {training_steps}\nCode Link: {code_link}"

with gr.Blocks() as demo:
    gr.Markdown("## Model Submission for Review")
    
    with gr.Row():
        github_username = gr.Textbox(label="Github Username")
        benchmark = gr.Dropdown(label="Benchmark", choices=list(benchmarks.keys()))
        environment = gr.Dropdown(label="Environment")
        training_steps = gr.Number(label="Training Steps", precision=0)
        code_link = gr.Textbox(label="Code Link")
    
    benchmark.change(update_environments, inputs=benchmark, outputs=environment)
    
    submit_button = gr.Button("Submit")
    output = gr.Textbox(label="Submission Result")
    
    submit_button.click(submit_model, inputs=[github_username, benchmark, environment, training_steps, code_link], outputs=output)

demo.launch()