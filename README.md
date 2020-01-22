# Como executar o projeto

1. faça o git clone 
	
	```
	git clone https://github.com/barueri-alunos/loja-barueri-api.git
	```

1. entre na pasta do projeto
	
	```
	cd loja-barueri-api
	```

1. crie o ambiente virtual
	
	```
	python -m venv venv
	```

1. ative o ambiente virtual
	
	```
	./venv/Scripts/activate 
	```

1. installe as dependencias
	
	```
	pip install -r requirements.txt
	```

1. faça as migrates
	
	```
	python manage.py migrate
	```

1. execute o servidor do django
	
	```
	python manage.py runserver
	```

