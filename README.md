# [WORK IN PROGRESS] My GenAI RAG Agent ReAct Backend

This project implements a RAG Agent using the ReAct pattern with FastAPI for the API layer. The structure is designed for modularity and production readiness.

The diagram below illustrates the main components and how a typical request flows through the application.

```mermaid
graph LR
    %% Nodes representing key components/modules
    Request((User Request)) --> APIRouter[API Router];

    APIRouter --> AgentLogic[Agent Logic];

    AgentLogic -- Uses --> LLMLayer[LLM Layer];
    AgentLogic -- Uses --> ToolsLayer[Tools Layer];

    %% Example of a tool interaction
    ToolsLayer -- |e.g., Vector Search Tool| --> VectorDBLayer[Vector DB Layer];

    LLMLayer --> LLM_Provider(LLM Provider);
    %% Standard database shape syntax
    VectorDBLayer --> VectorDB[(Vector Database)];

    Config[Configuration] --> AgentLogic;
    Config --> LLMLayer;
    Config --> VectorDBLayer;
    Config --> ToolsLayer;

    %% Flow of information/control during a request
    LLM_Provider -- Response/Action --> LLMLayer;
    LLMLayer -- Output --> AgentLogic;

    VectorDB -- Results --> VectorDBLayer;
    VectorDBLayer -- Observation --> ToolsLayer;
    ToolsLayer -- Observation --> AgentLogic;

    AgentLogic -- Final Answer --> APIRouter;
    APIRouter --> Response((User Response));

    %% Styling (Optional, makes external services stand out)
    %% Added color:#000; for black text on external nodes
    classDef external fill:#f9f,stroke:#333,stroke-width:2px,color:#000;
    class LLM_Provider,VectorDB external;

    %% Optional: Group internal source code modules
    %% Grouping application source code components
    subgraph Application Code
        APIRouter
        AgentLogic
        LLMLayer
        ToolsLayer
        VectorDBLayer
        Config
    end

    subgraph External Services
       LLM_Provider
       VectorDB
    end

    subgraph Scripts
        DataIngestion
    end