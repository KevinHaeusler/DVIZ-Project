FROM python:3.11
LABEL authors="kevin"

WORKDIR /app

# Clone the repository
RUN git clone https://github.com/KevinHaeusler/DVIZ-Project.git .

# Install dependencies
RUN pip install \
    altair>=5.4.1 \
    pandas>=2.2.3 \
    openpyxl>=3.1.5 \
    streamlit>=1.39.0

# Expose the Streamlit port
EXPOSE 8501

# Healthcheck for Streamlit
HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health || exit 1

# Correct entry point
ENTRYPOINT ["streamlit", "run", "DVIZ.py", "--server.port=8501", "--server.address=0.0.0.0"]