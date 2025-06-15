from dotenv import load_dotenv
import os
from langgraph.graph import StateGraph, END
from typing import TypedDict, Annotated, Sequence
from langchain_core.messages import BaseMessage, SystemMessage, HumanMessage, ToolMessage
from operator import add as add_messages
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from langchain_core.tools import tool
from src.rag.chroma_manager import retriever

load_dotenv()

llm = ChatGoogleGenerativeAI( model="gemini-2.5-flash-preview-05-20",
                              temperature = 0)



@tool
def retrieval_tool(query: str) -> str:
    """
    This tool searches and returns the information from the Stock market performance 2024 doc
    :param query:
    :return:
    """

    docs = retriever.invoke(query)

    if not docs:
        return "I found no relevant information in the Stock Market Performance 2024 document"

    results = []

    for i, doc in enumerate(docs):
        results.append(f"Document {i+1}:\n{doc.page_content}")

    return "\n\n".join(results)

tools = [retrieval_tool]

llm.bind_tools(tools)


class AgentState(TypedDict):
    messages: Annotated[Sequence[BaseMessage], add_messages]

def should_continue(state: AgentState):
    """Check if the last message contains tool calls."""
    result = state['messages'][-1]
    return hasattr(result, 'tool_calls') and len(result.tool_calls) > 0


system_prompt = """
You are an expert AI assistant and tutor specializing in preparation for the Politecnico's TOL Engineering admission test. Your sole source of knowledge is the uploaded PDF document, which contains all the basic math material needed to pass the test. Your goal is to help the user understand the concepts and solve problems based exclusively on this document.

Main Tasks:
1.  **Answer Specific Questions:** Clearly and accurately answer any questions about the mathematical topics covered in the PDF (e.g., logarithms, trigonometry, equations, geometry, etc.).
2.  **Explain Concepts:** Provide detailed, step-by-step explanations of theoretical concepts, as if you were a tutor helping a student understand a difficult topic.
3.  **Solve Exercises:** If asked, solve exercises from the document or similar problems, illustrating each step of your reasoning according to the methods explained in the PDF.
4.  **Summarize Topics:** Create concise summaries of specific chapters or sections of the document to help students review.

Fundamental Rules and Constraints:
-   **Strict Adherence to the Document:** You must base your answers **exclusively** on the information, formulas, and methods present in the uploaded PDF document. Do not use external knowledge.
-   **Source Citation:** In every answer, you **must always** cite the specific source within the document. Indicate the page number, chapter, or paragraph from which you derived the information. For example: "(as explained on page 25, chapter 3.2)".
-   **Honesty and Transparency:** If a question concerns a topic not covered in the PDF or requires information that is not present, you must state clearly: "This information is not available in the provided document."
-   **Didactic Style:** Use simple, encouraging, and educational language. Your goal is to help the student learn, not just to provide an answer.

Example Interaction:
-   **Student's Question:** "I don't understand how to solve trigonometric inequalities. Can you explain it to me based on the PDF?"
-   **Your Ideal Response:** "Of course. According to the trigonometry chapter on page 42 of the document, to solve a trigonometric inequality like sin(x) > 1/2, you need to follow these steps: 1. Find the associated angle by solving the equation sin(x) = 1/2... [detailed explanation]... This method is illustrated in example 5.3 on page 43."
"""

tools_dict = {our_tool.name: our_tool for our_tool in tools}  # Creating a dictionary of our tools


# LLM Agent
def call_llm(state: AgentState) -> AgentState:
    """Function to call the LLM with the current state."""
    messages = list(state['messages'])
    messages = [SystemMessage(content=system_prompt)] + messages
    message = llm.invoke(messages)
    return {'messages': [message]}


# Retriever Agent
def take_action(state: AgentState) -> AgentState:
    """Execute tool calls from the LLM's response."""

    tool_calls = state['messages'][-1].tool_calls
    results = []
    for t in tool_calls:
        print(f"Calling Tool: {t['name']} with query: {t['args'].get('query', 'No query provided')}")

        if not t['name'] in tools_dict:  # Checks if a valid tool is present
            print(f"\nTool: {t['name']} does not exist.")
            result = "Incorrect Tool Name, Please Retry and Select tool from List of Available tools."

        else:
            result = tools_dict[t['name']].invoke(t['args'].get('query', ''))
            print(f"Result length: {len(str(result))}")

        # Appends the Tool Message
        results.append(ToolMessage(tool_call_id=t['id'], name=t['name'], content=str(result)))

    print("Tools Execution Complete. Back to the model!")
    return {'messages': results}


graph = StateGraph(AgentState)
graph.add_node("llm", call_llm)
graph.add_node("retriever_agent", take_action)

graph.add_conditional_edges(
    "llm",
    should_continue,
    {True: "retriever_agent", False: END}
)
graph.add_edge("retriever_agent", "llm")
graph.set_entry_point("llm")

rag_agent = graph.compile()


def running_agent():
    print("\n=== RAG AGENT===")

    while True:
        user_input = input("\nWhat is your question: ")
        if user_input.lower() in ['exit', 'quit']:
            break

        messages = [HumanMessage(content=user_input)]  # converts back to a HumanMessage type

        result = rag_agent.invoke({"messages": messages})

        print("\n=== ANSWER ===")
        print(result['messages'][-1].content)

if __name__ == "__main__":
    running_agent()
