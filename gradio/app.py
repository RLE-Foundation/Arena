import gradio as gr
from benchmarks import benchmarks, update_environments
from model import submit_model

def clear_form():
    return [None, None, None, None, None, None]

with gr.Blocks(theme=gr.themes.Soft()) as demo:
    with gr.Row():
        with gr.Column(scale=2):
            with gr.Row():
                github_username = gr.Textbox(label="Github Username", info="Please enter your github username, e.g., username.")
                benchmark = gr.Dropdown(label="Benchmark", choices=list(benchmarks.keys()), value=None, info="Please select a benchmark, e.g., Procgen.")
            with gr.Row():
                environment = gr.Dropdown(label="Environment", choices=[], value=None, info="Please select an environment, e.g., Miner.")
                version = gr.Dropdown(label="Version", choices=[], value=None, info="Please select a version, e.g., v0.")
            with gr.Row():
                training_steps = gr.Number(label="Training Steps", precision=0, info="Please enter the training steps, e.g., 1000000.")
                code_link = gr.Textbox(label="Code Link", info="Example: https://github.com/username/repo, the link should be accessible.")
            with gr.Row():
                submit_button = gr.Button("Submit", variant="primary") 
                clear_button = gr.Button("Clear", variant="stop")
        with gr.Column(scale=1):
            # file uploader
            model_uploader = gr.File(label="Upload the agent here!")
            output = gr.Textbox(label="Evaluation Result")
    
    benchmark.change(
        fn=update_environments,  
        inputs=benchmark,
        outputs=[environment, version]
    )

    submit_button.click(submit_model, inputs=[github_username, benchmark, environment, version, training_steps, code_link, model_uploader], outputs=output)
    clear_button.click(clear_form, inputs=[], outputs=[github_username, benchmark, environment, version, training_steps, code_link])

        
demo.launch(allowed_paths=["./"])