# Modular RAG Baseline Application

A modular Retrieval-Augmented Generation (RAG) system built in native Python using official SDKs (`ollama`, `chromadb`).


## How to Run the Application

1. **Prerequisites:**
   Ensure Ollama is running locally with the required models downloaded:
   ```bash
   ollama pull llama3.2
   ollama pull nomic-embed-text
   1.Install Dependencies
   poetry install
   2.Ingest Documents
   Populate ChromaDB with vector embeddings of text files in data/:
   poetry run python -m app.ingest
   3.Run the interactive CLI
   poetry run python -m app.main

   ## Architectural Design Choices

   Chunking Strategy: Fixed-size chunking with sliding window overlap (chunk_size=500, chunk_overlap=100).

Reasoning: A 500-character chunk size preserves localized context and paragraphs without exceeding context windows. The 100-character overlap ensures critical context across chunk boundaries is not lost during text splitting.

Embedding Model: nomic-embed-text via Ollama API.

Reasoning: Outputs 768-dimensional embeddings designed specifically for semantic search tasks, running efficiently on local hardware.

Vector Database: ChromaDB (Persistent Mode).

Reasoning: Operates locally without requiring Docker containers or external servers, persisting vectors efficiently via an HNSW index (chroma.sqlite3).

Generation Model: llama3.2 via Ollama API.

Reasoning: Compact 3B parameter model providing fast inference and strict instruction-following capabilities for grounded answers.

### Deliverable 3: Test Log (Step 7 Sample)
```text
==================================================
 Welcome to the Modular RAG CLI Application!
==================================================
[Query 1 - In Context]
Enter your question: How to verify email account?

[1/2] Retrieving relevant context...
      Retrieved 3 chunks from: 001_Setting_Up_a_Mobile_Device_for_Company_Email.txt

[2/2] Generating answer using LLM...

==================================================
ANSWER:
==================================================
To verify an email account, follow these steps:
1. Wait for the email account to synchronize with the company email server.
2. Send a test email to yourself or a colleague to verify that email is sending and receiving correctly.

This process ensures the account is properly configured and functional.
==================================================
[Query 2 - Out Context]
Enter your question: What is the remote work policy?

[1/2] Retrieving relevant context...
      Retrieved 3 chunks from: 003_Configuring_VPN_Access_for_Remote_Workers.txt
[2/2] Generating answer using LLM...

==================================================
ANSWER:
==================================================
I don't have enough information to provide an answer to your question. The context only provides general information about configuring VPN access for remote workers and some security reminders, but it does not explicitly state a remote work policy.
==================================================

[Query 3 - In Context]
Enter your question: How do I clear a paper jam on the office printer?

[1/2] Retrieving relevant context...
      Retrieved 3 chunks from: 009_Resetting_a_Jammed_Printer.txt
[2/2] Generating answer using LLM...

==================================================
ANSWER:
==================================================
According to the provided context, to clear a paper jam on the office printer, follow the steps outlined in the "Resetting a Jammed Printer" section:

1. Turn Off the Printer
2. Open the Printer
3. Identify and Remove Jammed Paper
4. Check for Obstructions
==================================================

[Query 4 - In Context]
Enter your question: What security step are needed for wifi set up?

[1/2] Retrieving relevant context...
      Retrieved 3 chunks from: 008_Setting_Up_a_Secure_Wireless_Network.txt
[2/2] Generating answer using LLM...

==================================================
ANSWER:
==================================================
According to the provided context, the following security steps are needed for WiFi setup:

[Query 5 - In Context]
Enter your question: How do I configure VPN access for romote work?

[1/2] Retrieving relevant context...
      Retrieved 3 chunks from: 003_Configuring_VPN_Access_for_Remote_Workers.txt
[2/2] Generating answer using LLM...

==================================================
ANSWER:
==================================================
To configure VPN access for remote work, follow these steps:

1. Install the VPN client software by downloading it from the company's software portal.
2. Run the installer and follow the prompts to install the software.
3. Once installed, launch the VPN client software.
4. In the VPN client software, click on "New Connection".
5. Follow the prompts to authenticate with two-factor authentication (2FA) if required.
6. Establish the VPN connection by clicking the "Connect" or "Establish" button.
7. Verify your VPN connection by opening a web browser and navigating to `company.com`, and access company resources such as email, intranet, and file shares.
==================================================


1. **Step 1: Plan Your Wireless Network** - Identify the number of users, devices, and access points required, and determine the type of encryption and authentication methods to be used.
2. **Step 2: Choose a Secure Wireless Protocol** - Select a secure wireless protocol such as WPA2-PSK (AES) or WPA3-PSK (AES-256).
3. **Step 3: Set Up a Strong Password** - Create a strong password that is at least 12 characters long and includes a mix of uppercase and lowercase letters, numbers, and special characters.
4. **Step 4: Configure Your Router** - Change the default administrator password and network name (SSID), enable WPA2-PSK or WPA3-PSK encryption, and set the password created in Step 3.
5. **Step 5: Set Up a Guest Network (Optional)** - If needed, set up a separate guest network using a secure wireless protocol such as WPA2-PSK (AES) or WPA3-PSK (AES-256).

These steps ensure a secure WiFi setup by using a strong password, choosing a secure wireless protocol, and configuring the router accordingly.
==================================================

## Reflection & Takeaways

1. **Transitioning from Frameworks to Native SDKs:**
   Building a RAG application natively using `ollama` and `chromadb` SDKs directly provided clearer transparency into vector operations compared to high-level orchestration abstractions (like LangChain). Managing explicitly defined functions for document reading, chunking, embedding generation, vector indexing, and context injection simplified debugging.

2. **Retrieval Precision & Grounding:**
   Restricting the generation model's context strictly to retrieved vector database chunks effectively eliminated hallucinations. The system accurately deferred to provided facts and explicitly flagged missing context when queries fell outside the dataset scope.

3. **Performance Trade-offs:**
   Local execution of embedding and LLM generation via Ollama provided strict data privacy and zero API costs. The primary trade-off is inference latency dependent on local compute resources, which was mitigated by keeping chunk sizes optimized (`500` characters) and model parameter sizes focused 
