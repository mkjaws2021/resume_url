from flask import Flask,render_template

app = Flask(__name__)
print(type(app))

@app.route("/")
def hello_world():
    return render_template(template_name_or_list='resume_url.html')

if __name__ == '__main__':
    app.run(debug=True)