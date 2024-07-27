.PHONY: run
run:
	poetry run streamlit run src/app.py

.PHONY: install
install:
	poetry install