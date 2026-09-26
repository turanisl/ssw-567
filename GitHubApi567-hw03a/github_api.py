import requests

def get_repositories(user_id): # names of repos
    url = f"https://api.github.com/users/{user_id}/repos"
    response = requests.get(url, timeout=10)
    response.raise_for_status()

    repositories = response.json()
    return [repo["name"] for repo in repositories]


def get_commit_count(user_id, repo_name): # num of commits
    url = f"https://api.github.com/repos/{user_id}/{repo_name}/commits"
    response = requests.get(url, timeout=10)
    response.raise_for_status()

    commits = response.json()
    return len(commits)


def get_repo_summary(user_id): # repo name and num of commits
    repositories = get_repositories(user_id)
    results = []

    for repo_name in repositories:
        commit_count = get_commit_count(user_id, repo_name)
        results.append((repo_name, commit_count))

    return results


def display_repositories(user_id): # repos and commit count
    results = get_repo_summary(user_id)

    for repo_name, commit_count in results:
        print(f"Repo: {repo_name} Number of commits: {commit_count}")


if __name__ == "__main__":
    github_user = input("Enter GitHub user ID: ")
    display_repositories(github_user)