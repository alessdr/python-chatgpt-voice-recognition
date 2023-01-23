# Integrando Python com ChatGPT e Voz

### Descrição

Este é um exemplo bem simplificado de como podemos utilizar o ChatGPT de dentro de uma aplicação Python, com poucas linhas de código.

Mais detalhes sobre sua utilização, preparo e funcionamento podem ser obtidos neste [link](https://medium.com/@alessandro_rocha/integrando-aplica%C3%A7%C3%B5es-python-com-o-chatgpt-e1f4d55ef10b?source=friends_link&sk=68ea35269b19dfe814c3fbe37d3e80da).


### Pré-Requisitos

1. Python 3+ instalado.
2. Virtualenv instalada.
3. Chave de API fornecida pela [OpenAI](https://openai.com/api/).


### Preparação para execução

1. Clonar o projeto.
2. Abrir um terminal na pasta do projeto clonado.
3. Criar uma virtualenv com o Python na versão 3+.

```buildoutcfg
virtualenv VENV --python=python3
```

4. Ativar a virtualenv.

```buildoutcfg
source VENV/bin/activate
```

5. Após a virtual env ser criada e ativada, instalar as dependências do projeto.

```buildoutcfg
pip install -r requirements.txt
```

### Preparação do código

1. Abra o código fonte do exemplo em qualquer editor de texto simples (Sublime, VSCode, etc.)
2. Insira a sua Secret API Key como valor para a variável **auth_token**, na linha 6.
3. Salve o código.


### Execução

1. No mesmo terminal aberto acima e com a virtualenv ativada, execute o comando abaixo:

```buildoutcfg
python main.py
```

### Considerações finais

1. Você encontrará mais informações sobre como criar sua chave de API acessando o artigo neste [link](https://medium.com/@alessandro_rocha/integrando-aplica%C3%A7%C3%B5es-python-com-o-chatgpt-e1f4d55ef10b?source=friends_link&sk=68ea35269b19dfe814c3fbe37d3e80da).
2. Para alterar a pergunta feita ao ChatGPT, modifique o valor da variável **question**, presente na linha 28.
3. Este é apenas um exemplo didático e não se preocupa em seguir boas práticas de desenvolvimento e seguraça da informação.
