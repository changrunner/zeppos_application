REM Update Pip
python -m pip install --upgrade pip

REM install pipenv
pip install pipenv==2018.11.26

REM Remove Virtual Environment
pipenv --rm

REM install Virtual environment
pipenv install
pipenv install --dev

