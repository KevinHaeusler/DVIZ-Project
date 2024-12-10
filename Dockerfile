FROM shroominic/python-uv:3.11
LABEL authors="kevin"

WORKDIR /app

# Clone the repository
RUN git clone https://github.com/KevinHaeusler/DVIZ-Project.git .

# Navigate to the repository folder and install dependencies only
RUN uv pip install -r requirements.txt

# Expose the Streamlit port
EXPOSE 8501

HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health
ENTRYPOINT ["uv", "run", "python", "-m", "streamlit", "run", "DVIZ.py", "--server.port=8501", "--server.address=0.0.0.0"]
