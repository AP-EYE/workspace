from datetime import date
from pathlib import Path

from markitdown import MarkItDown

root = Path(__file__).resolve().parents[2] / "team_hub" / "docs" / "papers"
names = [
    "AuthScope_CCS17",
    "BACFuzz_2507.15984",
    "BolaZ_2507.02309",
    "ICST2020_REST-API-security-rules",
    "IDORacle_2609.12426",
    "TrafficAuthzRisk_2607.16754",
]
converter = MarkItDown()
for name in names:
    pdf = root / f"{name}.pdf"
    markdown = root / f"{name}.md"
    if markdown.exists():
        print(f"skip {markdown.name}")
        continue
    body = converter.convert(str(pdf)).text_content
    header = (
        f"> 원본: {pdf.name}; 변환: markitdown; {date.today().isoformat()}\n\n"
        "<!-- 2단 편집의 절·표·수식 순서가 깨질 수 있으므로 수치와 페이지는 원본 PDF로 확인한다. -->\n\n"
    )
    markdown.write_text(header + body, encoding="utf-8")
    print(f"wrote {markdown.name}: {markdown.stat().st_size} bytes")
