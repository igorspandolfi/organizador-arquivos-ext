"""Organizador simples de arquivos por extensão.

Este módulo fornece uma função `organizar_arquivos` que agrupa arquivos
em subpastas nomeadas pela extensão (ex: `PDF`, `TXT`).

Principais características:
- Comentários e tipagem para facilitar manutenção.
- Logging básico em vez de prints diretos.
- Interface de linha de comando opcional usando `argparse`.

Uso:
    python app.py /caminho/para/pasta
    ou
    python app.py   # será solicitado o caminho via input
"""

from pathlib import Path
import shutil
import argparse
import logging
import json
from typing import Optional, Dict

# Configura logging básico com nível INFO
logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
logger = logging.getLogger(__name__)

# Presets for grouping by media type
MEDIA_PRESETS = {
    "images": {"jpg", "jpeg", "png", "gif", "bmp", "svg", "webp", "tiff"},
    "videos": {"mp4", "mkv", "avi", "mov", "wmv", "flv", "webm"},
    "audio": {"mp3", "wav", "flac", "aac", "ogg"},
    "documents": {"pdf", "doc", "docx", "xls", "xlsx", "ppt", "pptx", "txt", "odt"},
}


def criar_pasta_se_nao_existir(pasta: Path) -> None:
    """Cria a pasta indicada se ela não existir.

    Args:
        pasta: Instância de `Path` representando a pasta a criar.
    """
    # mkdir com exist_ok evita exceção se a pasta já existir
    pasta.mkdir(parents=False, exist_ok=True)


def organizar_arquivos(
    diretorio: str,
    dry_run: bool = False,
    grouping: str = "extension",
    custom_map: Optional[Dict[str, str]] = None,
) -> None:
    """Organiza arquivos no diretório fornecido segundo opções.

    Args:
        diretorio: Caminho do diretório a organizar (string).
        dry_run: Se True, apenas mostra as operações sem executá-las.
        grouping: "extension" (padrão) ou "media" para agrupar por tipo.
        custom_map: Dicionário opcional mapeando extensões (sem ponto, minúsculas)
                    para nomes de pasta.
    """

    caminho = Path(diretorio)

    # Verificação inicial: o caminho deve existir e ser um diretório
    if not caminho.exists():
        logger.error("Diretório '%s' não existe.", diretorio)
        return

    if not caminho.is_dir():
        logger.error("Caminho fornecido não é um diretório: %s", diretorio)
        return

    # Itera exclusivamente pelos itens imediatos do diretório
    for item in caminho.iterdir():
        # Ignora subdiretórios — apenas processa arquivos regulares
        if not item.is_file():
            continue

        # Extensão sem ponto, em minúsculas para comparação
        ext = item.suffix[1:].lower()  # '' se não houver extensão

        # Determina a pasta destino segundo o mapeamento customizado ou preset
        if custom_map and ext in custom_map:
            pasta_nome = custom_map[ext]
        elif grouping == "media":
            found = False
            for grupo, exts in MEDIA_PRESETS.items():
                if ext in exts:
                    pasta_nome = grupo.upper()
                    found = True
                    break
            if not found:
                pasta_nome = ext.upper() if ext else "SEM_EXTENSAO"
        else:
            pasta_nome = ext.upper() if ext else "SEM_EXTENSAO"

        pasta_destino = caminho / pasta_nome

        try:
            criar_pasta_se_nao_existir(pasta_destino)

            destino_arquivo = pasta_destino / item.name

            if dry_run:
                logger.info("Simulação: %s -> %s/", item.name, pasta_nome)
            else:
                shutil.move(str(item), str(destino_arquivo))
                logger.info("Movido: %s → %s/", item.name, pasta_nome)
        except Exception as exc:
            logger.exception("Falha ao mover '%s': %s", item.name, exc)

    logger.info("Organização concluída!")


def parse_args() -> argparse.Namespace:
    """Cria e retorna o parser de argumentos para a linha de comando.

    Retorna um objeto com o atributo `diretorio` (opcional).
    """
    parser = argparse.ArgumentParser(description="Organiza arquivos por extensão")
    parser.add_argument(
        "diretorio",
        nargs="?",
        help="Caminho da pasta a organizar (se omitido será solicitado)",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Mostra o que seria movido, sem executar operações de disco",
    )
    parser.add_argument(
        "--grouping",
        choices=("extension", "media"),
        default="extension",
        help="Como agrupar: por extensão (padrão) ou por tipo de mídia",
    )
    parser.add_argument(
        "--map-file",
        help="Caminho para um arquivo JSON com mapeamento customizado {\"ext\": \"pasta\"}",
    )
    return parser.parse_args()


def main() -> None:
    """Ponto de entrada principal quando executado como script.

    - Lê argumentos via `argparse`.
    - Se nenhum diretório for passado, solicita ao usuário via `input()`.
    - Chama `organizar_arquivos`.
    """
    args = parse_args()
    diretorio_alvo: Optional[str] = args.diretorio

    # Se não foi passado por argumento, pede ao usuário
    if not diretorio_alvo:
        try:
            diretorio_alvo = input("Digite o caminho da pasta a organizar: ").strip()
        except (KeyboardInterrupt, EOFError):
            logger.info("Entrada cancelada pelo usuário.")
            return

    if not diretorio_alvo:
        logger.error("Nenhum diretório fornecido. Encerrando.")
        return

    custom_map: Optional[Dict[str, str]] = None
    if args.map_file:
        try:
            with open(args.map_file, "r", encoding="utf-8") as fh:
                raw = json.load(fh)
                # Normalize keys to lowercase without leading dots
                custom_map = {k.lstrip(".").lower(): v for k, v in raw.items()}
        except Exception as exc:
            logger.exception("Falha ao carregar map-file '%s': %s", args.map_file, exc)
            return

    organizar_arquivos(
        diretorio_alvo, dry_run=args.dry_run, grouping=args.grouping, custom_map=custom_map
    )


if __name__ == "__main__":
    main()
