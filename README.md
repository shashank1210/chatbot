clone the repo

cd backend

python -m venv virtual

virtual/scripts/activate

pip install rasa

rasa train 

rasa run

rasa run -m models --enable-api --cors "*" --debug
