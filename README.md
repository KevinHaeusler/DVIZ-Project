# Installation

Clone the repository

uv pip install -r pyproject.toml
uv run python -m streamlit run DVIZ.py 

Or with Python 3.10

pip install -r requirements.txt
streamlit run DVIZ.py

or build and run the Dockerfile 
docker build -t DVIZ .
docker run -p 8501:8501 DVIZ