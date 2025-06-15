## Project To-Do List (Simple)

This is a simplified list of tasks to track the main development progress.

*   [ ] **Basic Project Setup:**
    *   [ ] Create repository and set up initial file structure.
    *   [ ] Set up `.gitignore`, `requirements.txt`, and `.env.example`.
    *   [ ] Write basic `README.md`.

*   [ ] **FastAPI Backend & Agent Core:**
    *   [ ] Set up basic FastAPI application (`api.py`).
    *   [ ] Implement agent component initialization (LLM, Embeddings, Chroma, Tools, LangGraph) in FastAPI lifespan.
    *   [ ] Create `/chat` API endpoint in FastAPI to receive user messages.
    *   [ ] Integrate calling the LangGraph agent from the `/chat` endpoint and return the response.

*   [ ] **RAG System Implementation:**
    *   [ ] Implement document loading, splitting, and embedding.
    *   [ ] Set up ChromaDB persistence and adding documents.
    *   [ ] Implement the retriever logic.
    *   [ ] Integrate RAG into the LangGraph agent workflow.

*   [ ] **Tool Implementation & Integration:**
    *   [ ] Define the tools (API, code, email, file writing).
    *   [ ] Implement the logic for each tool.
    *   [ ] Add the tools to the LangGraph agent's available tools.

*   [ ] **Basic Web Frontend (Chat UI):**
    *   [ ] Create basic HTML structure for the chat page (`index.html`).
    *   [ ] Add basic CSS for styling (`style.css`).
    *   [ ] Implement JavaScript logic (`script.js`) for sending/receiving chat messages via the `/chat` API.
    *   [ ] Configure FastAPI to serve the static frontend files.

*   [ ] **Document Upload Feature:**
    *   [ ] Add file input and upload button to the frontend HTML.
    *   [ ] Implement JavaScript logic to send selected files to the backend.
    *   [ ] Create a new FastAPI endpoint (`/upload_documents`) to receive files.
    *   [ ] Implement backend logic to process uploaded files and add them to ChromaDB.

*   [ ] **Testing, Refinement & Documentation:**
    *   [ ] Test core agent functionality (RAG and Tools) via the API/GUI.
    *   [ ] Test document upload feature.
    *   [ ] Refine agent prompts and LangGraph workflow.
    *   [ ] Add comments to complex code sections.
    *   [ ] Complete and update the `README.md` with detailed instructions and features.