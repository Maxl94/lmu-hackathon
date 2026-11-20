from html import escape
from typing import Any

from app.models import RecordDetailOut, RecordSummaryOut, TrackOut

_BASE_CSS = """
:root {
  --bg: #f8fafc;
  --card: #ffffff;
  --border: #e2e8f0;
  --text: #0f172a;
  --muted: #64748b;
  --accent: #2563eb;
  --ok-bg: #dcfce7;
  --ok-fg: #166534;
  --warn-bg: #fef3c7;
  --warn-fg: #92400e;
  --err-bg: #fee2e2;
  --err-fg: #991b1b;
  --neutral-bg: #f1f5f9;
  --neutral-fg: #334155;
}
* { box-sizing: border-box; }
body {
  margin: 0;
  padding: 24px;
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
  background: var(--bg);
  color: var(--text);
  line-height: 1.45;
}
.container { max-width: 1280px; margin: 0 auto; }
header {
  display: flex;
  flex-wrap: wrap;
  justify-content: space-between;
  align-items: center;
  gap: 12px;
  margin-bottom: 20px;
}
h1 { font-size: 1.35rem; margin: 0; }
h2 { font-size: 1.05rem; margin: 24px 0 10px; }
.nav { display: flex; gap: 12px; font-size: 0.9rem; }
a { color: var(--accent); text-decoration: none; }
a:hover { text-decoration: underline; }
.stats {
  display: flex;
  flex-wrap: wrap;
  gap: 12px;
  margin-bottom: 16px;
}
.stat {
  background: var(--card);
  border: 1px solid var(--border);
  border-radius: 8px;
  padding: 10px 14px;
  min-width: 130px;
}
.stat-label { font-size: 0.75rem; color: var(--muted); text-transform: uppercase; letter-spacing: 0.04em; }
.stat-val { font-size: 1.25rem; font-weight: 600; margin-top: 2px; }
.toolbar {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
  align-items: center;
  margin-bottom: 12px;
}
input[type="search"], select {
  padding: 7px 10px;
  border: 1px solid var(--border);
  border-radius: 6px;
  background: var(--card);
  font-size: 0.9rem;
}
input[type="search"] { min-width: 260px; flex: 1; max-width: 420px; }
.btn {
  padding: 7px 12px;
  border: 1px solid var(--border);
  border-radius: 6px;
  background: var(--card);
  color: var(--text);
  font-size: 0.85rem;
  cursor: pointer;
}
.btn:hover { background: #f1f5f9; }
.card {
  background: var(--card);
  border: 1px solid var(--border);
  border-radius: 8px;
  overflow-x: auto;
}
table { width: 100%; border-collapse: collapse; font-size: 0.88rem; }
th, td {
  text-align: left;
  padding: 10px 12px;
  border-bottom: 1px solid var(--border);
  vertical-align: top;
}
th {
  background: #f8fafc;
  color: var(--muted);
  font-weight: 600;
  font-size: 0.78rem;
  text-transform: uppercase;
  letter-spacing: 0.03em;
  white-space: nowrap;
}
tr:last-child td { border-bottom: none; }
tbody tr:hover { background: #f8fafc; }
.mono { font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace; font-size: 0.83rem; }
.badge {
  display: inline-block;
  padding: 2px 8px;
  border-radius: 999px;
  font-size: 0.76rem;
  font-weight: 600;
  white-space: nowrap;
}
.badge-matched { background: var(--ok-bg); color: var(--ok-fg); }
.badge-needs_review { background: var(--warn-bg); color: var(--warn-fg); }
.badge-not_found { background: var(--err-bg); color: var(--err-fg); }
.badge-other { background: var(--neutral-bg); color: var(--neutral-fg); }
.empty { padding: 36px 20px; text-align: center; color: var(--muted); }
.meta-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
  gap: 12px;
  padding: 14px;
}
.meta-item .label { font-size: 0.75rem; color: var(--muted); text-transform: uppercase; }
.meta-item .val { font-size: 0.92rem; margin-top: 2px; word-break: break-word; }
"""


def _status_badge(status: str | None) -> str:
    s = status or "unknown"
    cls = s if s in {"matched", "needs_review", "not_found"} else "other"
    return f'<span class="badge badge-{cls}">{escape(s)}</span>'


def _format_duration(track: TrackOut) -> str:
    if track.duration_raw:
        return escape(track.duration_raw)
    if track.duration_sec is not None:
        mins, secs = divmod(track.duration_sec, 60)
        return f"{mins}:{secs:02d}"
    return "—"


def _format_credits(credits: list[dict[str, Any]]) -> str:
    if not credits:
        return "—"
    parts = []
    for c in credits:
        name = escape(str(c.get("artist_name") or ""))
        role = escape(str(c.get("role_raw") or ""))
        parts.append(f"{name} ({role})" if role else name)
    return ", ".join(parts)


def render_results_table(records: list[RecordSummaryOut]) -> str:
    total = len(records)
    matched = sum(1 for r in records if r.latest_status == "matched")
    needs_review = sum(1 for r in records if r.latest_status == "needs_review")
    not_found = sum(1 for r in records if r.latest_status == "not_found")

    rows_html = []
    for r in records:
        status_str = r.latest_status or "unknown"
        release_cell = (
            f'<a href="{escape(r.selected_release_url)}" target="_blank" rel="noopener">#{r.selected_release_id}</a>'
            if r.selected_release_id and r.selected_release_url
            else (f"#{r.selected_release_id}" if r.selected_release_id else "—")
        )
        checked_at = escape((r.latest_checked_at or "—")[:19].replace("T", " "))
        rows_html.append(
            f'<tr data-status="{escape(status_str)}">'
            f'<td class="mono">{r.input_id}</td>'
            f'<td class="mono">{escape(r.barcode_raw or "—")}</td>'
            f"<td>{escape(r.album_title_raw or '—')}</td>"
            f"<td>{escape(r.album_artist_raw or '—')}</td>"
            f"<td>{_status_badge(r.latest_status)}</td>"
            f'<td class="mono">{release_cell}</td>'
            f"<td>{escape(r.latest_source or '—')}</td>"
            f'<td class="mono">{checked_at}</td>'
            f'<td><a href="/results/{r.input_id}">Inspect</a></td>'
            f"</tr>"
        )

    table_body = (
        "\n".join(rows_html)
        if rows_html
        else '<tr><td colspan="9" class="empty">No records in database yet. Run a lookup or batch first.</td></tr>'
    )

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>Tracklist Discovery Results</title>
  <style>{_BASE_CSS}</style>
</head>
<body>
  <div class="container">
    <header>
      <h1>Tracklist Discovery Results</h1>
      <div class="nav">
        <a href="/records" target="_blank">JSON (/records)</a>
        <a href="/docs" target="_blank">API Docs (/docs)</a>
      </div>
    </header>

    <div class="stats">
      <div class="stat"><div class="stat-label">Total</div><div class="stat-val">{total}</div></div>
      <div class="stat"><div class="stat-label">Matched</div><div class="stat-val">{matched}</div></div>
      <div class="stat"><div class="stat-label">Needs Review</div><div class="stat-val">{needs_review}</div></div>
      <div class="stat"><div class="stat-label">Not Found</div><div class="stat-val">{not_found}</div></div>
    </div>

    <div class="toolbar">
      <input id="search" type="search" placeholder="Filter by barcode, title, artist..." oninput="filterRows()" />
      <select id="statusFilter" onchange="filterRows()">
        <option value="">All statuses</option>
        <option value="matched">matched</option>
        <option value="needs_review">needs_review</option>
        <option value="not_found">not_found</option>
      </select>
      <button class="btn" onclick="location.reload()">Refresh</button>
    </div>

    <div class="card">
      <table>
        <thead>
          <tr>
            <th>ID</th>
            <th>Barcode</th>
            <th>Album Title</th>
            <th>Album Artist</th>
            <th>Status</th>
            <th>Discogs Release</th>
            <th>Source</th>
            <th>Checked At (UTC)</th>
            <th>Details</th>
          </tr>
        </thead>
        <tbody id="resultsBody">
          {table_body}
        </tbody>
      </table>
    </div>
  </div>
  <script>
    function filterRows() {{
      const q = document.getElementById("search").value.toLowerCase();
      const st = document.getElementById("statusFilter").value;
      const rows = document.querySelectorAll("#resultsBody tr[data-status]");
      for (const row of rows) {{
        const text = row.textContent.toLowerCase();
        const rowStatus = row.getAttribute("data-status");
        const show = (!q || text.includes(q)) && (!st || rowStatus === st);
        row.style.display = show ? "" : "none";
      }}
    }}
  </script>
</body>
</html>"""


def render_record_detail(detail: RecordDetailOut) -> str:
    rec = detail.record
    rel = detail.selected_release

    if rel is not None:
        formats_str = ", ".join(
            str(f.get("name", "")) for f in rel.formats if f.get("name")
        ) or "—"
        release_html = f"""
        <div class="card meta-grid">
          <div class="meta-item"><div class="label">Release</div><div class="val"><a href="{escape(rel.url)}" target="_blank" rel="noopener">#{rel.discogs_release_id} — {escape(rel.title)}</a></div></div>
          <div class="meta-item"><div class="label">Artist</div><div class="val">{escape(rel.artist_display or '—')}</div></div>
          <div class="meta-item"><div class="label">Year / Country</div><div class="val">{escape(str(rel.year or '—'))} / {escape(rel.country or '—')}</div></div>
          <div class="meta-item"><div class="label">Formats</div><div class="val">{escape(formats_str)}</div></div>
          <div class="meta-item"><div class="label">Data Quality</div><div class="val">{escape(rel.data_quality or '—')}</div></div>
        </div>"""
    else:
        release_html = '<div class="card empty">No release selected.</div>'

    track_rows = []
    for t in detail.tracks:
        writers = _format_credits(t.credits.get("writers", []))
        producers = _format_credits(t.credits.get("producers", []))
        track_rows.append(
            f"<tr>"
            f'<td class="mono">{t.disc_number}</td>'
            f'<td class="mono">{escape(t.position or str(t.track_order))}</td>'
            f"<td>{escape(t.title)}</td>"
            f"<td>{escape(t.performing_artist_display or '—')}</td>"
            f'<td class="mono">{_format_duration(t)}</td>'
            f"<td>{writers}</td>"
            f"<td>{producers}</td>"
            f"</tr>"
        )
    tracks_body = (
        "\n".join(track_rows)
        if track_rows
        else '<tr><td colspan="7" class="empty">No tracks extracted.</td></tr>'
    )

    match_rows = []
    for m in detail.matches:
        sel_mark = "✓" if m.get("is_selected") else ""
        match_rows.append(
            f"<tr>"
            f'<td class="mono">{escape(str(m.get("match_rank", "")))}</td>'
            f"<td>{sel_mark}</td>"
            f'<td class="mono"><a href="{escape(str(m.get("url", "")))}" target="_blank" rel="noopener">#{escape(str(m.get("discogs_release_id", "")))}</a></td>'
            f"<td>{escape(str(m.get('title', '')))}</td>"
            f"<td>{escape(str(m.get('artist_display', '')))}</td>"
            f'<td class="mono">{escape(str(m.get("match_method", "")))}</td>'
            f'<td class="mono">{escape(str(m.get("score", "")))}</td>'
            f"</tr>"
        )
    matches_body = (
        "\n".join(match_rows)
        if match_rows
        else '<tr><td colspan="7" class="empty">No candidate matches recorded.</td></tr>'
    )

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>Record #{rec.input_id} — {escape(rec.album_title_raw or rec.barcode_raw or 'Details')}</title>
  <style>{_BASE_CSS}</style>
</head>
<body>
  <div class="container">
    <header>
      <h1>Record #{rec.input_id} {_status_badge(rec.latest_status)}</h1>
      <div class="nav">
        <a href="/results">← All Results</a>
        <a href="/records/{rec.input_id}" target="_blank">JSON</a>
        <a href="/docs" target="_blank">API Docs</a>
      </div>
    </header>

    <div class="card meta-grid">
      <div class="meta-item"><div class="label">Barcode (raw / norm)</div><div class="val mono">{escape(rec.barcode_raw or '—')} / {escape(rec.barcode_norm or '—')}</div></div>
      <div class="meta-item"><div class="label">Album Title</div><div class="val">{escape(rec.album_title_raw or '—')}</div></div>
      <div class="meta-item"><div class="label">Album Artist</div><div class="val">{escape(rec.album_artist_raw or '—')}</div></div>
      <div class="meta-item"><div class="label">Source / Checked At</div><div class="val">{escape(rec.latest_source or '—')} / <span class="mono">{escape((rec.latest_checked_at or '—')[:19].replace('T', ' '))}</span></div></div>
    </div>

    <h2>Selected Release</h2>
    {release_html}

    <h2>Tracklist ({len(detail.tracks)})</h2>
    <div class="card">
      <table>
        <thead>
          <tr>
            <th>Disc</th>
            <th>Pos</th>
            <th>Title</th>
            <th>Performing Artists</th>
            <th>Duration</th>
            <th>Writers</th>
            <th>Producers</th>
          </tr>
        </thead>
        <tbody>{tracks_body}</tbody>
      </table>
    </div>

    <h2>Candidate Matches ({len(detail.matches)})</h2>
    <div class="card">
      <table>
        <thead>
          <tr>
            <th>Rank</th>
            <th>Selected</th>
            <th>Release</th>
            <th>Title</th>
            <th>Artist</th>
            <th>Method</th>
            <th>Score</th>
          </tr>
        </thead>
        <tbody>{matches_body}</tbody>
      </table>
    </div>
  </div>
</body>
</html>"""
