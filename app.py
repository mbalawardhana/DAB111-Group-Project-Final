from flask import Flask, render_template
import sqlite3
import pathlib 

#always use the correct db path 
base_path = pathlib.Path(r'C:\Users\MalithaBalawardana\Downloads\DAB11-Group-Project\DAB11-Group-Project')
db_name = "heart_disease.db"
db_path = base_path / db_name
print(db_path)

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/data")
def data():
    
    con = sqlite3.connect(db_path)
    cursor = con.cursor()
    data = cursor.execute("SELECT * FROM heart_disease Limit 50").fetchall()
    con.close()
    
    
    column_headers = ['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg', 'thalach',
       'exang', 'oldpeak', 'slope']


    
    return render_template("data.html", column=column_headers, data=data)

if __name__ == "__main__":
    #need to use port 8000 because on mac port 5000 which is the defualt port has been used. #this project was inistially done on a mac 
    app.run(port=8000, debug=True)
