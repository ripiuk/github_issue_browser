from github_issue_browser.views import SendLink
routes = [
    ('*', '/', SendLink, 'send_link'),
]
