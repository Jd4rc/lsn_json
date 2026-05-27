import requests
import json


def fetch_github_repositories(
        username:str
) -> list[dict]:

    response = requests.get(
        f'https://api.github.com/users/{username}/repos'
    )

    response.raise_for_status()

    return response.json()


print(json.dumps(fetch_github_repositories('Jd4rc'), indent=4, ensure_ascii=False))