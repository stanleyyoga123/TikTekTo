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
   pip install -r requirements.txt
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

## API Call

This section documents the main API endpoints, their requests, and responses. All examples use `curl`. Replace `http://localhost:8080` with your deployed host if needed.

For the API call screenshot, you can navigate to [this folder](./img)

### 1. Pathway recommendation (from a document)

**Request**
```bash
curl --request POST \
    --url http://localhost:8080/api/user/pathway/create/document 
    --header 'Content-Type: multipart/form-data' \
    --form 'document=@/your/pdf/location' \
    --form objective=Back-End \
    --form username=stanley \
    --form role=ADHD
```

**Response**
```json
{
    "status": 200,
    "data": [
        {
            "general_idea": "RESTful APIs, HTTP fundamentals",
            "topics": [
                "HTTP methods, status codes",
                "API design principles (REST)",
                "JSON & data serialization",
                "Error handling strategies",
                "API documentation (OpenAPI/Swagger)"
            ]
    },
    ...
    ]
}
```
### 2. Path recommendation (from JSON forms)

**Request**
```bash
curl --request POST \
  --url http://localhost:8080/api/user/pathway/create \
  --header 'Content-Type: application/json' \
  --data '{
	"username": "Stanley",
	"role": "ADHD",
	"background": "computer science students",
	"additional": "have finished these courses:\n OOP\n Algorithm and Data Structures\n Web development\n Distributed Programming\n Artificial Intelligence\n Git and stuff",
	"objective": "backend engineering"
}'
```

**Response**
```json
{
	"status": 200,
	"data": [
		{
			"general_idea": "Build Your First API",
			"topics": [
				"HTTP/REST API Refresher",
				"Backend Language/Framework Selection (e.g., Node.js/Express, Python/Flask/Django, Go/Gin)",
				"Basic API Endpoints (CRUD operations)",
				"Postman/Insomnia Basics",
				"Basic Error Handling (HTTP status codes)"
			]
		},
		{
			"general_idea": "Data Persistence & Validation",
			"topics": [
				"Relational DB Fundamentals (SQL, schema design)",
				"Database Integration (ORM/ODM usage)",
				"Basic Data Validation",
				"Unit Testing Basics (API routes, utility functions)",
				"NoSQL DB Introduction (e.g., MongoDB, Redis)",
				"Transactions & Atomicity"
			]
		},
        ...
    ]
}
```

### 3. Question RAG 
   
**Request**
```bash
curl --request POST \
  --url http://localhost:8080/api/questions/retrieve \
  --header 'Content-Type: application/json' \
  --data '{
	"general_idea": "Build Your First API",
	"topics": [
		"HTTP/REST API Refresher",
		"Backend Language/Framework Selection (e.g., Node.js/Express, Python/Flask/Django, Go/Gin)",
		"Basic API Endpoints (CRUD operations)",
		"Postman/Insomnia Basics",
		"Basic Error Handling (HTTP status codes)"
	]
}'
```

**Response**
```json
{
	"status": 200,
	"data": [
		{
			"difficulty": "Easy",
			"question": "What are the advantages of using a microservices architecture?",
			"answer": "Advantages include easier scalability, flexibility in choosing technology, better fault isolation, and improved continuous deployment.",
			"category": "Back-end",
			"tags": "microservices, microservices architecture, scalability, fault isolation, continuous deployment, back-end"
		},
		{
			"difficulty": "Medium",
			"question": "What are microservices and how do they differ from monolithic architectures?",
			"answer": "Microservices are a software development technique—a variant of the service-oriented architecture architectural style that structures an application as a collection of loosely coupled services. In a monolithic architecture, all components are interconnected and interdependent.",
			"category": "Back-end",
			"tags": "microservices, monolithic architecture, software architecture, service-oriented architecture (soa), distributed systems, backend"
		},
        ...
	]
}
```
### 4. Flashcard Generation

**Request**
```bash
curl --request POST \
  --url http://localhost:8080/api/flashcard/generate \
  --header 'Content-Type: application/json' \
  --data '{
	"num_flashcards": 10,
	"general_idea": "Core web API foundations",
	"topics": [
		"HTTP Protocol",
		"REST API principles",
		"Backend Framework (e.g., Python Flask/Node.js Express)",
		"Routing, Request/Response handling",
		"JSON serialization/deserialization",
		"Basic error handling"
	],
	"is_highlighted": true
}'
```

**Response**
```json
{
	"status": 200,
	"data": [
		{
			"question": "What is <mark>HTTP</mark>?",
			"answer": "<mark>Hypertext Transfer Protocol</mark> for client-server communication. It defines how messages are formatted and transmitted."
		},
		{
			"question": "Name common <mark>HTTP methods</mark> and their purpose.",
			"answer": "<mark>GET</mark> (retrieve), <mark>POST</mark> (create), <mark>PUT</mark> (update/replace), <mark>DELETE</mark> (remove)."
		},
		{
			"question": "What does <mark>REST</mark> stand for in API design?",
			"answer": "<mark>Representational State Transfer</mark>. An architectural style for networked applications using standard HTTP methods."
		},
        ...
    ]
}
```

### 5. Answer checker

**Request**
```bash
curl --request POST \
  --url http://localhost:8080/api/questions/check \
  --header 'Content-Type: application/json' \
  --data '{
	"question": "What is the purpose of a constructor?",
	"true_answer": "A constructor initializes object properties upon class instantiation, ensuring a well-defined state.",
	"user_answer": "Constructor used to create an object",
	"is_highlighted": true
}'
```

**Response**
```json
{
	"status": 200,
	"data": {
		"is_correct": false,
		"reason": "The constructor <mark>initializes object properties</mark> of an <mark>already created object</mark>. It doesn't <mark>create the object itself</mark>, which is handled by the `new` operator or runtime."
	}
}
```



## Resources
- Kaggle dataset: [Software Engineering Interview Questions Dataset](https://www.kaggle.com/datasets/syedmharis/software-engineering-interview-questions-dataset)
