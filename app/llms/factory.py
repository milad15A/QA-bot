from langchain_ollama import ChatOllama
import os   

Model_name = os.environ.get("MODEL_NAME", "llama3.1")

def get_llm():
    try:
        llm = ChatOllama(
                    model=Model_name,
                    temperature=0.1)
        print(f"✅ Ollama model {Model_name} loaded successfully")
        return llm
    except Exception as e:
        print(f"⚠️ Ollama error: {e}")
        print("Make sure Ollama is running → ollama serve")
        return None
    
        from langchain_core.language_models import FakeListLLM
        return FakeListLLM(responses=["Ollama is not available"])
    
if __name__ == "__main__":
    llm = get_llm()

    response = llm.invoke("What is Python?")
    print(response.content)