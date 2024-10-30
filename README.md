versão python 3.11.5 depois de ter o python instalado e feito a clonagem dos arquivos utilize a linha de código a seguir no terminal 
na ORDEM SEGUIDA:

Configure o ambiente virtual:

python -m venv env

source env/bin/activate  # ou env\Scripts\activate no Windows


Instale as dependências:

pip install -r requirements.txt


Execute as migrações e inicie o servidor:

python manage.py makemigrations
python manage.py migrate
python manage.py runserver
