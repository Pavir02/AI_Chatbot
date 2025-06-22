# Persona Chatbot

## Requirements

- Python version 3.9
- Conda environment
- Transformers

## Installation

- To create virtual environment using Anaconda/Miniconda:
  Install Anaconda Python version manager
  https://www.anaconda.com/download/

- Install specific python version:  
  `conda create -n Chatbot python=3.9`

- For Windows Powershell terminal, run below command:  
  `conda init powershell`

- To activate environment:

  `conda activate Chatbot`

- Install required python packages:

  `pip install transformers accelerate torch protobuf sentencepiece accelerate hf_xet`

- Install huggingface cli:

  `pip install -U "huggingface_hub[cli]"`

- Get access token from (create a token with read access)
  https://huggingface.co/settings/tokens

- Login from the working terminal using below command, required to access mistral AI models:
  ` huggingface-cli login`

- Copy token and right click to paste in terminal and press enter

## Execution

- To run the project:
  `python ./main.py`

- Give a Person's name and short descritption to set the Persona of your choice after the prompt:
  `Set Persona`

- Continue to interact with the person after the prompt:  
  `Chat with {name}, (type 'exit' to quit)`
