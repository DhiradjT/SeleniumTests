from flask import Flask, render_template, request

#flask extensie

app = Flask(__name__, template_folder='templates')
logs = []

@app.route('/')
def index():
    return render_template('index.html', logs=logs)

@app.route('/recieve_logs', methods=['POST'])
def recieve_logs():
    data = request.get_json()
    logs.append(data['log'])
    return 'Logs recieved successfully!'

if __name__ == '__main__':
    app.run(debug=True)


