from github_issue_browser.views import SendLink, RepoIssuesStats

routes = [
    ('*', '/', SendLink, 'send_link'),
    ('*', '/repo_info', RepoIssuesStats, 'get_repo_issues_stats'),
]
