from flask import Flask, render_template, request
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/summarize', methods=['POST'])
def summarize():
    text = request.form['text']
    
    # Your text_summarizer function code goes here
    def text_summerizer(texts):
        stop_words = set(stopwords.words("english"))
        stop_words.add('.')
        words = word_tokenize(text=texts)
        freq_table = dict()
        for i in words:
            i = i.lower()
            if i in stop_words:
                continue
            if i in freq_table:
                freq_table[i] += 1
            else:
                freq_table[i] = 1
        sentences = sent_tokenize(text = texts)
        sentenceval = dict()
        for sentence in sentences:
            for word,freq in freq_table.items():
                if word in sentence.lower():
                    if sentence in sentenceval:
                        sentenceval[sentence] += freq
                    else:
                        sentenceval[sentence] = freq
        sumValues = 0
        for sentence in sentenceval:
            sumValues += sentenceval[sentence]
        # Average value of a sentence from the original text
            
        average = int(sumValues / len(sentenceval))
            
        # Storing sentences into our summary.
        summary = ''
        # summary = []
        for sentence in sentences:
            if (sentence in sentenceval) and (sentenceval[sentence] > (1.25 * average)):
                summary += " " + sentence
        return summary

    summary = text_summerizer(text)
    return render_template('result.html', summary=summary)
        # Call the text_summarizer function and get the summary sentences
    # summary_sentences = text_summerizer(text)
    
    # # Format the summary sentences as bullet points
    # summary_html = '<ul>'
    # for sentence in summary_sentences:
    #     summary_html += f'<li>{sentence}</li>'
    # summary_html += '</ul>'
    
    return summary_html
if __name__ == '__main__':
    nltk.download('stopwords')
    nltk.download('punkt')
    app.run(debug=True)
