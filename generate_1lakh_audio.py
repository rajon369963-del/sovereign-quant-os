import asyncio
import edge_tts
import pybase64 as base64
import os
from pathlib import Path

AUDIO_TEXT = """
नमस्कार राजन भाई। अब हम खड़े हैं अपनी यात्रा के चरम शिखर पर: 1,00,000 रुपये की पूंजी का महा-विश्लेषण।
1,000 रुपये से 1 करोड़ की दूरी 10,000 गुना थी।
10,000 रुपये से 1 करोड़ की दूरी 1,000 गुना थी।
लेकिन 1,00,000 रुपये से 1 करोड़ की दूरी मात्र 100 गुना रह जाती है।
इस 1 लाख की कैपिटल को 1 करोड़ में कैसे बदला जाए, इस पर 10 राउंड का महासंग्राम पूरा हो चुका है।

राउंड 1 में घनश्याम टेक ने कहा कि 1 लाख रुपये आने पर भी ऑप्शंस में 1 से 2 लॉट इन-द-मनी ऑप्शंस की ही हार्ड सीलिंग होगी। और सबसे बड़ा नियम: 50 प्रतिशत प्रॉफिट विथड्रॉल रूल। हर महीने का आधा मुनाफा तुरंत बैंक खाते में ट्रांसफर करो, क्योंकि जब तक पैसा बैंक में नहीं जाता, वह मार्केट का पैसा है।

राउंड 2 में विवेक बजाज ने 50/30/20 पोर्टफोलियो मॉडल दिया। 50,000 रुपये कोर स्विंग और ईटीएफ में, 30,000 रुपये हेज्ड स्प्रेड्स और 5x एमआईएस कैश में, और 20,000 रुपये लिक्विड कैश बफर में रखें।

राउंड 3 में नितिन मुरारका ने 5 लाख रुपये के इंट्राडे एक्सपोज़र पर चेतावनी दी कि 10:15 बजे के बाद ही ओपन इंटरेस्ट और वीडब्ल्यूपी के रीटेस्ट पर 1,500 रुपये के स्टॉपलॉस के साथ काम करें। 6-फिगर कैपिटल पर ओवरट्रेडिंग सबसे बड़ा हत्यारा है।

राउंड 4 में सुबाशीष पानी ने प्रति ट्रेड 1 से डेढ़ प्रतिशत यानी 1,000 से 1,500 रुपये का रिस्क तय किया। 1:3 रिस्क-रिवॉर्ड पर 3,000 से 4,500 रुपये का टारगेट मिलेगा और 2,500 रुपये के दैनिक नुकसान पर स्क्रीन बंद हो जाएगी।

राउंड 5 में साकेत आर ने बताया कि 1 लाख रुपये पर पहली बार सेबी के हेज्ड मार्जिन रूल्स अनलॉक होते हैं। अब आप बुल पुट या बेयर कॉल स्प्रेड बेच सकते हैं जहाँ थीटा डिके आपकी जेब भरता है और विन-रेट 75 प्रतिशत हो जाती है।

राउंड 6 में पीआर सुंदर ने आयरन कोंडोर से हर महीने 3 से 5 प्रतिशत की शांत कंपाउंडिंग और ब्लैक-स्वान गैप-डाउन प्रोटेक्शन का फॉर्मूला दिया।

राउंड 7 में अभिषेक कर ने रुपयों के बजाय सिर्फ पर्सेंटेज में सोचने और लाइफस्टाइल इन्फ्लेशन से बचने की सीख दी।

राउंड 8 में सिद्धार्थ भानुशाली ने 30,000 रुपये के 3 अलग-अलग 44-एमए स्विंग ट्रेड्स में 15 से 20 प्रतिशत के मूव्स और विनर्स में पिरामिडिंग से 1 साल में 3 से 5 लाख बनाने का रोडमैप दिया।

राउंड 9 में डॉ. मुकुल अग्रवाल ने डिफेंस और ग्रीन एनर्जी जैसे सेक्टर्स के 4-5 मल्टीकैप लीडर्स में पेशेंट इन्वेस्टिंग से 10 लाख का सफर तय किया।

और राउंड 10 में क्वांट रिपोज़ और एंटीग्रैविटी मास्टर आर्काइव ने साबित किया कि 100 गुना का सफर बहुत आसान है। और जब आपकी एआई एजेंसी हर महीने 50 हजार से 1 लाख रुपये ट्रेडिंग खाते में डालेगी, तो 1 करोड़ की मंजिल 4 साल के बजाय मात्र 18 से 24 महीनों में हासिल हो जाएगी।
"""

async def generate():
    voice = "hi-IN-MadhurNeural"
    output_mp3 = "/tmp/courier_1lakh_debate_audio_temp.mp3"
    print(f"Synthesizing 1 Lakh debate audio ({len(AUDIO_TEXT)} chars) with {voice}...")
    communicate = edge_tts.Communicate(AUDIO_TEXT, voice, rate="+5%")
    await communicate.save(output_mp3)
    
    with open(output_mp3, "rb") as f:
        b64_audio = base64.b64encode(f.read()).decode("utf-8")
        
    os.remove(output_mp3)
    print("Ephemeral MP3 purged. Creating HTML Artifact...")
    
    html_content = f"""<!DOCTYPE html>
<html lang="hi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>🏛️ Sovereign ₹1,00,000 Capital 10-Round Debate Masterclass</title>
    <style>
        :root {{
            --bg-primary: #0a0e17;
            --surface-glass: rgba(18, 26, 44, 0.75);
            --border-glass: rgba(255, 255, 255, 0.125);
            --accent-gold: #f59e0b;
            --accent-purple: #8b5cf6;
            --text-main: #f3f4f6;
            --text-sub: #9ca3af;
        }}
        body {{
            background: radial-gradient(circle at top, #4c1d95, var(--bg-primary));
            color: var(--text-main);
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
            margin: 0;
            padding: 24px;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            box-sizing: border-box;
        }}
        .player-card {{
            background: var(--surface-glass);
            backdrop-filter: blur(20px) saturate(180%);
            -webkit-backdrop-filter: blur(20px) saturate(180%);
            border: 1px solid var(--border-glass);
            border-radius: 20px;
            padding: 32px;
            max-width: 680px;
            width: 100%;
            box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.6), inset 0 1px 1px rgba(255, 255, 255, 0.1);
        }}
        .header {{
            display: flex;
            align-items: center;
            gap: 16px;
            margin-bottom: 20px;
        }}
        .badge {{
            background: linear-gradient(135deg, #a855f7, #6b21a8);
            color: #fff;
            font-weight: 800;
            font-size: 11px;
            padding: 4px 10px;
            border-radius: 9999px;
            text-transform: uppercase;
            letter-spacing: 0.05em;
        }}
        h1 {{
            font-size: 22px;
            margin: 0;
            font-weight: 700;
            background: linear-gradient(to right, #fff, #ddd6fe);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }}
        .subtitle {{
            color: var(--text-sub);
            font-size: 13px;
            margin-top: 4px;
        }}
        .controls {{
            display: flex;
            flex-direction: column;
            gap: 16px;
            margin-top: 24px;
            background: rgba(0, 0, 0, 0.3);
            padding: 20px;
            border-radius: 14px;
            border: 1px solid rgba(255, 255, 255, 0.05);
        }}
        audio {{
            width: 100%;
            height: 48px;
            border-radius: 8px;
            outline: none;
        }}
        .speed-bar {{
            display: flex;
            justify-content: space-between;
            align-items: center;
        }}
        .speed-btn-group {{
            display: flex;
            gap: 8px;
        }}
        .speed-btn {{
            background: rgba(255, 255, 255, 0.08);
            border: 1px solid var(--border-glass);
            color: var(--text-main);
            padding: 6px 14px;
            border-radius: 8px;
            cursor: pointer;
            font-size: 12px;
            font-weight: 600;
            transition: all 0.2s;
        }}
        .speed-btn.active {{
            background: #a855f7;
            color: #fff;
            border-color: #a855f7;
        }}
        .timeline-summary {{
            margin-top: 24px;
            font-size: 13px;
            line-height: 1.6;
            color: #d1d5db;
        }}
        .timeline-step {{
            margin-bottom: 12px;
            padding-left: 14px;
            border-left: 2px solid #a855f7;
        }}
        .timeline-step strong {{
            color: #fff;
        }}
    </style>
</head>
<body>
    <div class="player-card">
        <div class="header">
            <span class="badge">Charam Shikhar (₹1 Lakh)</span>
            <div>
                <h1>🏛️ ₹1,00,000 कैपिटल महा-डिबेट: ₹1L से ₹1 करोड़</h1>
                <div class="subtitle">9 यूट्यूबर गुरु + 200+ क्वांट रिपोज़ + एंटीग्रैविटी मास्टर आर्काइव</div>
            </div>
        </div>

        <div class="controls">
            <audio id="audioPlayer" controls>
                <source src="data:audio/mp3;base64,{b64_audio}" type="audio/mp3">
                Your browser does not support audio playback.
            </audio>
            <div class="speed-bar">
                <span style="font-size: 12px; color: var(--text-sub);">⚡ Playback Speed (Default 2.0x):</span>
                <div class="speed-btn-group">
                    <button class="speed-btn" onclick="setSpeed(1.0)">1.0x</button>
                    <button class="speed-btn" onclick="setSpeed(1.5)">1.5x</button>
                    <button class="speed-btn active" id="btn2x" onclick="setSpeed(2.0)">2.0x</button>
                    <button class="speed-btn" onclick="setSpeed(2.5)">2.5x</button>
                </div>
            </div>
        </div>

        <div class="timeline-summary">
            <div class="timeline-step">
                <strong>Round 1 (घनश्याम टेक):</strong> 1-2 लॉट ITM ऑप्शंस की हार्ड सीलिंग। 50% प्रॉफ़िट विथड्रॉल नियम से कैपिटल सुरक्षा।
            </div>
            <div class="timeline-step">
                <strong>Round 2 (विवेक बजाज):</strong> 50/30/20 पोर्टफोलियो: 50k कोर स्विंग + 30k हेज्ड स्प्रेड्स + 20k लिक्विड बफर।
            </div>
            <div class="timeline-step">
                <strong>Round 3 (नितिन मुरारका):</strong> 5 लाख एक्सपोज़र पर 10:15 AM के बाद OI कंसंट्रेशन व VWAP रीटेस्ट पर ही ट्रेड।
            </div>
            <div class="timeline-step">
                <strong>Round 4 (सुबाशीष पानी):</strong> 1-1.5% रिस्क (₹1,000-₹1,500), 1:3 RR पर ₹3,000-₹4,500 टारगेट, ₹2,500 दैनिक लॉस कैप।
            </div>
            <div class="timeline-step">
                <strong>Round 5 (साकेत आर):</strong> हेज्ड क्रेडिट स्प्रेड्स अनलॉक (~₹30k/लॉट)—थीटा कैप्चर व 75% विन रेट।
            </div>
            <div class="timeline-step">
                <strong>Round 6 (पीआर सुंदर):</strong> आयरन कोंडोर्स से 3-5% मासिक कम्पाउंडिंग और ब्लैक-स्वान गैप-डाउन प्रोटेक्शन।
            </div>
            <div class="timeline-step">
                <strong>Round 7 (अभिषेक कर):</strong> सिक्स-फिगर साइकोलॉजी—रुपयों से डिटैच होकर केवल पर्सेंटेज में सोचना।
            </div>
            <div class="timeline-step">
                <strong>Round 8 (सिद्धार्थ भानुशाली):</strong> 30k के 3 44-MA स्विंग पोजीशंस, पिरामिडिंग से 1 साल में 3-5 लाख तक स्केलिंग।
            </div>
            <div class="timeline-step">
                <strong>Round 9 (डॉ. मुकुल अग्रवाल):</strong> 4-5 मल्टीकैप सेक्टोरल लीडर्स में पेशेंट सेक्टर रोटेशन से 10 लाख का निर्माण।
            </div>
            <div class="timeline-step">
                <strong>Round 10 (क्वांट व एंटीग्रैविटी):</strong> मात्र 100x की दूरी! एआई एजेंसी कैशफ्लो + क्वांट बॉट से 18-24 माह में 1 करोड़!
            </div>
        </div>
    </div>

    <script>
        const audio = document.getElementById('audioPlayer');
        audio.playbackRate = 2.0;

        function setSpeed(speed) {{
            audio.playbackRate = speed;
            document.querySelectorAll('.speed-btn').forEach(btn => btn.classList.remove('active'));
            event.target.classList.add('active');
        }}
    </script>
</body>
</html>
"""
    dest_path = "/Users/rajondas/.gemini/antigravity/brain/406b1b3f-5aca-403c-b468-cf736f90106e/courier_1lakh_debate_master_audio.html"
    with open(dest_path, "w", encoding="utf-8") as f:
        f.write(html_content)
    print(f"Created Master ₹1 Lakh Audio Artifact at: {dest_path}")

asyncio.run(generate())
