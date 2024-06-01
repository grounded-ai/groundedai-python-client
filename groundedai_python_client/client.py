import requests


class GroundedAIClient:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://api.groundedai.tech"

    def _make_request(self, endpoint, payload):
        headers = {
            "Content-Type": "application/json",
            "X-API-Key": self.api_key, 
        }
        url = f"{self.base_url}{endpoint}"
        try:
            response = requests.post(url, headers=headers, json=payload)
            response.raise_for_status()  
            return response.json()
        except requests.RequestException as e:
            print(f"Error making request to {url}: {e}")
            return None

    def evaluate_answer(self, predicted_answers, ground_truth_answers, metrics):
        payload = {
            "answers": {
                "predicted": predicted_answers,
                "groundtruth": ground_truth_answers,
            },
            "metrics": metrics,
        }
        return self._make_request("/answer-eval", payload)

    def evaluate_statistical(self, ground_truth, retrieved_docs, metrics):
        payload = {
            "retrieval_data": {
                "ground_truth": ground_truth,
                "retrieved_documents": retrieved_docs,
            },
            "metrics": metrics,
        }
        return self._make_request("/statistical-eval/retrieval", payload)


    def model_evaluate_retrieval(self, questions, contexts, responses, metrics):
        payload = {
            "retrieval_data": {
                "questions": questions,
                "contexts": contexts,
                "responses": responses,
            },
            "metrics": metrics,
        }
        return self._make_request("/model-eval/retrieval", payload)
