FROM shroominic/python-uv:3.11
LABEL authors="kevin"

WORKDIR /app

RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    software-properties-common \
    git \
    && rm -rf /var/lib/apt/lists/*

RUN git clone https://github.com/KevinHaeusler/DVIZ-Project.git .

RUN uv pip install -r pyproject.toml
EXPOSE 8501

HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health
ENTRYPOINT ["uv", "run", "python", "-m", "streamlit", "run", "DVIZ.py", "--server.port=8501", "--server.address=0.0.0.0"]