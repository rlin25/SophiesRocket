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