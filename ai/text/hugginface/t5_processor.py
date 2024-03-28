from transformers import T5Tokenizer, T5ForConditionalGeneration


class T5Processor:
    """A processor using the T5 model for question answering and summarization."""

    def __init__(self, model_name='t5-base'):
        """Initialize the processor with the given model name."""
        # Load pre-trained T5 tokenizer and model
        self.tokenizer = T5Tokenizer.from_pretrained(model_name)
        self.model = T5ForConditionalGeneration.from_pretrained(model_name)

    def t5_ask_question(self, text, question):
    
        # Prepare input with question
        input_text = f"question: {question} context: {text}"
        inputs = self.tokenizer.encode(input_text, return_tensors='pt', max_length=512, truncation=True)

        # Generate answer
        answer_ids = self.model.generate(inputs, max_length=50, num_beams=4, early_stopping=True)

        # Decode answer
        answer = self.tokenizer.decode(answer_ids[0], skip_special_tokens=True)

        return answer

    def t5_summarize(self, text):

        # Tokenize input text
        inputs = self.tokenizer.encode("summarize: " + text, return_tensors='pt', max_length=512, truncation=True)

        # Generate summary
        summary_ids = self.model.generate(inputs, max_length=150, min_length=40, length_penalty=2.0, num_beams=4, early_stopping=True)

        # Decode summary
        summary = self.tokenizer.decode(summary_ids[0], skip_special_tokens=True)

        return summary
