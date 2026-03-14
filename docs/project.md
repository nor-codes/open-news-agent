# News Intelligence Platform

## Project Vision
Build a cloud-native platform that collects news from RSS feeds, indexes it in a search engine, and allows users to interact with the news using **AI-powered conversational search**.

This platform will demonstrate:

- Distributed data ingestion
- Event-driven architecture
- Search indexing
- AI-powered query interpretation
- Agentic workflows
- Scalable cloud infrastructure

---

## Functional Requirements

### 1. News Ingestion
The platform must ingest news from RSS feeds.

**Initial source:**

- [The New York Times](https://rss.nytimes.com/services/xml/rss/nyt/World.xml)

The system must support **multiple configurable feeds**.

Each article must store:

- Title
- Link
- Description
- Publication date
- Category
- Author
- Source
- Ingestion timestamp

---

### 2. Data Processing
The system must:

1. Fetch RSS feeds
2. Parse XML
3. Convert to structured JSON
4. Store raw data
5. Publish processed data to the indexing pipeline

---

### 3. Search
Users must be able to:

- Search news articles
- Filter by category
- Filter by date
- Search by keywords
- Search by topic

Search will be powered by:

- OpenSearch or Apache Solr

---

### 4. Conversational AI
Users interact through a **chat interface**.

Example queries:

- `What is happening in Ukraine today?`
- `Summarize the latest AI news`
- `What are the key global conflicts this week?`

The system should:

1. Understand the question
2. Convert it into search queries
3. Retrieve relevant articles
4. Generate a summary response

---

### 5. User Features
Users can:

- Create an account
- Login
- Save searches
- View search history
- Chat with the news assistant

---

## Non-Functional Requirements

- **Scalability:** Support multiple RSS feeds and large numbers of articles.
- **Reliability:** Raw RSS data must be stored for **2 months**.
- **Observability:** Logging and metrics must be supported.
- **Extensibility:** New news sources can be added without code changes.

---

## Architecture

            +------------------+
            |  RSS Sources     |
            | NYTimes etc      |
            +---------+--------+
                      |
                      v
            +------------------+
            | Crawler Service  |
            | Python           |
            +---------+--------+
                      |
                      v
                   SQS Queue
                      |
                      v
            +------------------+
            | Parser Service   |
            | Java             |
            +---------+--------+
                      |
             +--------+--------+
             |                 |
             v                 v
           S3               Kafka
       (raw xml)        (article events)
                               |
                               v
                     +------------------+
                     | Indexer Service  |
                     +--------+---------+
                              |
                              v
                       OpenSearch/Solr
                              |
                              v
                    +-------------------+
                    | Search Service    |
                    +---------+---------+
                              |
                              v
                       Agent Service
                              |
                              v
                         Main API
                              |
                              v
                          Frontend



---

## Service Breakdown

### 1. Crawler Service
**Language:** Python  
Responsibilities:

- Fetch RSS feeds
- Detect new articles
- Publish metadata to SQS

**Metadata Example:**

```json
{
  "source": "nytimes",
  "feed": "world",
  "url": "...",
  "timestamp": "..."
}
```


### 2. Parser Service
Responsibilities:

- Consume SQS messages
- Fetch RSS XML
- Parse articles
- Convert to JSON
- Store raw XML in S3
- Publish article events to Kafka

#### Event Example
```json
{
  "id": "...",
  "title": "...",
  "content": "...",
  "date": "...",
  "source": "nytimes",
  "url": "..."
}
```

### 3. Indexing Service
Responsibilities:

- Consume Kafka topic
- Index data into OpenSearch/Solr

### 4. Search Service 

Responsibilities:

- Expose search APIs
- Query OpenSearch
- Return results

```
GET /search?q=ai
GET /search?category=world
GET /search?date=today
```

### 5. Agent Service
Responsibilities:
- Interpret user queries
- Decide actions
- Call search service
- Summarize results with LLM

#### Agent Flow Example:
                        User question
                              |
                              v

                        LLM interprets
                              |
                              v
                        Agent decides:
                        - search news
                        - summarize
                              |
                              v
                    Calls search API
                              |
                              v
                    Returns summarized response
#### 6. Main Service

Authentication
User management
Chat sessions
API gateway

#### 7. Frontend
Framework: React
Features:
- Chat interface
- Search page
- Login/Register
- Article viewer