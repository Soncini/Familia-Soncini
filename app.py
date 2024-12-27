from flask import Flask, render_template

app = Flask(__name__)

# Dados das pessoas (exemplo)
pessoas = [
    {'id': 1, 'nome': 'Luciano Soncini', 'foto': 'person1.jpg', 'informacao': 'Luciano é um técnico de informática e empresário.'},
    {'id': 2, 'nome': 'Maria Silva', 'foto': 'person2.jpg', 'informacao': 'Maria é engenheira de software.'},
    {'id': 3, 'nome': 'João Souza', 'foto': 'person3.jpg', 'informacao': 'João é médico e especialista em cardiologia.'},
    {'id': 4, 'nome': 'Gilbran Soncini Da Rosa', 'foto': 'person4.jpg', 'informacao': 'Gilbran é advogado.', 'formacao': 'Formação em Direito'},
    {'id': 5, 'nome': 'Lauro Soncini Junior', 'foto': 'person5.jpg', 'informacao': 'Lauro é engenheiro.', 'formacao': 'Formação em Engenharia Civil'},
    {'id': 6, 'nome': 'Mariana Soncini', 'foto': 'person6.jpg', 'informacao': 'Mariana é professora.', 'formacao': 'Formação em Pedagogia'},
    {'id': 7, 'nome': 'Lino Soncini Junior', 'foto': 'person7.jpg', 'informacao': 'Lino é empresário.', 'formacao': 'Formação em Administração de Empresas'},
    {'id': 8, 'nome': 'Isabela Soncini Da Costa Lerina', 'foto': 'person8.jpg', 'informacao': 'Isabela é médica.', 'formacao': 'Formação em Medicina'},
    {'id': 9, 'nome': 'Ana Silveira Soncini', 'foto': 'person9.jpg', 'informacao': 'Ana é designer gráfica.', 'formacao': 'Formação em Design Gráfico'},
    {'id': 10, 'nome': 'Felipe Silveira Soncini', 'foto': 'person10.jpg', 'informacao': 'Felipe é programador.', 'formacao': 'Formação em Ciência da Computação'},
    {'id': 11, 'nome': 'Alessi Eduardo Brancher Soncini', 'foto': 'person11.jpg', 'informacao': 'Alessi é gestor financeiro.', 'formacao': 'Formação em Economia'},
    {'id': 12, 'nome': 'Mariana Soncini Lerina Kuerten', 'foto': 'person12.jpg', 'informacao': 'Mariana é arquiteta.', 'formacao': 'Formação em Arquitetura'},
    {'id': 13, 'nome': 'Marina Dutra Soncini', 'foto': 'person13.jpg', 'informacao': 'Marina é psicóloga.', 'formacao': 'Formação em Psicologia'},
    {'id': 14, 'nome': 'Lia Soncini Lerina', 'foto': 'person14.jpg', 'informacao': 'Lia é nutricionista.', 'formacao': 'Formação em Nutrição'},
    {'id': 15, 'nome': 'Bruno Da Silva Soncini', 'foto': 'person15.jpg', 'informacao': 'Bruno é contador.', 'formacao': 'Formação em Ciências Contábeis'},
    {'id': 16, 'nome': 'Vanessa Cristina Soncini Radtke', 'foto': 'person16.jpg', 'informacao': 'Vanessa é advogada.', 'formacao': 'Formação em Direito'},
    {'id': 17, 'nome': 'Maria Aparecida Brigido Soncini', 'foto': 'person17.jpg', 'informacao': 'Maria Aparecida é professora.', 'formacao': 'Formação em Letras'},
    {'id': 18, 'nome': 'Aline Soncini', 'foto': 'person18.jpg', 'informacao': 'Aline é psicóloga.', 'formacao': 'Formação em Psicologia'},
    {'id': 19, 'nome': 'Luisa Soncini Radtke', 'foto': 'person19.jpg', 'informacao': 'Luisa é médica.', 'formacao': 'Formação em Medicina'},
    {'id': 20, 'nome': 'Luíza Soncini Da Costa Lerina', 'foto': 'person20.jpg', 'informacao': 'Luíza é engenheira ambiental.', 'formacao': 'Formação em Engenharia Ambiental'},
    {'id': 21, 'nome': 'Maria Lucia Soncini Da Silva', 'foto': 'person21.jpg', 'informacao': 'Maria Lucia é pedagoga.', 'formacao': 'Formação em Pedagogia'},
    {'id': 22, 'nome': 'Libório Soncini', 'foto': 'person22.jpg', 'informacao': 'Libório é agricultor.', 'formacao': 'Formação em Agropecuária'},
    {'id': 23, 'nome': 'Claudio Soncini', 'foto': 'person23.jpg', 'informacao': 'Claudio é empresário.', 'formacao': 'Formação em Administração'},
    {'id': 24, 'nome': 'Gabriela Gomes Soncini', 'foto': 'person24.jpg', 'informacao': 'Gabriela é designer de interiores.', 'formacao': 'Formação em Design de Interiores'},
    {'id': 25, 'nome': 'Giulia Heineck De Vasconcelos Soncin', 'foto': 'person25.jpg', 'informacao': 'Giulia é arquiteta.', 'formacao': 'Formação em Arquitetura'},
    {'id': 26, 'nome': 'Thaise Cristina Brancher Soncini', 'foto': 'person26.jpg', 'informacao': 'Thaise é engenheira.', 'formacao': 'Formação em Engenharia de Produção'},
    {'id': 27, 'nome': 'George Ronald Soncini Da Rosa', 'foto': 'person27.jpg', 'informacao': 'George é técnico em informática.', 'formacao': 'Formação em TI'},
    {'id': 28, 'nome': 'Cristina Silveira Soncini Buratto', 'foto': 'person28.jpg', 'informacao': 'Cristina é fisioterapeuta.', 'formacao': 'Formação em Fisioterapia'},
    {'id': 29, 'nome': 'Juliana Da Silva Soncini Mund', 'foto': 'person29.jpg', 'informacao': 'Juliana é farmacêutica.', 'formacao': 'Formação em Farmácia'},
    {'id': 30, 'nome': 'Sérgio Soncini', 'foto': 'person30.jpg', 'informacao': 'Sérgio é médico.', 'formacao': 'Formação em Medicina'}
]

@app.route('/')
def index():
    return render_template('index.html', pessoas=pessoas)

@app.route('/')
def inicio():
    return render_template('inicio.html')

@app.route('/historia')
def historia():
    return render_template('historia.html')


@app.route('/arvore_genealogica')
def arvore_genealogica():
    return render_template('arvore_genealogica.html')

@app.route('/contato')
def contato():
    return render_template('contato.html')

@app.route('/pessoa/<int:id>')
def pessoa(id):
    pessoa_encontrada = next((pessoa for pessoa in pessoas if pessoa['id'] == id), None)
    if pessoa_encontrada:
        return render_template('pessoa.html', pessoa=pessoa_encontrada)
    return "Pessoa não encontrada", 404

if __name__ == "__main__":
   # app.run(debug=True)
    app.run(host='10.0.0.170', port=5000, debug=True)
