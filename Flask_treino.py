from app import app
import os

# arquivo principaçl, se tiver trabalhando com main, cria a variavel port, para que consiga
# do sistema operacional a nossa porta local - a porta que o servidor vai estar rodando
# se nao tiver nenhuma no heroku, pega a 5000, se tiver, pega a 0000 
if __name__ == 'main':
 port = int(os.getenv('PORT'), '5000')
 app.run(host='0.0.0.0', port = port)

 # Instalação gunicorn que possibilita o pyhton como serviço web