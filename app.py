from flask import Flask, render_template


app = Flask(__name__)


# Create homepage/welcome page


@app.route('/')
def root():
    return render_template('home_page.html')


@app.route('/neets')
def neets():
    return render_template('Neets.html')


@app.route('/volumes')
def volumes():
    return render_template('volumes.html')


@app.route('/bibs')
def bibs():
    return render_template('bibs.html')


if __name__ == '__main__':
    app.run(debug=True)

