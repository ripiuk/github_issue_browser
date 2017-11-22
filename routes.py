from github_issue_browser.views import SendLink, RepoIssuesStats

routes = [
    ('*', '/', SendLink, 'send_link'),
    ('*', '/issues_stats', RepoIssuesStats, 'get_repo_issues_stats'),
]
