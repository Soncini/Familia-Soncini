from flask import Flask, render_template
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# Carregar a imagem
img = mpimg.imread("Projeto_Familia_Soncini/static/img/person1.jpg")

# Mostrar a imagem
#plt.imshow(img)
#plt.axis('off')  # Esconder os eixos
#plt.show()

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/')
def inicio():
    return render_template('inicio.html')

@app.route('/historia')
def historia():
    return render_template('historia.html')

@app.route('/pessoa')
def pessoa():
    return render_template('pessoa.html')


@app.route('/arvore_genealogica')
def arvore_genealogica():
    return render_template('arvore_genealogica.html')

@app.route('/contato')
def contato():
    return render_template('contato.html')



if __name__ == "__main__":
    app.run(debug=True)
    
