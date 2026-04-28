from langchain.tools import tool
from datetime import datetime
import os

@tool
def save_report(content: str) -> str:
    """Saves the final compiled research report to a .txt file.
    Always call this as the last step with the complete report."""
    try:
        os.makedirs("reports", exist_ok=True)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"reports/report_{timestamp}.txt"
        with open(filename, "w", encoding="utf-8") as f:
            f.write("=" * 60 + "\n")
            f.write(f"RESEARCH REPORT\n")
            f.write(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write("=" * 60 + "\n\n")
            f.write(content)
        return f"✅ Report saved successfully as: {filename}"
    except Exception as e:
        return f"Save failed: {str(e)}"