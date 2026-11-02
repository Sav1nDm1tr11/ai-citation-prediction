"""Add PNG fallbacks to Plotly notebook outputs for GitHub previews."""

import base64
import json
import re
from pathlib import Path

import plotly.graph_objects as go


root = Path(__file__).resolve().parents[1]
notebook_path = root / "notebooks" / "model_training.ipynb"
plot_dir = root / "notebooks" / "plots"
notebook = json.loads(notebook_path.read_text(encoding="utf-8"))

final_cell = next(
    cell
    for cell in notebook["cells"]
    if "def save_figure" in "".join(cell.get("source", []))
)
filenames = re.findall(
    r'save_figure\(fig, "([^\"]+)\.html"',
    "".join(final_cell["source"]),
)
final_outputs = [
    output
    for output in final_cell["outputs"]
    if "application/vnd.plotly.v1+json" in output.get("data", {})
]
if len(filenames) != len(final_outputs):
    raise RuntimeError("Сначала выполните ноутбук: число графиков не совпадает с кодом")

plot_dir.mkdir(exist_ok=True)
exported = 0
final_names = iter(filenames)

for cell in notebook["cells"]:
    for output in cell.get("outputs", []):
        data = output.get("data", {})
        payload = data.get("application/vnd.plotly.v1+json")
        if payload is None:
            continue

        png = go.Figure(payload).to_image(format="png", scale=1.5)
        data["image/png"] = base64.b64encode(png).decode("ascii")

        if cell is final_cell:
            name = next(final_names)
            (plot_dir / f"{name}.png").write_bytes(png)

        exported += 1

notebook_path.write_text(
    json.dumps(notebook, ensure_ascii=False, indent=1) + "\n",
    encoding="utf-8",
)
print(f"PNG-превью добавлены для {exported} графиков; {len(filenames)} файлов сохранены в {plot_dir}")
