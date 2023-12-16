FROM quay.io/astronomer/astro-runtime-dev:10.0.0-alpha10

ENV AIRFLOW__WEBSERVER__ALLOW_RAW_HTML_DESCRIPTIONS=True
ENV AIRFLOW__WEBSERVER__NAVBAR_COLOR="#1a2e1e"
ENV AIRFLOW__WEBSERVER__NAVBAR_TEXT_COLOR="#7ef297" 
ENV AIRFLOW__WEBSERVER__INSTANCE_NAME="2.8 DAGs"