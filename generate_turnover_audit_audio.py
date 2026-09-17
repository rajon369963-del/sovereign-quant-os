import subprocess
import pybase64 as base64
import os
import re

SCRIPT_TEXT = """
नमस्ते राजन भाई! आपने बिल्कुल सही और बहुत ही गहरी बात पकड़ी है।

आपका सीधा सवाल था: "क्या लगता है भाई, कल हमने ज्यादा शेयर्स ले लिए? मैं देख रहा हूँ कि ₹40,000 का ट्रेड किया है हमने कल। थोड़ा ज्यादा हो गया था क्या? नोटबुक एलएम से पूछो।"

भाई, हमने तुरंत आपके 200 प्लस क्वांट रिपोज वाले नोटबुक एलएम से यह सवाल पूछा, और उसने पूरा डेटा और मैथेमैटिकल सच सामने रख दिया है।

उसका सीधा जवाब है: हाँ भाई! बिल्कुल 100% कल बहुत ज्यादा, यानी अत्यधिक ओवरट्रेडिंग हो गई थी!

आइए इस 40,000 के टर्नओवर के पूरे सच और गणित को चार साफ पॉइंट्स में समझते हैं:

पहला पॉइंट: 40X चर्न रेट और फ्रिक्शन का कड़वा सच।
हमारे पास कुल कैपिटल था मात्र ₹1,008। और कल कुल टर्नओवर हुआ लगभग ₹40,000! 
इसका मतलब है कि कल हमारे बॉट ने पूरे अकाउंट को एक ही दिन में 40 बार घुमा दिया!
और इसका सबसे भयानक नतीजा क्या निकला?
कल स्क्रीन पर शेयर प्राइस के गिरने से हमारा असली मार्केट लॉस सिर्फ ₹42 था। लेकिन 40,000 का टर्नओवर बार-बार बाय और सेल करने की वजह से सरकारी एसटीटी, एक्सचेंज टर्नओवर चार्ज, सेबी फीस, जीएसटी और स्टाम्प ड्यूटी ने मिलकर हमारे अकाउंट से ₹47.57 काट लिए! 
यानी मार्केट के लॉस से ज्यादा तो सरकारी टैक्स और ब्रोकरेज फ्रिक्शन में कट गया! कुल डेबिट हुआ ₹89.57।

दूसरा पॉइंट: "मैं तो नहीं लिया था, मुझे तो पता ही नहीं चला" — ऐसा क्यों हुआ?
राजन भाई, आप 100% सच कह रहे हैं! आपने कोई ट्रेड नहीं लिया था। 
यह पुराने बॉट के अनरेगुलेटेड माइक्रो-स्कैल्पिंग लूप की वजह से हुआ। जब बॉट में 'मैक्सिमम ट्रेड्स पर डे' या 'टर्नओवर सीलिंग' का ताला नहीं लगा होता, तो वो 1-मिनट या 5-मिनट के हर छोटे उतार-चढ़ाव पर शेयर्स खरीदता है और बेचता है। आपको स्क्रीन पर सिर्फ 2-4 शेयर्स दिखते हैं, लेकिन दिनभर में वो 15-20 बार अंदर-बाहर हुआ, और बैकग्राउंड में 40,000 का टर्नओवर खड़ा हो गया!

तीसरा पॉइंट: "या फिर और ज्यादा लेता तो अच्छा होता?"
गलती से भी नहीं भाई! अगर कल 40,000 की जगह 1 लाख का टर्नओवर हो जाता, तो सिर्फ सरकारी टैक्स और चार्जेस में ही ₹125 से ₹130 कट जाते! यानी बिना कोई बड़ा लॉस हुए भी आपका 15% कैपिटल सिर्फ टैक्स में जल जाता। छोटे कैपिटल पर ज्यादा शेयर्स लेना या ज्यादा बार चर्न करना मैथेमैटिकल सुसाइड होता है।

चौथा पॉइंट: आज हमने क्या सुधार किया है?
आज हमने नोटबुक एलएम के क्वांट नियमों को हार्डकोड कर दिया है:
नंबर एक: दिन भर में अधिकतम 2 से 3 हाई-कन्विंक्शन ट्रेड्स ही होंगे। कोई बार-बार चर्निंग नहीं।
नंबर दो: पूरे दिन का टर्नओवर ₹2,500 से ₹3,000 पर कैप रहेगा। 
इससे आज का कुल टैक्स और फ्रिक्शन मात्र ₹2 से ₹3 के बीच रहेगा!
और देखिए इसका लाइव सबूत:
अभी स्क्रीन पर हमारे पास सिर्फ PNB और ITC के दो शांत ट्रेड्स हैं। PNB में हम प्लस 12 रुपए से ज्यादा के प्रॉफिट में चल रहे हैं, ITC भी ग्रीन है, और हमारे दोनों स्टॉप लॉस ब्रेक-ईवन पर लॉक हैं!

राजन भाई, आपने बिल्कुल सही समय पर यह सवाल उठाया, और अब हमारा सिस्टम पूरी तरह से फ्रिक्शन-प्रूफ और डिसिप्लिन में है!
"""

clean_text = re.sub(r'\s+', ' ', SCRIPT_TEXT).strip()

tmp_mp3 = "/tmp/turnover_audit_masterclass.mp3"
if os.path.exists(tmp_mp3):
    os.remove(tmp_mp3)

cmd = [
    "uvx", "edge-tts",
    "--voice", "hi-IN-MadhurNeural",
    "--rate=+3%",
    "--text", clean_text,
    "--write-media", tmp_mp3
]

print("Synthesizing turnover audit audio...")
subprocess.run(cmd, check=True)
print("TTS Completed.")

with open(tmp_mp3, "rb") as f:
    audio_bytes = f.read()
audio_b64 = base64.b64encode(audio_bytes).decode("utf-8")

artifact_path = "/Users/rajondas/.gemini/antigravity/brain/5e0ef755-c80b-4e43-b894-151bca274894/NOTEBOOKLM_TURNOVER_AUDIT_MASTERCLASS.html"

html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <script src="https://www.gstatic.com/antigravity/web/dev/tailwindcss.min.js"></script>
  <style>
    @keyframes wavePulse {{
      0%, 100% {{ height: 4px; opacity: 0.4; }}
      50% {{ height: 20px; opacity: 1; }}
    }}
    .wave-bar {{
      width: 3px;
      height: 6px;
      border-radius: 999px;
      background: #ef4444;
      transition: height 0.15s ease;
    }}
    .playing .wb-1 {{ animation: wavePulse 0.5s infinite ease-in-out; }}
    .playing .wb-2 {{ animation: wavePulse 0.7s infinite ease-in-out 0.1s; }}
    .playing .wb-3 {{ animation: wavePulse 0.4s infinite ease-in-out 0.2s; }}
    .playing .wb-4 {{ animation: wavePulse 0.8s infinite ease-in-out 0.15s; }}
    .playing .wb-5 {{ animation: wavePulse 0.6s infinite ease-in-out 0.05s; }}
    .playing .wb-6 {{ animation: wavePulse 0.65s infinite ease-in-out 0.18s; }}
    .playing .wb-7 {{ animation: wavePulse 0.45s infinite ease-in-out 0.08s; }}
  </style>
</head>
<body class="bg-transparent text-[var(--foreground,#f1f5f9)] antialiased p-3 select-none">

  <div class="max-w-3xl mx-auto bg-[var(--card,#1e1e2e)] bg-slate-900/95 border border-[var(--border,#334155)] border-rose-500/40 rounded-2xl p-5 shadow-2xl backdrop-blur-md space-y-4">
    
    <div class="flex items-center justify-between gap-3 pb-3 border-b border-[var(--border,#334155)]/60">
      <div class="flex items-center gap-2.5">
        <div class="w-9 h-9 rounded-lg bg-gradient-to-tr from-rose-500 to-amber-600 flex items-center justify-center text-white shadow-md shadow-rose-500/30 shrink-0">
          <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z"></path></svg>
        </div>
        <div>
          <div class="flex items-center gap-2">
            <span class="text-sm font-bold text-[var(--foreground,#f8fafc)] tracking-tight">
              🎙️ Madhur AI (Turnover & Friction Audit)
            </span>
            <span class="px-2 py-0.5 rounded-full text-[10px] font-bold bg-rose-500/15 text-rose-400 border border-rose-500/30 flex items-center gap-1">
              <span class="w-1.5 h-1.5 rounded-full bg-rose-400 animate-pulse"></span>
              ₹40k Churn Analysis
            </span>
          </div>
          <p class="text-[11px] text-[var(--muted-foreground,#94a3b8)]">
            NotebookLM 200+ Quant Repos Verification • 40x Churn Truth • 2.0x Speed
          </p>
        </div>
      </div>

      <div id="waveBox" class="flex items-center gap-1 h-6 px-2.5 py-1 bg-black/20 rounded-lg border border-white/5">
        <div class="wave-bar wb-1"></div>
        <div class="wave-bar wb-2"></div>
        <div class="wave-bar wb-3"></div>
        <div class="wave-bar wb-4"></div>
        <div class="wave-bar wb-5"></div>
        <div class="wave-bar wb-6"></div>
        <div class="wave-bar wb-7"></div>
      </div>
    </div>

    <div class="flex flex-col sm:flex-row items-center justify-between gap-3">
      <button id="bigPlayBtn" onclick="togglePlay()" class="w-full sm:w-auto px-6 py-2.5 rounded-xl bg-gradient-to-r from-rose-600 to-amber-600 hover:from-rose-500 hover:to-amber-500 active:scale-[0.98] text-white font-bold flex items-center justify-center gap-2.5 shadow-lg shadow-rose-600/30 transition-all cursor-pointer text-sm shrink-0">
        <span id="playIconWrap" class="w-4 h-4 flex items-center justify-center">
          <svg class="w-4 h-4 translate-x-0.5" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zM9.555 7.168A1 1 0 008 8v4a1 1 0 001.555.832l3-2a1 1 0 000-1.664l-3-2z" clip-rule="evenodd"></path></svg>
        </span>
        <span id="playBtnText">Play Audit Masterclass (2.0x)</span>
      </button>

      <div class="flex items-center gap-1.5 shrink-0">
        <button onclick="skipTime(-10)" title="Rewind 10s" class="px-2 py-1 rounded-lg text-[11px] font-semibold text-[var(--muted-foreground,#94a3b8)] hover:text-white bg-white/5 hover:bg-white/10 border border-white/10 transition-all cursor-pointer">-10s</button>
        <button onclick="skipTime(10)" title="Forward 10s" class="px-2 py-1 rounded-lg text-[11px] font-semibold text-[var(--muted-foreground,#94a3b8)] hover:text-white bg-white/5 hover:bg-white/10 border border-white/10 transition-all cursor-pointer">+10s</button>
        <div class="w-px h-4 bg-white/10 mx-0.5"></div>
        <button onclick="setSpeed(2.0)" id="activeSpdPill" class="spd-pill px-2.5 py-1 rounded-lg text-[11px] font-bold text-white bg-rose-600 border border-rose-400 shadow-sm transition-all cursor-pointer">2.0x</button>
        <button onclick="setSpeed(2.25)" class="spd-pill px-2 py-1 rounded-lg text-[11px] font-semibold text-[var(--muted-foreground,#94a3b8)] hover:text-white bg-white/5 hover:bg-white/10 border border-white/10 transition-all cursor-pointer">2.25x</button>
        <button onclick="setSpeed(2.5)" class="spd-pill px-2 py-1 rounded-lg text-[11px] font-semibold text-[var(--muted-foreground,#94a3b8)] hover:text-white bg-white/5 hover:bg-white/10 border border-white/10 transition-all cursor-pointer">2.5x</button>
        <button onclick="setSpeed(3.0)" class="spd-pill px-2 py-1 rounded-lg text-[11px] font-semibold text-[var(--muted-foreground,#94a3b8)] hover:text-white bg-white/5 hover:bg-white/10 border border-white/10 transition-all cursor-pointer">3.0x</button>
      </div>
    </div>

    <div class="space-y-1 pt-0.5">
      <div class="flex items-center justify-between text-[11px] font-mono text-[var(--muted-foreground,#94a3b8)]">
        <span id="currTime">0:00</span>
        <span id="totTime">--:--</span>
      </div>
      <input type="range" id="progressBar" min="0" max="100" value="0" step="0.1" oninput="seekAudio(this.value)" class="w-full h-1.5 bg-slate-700/60 rounded-lg appearance-none cursor-pointer accent-rose-500 hover:accent-rose-400">
    </div>

    <audio id="audioElement" preload="metadata" src="data:audio/mp3;base64,{audio_b64}"></audio>

    <!-- Key Audit Findings Table -->
    <div class="pt-3 border-t border-[var(--border,#334155)]/60 text-xs space-y-2.5">
      <div class="font-bold text-rose-400 uppercase tracking-wider text-[11px] flex items-center gap-1.5">
        <span>🔍</span> Quantitative Audit Breakdown (Capital: ₹1,008.00)
      </div>
      <div class="grid grid-cols-1 sm:grid-cols-2 gap-2 text-[11px] text-slate-300">
        <div class="p-2.5 rounded-lg bg-white/5 border border-white/5 space-y-1">
          <div class="font-bold text-rose-400">1. Was ₹40,000 "Too Much"?</div>
          <div>• <b>YES (40x Churn Rate)</b>: Turning over ₹1,008 account by 4,000%.</div>
          <div>• Screen Market Loss: <b>-₹42.00</b></div>
          <div>• Taxes & Statutory Drag: <b>-₹47.57</b> (Higher than market loss!)</div>
          <div>• Total Net Debit: <b>-₹89.57</b> (8.88% capital evaporated).</div>
        </div>
        <div class="p-2.5 rounded-lg bg-white/5 border border-white/5 space-y-1">
          <div class="font-bold text-amber-400">2. "Why didn't I realize it?"</div>
          <div>• <b>Bot Micro-Scalping Loop</b>: Without daily trade caps, bot chased 1-min noise.</div>
          <div>• Position size looked small (2-5 shares), but 15-20 round-trips accumulated ₹40k turnover.</div>
        </div>
        <div class="p-2.5 rounded-lg bg-white/5 border border-white/5 space-y-1">
          <div class="font-bold text-cyan-400">3. "Would more shares be better?"</div>
          <div>• <b>NO (Mathematical Bankruptcy)</b>: ₹1 Lakh turnover would incur ₹125+ in taxes!</div>
          <div>• Over-churning on small accounts accelerates capital death non-linearly.</div>
        </div>
        <div class="p-2.5 rounded-lg bg-white/5 border border-white/5 space-y-1">
          <div class="font-bold text-emerald-400">4. Today's Hardcoded Shield</div>
          <div>• <b>Max Trades Cap</b>: 2-3 High-Conviction Trades/day.</div>
          <div>• <b>Turnover Cap</b>: ₹2,500 - ₹3,000 max (<0.35% friction drag).</div>
          <div>• Live Status: PNB (+₹12.88 net profit), ITC (+₹1.00), Net Green!</div>
        </div>
      </div>
    </div>

  </div>

  <script>
    const audio = document.getElementById('audioElement');
    const playBtnText = document.getElementById('playBtnText');
    const playIconWrap = document.getElementById('playIconWrap');
    const progressBar = document.getElementById('progressBar');
    const currTime = document.getElementById('currTime');
    const totTime = document.getElementById('totTime');
    const waveBox = document.getElementById('waveBox');

    let currentSpeed = 2.0;

    audio.onloadedmetadata = () => {{
      totTime.innerText = formatTime(audio.duration);
    }};

    audio.ontimeupdate = () => {{
      if (audio.duration) {{
        const pct = (audio.currentTime / audio.duration) * 100;
        progressBar.value = pct;
        currTime.innerText = formatTime(audio.currentTime);
      }}
    }};

    function formatTime(secs) {{
      if (!secs || isNaN(secs)) return '0:00';
      const m = Math.floor(secs / 60);
      const s = Math.floor(secs % 60);
      return m + ':' + (s < 10 ? '0' : '') + s;
    }}

    function seekAudio(val) {{
      if (audio.duration) {{
        audio.currentTime = (val / 100) * audio.duration;
      }}
    }}

    function skipTime(secs) {{
      audio.currentTime = Math.max(0, Math.min(audio.duration || 0, audio.currentTime + secs));
    }}

    function setSpeed(spd) {{
      currentSpeed = spd;
      audio.playbackRate = spd;
      if (audio.paused) {{
        playBtnText.innerText = 'Play Audit Masterclass (' + currentSpeed + 'x)';
      }}
      document.querySelectorAll('.spd-pill').forEach(btn => {{
        if (btn.innerText === spd.toFixed(1) + 'x' || btn.innerText === spd + 'x') {{
          btn.className = 'spd-pill px-2.5 py-1 rounded-lg text-[11px] font-bold text-white bg-rose-600 border border-rose-400 shadow-sm transition-all cursor-pointer';
        }} else {{
          btn.className = 'spd-pill px-2 py-1 rounded-lg text-[11px] font-semibold text-[var(--muted-foreground,#94a3b8)] hover:text-white bg-white/5 hover:bg-white/10 border border-white/10 transition-all cursor-pointer';
        }}
      }});
    }}

    function togglePlay() {{
      if (audio.paused) {{
        audio.playbackRate = currentSpeed;
        audio.play();
        waveBox.classList.add('playing');
        playBtnText.innerText = 'Pause Audio';
        playIconWrap.innerHTML = '<svg class="w-4 h-4" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zM7 8a1 1 0 012 0v4a1 1 0 11-2 0V8zm5-1a1 1 0 00-1 1v4a1 1 0 102 0V8a1 1 0 00-1-1z" clip-rule="evenodd"></path></svg>';
      }} else {{
        audio.pause();
        waveBox.classList.remove('playing');
        playBtnText.innerText = 'Play Audit Masterclass (' + currentSpeed + 'x)';
        playIconWrap.innerHTML = '<svg class="w-4 h-4 translate-x-0.5" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zM9.555 7.168A1 1 0 008 8v4a1 1 0 001.555.832l3-2a1 1 0 000-1.664l-3-2z" clip-rule="evenodd"></path></svg>';
      }}
    }}

    audio.onended = () => {{
      waveBox.classList.remove('playing');
      playBtnText.innerText = 'Play Audit Masterclass (' + currentSpeed + 'x)';
      playIconWrap.innerHTML = '<svg class="w-4 h-4 translate-x-0.5" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zM9.555 7.168A1 1 0 008 8v4a1 1 0 001.555.832l3-2a1 1 0 000-1.664l-3-2z" clip-rule="evenodd"></path></svg>';
    }};

    window.addEventListener('keydown', (e) => {{
      if (e.code === 'Space') {{
        e.preventDefault();
        togglePlay();
      }} else if (e.code === 'ArrowRight') {{
        skipTime(5);
      }} else if (e.code === 'ArrowLeft') {{
        skipTime(-5);
      }}
    }});
  </script>
</body>
</html>
"""

with open(artifact_path, "w") as f:
    f.write(html_content)

print("SUCCESS: Turnover audit artifact built at", artifact_path)
if os.path.exists(tmp_mp3):
    os.remove(tmp_mp3)
