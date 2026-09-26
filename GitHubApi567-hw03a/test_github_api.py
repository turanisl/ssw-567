import unittest
from unittest.mock import patch, Mock

from github_api import (
    get_repositories,
    get_commit_count,
    get_repo_summary,
)

class GitHubApiTest(unittest.TestCase):

    @patch("github_api.requests.get")
    def test_get_repositories(self, mock_get):
        mock_response = Mock()
        mock_response.json.return_value = [
            {"name": "Repo1"},
            {"name": "Repo2"}
        ]
        mock_get.return_value = mock_response

        result = get_repositories("testuser")

        self.assertEqual(result, ["Repo1", "Repo2"])


    @patch("github_api.requests.get")
    def test_get_commit_count(self, mock_get):
        mock_response = Mock()
        mock_response.json.return_value = [
            {"sha": "commit1"},
            {"sha": "commit2"},
            {"sha": "commit3"}
        ]
        mock_get.return_value = mock_response

        result = get_commit_count("testuser", "Repo1")

        self.assertEqual(result, 3)


    @patch("github_api.get_commit_count")
    @patch("github_api.get_repositories")
    def test_get_repo_summary(self, mock_repositories, mock_commit_count):
        mock_repositories.return_value = ["Repo1", "Repo2"]
        mock_commit_count.side_effect = [3, 5]

        result = get_repo_summary("testuser")

        self.assertEqual(
            result,
            [
                ("Repo1", 3),
                ("Repo2", 5)
            ]
        )

if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)