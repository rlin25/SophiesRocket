import requests

def query_llm(prompt):
    url = "http://localhost:11434/v1/chat/completions"
    headers = {
        "Content-Type": "application/json"
    }
    data = {
        "model": "openhermes",
        "messages": [
            {"role": "user", "content": prompt}
        ]
    }

    response = requests.post(url, json=data, headers=headers)
    response.raise_for_status()  # Throws error for non-2xx responses

    result = response.json()
    return result['choices'][0]['message']['content']

if __name__ == "__main__":
    try:
        print("Pinging Ollama API...")
        res = requests.get("http://localhost:11434", timeout=5)
        res.raise_for_status()
        print("Response:", res.text)
        print("✅ Ollama is reachable!")
    except Exception as e:
        print("❌ Failed to reach Ollama:", e)
