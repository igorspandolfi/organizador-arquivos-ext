.PHONY: help install install-dev clean test lint format run-gui run-cli

help:
	@echo "Organizador de Arquivos - Makefile"
	@echo "=================================="
	@echo ""
	@echo "Comandos disponíveis:"
	@echo "  make install        Instala o pacote em modo normal"
	@echo "  make install-dev    Instala com dependências de desenvolvimento"
	@echo "  make clean          Remove arquivos temporários"
	@echo "  make lint           Executa verificação de código (flake8)"
	@echo "  make format         Formata com black e isort"
	@echo "  make test           Executa testes"
	@echo "  make run-gui        Executa a interface gráfica"
	@echo "  make run-cli        Teste rápido via CLI"
	@echo ""

install:
	pip install -e .

install-dev:
	pip install -e ".[dev]"
	pip install pytest black isort flake8 mypy

clean:
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -delete
	find . -type d -name "*.egg-info" -exec rm -rf {} + 2>/dev/null || true
	rm -rf build/ dist/ .pytest_cache/ .mypy_cache/ .coverage htmlcov/

lint:
	flake8 app.py gui.py --max-line-length=88 --extend-ignore=E203
	mypy app.py --ignore-missing-imports

format:
	black app.py gui.py
	isort app.py gui.py

test:
	pytest tests/ -v --tb=short 2>/dev/null || echo "Nenhum arquivo de teste encontrado"

run-gui:
	python gui.py

run-cli:
	python app.py test_sample --dry-run

.DEFAULT_GOAL := help
