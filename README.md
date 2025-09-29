# TikTekTo

## Requirements
- Python **3.12 or higher**
- [Docker](https://docs.docker.com/get-docker/) installed
- [Kaggle account](https://www.kaggle.com/) to download the dataset
- [Google AI Studio](https://aistudio.google.com/) account to generate API keys

## Setup Instructions

1. **Download the dataset**  
   Get the *Software Engineering Interview Questions Dataset* from Kaggle:  
   [Kaggle Dataset Link](https://www.kaggle.com/datasets/syedmharis/software-engineering-interview-questions-dataset)

2. **Create an API key**  
   In [Google AI Studio](https://aistudio.google.com/), generate a new API key.

3. **Set your environment variable**  
   Add the API key to your environment variables under the name:
   ```bash
   GEMINI_API_KEY=your_api_key_here
   ```

4. **Start the databases**  
   Run the following command to start the required services in the background:
   ```bash
   docker-compose up --detach
   ```

5. **Install dependencies**  
   Use the same dependencies as the backend service:
   ```bash
   pip install -r backend/requirements.txt
   ```

6. **Run the adhoc scripts (in order)**  
   Execute the following scripts sequentially:
   ```bash
   python adhoc/populate_tags.py
   python adhoc/combine_tags.py
   python adhoc/create_embeddings.py
   python adhoc/create_db.py
   ```

7. **Start the backend service**  
   Once the adhoc scripts finish, launch the backend with:
   ```bash
   docker-compose --profile dev up --build --detach
   ```

## Resources
- Kaggle dataset: [Software Engineering Interview Questions Dataset](https://www.kaggle.com/datasets/syedmharis/software-engineering-interview-questions-dataset)
