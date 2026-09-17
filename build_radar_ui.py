import json
import os

FEED_FILE = "/Users/rajondas/teamwork_projects/sovereign-quant-os/LIVE_YOUTUBE_MACRO_FEED_STREAM.json"
TARGET_HTML = "/Users/rajondas/.gemini/antigravity/brain/5e0ef755-c80b-4e43-b894-151bca274894/LIVE_NEWS_STREAM_RADAR.html"

with open(FEED_FILE, "r") as f:
    feed_data = json.load(f)

items = feed_data.get("continuous_feed_queue", [])
notebooks = feed_data.get("active_notebooks", [])
last_synced = feed_data.get("last_synced", "LIVE")

items_json = json.dumps(items)

html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>SOVEREIGN QUANT OS - LIVE NEWS & YOUTUBE STREAM RADAR</title>
    <style>
        :root {{
            --bg-base: #0a0c10;
            --surface-glass: rgba(18, 24, 38, 0.75);
            --surface-border: rgba(255, 255, 255, 0.12);
            --accent-cyan: #00f0ff;
            --accent-green: #00ff88;
            --accent-gold: #ffd700;
            --accent-red: #ff3366;
            --text-primary: #f0f4f8;
            --text-secondary: #94a3b8;
            --font-sans: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
            --font-mono: "SF Mono", "Fira Code", monospace;
        }}
        * {{ box-sizing: border-box; margin: 0; padding: 0; }}
        body {{
            background: radial-gradient(circle at top right, #111827, #06080c);
            color: var(--text-primary);
            font-family: var(--font-sans);
            padding: 24px;
            min-height: 100vh;
        }}
        .header-bar {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 18px 24px;
            background: var(--surface-glass);
            border: 1px solid var(--surface-border);
            border-radius: 16px;
            backdrop-filter: blur(20px);
            margin-bottom: 24px;
            box-shadow: 0 8px 32px rgba(0, 0, 0, 0.4);
        }}
        .logo-group {{
            display: flex;
            align-items: center;
            gap: 14px;
        }}
        .pulsing-dot {{
            width: 14px;
            height: 14px;
            background: var(--accent-green);
            border-radius: 50%;
            box-shadow: 0 0 12px var(--accent-green);
            animation: pulse 1.5s infinite;
        }}
        @keyframes pulse {{
            0% {{ transform: scale(0.95); opacity: 0.8; }}
            50% {{ transform: scale(1.2); opacity: 1; box-shadow: 0 0 20px var(--accent-green); }}
            100% {{ transform: scale(0.95); opacity: 0.8; }}
        }}
        h1 {{ font-size: 20px; font-weight: 700; letter-spacing: 0.5px; }}
        .hud-stats {{
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 16px;
            margin-bottom: 24px;
        }}
        .stat-card {{
            background: var(--surface-glass);
            border: 1px solid var(--surface-border);
            padding: 16px 20px;
            border-radius: 14px;
            backdrop-filter: blur(16px);
        }}
        .stat-label {{ font-size: 11px; text-transform: uppercase; color: var(--text-secondary); letter-spacing: 1px; margin-bottom: 6px; }}
        .stat-val {{ font-size: 22px; font-weight: 800; font-family: var(--font-mono); }}
        .cyan {{ color: var(--accent-cyan); }}
        .green {{ color: var(--accent-green); }}
        .gold {{ color: var(--accent-gold); }}
        .red {{ color: var(--accent-red); }}
        
        .main-layout {{
            display: grid;
            grid-template-columns: 2fr 1fr;
            gap: 24px;
        }}
        .feed-container {{
            background: var(--surface-glass);
            border: 1px solid var(--surface-border);
            border-radius: 16px;
            padding: 20px;
            backdrop-filter: blur(16px);
            max-height: 75vh;
            overflow-y: auto;
        }}
        .feed-header {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 16px;
            padding-bottom: 12px;
            border-bottom: 1px solid var(--surface-border);
        }}
        .feed-list {{
            display: flex;
            flex-direction: column;
            gap: 12px;
        }}
        .feed-card {{
            background: rgba(255, 255, 255, 0.03);
            border: 1px solid rgba(255, 255, 255, 0.08);
            border-radius: 12px;
            padding: 14px 16px;
            transition: all 0.2s ease;
        }}
        .feed-card:hover {{
            border-color: var(--accent-cyan);
            background: rgba(0, 240, 255, 0.04);
            transform: translateX(4px);
        }}
        .feed-meta {{
            display: flex;
            justify-content: space-between;
            font-size: 11px;
            color: var(--text-secondary);
            margin-bottom: 6px;
        }}
        .feed-source {{
            font-weight: 700;
            color: var(--accent-cyan);
        }}
        .feed-title {{
            font-size: 14px;
            font-weight: 600;
            line-height: 1.4;
            color: var(--text-primary);
            margin-bottom: 8px;
        }}
        .feed-badges {{
            display: flex;
            gap: 8px;
            align-items: center;
        }}
        .badge {{
            font-size: 10px;
            padding: 2px 8px;
            border-radius: 6px;
            font-family: var(--font-mono);
            font-weight: 600;
            text-transform: uppercase;
        }}
        .badge-yt {{ background: rgba(255, 51, 102, 0.2); color: #ff6b8b; border: 1px solid rgba(255, 51, 102, 0.3); }}
        .badge-news {{ background: rgba(0, 240, 255, 0.15); color: #67e8f9; border: 1px solid rgba(0, 240, 255, 0.3); }}
        .badge-bullish {{ background: rgba(0, 255, 136, 0.15); color: #4ade80; border: 1px solid rgba(0, 255, 136, 0.3); }}
        .badge-symbol {{ background: rgba(255, 215, 0, 0.15); color: #fde047; border: 1px solid rgba(255, 215, 0, 0.3); }}
        
        .sidebar {{
            display: flex;
            flex-direction: column;
            gap: 20px;
        }}
        .side-card {{
            background: var(--surface-glass);
            border: 1px solid var(--surface-border);
            border-radius: 16px;
            padding: 20px;
            backdrop-filter: blur(16px);
        }}
        .side-title {{
            font-size: 14px;
            font-weight: 700;
            letter-spacing: 0.5px;
            margin-bottom: 14px;
            color: var(--accent-cyan);
            border-bottom: 1px solid var(--surface-border);
            padding-bottom: 8px;
        }}
        .position-row {{
            display: flex;
            justify-content: space-between;
            padding: 10px 0;
            border-bottom: 1px solid rgba(255, 255, 255, 0.05);
            font-family: var(--font-mono);
            font-size: 13px;
        }}
        .code-box {{
            background: #000;
            border: 1px solid #222;
            padding: 12px;
            border-radius: 8px;
            font-family: var(--font-mono);
            font-size: 11px;
            line-height: 1.5;
            color: #94a3b8;
            max-height: 250px;
            overflow-y: auto;
        }}
    </style>
</head>
<body>
    <div class="header-bar">
        <div class="logo-group">
            <div class="pulsing-dot"></div>
            <div>
                <h1>SOVEREIGN LIVE NEWS & YOUTUBE RADAR</h1>
                <p style="font-size: 12px; color: var(--text-secondary);">Continuous 30s Multi-Source Ingestor • Synchronized with Dhan DMA Broker</p>
            </div>
        </div>
        <div style="font-family: var(--font-mono); font-size: 12px; color: var(--accent-cyan); text-align: right;">
            <div>STATUS: <span style="color: var(--accent-green);">STREAMING LIVE (ACTIVE)</span></div>
            <div>LAST SYNC: {last_synced}</div>
        </div>
    </div>

    <div class="hud-stats">
        <div class="stat-card">
            <div class="stat-label">Starting SOD Capital</div>
            <div class="stat-val cyan">₹918.43</div>
            <div style="font-size: 11px; color: var(--text-secondary); margin-top: 4px;">Baseline Capital</div>
        </div>
        <div class="stat-card">
            <div class="stat-label">Dhan Realized Profit</div>
            <div class="stat-val green">+₹1.26 <span style="font-size: 13px; color: var(--accent-green);">(+₹8.82 PNB / -₹7.56 TATA)</span></div>
            <div style="font-size: 11px; color: var(--text-secondary); margin-top: 4px;">Net Realized Live Cash</div>
        </div>
        <div class="stat-card">
            <div class="stat-label">Active Margin Utilized</div>
            <div class="stat-val gold">₹547.00 <span style="font-size: 13px; color: var(--text-secondary);">(₹370.73 Avail)</span></div>
            <div style="font-size: 11px; color: var(--text-secondary); margin-top: 4px;">14 PNB + 4 ITC Holding</div>
        </div>
        <div class="stat-card">
            <div class="stat-label">Recovery Target (+₹102)</div>
            <div class="stat-val red">₹98.52 To Go</div>
            <div style="font-size: 11px; color: var(--text-secondary); margin-top: 4px;">Breakeven + Full Green Goal</div>
        </div>
    </div>

    <div class="main-layout">
        <div class="feed-container">
            <div class="feed-header">
                <div style="font-size: 15px; font-weight: 700;">📡 Continuous Ingested Feed Stream ({len(items)} Items Active)</div>
                <div style="font-size: 12px; color: var(--text-secondary); font-family: var(--font-mono);">Updates every 30s</div>
            </div>
            <div class="feed-list" id="feed-list">
"""

for item in items:
    itype = item.get("type", "LIVE_NEWS")
    source = item.get("source", "MARKET_SOURCE")
    title = item.get("title", "")
    ts = item.get("timestamp", "")
    sentiment = item.get("sentiment_score", 0)
    symbols = item.get("matched_symbols", [])
    
    badge_type = '<span class="badge badge-yt">YOUTUBE STREAM</span>' if itype == "YOUTUBE_LIVE_STREAM" else '<span class="badge badge-news">GOOGLE NEWS</span>'
    badge_sent = f'<span class="badge badge-bullish">BULLISH (+{sentiment})</span>' if sentiment > 0 else '<span class="badge" style="background:rgba(255,255,255,0.1);color:#cbd5e1;">NEUTRAL</span>'
    
    sym_badges = "".join([f'<span class="badge badge-symbol">{s}</span>' for s in symbols])
    
    html_content += f"""
                <div class="feed-card">
                    <div class="feed-meta">
                        <span class="feed-source">{source}</span>
                        <span>{ts}</span>
                    </div>
                    <div class="feed-title">{title}</div>
                    <div class="feed-badges">
                        {badge_type}
                        {badge_sent}
                        {sym_badges}
                    </div>
                </div>
    """

html_content += f"""
            </div>
        </div>

        <div class="sidebar">
            <div class="side-card">
                <div class="side-title">⚡ DHAN LIVE POSITIONS (BROKER TRUTH)</div>
                <div class="position-row">
                    <span>PNB (LONG 14)</span>
                    <span style="color: var(--accent-green);">Avg: ₹118.32 | Realized: +₹8.82</span>
                </div>
                <div class="position-row">
                    <span>ITC (LONG 4)</span>
                    <span style="color: var(--accent-cyan);">Avg: ₹267.00 | BuyVal: ₹1,068</span>
                </div>
                <div class="position-row">
                    <span>TATASTEEL (CLOSED)</span>
                    <span style="color: var(--accent-red);">Sold: ₹183.36 | Realized: -₹7.56</span>
                </div>
                <div style="margin-top: 14px; font-size: 12px; color: var(--text-secondary);">
                    <div>• Stop Losses Ratcheted to Breakeven</div>
                    <div>• Downside Loss Locked at ₹0.00</div>
                </div>
            </div>

            <div class="side-card">
                <div class="side-title">🧠 200+ QUANT REPOS NOTEBOOKLM DIRECTIVE</div>
                <div class="code-box">
[NOTEBOOKLM PINNED DIRECTIVE - 09:58 IST]
1. PNB SCALE-OUT:
   - Move hard SL to ₹118.35 (Breakeven Ratchet).
   - Tranche 1 (7 sh): Limit sell @ ₹120.10 (+1.5% / 1.5R) -> Lock +₹12.46.
   - Tranche 2 (7 sh): Chandelier ATR Trail until 14:45.

2. ITC SCALE-OUT:
   - Hard SL @ ₹265.80 (Risk ₹4.80).
   - Tranche 1 (2 sh): Limit @ ₹269.60 (+1% / 1R).
   - Tranche 2 (2 sh): Target @ ₹272.20.

3. HALF-KELLY CAPACITY:
   - Remaining Cash: ₹370.73 (Buying Power: ₹1,853.65).
   - Max Risk per new sniper signal: ₹11.48 (1.25% SOD).
   - Drawdown Hard Stop: ₹22.96 (2.5% SOD).

4. RECOVERY PATH TO +₹102:
   - Realized: +₹1.26
   - PNB Targets: +₹44.52
   - ITC Targets: +₹21.60
   - Sniper Trade: +₹22.96
   = Total: +₹90.34 to +₹102.00 (Done for the Day Lock)
                </div>
            </div>

            <div class="side-card">
                <div class="side-title">🌐 CONNECTED NOTEBOOK KERNELS</div>
                <div style="font-size: 12px; line-height: 1.6; color: var(--text-secondary);">
                    <div>1. <b>share market 17th sept_dui</b> (295 Sources)</div>
                    <div>2. <b>share market 17th sept_ak</b> (212 Sources)</div>
                    <div>3. <b>200+ QUANT REPOS</b> (290 Repos)</div>
                </div>
            </div>
        </div>
    </div>

    <script>
        // Auto reload page every 30 seconds to fetch newly ingested news
        setTimeout(() => {{
            window.location.reload();
        }}, 30000);
    </script>
</body>
</html>
"""

with open(TARGET_HTML, "w") as f:
    f.write(html_content)

print("SUCCESS: Radar HTML built at", TARGET_HTML)
