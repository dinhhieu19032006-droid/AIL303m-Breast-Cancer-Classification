from __future__ import annotations

import json
import unittest
from pathlib import Path


NOTEBOOK = Path(__file__).resolve().parents[1] / "notebooks" / "01_kham_pha_va_tien_xu_ly.ipynb"


class EdaNotebookScopeTests(unittest.TestCase):
    def test_notebook_has_required_scope_without_model_training(self) -> None:
        """The first notebook documents data preparation only, not model experiments."""
        notebook = json.loads(NOTEBOOK.read_text(encoding="utf-8"))
        content = "\n".join("".join(cell["source"]) for cell in notebook["cells"])

        self.assertEqual(notebook["nbformat"], 4)
        for topic in [
            "Nguồn dữ liệu",
            "Kiểm tra chất lượng dữ liệu",
            "Khám phá dữ liệu",
            "Tiền xử lý dữ liệu",
            "Chuẩn bị dữ liệu cho giai đoạn mô hình",
        ]:
            self.assertIn(topic, content)

        for operation in [
            "dropna(axis=\"columns\", how=\"all\")",
            "drop(columns=[\"id\", \"diagnosis\"])",
            "map({\"B\": 0, \"M\": 1})",
            "breast_cancer_clean.csv",
            "to_csv(clean_data_path, index=False)",
        ]:
            self.assertIn(operation, content)

        for forbidden_item in ["SVC(", "KNeighborsClassifier", "DecisionTreeClassifier", "GridSearchCV"]:
            self.assertNotIn(forbidden_item, content)


if __name__ == "__main__":
    unittest.main()
