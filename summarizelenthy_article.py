from transformers import pipeline

def summarize_article(text):
    summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
    summary = summarizer(text, max_length=130, min_length=30, do_sample=False)
    return summary[0]['summary_text']

# Example usage
if __name__ == "__main__":
    print("Paste your article below (press Enter then CTRL+D to finish):")
    try:
        text = ""
        while True:
            line = input()
            text += line + "\n"
    except EOFError:
        pass

    if text.strip():
        print("\nSummary:\n")
        print(summarize_article(text))
    else:
        print("No text provided.")
