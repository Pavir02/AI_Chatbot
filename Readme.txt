Python:
Creating virtual environment - https://docs.python.org/3/library/venv.html
https://pypi.org - package manager
python -m venv D:\PythonVirtualEnv\Chatbot

Activate virtual environment:
D:\PythonVirtualEnv\Chatbot\bin\Activate.ps1

================================================

For virtual environment using Anaconda/Miniconda:

Install Anaconda Python version manager 
https://www.anaconda.com/download/

Install specific python version: 
conda create -n Chatbot python=3.9

For Windows Powershell terminal - conda init powershell

conda activate Chatbot

================================================

Install required python packages:
pip install transformers accelerate torch protobuf sentencepiece accelerate hf_xet


Hugging face text models - https://huggingface.co/models?pipeline_tag=text-generation&sort=trending
Transformers - https://huggingface.co/docs/transformers/en/index


Install huggingface cli - pip install -U "huggingface_hub[cli]"
Get access token from (create a token with read access) - https://huggingface.co/settings/tokens
Login in the working terminal using command - huggingface-cli login 
Copy token and right click to paste in terminal and press enter

=> To Intall spacy for named entity recognition: (Not used)
-------------------------------------------------
pip install spacy

-> if it gives error, install using conda : 
conda install -c conda-forge spacy

-> download the English model:
python -m spacy download en_core_web_sm

