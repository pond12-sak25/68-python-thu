from flask import Flask , render_template_string
app = Flask(__name__)

html_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h1>hi</h1>
</body>
</html>
"""
@app.route('/')
def home():
    return render_template_string(html_template, name="Hunsen")
@app.route('/greet/<name>')
def greet(name):
    return render_template_string(html_template, name=name)
if __name__ == '__main__':
    app.run(debug=True)