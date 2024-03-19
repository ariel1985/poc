from transformers import BertTokenizer, BertForSequenceClassification
import torch

def bert_summarize(text):
    # Load pre-trained BERT tokenizer
    tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')

    # Tokenize input text
    inputs = tokenizer(text, return_tensors='pt', max_length=512, truncation=True)

    # Load pre-trained BERT model for sequence classification
    model = BertForSequenceClassification.from_pretrained('bert-base-uncased')

    # Get logits (scores) for each token
    outputs = model(**inputs)

    # Compute softmax to get probabilities
    probabilities = torch.softmax(outputs.logits, dim=1)

    # Extract the most probable token indices for summary
    summary_token_indices = torch.argmax(probabilities, dim=1)

    # Decode token indices back to text
    summary_tokens = tokenizer.convert_ids_to_tokens(summary_token_indices.squeeze())

    # Convert tokens back to a summary string
    summary = tokenizer.convert_tokens_to_string(summary_tokens)

    return summary

# Example text
input_text = """
    Add your text here...
"""

# Generate summary
summary = bert_summarize(input_text)

print(summary)
