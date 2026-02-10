# Comandos Prontos para Executar

Use estes comandos prontos — não precisa substituir nada!

## 1. Inicializar e Fazer Push ao GitHub

```powershell
cd D:\GitHub\organizador-arquivos-ext

# Inicializar repositório
git init

# Adicionar todos os arquivos
git add .

# Primeiro commit
git commit -m "Initial commit: File organizer with CLI, GUI, and dry-run mode"

# Configurar branch principal 
git branch -M main

# Adicionar remoto (substitua com seu token se necessário)
git remote add origin https://github.com/igorspandolfi/organizador-arquivos-ext.git

# Push para o GitHub
git push -u origin main
```

## 2. Testar Localmente Antes de Publicar

```powershell
# Teste da simulação
python app.py test_sample --dry-run

# Teste da GUI
python gui.py

# Teste da instalação local
pip install -e .
organizador test_sample --dry-run
```

## 3. Publicar no PyPI (Depois)

```powershell
# Instalar ferramentas
pip install build twine

# Build do pacote
python -m build

# Upload (será pedido usuário/senha do PyPI)
python -m twine upload dist/*
```

## Seu Usuário GitHub

**igorspandolfi**

Todos os links estão corretos em:
- ✅ `setup.cfg` 
- ✅ `README.md`
- ✅ `GITHUB_SETUP.md`
- ✅ `QUICKSTART.md`

---

**Pronto!** Execute o bloco 1 acima para fazer o push inicial. 🚀
