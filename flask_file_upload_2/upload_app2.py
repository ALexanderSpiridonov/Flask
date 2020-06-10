from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import pandas as pd

app = Flask(__name__)
app.config['SECRET_KEY'] = '60d198c06f34330635165c34358eedc4'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///filestorage.db'
db = SQLAlchemy(app)


class FileContent(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(300))
    data = db.Column(db.LargeBinary)

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['inputFile']

    #newFile = FileContent(name=file.filename, data=file.read())
    data_frame = pd.read_excel(file, sheet_name=2)
    data_frame['User_id'] = 'test_user_id'
    # db.session.add(newFile)
    # db.session.commit()

    return data_frame.to_html()


# @app.route('/data', methods=['GET', 'POST'])
# def data():
#     if request.method == 'POST':
#         file = request.form['upload-file']
#         path_to_file = "files/" + file
#         data = pd.read_excel(path_to_file)
#         data = data.dropna(how='all', axis=0)
#         data = data.dropna(how='all', axis=1)
#         data.index = range(len(data))
#         data = prev_val_fill(data)
#         return render_template('data.html', data = data.to_dict())  #data.to_html()


if __name__ == '__main__':
    app.run(debug=True)