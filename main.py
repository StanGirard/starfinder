import os
import csv
import requests
from dotenv import load_dotenv
import pandas as pd

load_dotenv()  # take environment variables from .env.


def save_to_csv(data, filename):
    """Saves a list of dictionaries to a CSV file.

    Args:
        data (list of dict): The data to save.
        filename (str): The name of the file to save the data in.
    """

    print("Saving to CSV")
    print("Filename:", filename)
    if not data:
        return

    keys = data[0].keys()
    with open(filename, "w", newline="") as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(data)


def get_user_info(username: str, github_token: str) -> dict:
    """Takes a GitHub username and token, and returns the user's information.

    Args:
        username (str): The GitHub username.
        github_token (str): The GitHub token.

    Returns:
        dict: The user's information.
    """
    try:
        print(f"Getting user info for {username}")
        url = f"https://api.github.com/users/{username}"
        headers = {
            "Authorization": f"token {github_token}",
            "Accept": "application/vnd.github.v3+json",
        }
        response = requests.get(url, headers=headers)
        user = response.json()
        user_info = {
            "username": user.get("login"),
            "html_url": user.get("html_url"),
            "type": user.get("type"),
            "name": user.get("name"),
            "blog": user.get("blog"),
            "location": user.get("location"),
            "email": user.get("email"),
            "bio": user.get("bio"),
            "twitter_username": user.get("twitter_username"),
            "followers": user.get("followers"),
            "following": user.get("following"),
            "created_at": user.get("created_at"),
            "updated_at": user.get("updated_at"),
            "public_repos": user.get("public_repos"),
        }
        return user_info
    except Exception as e:
        print(f"Error getting user info for {username}: {e}")
        return None


def get_forks(repository: str, github_token: str) -> list:
    """Takes the github token and returns the list of forked usernames.

    Args:
        github_token (_type_): _description_

    Returns:
        _type_: _description_
    """
    print("Getting forks")
    if os.path.exists("forks.csv"):
        print("Forks already saved")
        return pd.read_csv("forks.csv").to_dict("records")

    forks_info = []
    page = 1
    while True:
        url = (
            f"https://api.github.com/repos/{repository}/forks?page={page}&per_page=100"
        )
        headers = {
            "Authorization": f"token {github_token}",
            "Accept": "application/vnd.github.v3+json",
        }
        response = requests.get(url, headers=headers)
        forks = response.json()
        if not forks:
            break
        for fork in forks:
            forks_info.append(
                {
                    "username": fork["owner"]["login"],
                    "created_at": fork["created_at"],
                    "updated_at": fork["updated_at"],
                }
            )
        page += 1
        print(f"Page {page} done")
    return forks_info


if __name__ == "__main__":
    github_token = os.getenv("GITHUB_TOKEN")
    forks_info = get_forks("quivrhq/quivr", github_token)
    save_to_csv(forks_info, "forks.csv")

    user_info_list = []
    user_number = 0
    for fork in forks_info:
        user_info = get_user_info(fork["username"], github_token)
        if user_info is not None:
            print(f"User {user_number} done")
            user_number += 1
            user_info_list.append(user_info)

    save_to_csv(user_info_list, "user_info.csv")
