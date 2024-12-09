global lista_spesa

from flask import Flask, render_template

from flask_sqlalchemy import SQLAlchemy


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///lista_spesa.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
with app.app_context():
db.create_all()






app = Flask(__name__)

#rotta principale
@app.route('/')
def home():
    return render_template("index.html")





# route per aggiungere elementi alla lista
@app.route('/aggiungi', methods=['POST'])
def aggiungi():
    elemento = request.form['elemento']
    if elemento:
        lista_spesa.append(elemento)
    return redirect(url_for('home'))


#route per rimuovere elementi grazie all'indice
@app.route('/rimuovi/<int:indice>', methods=['POST'])
def rimuovi(indice):
    if 0 <= indice < len(lista_spesa):
        lista_spesa.pop(indice)
    return redirect(url_for('home'))















#avvio dell'app Flask




if __name__ == '__main__':
    app.run(debug=True)
























