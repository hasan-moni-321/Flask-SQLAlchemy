from flask import Flask, render_template, request  
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
engine = create_engine('sqlite:///college.db', echo = True)
meta = MetaData()


app = Flask(__name__) 


students = Table(
   'students', meta, 
   Column('id', Integer, primary_key = True), 
   Column('name', String), 
   Column('city', String),
   Column('address', String), 
   Column('pin', String)  
)
meta.create_all(engine)


@app.route('/') 
def home(): 
    return render_template("student_info.html") 


@app.route('/result', methods=['POST', 'GET']) 
def stu_info(): 
    if request.method == 'POST': 
        name = request.form['name']
        city = request.form['city']
        address = request.form['address']
        pin = request.form['pin'] 

        try: 
            ins = students.insert().values(name=name, city=city, address=address, pin=pin) 
            conn = engine.connect() 
            result = conn.execute(ins) 
            msg = "Data inserted" 
        except: 
            msg = "Something wrong in inserting of the data"  
        finally: 
            return render_template('result.html', msg) 

if __name__ == '__main__': 
    app.run(debug=True)  

