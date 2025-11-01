
import requests

def get_embedding(prompt, model="nomic-embed-text"):
    url = "http://localhost:11434/api/embeddings"
    headers = {"Content-Type": "application/json"}
    data = {"prompt": prompt, "model": model}

    response = requests.post(url, headers=headers, json=data)
    print("Status:", response.status_code)
    print("Response:", response.text[:200])  # show only first 200 chars

    if response.status_code == 200:
        return response.json().get("embedding", [])
    else:
        raise Exception(
            f"Error fetching embedding: {response.status_code}, {response.text}"
        )


if __name__ == "__main__":
    sample_prompt = "The sky is blue because of Rayleigh scattering."
    try:
        embedding = get_embedding(sample_prompt)
        if not embedding:
            print(f"⚠️ No embedding generated for: {title}")
        print("Embedding Dimesion:", len(embedding))
        print("Embedding:", embedding)
    except Exception as e:
        print(f"Failed to get embedding: {e}")
