# Controle de Estoque de Óleo

Sistema de controle de estoque de óleo desenvolvido em Django para gerenciar entradas e saídas de óleo em projetos e máquinas.

## 📋 Funcionalidades

- **Gestão de Óleo**: Cadastro e controle automático de quantidade em estoque
- **Controle de Entradas**: Registro de compras e adições ao estoque com nota fiscal
- **Controle de Saídas**: Registro de uso de óleo por máquinas e projetos
- **Gestão de Máquinas**: Cadastro de equipamentos que utilizam óleo
- **Gestão de Projetos**: Organização por projetos
- **Controle de Responsáveis**: Identificação de quem retirou o óleo
- **Interface Administrativa**: Interface web completa para gerenciamento
- **Validação de Estoque**: Impede saídas maiores que o estoque disponível

## 🚀 Tecnologias Utilizadas

- **Backend**: Django 2.2.7
- **Banco de Dados**: SQLite (desenvolvimento) / PostgreSQL (produção)
- **Deploy**: Heroku
- **Interface**: Django Admin
- **Localização**: Português Brasileiro

## 📦 Instalação

### Pré-requisitos

- Python 3.6+
- pip

### Configuração Local

1. Clone o repositório:
```bash
git clone https://github.com/rafaelgontijo/controle_estoque.git
cd controle_estoque
```

2. Crie um ambiente virtual:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate  # Windows
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

4. Execute as migrações:
```bash
python manage.py migrate
```

5. Crie um superusuário:
```bash
python manage.py createsuperuser
```

6. Execute o servidor de desenvolvimento:
```bash
python manage.py runserver
```

7. Acesse o sistema em `http://localhost:8000/admin`

## 🏗️ Estrutura do Projeto

```
controle_estoque/
├── controle_estoque/          # Configurações do projeto Django
│   ├── __init__.py
│   ├── settings.py           # Configurações principais
│   ├── urls.py              # URLs principais
│   └── wsgi.py              # Configuração WSGI
├── estoque/                  # App principal do sistema
│   ├── __init__.py
│   ├── admin.py             # Configuração do Django Admin
│   ├── apps.py
│   ├── models.py            # Modelos de dados
│   ├── tests.py
│   └── views.py
├── manage.py                # Script de gerenciamento Django
├── requirements.txt         # Dependências do projeto
├── Procfile                # Configuração para deploy no Heroku
└── README.md               # Este arquivo
```

## 📊 Modelos de Dados

### Óleo
- **Descrição**: Tipo/marca do óleo
- **Quantidade**: Calculada automaticamente (entradas - saídas)

### Entrada de Óleo
- **Óleo**: Referência ao tipo de óleo
- **Quantidade**: Quantidade adicionada ao estoque
- **Nota Fiscal**: Número da nota fiscal da compra
- **Data de Entrada**: Data da entrada no estoque

### Saída de Óleo
- **Óleo**: Referência ao tipo de óleo
- **Quantidade**: Quantidade retirada do estoque
- **Máquina**: Equipamento que utilizará o óleo
- **Projeto**: Projeto ao qual a saída está vinculada
- **Responsável**: Pessoa responsável pela retirada
- **Data de Saída**: Data da retirada do estoque

### Máquina
- **Modelo**: Modelo da máquina
- **Número**: Número de identificação da máquina

### Projeto
- **Nome**: Nome do projeto

### Responsável
- **Nome**: Nome da pessoa responsável

## 🔧 Uso do Sistema

1. **Acesse a interface administrativa** em `/admin`
2. **Cadastre os dados básicos**:
   - Responsáveis
   - Projetos
   - Máquinas
   - Tipos de óleo
3. **Registre entradas de óleo** com nota fiscal
4. **Registre saídas de óleo** informando máquina, projeto e responsável
5. **Monitore o estoque** através da listagem de óleos

## 🚀 Deploy no Heroku

O projeto está configurado para deploy no Heroku:

1. Crie um app no Heroku
2. Configure as variáveis de ambiente necessárias
3. Faça o deploy:
```bash
git push heroku main
```

4. Execute as migrações no Heroku:
```bash
heroku run python manage.py migrate
```

5. Crie um superusuário:
```bash
heroku run python manage.py createsuperuser
```

## 🤝 Contribuindo

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 📝 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## 👨‍💻 Autor

**Rafael Gontijo**

- GitHub: [@rafaelgontijo](https://github.com/rafaelgontijo)

---

⭐ Se este projeto foi útil para você, considere dar uma estrela no repositório!