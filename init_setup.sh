echo "[ `date` ]": "START"
echo "[ `date` ]": "Creating virtual env" 
python3 -m venv venv/
echo "[ `date` ]": "activate venv"
source venv/bin/activate
echo "[ `date` ]": "installing the requirements" 
pip install -r requirements.txt
python3 -m spacy download en_core_web_lg
echo "[ `date` ]": "END"
