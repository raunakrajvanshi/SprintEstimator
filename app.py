from flask import Flask, render_template, request
from estimator import generate_prompt, get_estimation

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    estimation = ""
    if request.method == 'POST':
        description = request.form['description']
        criteria = request.form['criteria']
        team_size = request.form['team_size']
        dependencies = request.form['dependencies']
        risks = request.form['risks']

        prompt = generate_prompt(description, criteria, team_size, dependencies, risks)
        estimation = get_estimation(prompt)

    return render_template('index.html', estimation=estimation)

if __name__ == '__main__':
    app.run(debug=True)
