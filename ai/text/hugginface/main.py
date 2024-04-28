import time
from t5_processor import T5Processor

def main():
    # load text from date/chat4u.txt
    try:
        input_text = open("data/chat4u.txt", "r").read()
    except FileNotFoundError:
        print("File not found. Please run scraper.py to download the content first.")
        return
    except IOError:
        print("Error reading file. Please run scraper.py to download the content first.")
        return

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
    
