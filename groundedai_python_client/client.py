import requests

class GroundedAIClient:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://api.groundedai.tech"

    def _make_request(self, endpoint, payload):
        headers = {
            "Content-Type": "application/json",
            "X-API-Key": self.api_key,  # Include the API key as a header
        }
        url = f"{self.base_url}{endpoint}"
        try:
            response = requests.post(url, headers=headers, json=payload)
            response.raise_for_status()  # Raise exception for HTTP errors (4xx or 5xx)
            return response.json()
        except requests.RequestException as e:
            print(f"Error making request to {url}: {e}")
            return None

    def evaluate_answer(self, prompt, answer, context=None):
        payload = {
            "prompt": prompt,
            "answer": answer,
            "context": context,
        }
        return self._make_request("/evaluate", payload)
    
    def evaluate_statistical(self, ground_truth, retrieved_docs, metrics):
        payload = {
            "retrieval_data": {
                "ground_truth": ground_truth,
                "retrieved_documents": retrieved_docs,
            },
            "metrics": metrics,
        }
        return self._make_request("/statistical-eval/retrieval", payload)

# Example usage
client = GroundedAIClient("JxIMMg8kE4amuQfjY5gJPafDA7jm3U6Y5meRhsX5")

# Example statistical evaluator usage:
ground_truth = [
    ["Country A", "Country B", "Country C"],
    ["Era X", "Era Y", "Era Z"]
]
retrieved_docs = [
    ["Country A", "Country D", "Country F"],
    ["Era X", "Era Y", "Era Alpha", "Era Beta"]
]
metrics = [
    "mrr",
    "map",
    "recall"
]

evaluation_results = client.evaluate_statistical(ground_truth, retrieved_docs, metrics)
print(evaluation_results)

