
# Extension: Add LLM task parsing (Hugging Face model)

from transformers import pipeline, AutoTokenizer, AutoModelForSeq2SeqLM

# -------------------
# Load LLM and Tokenizer
# -------------------
model_name = "google/flan-t5-small"  # Lightweight and fast
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
llm = pipeline("text2text-generation", model=model, tokenizer=tokenizer)

# -------------------
# Parse Task from Natural Language
# -------------------
def parse_task(natural_input):
    prompt = f"Extract a clear task and time from this sentence: '{natural_input}'. Format as: TASK | YYYY-MM-DD HH:MM"
    result = llm(prompt, max_length=50, do_sample=False)[0]['generated_text']
    try:
        task, time_str = result.split(" | ")
        datetime.strptime(time_str.strip(), "%Y-%m-%d %H:%M")  # validate format
        return add_task(task.strip(), time_str.strip())
    except Exception as e:
        return f"Failed to parse: {result} (Error: {e})"

# Add to Gradio UI
with demo:
    gr.Markdown("## Smart Task Parser")
    natural_input = gr.Text(label="Task in natural language")
    smart_output = gr.Textbox(label="Parsed Output")
    smart_btn = gr.Button("Parse and Add Task")
    smart_btn.click(parse_task, inputs=[natural_input], outputs=smart_output)
