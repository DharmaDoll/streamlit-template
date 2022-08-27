FROM python:3.10

COPY . /opt/app
WORKDIR /opt/app/streamlit_sample

RUN pip3 install -r requirements.txt

EXPOSE 8501
USER root

ENTRYPOINT ["streamlit", "run"]
CMD ["Hello.py"]
# https://qiita.com/SatoshiGachiFujimoto/items/d8273194e88d8eb30213


