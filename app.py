global lista_spesa

from flask import Flask, render_template,redirect, url_for, request

from flask_sqlalchemy import SQLAlchemy
from models import db,ListaSpesa


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///lista_spesa.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)


with app.app_context():
    db.create_all()







#rotta principale
@app.route('/')
def home():
    lista_spesa = ListaSpesa.query.all() #sto ottenendo tutta la tabella del database per utilizzarla.
    return render_template('index.html', lista=lista_spesa)





# route per aggiungere elementi alla lista
@app.route('/aggiungi', methods=['POST'])
def aggiungi():
    elemento = request.form['elemento']
    if elemento:
        
        nuovo_elemento = ListaSpesa(elemento=elemento) #assegniamo l'elemento chiesto dall'utente nel database
        db.session.add(nuovo_elemento) #aggiungiamo alla sessione corrente del database l'elemento dell'utente
        db.session.commit() #invio dei dati nella sessione del database
    
    
    return redirect(url_for('home'))


#route per rimuovere elementi grazie all'indice
@app.route('/rimuovi/<int:indice>', methods=['POST'])
def rimuovi(indice):
    elemento = ListaSpesa.query.get_or_404(indice) #otteniamo l'indice dell'elemento
    db.session.delete(elemento) #eliminiamo l'elemento con l'indice venuto per ultimo
    db.session.commit() #iviamo i dati nella sessione corrente del database
    
    
    return redirect(url_for('home'))




@app.route('/svuota', methods=['POST'])
def svuota():
    ListaSpesa.query.delete() #ultimo elemento dell'utente eliminato.
    db.session.commit() #assicurazione dell'eliminazione dell'elemento sull'app
    
    return redirect(url_for('home'))








#avvio dell'app Flask




if __name__ == '__main__':
    app.run(debug=True)
























