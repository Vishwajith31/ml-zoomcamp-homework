FROM agrigorev/zoomcamp-model:2025

WORKDIR /app

COPY pyproject.toml .
COPY uv.lock . 

RUN pip install uv
RUN uv sync --frozen

COPY app.py .

EXPOSE 8000

CMD ["uv", "run", "uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]