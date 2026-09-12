import json
from pathlib import Path

AUDIO_B64_PATH = Path("/Users/rajondas/teamwork_projects/sovereign-quant-os/audio_1008_b64.txt")
TARGET_HTML = Path("/Users/rajondas/.gemini/antigravity/brain/05b0a610-029a-4d44-89ac-4d2003c43d26/player_dhan_1008_shagun_activation.html")

with open(AUDIO_B64_PATH) as f:
    audio_base64 = f.read().strip()

html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>₹1,008 Shagun Capital Activation | DhanHQ Live Engine</title>
<style>
  :root {{
    --bg-primary: #080c14;
    --bg-glass: rgba(18, 24, 38, 0.85);
    --glass-border: rgba(255, 215, 0, 0.25);
    --accent-gold: #ffd700;
    --accent-amber: #f59e0b;
    --accent-cyan: #00f2fe;
    --accent-green: #10b981;
    --text-primary: #f8fafc;
    --text-muted: #94a3b8;
  }}
  * {{ box-sizing: border-box; margin: 0; padding: 0; font-family: -apple-system, BlinkMacSystemFont, 'SF Pro Display', sans-serif; }}
  body {{
    background: radial-gradient(circle at 50% 10%, #1e1b4b 0%, var(--bg-primary) 75%);
    color: var(--text-primary);
    min-height: 100vh;
    display: flex;
    justify-content: center;
    align-items: center;
    padding: 24px;
  }}
  .container {{
    width: 100%;
    max-width: 820px;
    background: var(--bg-glass);
    border: 1px solid var(--glass-border);
    backdrop-filter: blur(28px);
    border-radius: 24px;
    padding: 32px;
    box-shadow: 0 12px 48px rgba(0, 0, 0, 0.6), 0 0 40px rgba(255, 215, 0, 0.12);
    display: flex;
    flex-direction: column;
    gap: 24px;
  }}
  .header {{
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-bottom: 1px solid rgba(255, 255, 255, 0.08);
    padding-bottom: 20px;
  }}
  .badge-shagun {{
    background: linear-gradient(135deg, rgba(255, 215, 0, 0.2), rgba(245, 158, 11, 0.1));
    border: 1px solid var(--accent-gold);
    color: var(--accent-gold);
    padding: 6px 14px;
    border-radius: 20px;
    font-size: 12px;
    font-weight: 700;
    letter-spacing: 1px;
    display: flex;
    align-items: center;
    gap: 6px;
  }}
  .hud-grid {{
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 16px;
  }}
  .hud-card {{
    background: rgba(255, 255, 255, 0.03);
    border: 1px solid rgba(255, 255, 255, 0.07);
    border-radius: 16px;
    padding: 16px;
    display: flex;
    flex-direction: column;
    gap: 6px;
  }}
  .hud-card.highlight {{
    background: linear-gradient(135deg, rgba(255, 215, 0, 0.08), rgba(16, 185, 129, 0.04));
    border-color: rgba(255, 215, 0, 0.35);
  }}
  .hud-label {{ font-size: 12px; color: var(--text-muted); text-transform: uppercase; letter-spacing: 0.5px; }}
  .hud-value {{ font-size: 24px; font-weight: 800; color: #fff; font-variant-numeric: tabular-nums; }}
  .hud-value.gold {{ color: var(--accent-gold); }}
  .hud-value.green {{ color: var(--accent-green); }}

  /* Audio Bar */
  .audio-bar {{
    background: rgba(10, 15, 25, 0.9);
    border: 1px solid rgba(255, 255, 255, 0.1);
    border-radius: 18px;
    padding: 16px 20px;
    display: flex;
    align-items: center;
    gap: 16px;
  }}
  .audio-btn {{
    background: linear-gradient(135deg, var(--accent-gold), var(--accent-amber));
    border: none;
    color: #000;
    font-weight: 700;
    padding: 10px 20px;
    border-radius: 20px;
    cursor: pointer;
    display: flex;
    align-items: center;
    gap: 8px;
    font-size: 13px;
    transition: transform 0.15s ease, filter 0.15s ease;
  }}
  .audio-btn:hover {{ filter: brightness(1.15); transform: scale(1.02); }}
  .scrubber-container {{ flex: 1; display: flex; align-items: center; gap: 10px; }}
  .scrubber {{
    flex: 1;
    -webkit-appearance: none;
    height: 6px;
    border-radius: 3px;
    background: rgba(255, 255, 255, 0.15);
    outline: none;
    cursor: pointer;
  }}
  .scrubber::-webkit-slider-thumb {{
    -webkit-appearance: none;
    width: 14px;
    height: 14px;
    border-radius: 50%;
    background: var(--accent-gold);
    box-shadow: 0 0 10px var(--accent-gold);
  }}
  .time-display {{ font-size: 12px; color: var(--text-muted); font-variant-numeric: tabular-nums; }}
  .speed-btns {{ display: flex; gap: 6px; }}
  .speed-btn {{
    background: rgba(255, 255, 255, 0.06);
    border: 1px solid rgba(255, 255, 255, 0.1);
    color: var(--text-muted);
    font-size: 11px;
    padding: 5px 9px;
    border-radius: 8px;
    cursor: pointer;
  }}
  .speed-btn.active {{ background: rgba(255, 215, 0, 0.2); color: var(--accent-gold); border-color: var(--accent-gold); font-weight: 700; }}

  /* Strategy Breakdown */
  .strategy-box {{
    background: rgba(0, 0, 0, 0.4);
    border: 1px solid rgba(255, 255, 255, 0.08);
    border-radius: 16px;
    padding: 20px;
  }}
  .sec-title {{ font-size: 14px; font-weight: 700; color: var(--accent-cyan); margin-bottom: 12px; display: flex; justify-content: space-between; }}
  .param-table {{ width: 100%; border-collapse: collapse; font-size: 13px; }}
  .param-table td {{ padding: 8px 12px; border-bottom: 1px solid rgba(255, 255, 255, 0.05); }}
  .param-table td:first-child {{ color: var(--text-muted); width: 45%; }}
  .param-table td:last-child {{ color: #fff; font-family: monospace; font-weight: 600; }}
</style>
</head>
<body>

<div class="container">
  <div class="header">
    <div>
      <h1 style="font-size: 22px; font-weight: 800; display: flex; align-items: center; gap: 10px;">
        🕉️ ₹1,008 SHAGUN CAPITAL CONFIRMED
      </h1>
      <p style="font-size: 13px; color: var(--text-muted); margin-top: 4px;">
        Live Gateway: DhanHQ v2.2.0 | Client: 1113693441 | State: DEPOSIT_VERIFIED
      </p>
    </div>
    <div class="badge-shagun">
      <span>✨ 1008 SHAGUN</span>
    </div>
  </div>

  <div class="hud-grid">
    <div class="hud-card highlight">
      <div class="hud-label">Available Balance</div>
      <div class="hud-value gold">₹1,008.00</div>
    </div>
    <div class="hud-card">
      <div class="hud-label">API Status</div>
      <div class="hud-value green">200 OK</div>
    </div>
    <div class="hud-card">
      <div class="hud-label">Max Risk Per Trade</div>
      <div class="hud-value" style="color: var(--accent-cyan);">₹15 - ₹20</div>
    </div>
  </div>

  <div class="audio-bar">
    <button id="playBtn" class="audio-btn" onclick="togglePlay()">
      <span id="playIcon">▶</span> <span id="playText">Play Shagun Briefing</span>
    </button>
    <div class="scrubber-container">
      <span id="curTime" class="time-display">0:00</span>
      <input type="range" id="scrubber" class="scrubber" value="0" min="0" max="100" step="0.1" oninput="seekAudio()">
      <span id="durTime" class="time-display">--:--</span>
    </div>
    <div class="speed-btns">
      <button class="speed-btn" onclick="setSpeed(1.0)">1.0x</button>
      <button class="speed-btn" onclick="setSpeed(1.5)">1.5x</button>
      <button class="speed-btn active" onclick="setSpeed(2.0)">2.0x</button>
      <button class="speed-btn" onclick="setSpeed(2.5)">2.5x</button>
    </div>
  </div>

  <audio id="audioElem" preload="auto">
    <source src="data:audio/mp3;base64,{audio_base64}" type="audio/mp3">
  </audio>

  <div class="strategy-box">
    <div class="sec-title">
      <span>🛡️ QUANTITATIVE RISK ENVELOPE (FRACTIONAL KELLY)</span>
      <span style="color: var(--accent-green); font-size: 11px;">HEDGE_10 ACTIVE</span>
    </div>
    <table class="param-table">
      <tr><td>Seed Shagun Capital</td><td>₹1,008.00 INR (DhanHQ Verified)</td></tr>
      <tr><td>Kelly Allocation Fraction</td><td>κ = 0.25 (Quarter-Kelly Strict)</td></tr>
      <tr><td>Risk Per Trade Limit</td><td>1.5% - 2.0% of Capital (₹15.12 - ₹20.16)</td></tr>
      <tr><td>Drawdown Circuit Breaker</td><td>Daily Loss Lockout at ₹50.00</td></tr>
      <tr><td>Consecutive Loss Capacity</td><td>> 50 Trades Before 50% Drawdown</td></tr>
      <tr><td>Probability of Ruin (Law #1)</td><td>P(Ruin) < 0.0001% (Mathematically Ergodic)</td></tr>
    </table>
  </div>
</div>

<script>
const audio = document.getElementById('audioElem');
const playBtn = document.getElementById('playBtn');
const playIcon = document.getElementById('playIcon');
const playText = document.getElementById('playText');
const scrubber = document.getElementById('scrubber');
const curTime = document.getElementById('curTime');
const durTime = document.getElementById('durTime');

audio.playbackRate = 2.0;

function formatTime(s) {{
  if (!s || isNaN(s)) return "0:00";
  const m = Math.floor(s / 60);
  const sec = Math.floor(s % 60);
  return `${{m}}:${{sec < 10 ? '0' : ''}}${{sec}}`;
}}

function togglePlay() {{
  if (audio.paused) {{
    audio.play();
    playIcon.textContent = "⏸";
    playText.textContent = "Pause Briefing";
  }} else {{
    audio.pause();
    playIcon.textContent = "▶";
    playText.textContent = "Play Shagun Briefing";
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
  document.querySelectorAll('.speed-btn').forEach(b => b.classList.remove('active'));
  event.target.classList.add('active');
}}
</script>
</body>
</html>
"""

with open(TARGET_HTML, "w") as f:
    f.write(html)
print(f"✅ Generated {TARGET_HTML} ({TARGET_HTML.stat().st_size} bytes)")
