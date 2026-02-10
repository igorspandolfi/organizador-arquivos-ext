# Organizador de Arquivos por Extensão

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)

Organize arquivos em um diretório agrupando-os em subpastas nomeadas pela extensão (ou tipo de mídia). Simples, rápido e flexível.

## Sumário

- [Características](#características)
- [Instalação](#instalação)
- [Uso](#uso)
  - [CLI](#cli)
  - [GUI](#gui)
  - [Programaticamente](#programaticamente)
- [Examplos](#exemplos)
- [Documentação Avançada](#documentação-avançada)
- [Desenvolvendo](#desenvolvendo)
- [Licença](#licença)

## Características

- ✅ **Agrupamento por Extensão** — Organiza por `.pdf`, `.txt`, etc.
- ✅ **Agrupamento por Tipo de Mídia** — Presets para imagens, vídeos, áudio, documentos
- ✅ **Modo Simulação** (`--dry-run`) — Mostra o que seria movido **sem executar**
- ✅ **Mapeamento Customizado** — Use `--map-file` para regras personalidas
- ✅ **Interface Gráfica** — GUI simples com Tkinter
- ✅ **CLI Power** — Argumentos de linha de comando para automação
- ✅ **Logging Estruturado** — Mensagens claras e informativas

## Instalação

### Via pip (recomendado)

```bash
pip install organizador-arquivos-ext
```

### Instalação Local (desenvolvimento)

```bash
git clone https://github.com/igorspandolfi/organizador-arquivos-ext.git
cd organizador-arquivos-ext
pip install -e .
```

## Uso

### CLI

Organizar uma pasta por extensão:

```bash
organizador /caminho/para/pasta
# ou
python app.py /caminho/para/pasta
```

Simulação (sem mover arquivos):

```bash
python app.py /caminho/para/pasta --dry-run
```

Agrupar por tipo de mídia:

```bash
python app.py /caminho/para/pasta --grouping media
```

Com mapeamento customizado:

```bash
python app.py /caminho/para/pasta --map-file mapping.json
```

**Argumentos disponíveis:**

```
positional arguments:
  diretorio                  Caminho da pasta a organizar

optional arguments:
  -h, --help                 Mostra esta mensagem e sai
  --dry-run                  Simula sem executar
  --grouping {extension,media}
                             Modo de agrupamento (padrão: extension)
  --map-file FILE            Arquivo JSON com mapeamento customizado
```

### GUI

Inicie a interface gráfica:

```bash
python gui.py
```

Recursos:
- Seletor de pasta com explorador
- Opções de agrupamento
- Checkbox de simulação
- Log em tempo real

### Programaticamente

```python
from app import organizar_arquivos

# Agrupamento por extensão (padrão)
organizar_arquivos('/caminho/para/pasta')

# Simulação
organizar_arquivos('/caminho/para/pasta', dry_run=True)

# Agrupamento por mídia
organizar_arquivos('/caminho/para/pasta', grouping='media')

# Com mapeamento customizado
custom_map = {'pdf': 'DOCS', 'jpg': 'IMAGENS'}
organizar_arquivos('/caminho/para/pasta', custom_map=custom_map)
```

## Exemplos

### Exemplo 1: Organizar Downloads por tipo

```bash
python app.py ~/Downloads --grouping media --dry-run
```

Resultado esperado:

```
INFO: Simulação: video.mp4 -> VIDEOS/
INFO: Simulação: foto.jpg -> IMAGES/
INFO: Simulação: documento.pdf -> DOCUMENTS/
INFO: Simulação: musica.mp3 -> AUDIO/
```

### Exemplo 2: Mapeamento Customizado

Crie `mapping.json`:

```json
{
  "md": "MARKDOWN",
  "txt": "DOCUMENTOS",
  "log": "LOGS",
  "tmp": "TEMPORARIOS"
}
```

Execute:

```bash
python app.py /minha/pasta --map-file mapping.json
```

### Exemplo 3: Estrutura Criada

Antes:

```
minha_pasta/
  documento.pdf
  nota.txt
  video.mp4
  imagem.jpg
  arquivo_sem_extensao
```

Depois (com `--grouping media`):

```
minha_pasta/
  DOCUMENTS/
    documento.pdf
  TEXT/
    nota.txt
  VIDEOS/
    video.mp4
  IMAGES/
    imagem.jpg
  SEM_EXTENSAO/
    arquivo_sem_extensao
```

## Documentação Avançada

### Presets de Mídia

Quando usa `--grouping media`, as extensões são mapeadas para:

- **IMAGES**: jpg, jpeg, png, gif, bmp, svg, webp, tiff
- **VIDEOS**: mp4, mkv, avi, mov, wmv, flv, webm
- **AUDIO**: mp3, wav, flac, aac, ogg
- **DOCUMENTS**: pdf, doc, docx, xls, xlsx, ppt, pptx, txt, odt

Extensões não mapeadas usam a capa padrão (nome da extensão em maiúsculas).

### Formato do Arquivo de Mapeamento

O arquivo JSON deve ter extensões como chaves (com ou sem ponto) e nomes de pasta como valores:

```json
{
  "pdf": "DOCUMENTOS",
  ".doc": "WORD",
  "jpg": "IMAGENS"
}
```

As chaves são normalizadas para minúsculas sem ponto.

## Desenvolvendo

### Setup de Desenvolvimento

```bash
# Clone
git clone <repo>
cd organizador-arquivos-ext

# Virtual env
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

# Dependências
pip install -e .
```

### Testando

Crie arquivos de exemplo:

```bash
mkdir test_sample
touch test_sample/{doc.pdf,note.txt,photo.jpg,video.mp4}
python app.py test_sample --dry-run
```

### Contribuindo

Veja [CONTRIBUTING.md](CONTRIBUTING.md) para diretrizes de contribuição.

## FAQ

**P: E se um arquivo já existe na pasta de destino?**  
R: O `shutil.move` sobrescreve. Considere fazer backup ou use `--dry-run` primeiro.

**P: Posso organizar recursivamente?**  
R: Atualmente, apenas o nível superior é processado. Para subdirs, execute novamente em cada pasta.

**P: Como desfaço as mudanças?**  
R: Sem um sistema de backup integrado. Dica: sempre use `--dry-run` antes de executar!

## Roadmap

- [ ] Suporte a organizações recursivas
- [ ] Banco de dados de histórico (undo/redo)
- [ ] Regras avançadas por tamanho/data
- [ ] Testes automatizados
- [ ] Documentação em Sphinx

## Licença

Este projeto é licenciado sob a [MIT License](LICENSE).

---

**Precisa de ajuda?** Abra uma [issue](https://github.com/igorspandolfi/organizador-arquivos-ext/issues).
