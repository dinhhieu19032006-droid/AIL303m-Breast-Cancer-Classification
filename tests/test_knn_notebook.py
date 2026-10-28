from __future__ import annotations

import json
import unittest
from pathlib import Path


NOTEBOOK = Path(__file__).resolve().parents[1] / "notebooks" / "03_knn.ipynb"


class KnnNotebookScopeTests(unittest.TestCase):
    def test_knn_notebook_uses_shared_split_and_required_visualizations(self) -> None:
        """KNN tuning must be fair, reproducible, and produce the agreed analysis artifacts."""
        notebook = json.loads(NOTEBOOK.read_text(encoding="utf-8"))
        content = "\n".join("".join(cell["source"]) for cell in notebook["cells"])

        self.assertEqual(notebook["nbformat"], 4)
        for required_item in [
            "train_indices.csv",
            "test_indices.csv",
            "split_metadata.json",
            "StandardScaler",
            "KNeighborsClassifier",
            "GridSearchCV",
            "StratifiedKFold",
            "f1_macro",
            "GRID_SEARCH_N_JOBS = 1",
            "verbose=2",
            "confusion_matrix.png",
            "roc_curve.png",
            "heatmap_euclidean.png",
            "heatmap_manhattan.png",
            "line_chart_k_f1_macro.png",
            "scatter_f1_vs_recall_malignant.png",
        ]:
            self.assertIn(required_item, content)

        self.assertNotIn("train_test_split(", content)
        self.assertNotIn("SVC(", content)
        self.assertNotIn("DecisionTreeClassifier", content)


if __name__ == "__main__":
    unittest.main()
