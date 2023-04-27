make install-deps:
	brew install pipenv
	brew install tesseract
	pipenv install
start:
	streamlit run home.py
