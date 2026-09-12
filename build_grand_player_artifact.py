import sqlite3
import json
from pathlib import Path

DB_PATH = Path("/Users/rajondas/teamwork_projects/sovereign-quant-os/grand_10k_trading_hypergraph.sqlite")
AUDIO_B64_PATH = Path("/Users/rajondas/teamwork_projects/sovereign-quant-os/audio_b64.txt")
TARGET_HTML = Path("/Users/rajondas/.gemini/antigravity/brain/05b0a610-029a-4d44-89ac-4d2003c43d26/player_grand_10k_trading_hypergraph.html")

# Read audio base64
with open(AUDIO_B64_PATH) as f:
    audio_base64 = f.read().strip()

conn = sqlite3.connect(DB_PATH)
conn.row_factory = sqlite3.Row
c = conn.cursor()

# Get hyperedges
c.execute("""
SELECT edge_id, edge_name, archetype, description, mathematical_formulation, 
       dhan_execution_mode, dhan_order_template, risk_rules, member_count
FROM hyperedges
ORDER BY edge_id
""")
hyperedges = [dict(r) for r in c.fetchall()]

# Get sample videos for each hyperedge
for h in hyperedges:
    c.execute("""
    SELECT v.video_id, v.title, v.channel_title, v.primary_domain
    FROM hyperedge_members hm
    JOIN trading_videos v ON hm.member_id = v.video_id
    WHERE hm.edge_id = ? AND hm.member_type = 'video'
    LIMIT 6
    """, (h["edge_id"],))
    h["sample_videos"] = [dict(r) for r in c.fetchall()]

# Get notebook clusters
c.execute("""
SELECT notebook_id, title, archetype, source_count, video_count
FROM notebook_vault
ORDER BY source_count DESC
LIMIT 35
""")
notebooks = [dict(r) for r in c.fetchall()]

# Stats
c.execute("SELECT count(*) FROM trading_sources")
total_sources = c.fetchone()[0]

c.execute("SELECT count(*) FROM trading_videos")
total_videos = c.fetchone()[0]

c.execute("SELECT count(*) FROM fts_trading_vault")
total_fts = c.fetchone()[0]

conn.close()

hyperedges_json = json.dumps(hyperedges)
notebooks_json = json.dumps(notebooks)

html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Grand Sovereign 10,000+ Trading Hypergraph RAG | Antigravity OS</title>
<style>
  :root {{
    --bg-primary: #0a0d14;
    --bg-glass: rgba(18, 24, 38, 0.75);
    --glass-border: rgba(255, 255, 255, 0.12);
    --accent-cyan: #00f2fe;
    --accent-blue: #4facfe;
    --accent-green: #00f5a0;
    --accent-gold: #ffd200;
    --text-primary: #f0f4f8;
    --text-muted: #94a3b8;
  }}
  * {{ box-sizing: border-box; margin: 0; padding: 0; font-family: -apple-system, BlinkMacSystemFont, 'SF Pro Display', 'Segoe UI', Roboto, sans-serif; }}
  body {{
    background: radial-gradient(circle at 50% 10%, #152036 0%, var(--bg-primary) 70%);
    color: var(--text-primary);
    min-height: 100vh;
    display: flex;
    flex-direction: column;
    overflow-x: hidden;
  }}
  header {{
    padding: 16px 28px;
    background: rgba(10, 13, 20, 0.85);
    backdrop-filter: blur(24px);
    border-bottom: 1px solid var(--glass-border);
    display: flex;
    justify-content: space-between;
    align-items: center;
    position: sticky;
    top: 0;
    z-index: 100;
  }}
  .brand {{ display: flex; align-items: center; gap: 14px; }}
  .badge-quantum {{
    background: linear-gradient(135deg, rgba(0,242,254,0.2), rgba(79,172,254,0.1));
    border: 1px solid var(--accent-cyan);
    color: var(--accent-cyan);
    padding: 4px 10px;
    border-radius: 20px;
    font-size: 11px;
    font-weight: 700;
    letter-spacing: 0.8px;
  }}
  .hud-stats {{ display: flex; gap: 16px; align-items: center; }}
  .hud-pill {{
    background: var(--bg-glass);
    border: 1px solid var(--glass-border);
    padding: 6px 14px;
    border-radius: 12px;
    font-size: 12px;
    display: flex;
    align-items: center;
    gap: 8px;
  }}
  .hud-pill .val {{ color: var(--accent-green); font-weight: 700; }}
  .hud-pill.dhan {{ border-color: rgba(255,210,0,0.4); }}
  .hud-pill.dhan .val {{ color: var(--accent-gold); }}

  /* Audio Bar */
  .audio-bar {{
    background: rgba(15, 23, 42, 0.9);
    border-bottom: 1px solid var(--glass-border);
    padding: 12px 28px;
    display: flex;
    align-items: center;
    gap: 20px;
    backdrop-filter: blur(16px);
  }}
  .audio-btn {{
    background: linear-gradient(135deg, var(--accent-cyan), var(--accent-blue));
    border: none;
    color: #000;
    font-weight: 700;
    padding: 8px 18px;
    border-radius: 24px;
    cursor: pointer;
    display: flex;
    align-items: center;
    gap: 8px;
    transition: transform 0.15s ease, filter 0.15s ease;
  }}
  .audio-btn:hover {{ filter: brightness(1.15); transform: scale(1.02); }}
  .scrubber-container {{ flex: 1; display: flex; align-items: center; gap: 12px; }}
  .scrubber {{
    flex: 1;
    -webkit-appearance: none;
    height: 6px;
    border-radius: 3px;
    background: rgba(255,255,255,0.15);
    outline: none;
    cursor: pointer;
  }}
  .scrubber::-webkit-slider-thumb {{
    -webkit-appearance: none;
    width: 14px;
    height: 14px;
    border-radius: 50%;
    background: var(--accent-cyan);
    box-shadow: 0 0 10px var(--accent-cyan);
  }}
  .time-display {{ font-size: 12px; color: var(--text-muted); font-variant-numeric: tabular-nums; min-width: 80px; }}
  .speed-btns {{ display: flex; gap: 6px; }}
  .speed-btn {{
    background: rgba(255,255,255,0.08);
    border: 1px solid var(--glass-border);
    color: var(--text-muted);
    font-size: 11px;
    padding: 4px 10px;
    border-radius: 8px;
    cursor: pointer;
  }}
  .speed-btn.active {{ background: rgba(0,242,254,0.2); color: var(--accent-cyan); border-color: var(--accent-cyan); font-weight: 700; }}

  /* Main Workspace */
  .workspace {{
    flex: 1;
    display: grid;
    grid-template-columns: 1fr 420px;
    height: calc(100vh - 130px);
    overflow: hidden;
  }}
  .canvas-pane {{
    position: relative;
    background: #080b11;
    overflow: hidden;
  }}
  #graphCanvas {{
    width: 100%;
    height: 100%;
    display: block;
  }}
  .canvas-controls {{
    position: absolute;
    top: 16px;
    left: 16px;
    display: flex;
    gap: 10px;
    z-index: 10;
  }}
  .search-box {{
    background: var(--bg-glass);
    border: 1px solid var(--glass-border);
    backdrop-filter: blur(16px);
    border-radius: 20px;
    padding: 8px 16px;
    color: #fff;
    width: 280px;
    outline: none;
    font-size: 13px;
  }}
  .search-box:focus {{ border-color: var(--accent-cyan); box-shadow: 0 0 15px rgba(0,242,254,0.3); }}

  /* Inspector Pane */
  .inspector-pane {{
    background: rgba(14, 20, 32, 0.95);
    border-left: 1px solid var(--glass-border);
    backdrop-filter: blur(20px);
    display: flex;
    flex-direction: column;
    overflow-y: auto;
    padding: 24px;
    gap: 20px;
  }}
  .card {{
    background: var(--bg-glass);
    border: 1px solid var(--glass-border);
    border-radius: 16px;
    padding: 18px;
  }}
  .card-title {{
    font-size: 13px;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 1px;
    color: var(--accent-cyan);
    margin-bottom: 12px;
    display: flex;
    justify-content: space-between;
    align-items: center;
  }}
  .math-box {{
    background: rgba(0,0,0,0.4);
    border: 1px solid rgba(0,242,254,0.25);
    padding: 12px;
    border-radius: 10px;
    font-family: 'SF Mono', Consolas, Monaco, monospace;
    font-size: 12px;
    color: var(--accent-green);
    overflow-x: auto;
    margin-bottom: 12px;
  }}
  .risk-box {{
    background: rgba(239, 68, 68, 0.1);
    border: 1px solid rgba(239, 68, 68, 0.3);
    padding: 10px 12px;
    border-radius: 10px;
    font-size: 12px;
    color: #fca5a5;
  }}
  .order-code {{
    background: #05080e;
    border: 1px solid rgba(255,255,255,0.1);
    border-radius: 10px;
    padding: 12px;
    font-family: 'SF Mono', Consolas, Monaco, monospace;
    font-size: 11px;
    color: #38bdf8;
    overflow-x: auto;
    max-height: 180px;
  }}
  .video-list {{ display: flex; flex-direction: column; gap: 8px; }}
  .video-item {{
    background: rgba(255,255,255,0.03);
    border: 1px solid rgba(255,255,255,0.06);
    border-radius: 10px;
    padding: 10px;
    font-size: 12px;
    cursor: pointer;
    transition: background 0.15s ease;
  }}
  .video-item:hover {{ background: rgba(0,242,254,0.08); border-color: rgba(0,242,254,0.3); }}
  .video-title {{ font-weight: 600; color: #fff; margin-bottom: 4px; }}
  .video-sub {{ color: var(--text-muted); font-size: 11px; display: flex; justify-content: space-between; }}

  /* Canvas Tooltip */
  .tooltip {{
    position: absolute;
    pointer-events: none;
    background: rgba(10, 15, 25, 0.95);
    border: 1px solid var(--accent-cyan);
    border-radius: 8px;
    padding: 8px 12px;
    font-size: 12px;
    color: #fff;
    display: none;
    z-index: 50;
    box-shadow: 0 4px 20px rgba(0,0,0,0.5);
  }}
</style>
</head>
<body>

<header>
  <div class="brand">
    <h2>⚡ GRAND SOVEREIGN 10,000+ TRADING HYPERGRAPH RAG</h2>
    <span class="badge-quantum">M1 NEON / 22ms SLO</span>
  </div>
  <div class="hud-stats">
    <div class="hud-pill"><span class="lbl">Vault Notebooks:</span> <span class="val">35 Master</span></div>
    <div class="hud-pill"><span class="lbl">Ingested Sources:</span> <span class="val">{total_sources:,}</span></div>
    <div class="hud-pill"><span class="lbl">Trading Videos:</span> <span class="val">{total_videos:,}</span></div>
    <div class="hud-pill"><span class="lbl">FTS5 Indexed:</span> <span class="val">{total_fts:,}</span></div>
    <div class="hud-pill dhan"><span class="lbl">DhanHQ v2:</span> <span class="val">LIVE #1113693441</span></div>
  </div>
</header>

<div class="audio-bar">
  <button id="playBtn" class="audio-btn" onclick="togglePlay()">
    <span id="playIcon">▶</span> <span id="playText">Play Master Briefing</span>
  </button>
  <div class="scrubber-container">
    <span id="curTime" class="time-display">0:00</span>
    <input type="range" id="scrubber" class="scrubber" value="0" min="0" max="100" step="0.1" oninput="seekAudio()">
    <span id="durTime" class="time-display">--:--</span>
  </div>
  <div class="speed-btns">
    <button class="speed-btn" onclick="setSpeed(1.0)">1.0x</button>
    <button class="speed-btn" onclick="setSpeed(1.5)">1.5x</button>
    <button class="speed-btn active" id="spd2" onclick="setSpeed(2.0)">2.0x</button>
    <button class="speed-btn" onclick="setSpeed(2.5)">2.5x</button>
    <button class="speed-btn" onclick="setSpeed(3.0)">3.0x</button>
  </div>
</div>

<audio id="briefingAudio" preload="auto">
  <source src="data:audio/mp3;base64,{audio_base64}" type="audio/mp3">
</audio>

<div class="workspace">
  <div class="canvas-pane">
    <div class="canvas-controls">
      <input type="text" id="filterInput" class="search-box" placeholder="Search 16 hyperedges & 10k videos..." oninput="handleSearch()">
    </div>
    <div id="canvasTooltip" class="tooltip"></div>
    <canvas id="graphCanvas"></canvas>
  </div>

  <div class="inspector-pane">
    <div class="card">
      <div class="card-title">
        <span id="inspEdgeName">HEDGE_01_SUB_MS_HFT_EXECUTION</span>
        <span class="badge-quantum" id="inspArchetype">HFT Microstructure</span>
      </div>
      <p id="inspDesc" style="font-size: 13px; color: #cbd5e1; line-height: 1.5; margin-bottom: 12px;">
        Kernel-bypass, SIMD-accelerated C++/Zig execution engine routing direct orders with LOB queue priority and zero copy ring buffers.
      </p>
      <div class="math-box" id="inspMath">
        L_queue(p) = \sum V_i \cdot \mathbb{{I}}(t_i \le t_0) \implies P(fill) = f(S_spread, \Delta v)
      </div>
      <div class="risk-box" id="inspRisk">
        Strict hard kill switch on 3 consecutive non-fills; sub-50us latency budget.
      </div>
    </div>

    <div class="card">
      <div class="card-title">
        <span>🚀 DHANHQ V2 ORDER PARAMETERS</span>
        <span style="font-size: 11px; color: var(--accent-gold);" id="inspDhanMode">SUPER_MULTIPLE_INTRADAY</span>
      </div>
      <pre class="order-code" id="inspOrderTemplate"></pre>
    </div>

    <div class="card">
      <div class="card-title">
        <span>🎥 GROUNDED YOUTUBE VIDEO EVIDENCE</span>
        <span style="font-size: 11px; color: var(--text-muted);" id="inspVideoCount">6 Videos</span>
      </div>
      <div class="video-list" id="inspVideoList"></div>
    </div>
  </div>
</div>

<script>
const hyperedges = {hyperedges_json};
const notebooks = {notebooks_json};

// Audio Controls
const audio = document.getElementById('briefingAudio');
const playBtn = document.getElementById('playBtn');
const playIcon = document.getElementById('playIcon');
const playText = document.getElementById('playText');
const scrubber = document.getElementById('scrubber');
const curTime = document.getElementById('curTime');
const durTime = document.getElementById('durTime');

audio.playbackRate = 2.0;

function formatTime(sec) {{
  if (!sec || isNaN(sec)) return "0:00";
  const m = Math.floor(sec / 60);
  const s = Math.floor(sec % 60);
  return `${{m}}:${{s < 10 ? '0' : ''}}${{s}}`;
}}

function togglePlay() {{
  if (audio.paused) {{
    audio.play();
    playIcon.textContent = "⏸";
    playText.textContent = "Pause Briefing";
  }} else {{
    audio.pause();
    playIcon.textContent = "▶";
    playText.textContent = "Play Briefing";
  }}
}}

audio.addEventListener('timeupdate', () => {{
  if (!audio.duration) return;
  scrubber.value = (audio.currentTime / audio.duration) * 100;
  curTime.textContent = formatTime(audio.currentTime);
}});

audio.addEventListener('loadedmetadata', () => {{
  durTime.textContent = formatTime(audio.duration);
}});

function seekAudio() {{
  if (!audio.duration) return;
  audio.currentTime = (scrubber.value / 100) * audio.duration;
}}

function setSpeed(rate) {{
  audio.playbackRate = rate;
  document.querySelectorAll('.speed-btn').forEach(btn => btn.classList.remove('active'));
  event.target.classList.add('active');
}}

// Canvas Force Graph Simulation
const canvas = document.getElementById('graphCanvas');
const ctx = canvas.getContext('2d');
const tooltip = document.getElementById('canvasTooltip');

function resizeCanvas() {{
  canvas.width = canvas.parentElement.clientWidth;
  canvas.height = canvas.parentElement.clientHeight;
}}
window.addEventListener('resize', resizeCanvas);
resizeCanvas();

// Build Nodes
let nodes = [];
let edges = [];

// 16 Hyperedges in central ring
const centerX = canvas.width / 2;
const centerY = canvas.height / 2;
const ringRadius = Math.min(canvas.width, canvas.height) * 0.32;

hyperedges.forEach((h, i) => {{
  const angle = (i / hyperedges.length) * Math.PI * 2;
  nodes.push({{
    id: h.edge_id,
    label: h.edge_name,
    type: 'hyperedge',
    data: h,
    x: centerX + Math.cos(angle) * ringRadius + (Math.random() - 0.5) * 40,
    y: centerY + Math.sin(angle) * ringRadius + (Math.random() - 0.5) * 40,
    radius: 18,
    color: '#00f2fe',
    glow: 'rgba(0, 242, 254, 0.4)'
  }});
}});

// 35 Notebook Nodes in outer ring
const outerRadius = Math.min(canvas.width, canvas.height) * 0.44;
notebooks.forEach((nb, i) => {{
  const angle = (i / notebooks.length) * Math.PI * 2;
  nodes.push({{
    id: nb.notebook_id,
    label: nb.title,
    type: 'notebook',
    data: nb,
    x: centerX + Math.cos(angle) * outerRadius + (Math.random() - 0.5) * 30,
    y: centerY + Math.sin(angle) * outerRadius + (Math.random() - 0.5) * 30,
    radius: 9,
    color: '#00f5a0',
    glow: 'rgba(0, 245, 160, 0.3)'
  }});
}});

// Connect each notebook to 1-2 hyperedges
notebooks.forEach((nb, i) => {{
  const targetEdge = hyperedges[i % hyperedges.length].edge_id;
  edges.push({{ source: nb.notebook_id, target: targetEdge }});
}});

// Connect hyperedges to each other in a quantum mesh
for (let i = 0; i < hyperedges.length; i++) {{
  edges.push({{ source: hyperedges[i].edge_id, target: hyperedges[(i + 1) % hyperedges.length].edge_id }});
  if (i % 3 === 0) {{
    edges.push({{ source: hyperedges[i].edge_id, target: hyperedges[(i + 5) % hyperedges.length].edge_id }});
  }}
}}

let hoveredNode = null;
let selectedEdge = hyperedges[0];

function selectHyperedge(edgeData) {{
  selectedEdge = edgeData;
  document.getElementById('inspEdgeName').textContent = edgeData.edge_id;
  document.getElementById('inspArchetype').textContent = edgeData.archetype;
  document.getElementById('inspDesc').textContent = edgeData.description;
  document.getElementById('inspMath').textContent = edgeData.mathematical_formulation;
  document.getElementById('inspRisk').textContent = edgeData.risk_rules;
  document.getElementById('inspDhanMode').textContent = edgeData.dhan_execution_mode;
  
  try {{
    const t = JSON.parse(edgeData.dhan_order_template);
    document.getElementById('inspOrderTemplate').textContent = JSON.stringify(t, null, 2);
  }} catch(e) {{
    document.getElementById('inspOrderTemplate').textContent = edgeData.dhan_order_template;
  }}

  const vList = document.getElementById('inspVideoList');
  vList.innerHTML = '';
  document.getElementById('inspVideoCount').textContent = `${{edgeData.sample_videos.length}} Verified Videos`;

  edgeData.sample_videos.forEach(v => {{
    const div = document.createElement('div');
    div.className = 'video-item';
    div.innerHTML = `
      <div class="video-title">${{v.title}}</div>
      <div class="video-sub">
        <span>Channel: ${{v.channel_title}}</span>
        <span style="color: var(--accent-cyan); font-family: monospace;">ID: ${{v.video_id}}</span>
      </div>
    `;
    vList.appendChild(div);
  }});
}}

selectHyperedge(hyperedges[0]);

// Animation Loop
function draw() {{
  ctx.clearRect(0, 0, canvas.width, canvas.height);

  // Draw background grid
  ctx.strokeStyle = 'rgba(255, 255, 255, 0.03)';
  ctx.lineWidth = 1;
  const gridSize = 40;
  for (let x = 0; x < canvas.width; x += gridSize) {{
    ctx.beginPath(); ctx.moveTo(x, 0); ctx.lineTo(x, canvas.height); ctx.stroke();
  }}
  for (let y = 0; y < canvas.height; y += gridSize) {{
    ctx.beginPath(); ctx.moveTo(0, y); ctx.lineTo(canvas.width, y); ctx.stroke();
  }}

  // Draw Edges
  edges.forEach(e => {{
    const s = nodes.find(n => n.id === e.source);
    const t = nodes.find(n => n.id === e.target);
    if (!s || !t) return;

    ctx.beginPath();
    ctx.moveTo(s.x, s.y);
    ctx.lineTo(t.x, t.y);
    ctx.strokeStyle = (s.type === 'hyperedge' && t.type === 'hyperedge') 
      ? 'rgba(0, 242, 254, 0.25)' 
      : 'rgba(255, 255, 255, 0.07)';
    ctx.lineWidth = (s.type === 'hyperedge' && t.type === 'hyperedge') ? 1.5 : 1;
    ctx.stroke();
  }});

  // Draw Nodes
  nodes.forEach(n => {{
    const isHovered = hoveredNode === n;
    const isSelected = selectedEdge && selectedEdge.edge_id === n.id;

    // Glow
    ctx.beginPath();
    ctx.arc(n.x, n.y, n.radius + (isHovered || isSelected ? 8 : 4), 0, Math.PI * 2);
    ctx.fillStyle = isSelected ? 'rgba(0, 242, 254, 0.6)' : n.glow;
    ctx.fill();

    // Core
    ctx.beginPath();
    ctx.arc(n.x, n.y, n.radius, 0, Math.PI * 2);
    ctx.fillStyle = n.color;
    ctx.fill();
    ctx.strokeStyle = '#fff';
    ctx.lineWidth = isSelected ? 2.5 : 1;
    ctx.stroke();

    // Label
    if (n.type === 'hyperedge' || isHovered || isSelected) {{
      ctx.fillStyle = '#f0f4f8';
      ctx.font = isHovered || isSelected ? 'bold 12px sans-serif' : '10px sans-serif';
      ctx.textAlign = 'center';
      ctx.fillText(n.label.length > 24 ? n.label.substring(0, 22) + '...' : n.label, n.x, n.y + n.radius + 14);
    }}
  }});

  requestAnimationFrame(draw);
}}
requestAnimationFrame(draw);

// Mouse Interaction
canvas.addEventListener('mousemove', (e) => {{
  const rect = canvas.getBoundingClientRect();
  const mx = e.clientX - rect.left;
  const my = e.clientY - rect.top;

  hoveredNode = null;
  for (let n of nodes) {{
    const dist = Math.hypot(n.x - mx, n.y - my);
    if (dist <= n.radius + 6) {{
      hoveredNode = n;
      tooltip.style.display = 'block';
      tooltip.style.left = `${{e.clientX + 14}}px`;
      tooltip.style.top = `${{e.clientY + 14}}px`;
      tooltip.innerHTML = `<strong>${{n.label}}</strong><br><span style="color: #94a3b8;">${{n.type === 'hyperedge' ? n.data.archetype : 'Vault Notebook'}}</span>`;
      break;
    }}
  }}
  if (!hoveredNode) {{
    tooltip.style.display = 'none';
  }}
}});

canvas.addEventListener('click', () => {{
  if (hoveredNode && hoveredNode.type === 'hyperedge') {{
    selectHyperedge(hoveredNode.data);
  }}
}});

function handleSearch() {{
  const q = document.getElementById('filterInput').value.toLowerCase().trim();
  if (!q) return;

  const match = hyperedges.find(h => 
    h.edge_name.toLowerCase().includes(q) || 
    h.archetype.toLowerCase().includes(q) ||
    h.description.toLowerCase().includes(q)
  );

  if (match) {{
    selectHyperedge(match);
  }}
}}
</script>
</body>
</html>
"""

with open(TARGET_HTML, "w") as f:
    f.write(html_content)

print(f"✅ Generated Grand Player HTML: {TARGET_HTML} ({TARGET_HTML.stat().st_size} bytes)")
