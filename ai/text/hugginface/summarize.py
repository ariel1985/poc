from transformers import T5Tokenizer, T5ForConditionalGeneration

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

# if main
if __name__ == "__main__":
    # load text from date/chat4u.txt
    input_text = open("data/chat4u.txt", "r").read()

    # print first 1000 characters

    print('\n*********Input Text*********')
    print(input_text[:100])

    # Generate summary
    summary = t5_summarize(input_text)

    print('\n*********Summary*********')
    print(summary)
