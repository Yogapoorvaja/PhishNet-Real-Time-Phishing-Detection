from flask import Flask, render_template, request
from phising_checker import check_phishing
from cloaking_detector import check_cloaking

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = {}
    if request.method == 'POST':
        url = request.form['url']
        phishing_result = check_phishing(url)
        cloaking_result = check_cloaking(url)
        result = {
            'url': url,
            'phishing_score': phishing_result['score'],
            'phishing_reasons': phishing_result['reasons'],
            'cloaking_suspected': cloaking_result['cloaking'],
            'cloaking_difference': cloaking_result['difference']
        }
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
