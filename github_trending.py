import requests
import datetime


def get_trending_repositories():
    trending_repos = requests.get(url).json()
    return trending_repos


def get_open_issues_amount(trending_repos):
    dictionary_of_names_and_issues = {}
    for feature in trending_repos['items']:
        dictionary_of_names_and_issues[feature["name"]] = [feature['open_issues_count'], feature['svn_url']]
    for repo_name in sorted(dictionary_of_names_and_issues, key=lambda capital_letter: capital_letter.upper()):
        repo_issues = dictionary_of_names_and_issues[repo_name]
        print(repo_name, "-", repo_issues)


if __name__ == '__main__':
    today = datetime.date.today()
    week_ago = today - datetime.timedelta(days=7)
    url = 'https://api.github.com/search/repositories?q=created:>=' + str(
        week_ago) + '&sort=stars&order=desc&page=1&per_page=20'
    print(get_open_issues_amount(get_trending_repositories()))
