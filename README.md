# 🧠 MCP Multi-Server Client with  LLM  
A modular **Model Context Protocol (MCP)** project showcasing how a single AI client can connect to multiple independent servers.

This repository demonstrates:

- 🔢 **Arithmetic Calculator Server**  
- 🌤️ **Weather API Server**  
- 💱 **Real-Time Currency Converter Server**  
- 🤖 **LLM Client powered by Groq's LLaMA 3.1 8B /Any LLM**  
- ⚡ Built using **FastMCP**, **LangChain**, and **uv** package manager  

This project is perfect for learning how to build real-world MCP tools and integrate them into a unified AI assistant.

---

## 🚀 Features

### **1. Arithmetic Calculator Server**
A simple MCP tool that performs:

- Addition  
- Subtraction  
- Multiplication  
- Division  

Supports symbolic (`*`) and text (`multiply`) operations.

---

### **2. Weather Server**
Provides:

- Current weather  
- Weather forecast  
- Comparison of two cities  

Uses external weather API with API keys managed through environment variables.

---

### **3. Currency Converter Server**
Real-time conversion using open APIs:

- USD → INR  
- INR → EUR  
- GBP → USD  
- and many more…

Returns JSON with rate and converted value.

---

### **4. Unified AI Client**
A centralized client built using:

- **LangChain** for LLM handling  
- **ChatGroq (LLaMA 3.1 8B)/ You can use any LLM** for reasoning  
- **MultiServerMCPClient** for dynamic tool loading  

The client automatically:

- Reads all registered tools  
- Allows LLM to decide when to call which tool  
- Combines tool responses to generate a final user-friendly output

---

## 🛠️ Tech Stack

| Component | Technology |
|----------|------------|
| MCP Servers | FastMCP |
| MCP Client | LangChain + MultiServerMCPClient |
| LLM | Groq LLaMA | OpenAI
| Package Manager | uv |
| API Calls | httpx |
| Environment Management | python-dotenv |

---
## Steps to Use this Repo
### 🔑 Environment Variables

Create a `.env` file in the project root:

- WEATHER_API_KEY=your_api_key_here
- GROQ_API_KEY=your_groq_key_here

  
> ⚠️ **IMPORTANT NOTE:**  
> The Weather Server requires a **valid Weather API key**.  
> Use you own API KEY  
> Each user must obtain their **own API key** from the weather provider and place it inside their personal `.env` file.  
>  
> Example sources for weather API keys:   
> - https://weatherapi.com  

### 1. Clone the repository

```bash
git clone https://github.com/Abhishek3689/Mcp-Multiserver-Client.git
```
### 2.Install dependencies using uv
```
uv init
uv add fastmcp langchain langchain-core langchain-groq langchain-mcp-adapters httpx python-dotenv
```

### 3.Run client 
```
python client.py
```
or
```
uv run client.py
```



