import requests
import datetime


def get_trending_repositories():
    repos_api_link = "https://api.github.com/search/repositories"
    today = datetime.date.today()
    week_ago = today - datetime.timedelta(days=7)
    number_of_repos = 20
    params = {
        "q": "created:>={}".format(week_ago.isoformat()),
        "sort": "stars",
        "order": "desc",
        "page": "1",
        "per_page": number_of_repos,
    }
    trending_repos = requests.get(repos_api_link, params=params)
    return trending_repos.json()


def get_open_issues_amount(link):
    issues_url = "{0}/issues".format(link)
    return len(requests.get(issues_url).json())


if __name__ == '__main__':
    for repo in get_trending_repositories()["items"]:
        repo_name = repo["name"]
        user_name = repo["owner"]["login"]
        link = repo["url"]
        print("User name - ", user_name, end="; ")
        print("Repository name - ", repo_name, end="; ")
        print("Number of issues - ", get_open_issues_amount(link))
