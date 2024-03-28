from transformers import T5Tokenizer, T5ForConditionalGeneration
import time

def t5_ask_question(text, question):
    # Assuming tokenizer and model are already loaded as shown above
    tokenizer = T5Tokenizer.from_pretrained('t5-base')
    model = T5ForConditionalGeneration.from_pretrained('t5-base')
    
    # Prepare input with question
    input_text = f"question: {question} context: {text}"
    inputs = tokenizer.encode(input_text, return_tensors='pt', max_length=512, truncation=True)

    # Generate answer
    answer_ids = model.generate(inputs, max_length=50, num_beams=4, early_stopping=True)

    # Decode answer
    answer = tokenizer.decode(answer_ids[0], skip_special_tokens=True)

    return answer

def t5_summarize(text):
    # Load pre-trained T5 tokenizer and model
    tokenizer = T5Tokenizer.from_pretrained('t5-base')
    model = T5ForConditionalGeneration.from_pretrained('t5-base')

    # Tokenize input text
    inputs = tokenizer.encode("summarize: " + text, return_tensors='pt', max_length=512, truncation=True)

    # Generate summary
    summary_ids = model.generate(inputs, max_length=150, min_length=40, length_penalty=2.0, num_beams=4, early_stopping=True)

    # Decode summary
    summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)

    return summary

def main():
    # load text from date/chat4u.txt
    input_text = open("data/chat4u.txt", "r").read()

    # print first 1000 characters

    print('\n*********Input Text*********')
    print(input_text[:100])

    # Generate summary
    summary = t5_summarize(input_text)

    print('\n*********Summary*********')
    print(summary)

    # Example question
    question = "What is the main topic of the summarized text?"
    answer = t5_ask_question(summary, question)
    print('\n*********Answer*********')
    print(answer)
    
if __name__ == "__main__":
    
    start_time = time.time()
    main()
    print("--- script took %s seconds ---" % (time.time() - start_time))
    
