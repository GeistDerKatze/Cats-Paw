# test_yoink.py
import pytest
from yoink import get_first_google_result
from unittest.mock import patch

@patch('yoink.GoogleSearch')
def test_get_first_google_result_structure(mock_search):
    mock_result = {
        "organic_results": [
            {
                "title": "Example Title",
                "link": "https://example.com",
                "snippet": "Example snippet"
            }
        ]
    }
    mock_search.return_value.get_dict.return_value = mock_result

    result = get_first_google_result("example search")
    assert isinstance(result, dict)
    assert "title" in result
    assert "link" in result
    assert "snippet" in result

