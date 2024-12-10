FROM shroominic/python-uv:3.11
LABEL authors="kevin"

WORKDIR /app


RUN git clone https://github.com/KevinHaeusler/DVIZ-Project.git .

RUN uv pip install \
    altair>=5.4.1 \
    pandas>=2.2.3 \
    streamlit>=1.39.0

EXPOSE 8501

HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health
ENTRYPOINT ["uv", "run", "python", "-m", "streamlit", "run", "DVIZ.py", "--server.port=8501", "--server.address=0.0.0.0"]