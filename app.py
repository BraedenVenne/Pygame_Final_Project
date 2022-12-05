from flask import Flask, render_template
from models.scores import Score

app = Flask(__name__)

# route for the home page
@app.route('/')
def scoreboard():
    score = Score('scores.json')
    return render_template('scoreboard.html', score=score)

if __name__ == '__main__':
    app.run(debug=True)
