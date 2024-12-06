mypy --strict src && \
pylint --enable=all --disable=import-error **/*.py && \
pytest --cov --durations=0 --durations-min=0.2