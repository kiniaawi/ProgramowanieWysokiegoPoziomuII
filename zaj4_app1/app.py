from flask import Flask, render_template

app = Flask(__name__)

# Dane użytkowników
users = {
    1: {"name": "Ala", "age": 22},
    2: {"name": "Bartek", "age": 25},
    3: {"name": "Celina", "age": 30}
}

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/users')
def user_list():
    return render_template('users.html', users=users)

@app.route('/user/<int:user_id>')
def user_profile(user_id):
    user = users.get(user_id)
    if user:
        return render_template('user_profile.html', user=user, user_id=user_id)
    else:
        return render_template('user_not_found.html', user_id=user_id)

if __name__ == '__main__':
    app.run(debug=True)