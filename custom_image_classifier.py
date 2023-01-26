import base64
import json
import random

import requests
from label_studio_ml.model import LabelStudioMLBase
from label_studio_ml.utils import (get_choice, get_local_path,
                                   get_single_tag_keys, is_skipped)
from requests import Response

model_endpoint = "https://isjghav76e.execute-api.ap-south-1.amazonaws.com/dev/inference"


def inference(url):

    image_path = get_local_path(url)

    with open(image_path, "rb") as f:
        ext = image_path.split(".")[-1]
        prefix = f"data:image/{ext};base64,"
        base64_data = prefix + base64.b64encode(f.read()).decode("utf-8")

    payload = json.dumps({"body": [base64_data]})

    headers = {"Content-Type": "application/json"}

    response: Response = requests.request(
        "POST", model_endpoint, headers=headers, data=payload, timeout=15
    )
    data = response.json()[0]

    label = max(data, key=data.get)
    score = data[label]

    print(f"\t :: {image_path} -> ", label, " | ", score)
    return label, score


class ImageClassifierAPI(LabelStudioMLBase):
    def __init__(self, **kwargs):
        super(ImageClassifierAPI, self).__init__(**kwargs)
        self.from_name, self.to_name, self.value, self.classes = get_single_tag_keys(
            self.parsed_label_config, "Choices", "Image"
        )

    def predict(self, tasks, **kwargs):
        image_urls = [task["data"][self.value] for task in tasks]
        predictions = []

        for url in image_urls:
            predicted_label, score = inference(url)

            result = [
                {
                    "from_name": self.from_name,
                    "to_name": self.to_name,
                    "type": "choices",
                    "value": {"choices": [predicted_label]},
                }
            ]

            # expand predictions with their scores for all tasks
            predictions.append({"result": result, "score": float(score)})

        return predictions

    def fit(self, completions, workdir=None, batch_size=32, num_epochs=10, **kwargs):
        """This is where training happens: train your model given list of completions,
        then returns dict with created links and resources

        :param completions: aka annotations, the labeling results from Label Studio
        :param workdir: current working directory for ML backend
        """
        # save some training outputs to the job result
        return {"random": random.randint(1, 10)}
