from flask import Flask, redirect, url_for, request, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')
@app.route('/success/<name>')
def success(name):
    return f'Welcome, {name}!'

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form.get('nm')  # Mengambil nilai 'nm' dari form
        if not user:  # Validasi jika user kosong
            return "Error: Name is required!", 400  # Kirim error jika nama kosong
        return redirect(url_for('success', name=user))
    else:
        user = request.args.get('nm')  # Mengambil nilai 'nm' dari query parameter
        if not user:  # Validasi jika user kosong
            return "Error: Name is required!", 400  # Kirim error jika nama kosong
        return redirect(url_for('success', name=user))

if __name__ == '__main__':
    app.run(debug=True)
