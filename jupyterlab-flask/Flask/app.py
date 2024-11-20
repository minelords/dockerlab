from flask import Flask, render_template,request
app1 = Flask(__name__)
#app1
@app1.route('/')
def home():
    username=request.args.get('username','Guest')
    return render_template('home.html',username=username)

@app1.route('/about')
def about():
    return render_template('about.html')

@app1.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app1.run(debug=True)                         
