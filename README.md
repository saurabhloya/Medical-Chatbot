# Medical-Chatbot

### Setup Instructions

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/saurabhloya/
    ```

2. **Create a Virtual Environment**:
   ```bash
   conda create -p venv python=3.9 -y
   conda activate venv
   ```

3. **Install Requirements**:
   ```bash
   pip install -r requirements.txt
   ```


4. Create a `.env` file in the root directory and add your Pinecone credentials as follows:

    ```ini
    PINECONE_API_KEY = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
    ```


5. Download the quantize model from the link provided in model folder & keep the model in the model directory:

    ```ini
    ## Download the Llama 2 Model:

    llama-2-7b-chat.ggmlv3.q4_0.bin


    ## From the following link:
    https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGML/tree/main
    ```

6. **Run the following command**:
    ```bash
    # run the following command
    python store_index.py
    ```

7. **Run the Application**:
    ```bash
    # Finally run the following command
    python app.py
    ```

8. **Access the Application**:
   - Open your web browser and go to `http://localhost:5000`.

### Techstack Used:

- Python
- LangChain
- Flask
- Meta Llama2
- Pinecone

