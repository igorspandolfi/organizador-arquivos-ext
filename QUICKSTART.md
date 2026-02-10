# Quickstart

## Instalação Rápida

```bash
# Clone ou download
git clone https://github.com/seuusuario/organizador-arquivos-ext.git
cd organizador-arquivos-ext

# Ambiente virtual (recomendado)
python -m venv .venv
source .venv/bin/activate  # Mac/Linux: . .venv/bin/activate

# Não requer dependências externas — só Python!
pip install -e .
```

## Seu Primeiro Uso

### 1. Teste com Simulação

```bash
python app.py ~/Downloads --dry-run
```

Veja o que seria movido **sem realmente mover nada**.

### 2. Interface Gráfica (Fácil)

```bash
python gui.py
```

- Clique "Escolher..."
- Marque "Simular" se quiser ver antes
- Clique "Executar/Simular"

### 3. Executar de Verdade

```bash
python app.py ~/Documentos
```

Seus arquivos serão organizados em subpastas!

## Exemplos Comuns

### Downloads Organizados

```bash
python app.py ~/Downloads --grouping media --dry-run
# Se tiver certeza:
python app.py ~/Downloads --grouping media
```

**Resultado:** Pastas `IMAGES/`, `VIDEOS/`, `DOCUMENTS/`, `AUDIO/`, etc.

### Regras Customizadas

`meu_mapeamento.json`:
```json
{
  "log": "LOGS",
  "tmp": "TEMP",
  "exe": "PROGRAMAS"
}
```

```bash
python app.py ~/MeusDados --map-file meu_mapeamento.json
```

## Ajuda

```bash
python app.py --help
```

---

**Pronto!** Vou para [README.md](README.md) para mais detalhes.
