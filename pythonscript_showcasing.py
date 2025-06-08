#pip install transformers torch

from transformers import pipeline

def summarize_text(text):
    # Load summarization pipeline
    summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
    # Generate summary
    summary = summarizer(text, max_length=100, min_length=30, do_sample=False)
    return summary[0]['summary_text']

def main():
    print("=== TEXT SUMMARIZER ===")
    print("Paste your article below. Press Enter, then Ctrl+Z (Windows) or Ctrl+D (Linux/Mac) to submit:\n")

    # Read multiline input
    try:
        input_text = ""
        while True:
            line = input()
            input_text += line + "\n"
    except EOFError:
        pass

    input_text = input_text.strip()
    if not input_text:
        print("❌ No input text provided.")
        return

    print("\n--- Original Text ---")
    print(input_text)

    print("\n--- Summary ---")
    summary = summarize_text(input_text)
    print(summary)

if __name__ == "__main__":
    main()
