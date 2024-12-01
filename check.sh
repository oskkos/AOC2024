mypy --strict src && \
pylint --enable=all --disable=import-error **/*.py && \
pytest --cov