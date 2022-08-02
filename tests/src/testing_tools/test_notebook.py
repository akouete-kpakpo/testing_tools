from pathlib import Path
from typing import Any

import pytest

from testing_tools.common_path import NOTEBOOK_PATH, ROOT_DIR
from testing_tools.error import does_not_raise


@pytest.mark.ut
@pytest.mark.parametrize("path", [ROOT_DIR / "notebook"])
def test_list_notebooks_lists_all_notebooks_relative_path(path: Path) -> None:
    # Given
    from testing_tools.notebook import list_notebooks

    expected = sorted(
        [
            "notebook/01-0-output-0-error.ipynb",
            "notebook/02-1-output-0-error.ipynb",
            "notebook/03-0-output-1-error.ipynb",
            "notebook/04-1-output-1-error.ipynb",
            "notebook/05-0-output-0-error-1-markdown.ipynb",
            "notebook/06-1-output-0-error-1-markdown.ipynb",
            "notebook/07-0-output-1-error-1-markdown.ipynb",
            "notebook/08-1-output-1-error-1-markdown.ipynb",
            "notebook/09-tqdm.ipynb",
        ]
    )
    # When
    notebooks = list_notebooks(path, relative=ROOT_DIR)

    # Then
    assert notebooks == expected


@pytest.mark.ut
@pytest.mark.parametrize(
    "notebook, expectation",
    [
        ("01-0-output-0-error.ipynb", does_not_raise()),
        ("02-1-output-0-error.ipynb", pytest.raises(AssertionError)),
        ("03-0-output-1-error.ipynb", does_not_raise()),
        ("04-1-output-1-error.ipynb", pytest.raises(AssertionError)),
        ("05-0-output-0-error-1-markdown.ipynb", does_not_raise()),
        ("06-1-output-0-error-1-markdown.ipynb", pytest.raises(AssertionError)),
        ("07-0-output-1-error-1-markdown.ipynb", does_not_raise()),
        ("08-1-output-1-error-1-markdown.ipynb", pytest.raises(AssertionError)),
        ("09-tqdm.ipynb", does_not_raise()),
    ],
)
def test_assert_notebook_is_without_output_raises_when_expected(
    notebook: str, expectation: Any
) -> None:
    # Given
    from testing_tools.notebook import assert_notebook_is_without_outputs

    # Then
    with expectation:
        assert_notebook_is_without_outputs(NOTEBOOK_PATH / notebook)
