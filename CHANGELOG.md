# Changelog

Todas as mudanças notáveis neste projeto serão documentadas neste arquivo.

O formato é baseado em [Keep a Changelog](https://keepachangelog.com/),
e este projeto aderenta a [Semantic Versioning](https://semver.org/).

## [0.1.0] - 2026-02-10

### Added
- Interface CLI com argparse (`app.py`)
- Interface GUI com Tkinter (`gui.py`)
- Modo simulação (`--dry-run`) para prévia sem modificação
- Agrupamento por extensão (padrão)
- Agrupamento por tipo de mídia (imagens, vídeos, áudio, documentos)
- Suporte a mapeamento customizado via arquivo JSON (`--map-file`)
- Logging estruturado para mensagens informativas
- Documentação completa em português
- Arquivos de empacotamento para PyPI (`setup.cfg`, `pyproject.toml`)
- GitHub-ready com `.gitignore`, `LICENSE`, `CONTRIBUTING.md`
- Type hints em funções principais
- Tratamento robusto de erros com exception logging

### Changed
- N/A

### Deprecated
- N/A

### Removed
- N/A

### Fixed
- N/A

### Security
- N/A

---

## Planejado para Futuras Versões

### [0.2.0] - TBD
- Suporte a organização recursiva (subdiretórios)
- Sistema de undo/redo com histórico
- Regras baseadas em tamanho ou data de modificação
- Testes automatizados com pytest
- CI/CD com GitHub Actions

### [0.3.0] - TBD
- Integração com sistemas de nuvem (Google Drive, OneDrive)
- Notificações de conclusão
- Modo agendado/scheduler
- Dashboard melhorado
