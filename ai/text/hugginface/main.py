from transformers import T5Tokenizer, T5ForConditionalGeneration
import time


class T5Processor:
    
    def __init__(self):
        # Load pre-trained T5 tokenizer and model
        self.tokenizer = T5Tokenizer.from_pretrained('t5-base')
        self.model = T5ForConditionalGeneration.from_pretrained('t5-base')

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

def main():
    # load text from date/chat4u.txt
    input_text = open("data/chat4u.html", "r").read()

    print('\n*********Input Text*********')
    # print first 1000 characters
    print(input_text[:10])

    proccessor = T5Processor()

    # Generate summary
    summary = proccessor.t5_summarize(input_text)

    print('\n*********Summary*********')
    print(summary)

    # Example question
    print('\n*********Question*********')
    # question = "What is the main topic of the summarized text?"
    question = "What is the company name?"
    print(question)
    
    answer = proccessor.t5_ask_question(summary, question)
    
    print('\n*********Answer*********')
    print(answer)
    
if __name__ == "__main__":
    
    start_time = time.time()
    main()
    print("\n--- script took %s seconds ---" % (time.time() - start_time))
    
