from flask import Flask , render_template

app = Flask(__name__)


@app.route('/')
@app.route('/home')
@app.route('/index')
def main_page():  # put application's code here
    return render_template("index.html")

@app.route('/blog')
def blog_page():
    return 'This is blog page'

@app.route('/contact')
def contact_page():
    return 'This is contact page'

if __name__ == '__main__':
    app.run()
