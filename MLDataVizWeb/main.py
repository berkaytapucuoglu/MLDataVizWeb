from flask import Flask, render_template, request, jsonify, redirect, url_for
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Berkay2002!'
app.config['MYSQL_DB'] = 'capstone_project'

mysql = MySQL(app)

@app.route('/register', methods=['POST'])
def register():
    if 'username' in request.form and 'password' in request.form:
        # Get data from the form
        username = request.form['username']
        password = request.form['password']

        # Check if the user already exists in the database
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM users WHERE username = %s", (username,))
        existing_user = cur.fetchone()

        if existing_user:
            return jsonify({"message": "This email is already in use!"}), 400
        else:
            # Insert into the database
            cur.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, password))
            mysql.connection.commit()
            cur.close()

            return jsonify({"message": "Registration completed successfully!"}), 200
    else:
        return jsonify({"message": "Invalid request!"}), 400

@app.route('/login', methods=['POST'])
def login():
    if 'username' in request.form and 'password' in request.form:
        # Get data from the form
        username = request.form['username']
        password = request.form['password']

        # Query the user from the database
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM users WHERE username = %s AND password = %s", (username, password))
        user = cur.fetchone()
        cur.close()

        if user:
            # Return JSON response on successful login
            return jsonify({"message": "Login successful!"}), 200
        else:
            # Return JSON response on failed login
            return jsonify({"message": "Invaild Email or Password"}), 401
    else:
        return jsonify({"message": "Invalid request!"}), 400


@app.route('/exercise/<int:participant_id>/<int:exercise_number>')
def exercise(participant_id, exercise_number):
    cur = mysql.connection.cursor()
    sql = """
        SELECT e.exercise_name, e.graph_path_1, e.graph_path_2, e.graph_path_3, e.graph_path_4, 
               p.name, p.weight, p.height
        FROM exercises e
        JOIN participants p ON e.participant_id = p.id
        WHERE e.id = %s AND p.id = %s
    """
    cur.execute(sql, (exercise_number, participant_id))
    result = cur.fetchone()
    cur.close()

    if not result:
        return jsonify({"message": "Exercise not found"}), 404

    # Format the result as a dictionary
    exercise_data = {
        "exercise_name": result[0],
        "graph_path_1": result[1],
        "graph_path_2": result[2],
        "graph_path_3": result[3],
        "graph_path_4": result[4],
        "name": result[5],
        "weight": result[6],
        "height": result[7]
    }

    return render_template('exercise_results.html', exercise=exercise_data)

@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('q')
    if not query:
        return jsonify({"message": "No search query provided"}), 400

    cur = mysql.connection.cursor()
    sql = """
        SELECT id, name FROM participants
        WHERE name LIKE %s
    """
    search_query = f"%{query}%"
    cur.execute(sql, (search_query,))
    results = cur.fetchall()
    cur.close()

    if not results:
        return render_template('search_results.html', message="No results found"), 404

    search_results = []
    for row in results:
        search_results.append({
            "id": row[0],
            "name": row[1]
        })

    return render_template('search_results.html', results=search_results)







@app.route('/main_page')
def main_page():
    return render_template('main_page.html')

@app.route('/how_it_works')
def how_it_works():
    return render_template('how_it_works.html')


@app.route('/')
def index():
    return render_template('project.html')

if __name__ == '__main__':
    app.run(debug=True)
