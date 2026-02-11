# Guia de Publicação no GitHub

## Estrutura Finalizada

```
organizador-arquivos-ext/
├── .gitignore              # Ignora arquivos Python temp, venv, etc
├── .gitattributes          # Normaliza line endings
├── LICENSE                 # MIT License
├── README.md               # Documentação principal com badges
├── QUICKSTART.md          # Início rápido (5 minutos)
├── CONTRIBUTING.md         # Diretrizes para contribuidores
├── CHANGELOG.md            # Histórico de versões
├── Makefile                # Atalhos para comandos comuns
├── requirements.txt        # Dependências (vazio — só stdlib)
├── pyproject.toml          # Configuração build moderna (PEP 517)
├── setup.cfg               # Metadata e entry points
├── __init__.py             # Pacote Python
├── app.py                  # Core: CLI organização
├── gui.py                  # Interface gráfica Tkinter
├── mapping_example.json    # Exemplo de arquivo de mapeamento
└── test_sample/            # Pasta de teste com exemplos
    ├── MP3/, PDF/, JPG/, etc  # Pastas simuladas
    └── arquivos de teste
```

## Próximos Passos

### 1. Inicialize um Repositório Git Local

```bash
cd C:\Users\YourUser\GitHub\organizador-arquivos-ext
git init
git add .
git commit -m "Initial commit: File organizer with CLI, GUI, and dry-run mode"
```

### 2. Crie um Repositório no GitHub

1. Vá para https://github.com/new
2. Nome: `organizador-arquivos-ext`
3. Descrição: "Organize files by extension or media type with CLI and GUI"
4. **NÃO** inicialize com README (já tem um)
5. Clique "Create repository"

### 3. Conecte ao Repositório Remoto

```bash
git remote add origin https://github.com/igorspandolfi/organizador-arquivos-ext.git
git branch -M main
git push -u origin main
```

### 4. Teste a Estrutura Localmente

```bash
# Teste a simulação
python app.py test_sample --dry-run

# Teste a GUI (se quiser)
python gui.py

# Teste o comando instalado
pip install -e .
organizador test_sample --dry-run
```

## Arquivos Importantes Explicados

| Arquivo | Propósito |
|---------|-----------|
| `README.md` | Documentação principal para o GitHub |
| `QUICKSTART.md` | Começo rápido em 5 minutos |
| `CONTRIBUTING.md` | Como colaborar com o projeto |
| `CHANGELOG.md` | Histórico de releases |
| `setup.cfg` | Metadata: descrição, autor, versão, etc |
| `pyproject.toml` | Build system moderno (PEP 517/518) |
| `.gitignore` | O quê não fazer commit |
| `LICENSE` | MIT License (permite uso livre) |
| `Makefile` | Atalhos: `make install`, `make lint`, etc |
