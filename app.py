import gradio as gr


def hello():
    return "Hello World"


demo = gr.Interface(fn=hello, inputs=None, outputs="text")
demo.launch()
