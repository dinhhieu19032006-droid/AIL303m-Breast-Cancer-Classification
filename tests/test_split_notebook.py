from __future__ import annotations

import json
import unittest
from pathlib import Path


NOTEBOOK = Path(__file__).resolve().parents[1] / "notebooks" / "02_thiet_lap_du_lieu_thi_nghiem.ipynb"


class SplitNotebookScopeTests(unittest.TestCase):
    def test_notebook_creates_reproducible_split_without_model_training(self) -> None:
        """Notebook 02 must only create one shared, reproducible experiment split."""
        notebook = json.loads(NOTEBOOK.read_text(encoding="utf-8"))
        content = "\n".join("".join(cell["source"]) for cell in notebook["cells"])

        self.assertEqual(notebook["nbformat"], 4)
        for required_item in [
            "train_test_split",
            "test_size=0.20",
            "stratify=y",
            "random_state=42",
            "train_indices.csv",
            "test_indices.csv",
            "split_metadata.json",
            "sha256",
        ]:
            self.assertIn(required_item, content)

        for forbidden_item in ["StandardScaler", "SVC(", "KNeighborsClassifier", "DecisionTreeClassifier", "GridSearchCV"]:
            self.assertNotIn(forbidden_item, content)


if __name__ == "__main__":
    unittest.main()
