# 🧠 PatendMind: Advanced Local RAG for Patent Intelligence

**PatendMind** is an advanced end-to-end **Retrieval-Augmented Generation (RAG)** system designed to perform **patent trend forecasting and innovation analysis** locally.  
It integrates **CrewAI agents**, **LangChain**, **DeepSeek via Ollama**, **OpenSearch**, **Docker**, and **SerpAPI** to autonomously fetch, embed, and analyze patent data — all while running entirely on your local environment for **data privacy and performance**.

---

## 🚀 Core Capabilities

- 🔍 **Fetch real-time patent data** from global sources using **SerpAPI**
- 🧬 **Generate embeddings locally** using **Nomic Embed (nomic-embed-text)** via **Ollama**
- 🧠 **Use DeepSeek LLM** for reasoning, summarization, and patent insight generation
- 🔗 **Perform keyword, semantic, and hybrid retrieval** using **OpenSearch Vector DB**
- 🤖 **Build autonomous multi-agent workflows** with **CrewAI** and **LangChain**
- 📊 **Implement chunked RAG pipelines** for contextual and efficient retrieval
- 📈 **Forecast innovation trends** (e.g., Lithium Battery Technology case study)

---

## 🧩 Technology Stack

| Layer | Technology | Purpose |
|-------|-------------|----------|
| **Agents & Orchestration** | [CrewAI](https://github.com/joaomdmoura/crewai) | Manages multi-agent workflows for analysis |
| **Framework** | [LangChain](https://www.langchain.com/) | Chains components for RAG and memory |
| **LLM Runtime** | [Ollama](https://ollama.ai/) | Runs DeepSeek locally for reasoning |
| **LLM Model** | DeepSeek | Local model for contextual reasoning |
| **Embeddings** | Nomic Embed (nomic-embed-text) | Converts patent text to dense vector embeddings |
| **Database** | [OpenSearch](https://opensearch.org/) | Stores and retrieves vector + keyword data |
| **Data Source** | [SerpAPI](https://serpapi.com/) | Fetches real-time patent data |
| **Containerization** | [Docker](https://www.docker.com/) | Runs OpenSearch and Ollama containers |
| **Language** | Python 3.11+ | Core application logic |
| **Environment** | macOS | Tested on local macOS setup |

---

## 🧠 System Flow

```text
User Query
   │
   ▼
SerpAPI → Fetch Patent Data
   │
   ▼
Nomic Embed (via Ollama) → Generate Embeddings
   │
   ▼
OpenSearch → Store and Retrieve Vectors
   │
   ▼
CrewAI + LangChain → Multi-Agent Analysis
   │
   ▼
DeepSeek → Generate Insights and Forecasts
