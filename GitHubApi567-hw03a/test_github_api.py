import unittest

from github_api import (
    get_repositories,
    get_commit_count,
    get_repo_summary,
)


class GitHubApiTest(unittest.TestCase):

    def test_get_repositories(self):
        repositories = get_repositories("richkempinski")

        self.assertIn("hellogitworld", repositories)


    def test_get_commit_count(self):
        commit_count = get_commit_count(
            "richkempinski",
            "hellogitworld"
        )

        self.assertGreater(commit_count, 0)


    def test_get_repo_summary(self):
        results = get_repo_summary("richkempinski")

        repository_names = [
            repo_name for repo_name, commit_count in results
        ]

        self.assertIn("hellogitworld", repository_names)


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)