#Image: jakew57/ml-hurricane_damage-api

FROM python:3.11

RUN pip install Flask==3.0 tensorflow==2.15 datasets transformers metrics

COPY api.py api.py
COPY models /models

CMD ["python", "api.py"]