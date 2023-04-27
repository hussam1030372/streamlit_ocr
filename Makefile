make install-deps:
	brew install pipenv
	pipenv install
start:
	streamlit run home.py
