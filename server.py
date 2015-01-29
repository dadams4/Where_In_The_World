from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def mainIndex():
    return render_template('index.html', selectedMenu='Home')

if __name__ == '__main__':
    app.debug=True
    app.run(host='0.0.0.0', port=8080)
