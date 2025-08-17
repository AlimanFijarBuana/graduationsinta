import streamlit as st
import streamlit.components.v1 as components
import base64
import json
import os

# ==================== PAGE CONFIGURATION ====================
st.set_page_config(
    page_title="✨ Graduation Sinta Istamarina ✨",
    page_icon="👑",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ==================== GRADUATION DATA ====================
data = {
    "name": "Sinta Istamarina",
    "degree": "S.M.",
    "university": "Universitas Pelita Bangsa",
    "faculty": "Fakultas Ekonomi dan Bisnis",
    "graduation_year": "2025",
    "quote": "Bermimpilah setinggi langit, dan bersinarlah lebih terang! ✨"
}

# ==================== PHOTO GALLERY ====================
gallery = [
    {"path": "img/IMG_7972.jpg", "caption": "My Shining Moment ✨"},
    {"path": "img/IMG_8010.jpg", "caption": "Little moments, big memories 🌸"},
    {"path": "img/IMG_8041.jpg", "caption": "With My Sunshine 💫"}
]

# ==================== UTILITY FUNCTIONS ====================
def get_base64_of_file(path):
    """Membaca file dan mengonversinya menjadi string Base64."""
    try:
        with open(path, "rb") as f:
            data = f.read()
        return base64.b64encode(data).decode("utf-8")
    except FileNotFoundError:
        st.error(f"File tidak ditemukan: {path}")
        return None

def fire_confetti():
    """Mengaktifkan efek confetti menggunakan JavaScript."""
    components.html("""
    <script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.5.1/dist/confetti.browser.min.js"></script>
    <script>
    function fireConfetti() {
        confetti({
            particleCount: 500,
            spread: 120,
            origin: { y: 0.6 },
            colors: ['#ff69b4', '#ffb6c1', '#ffc0cb', '#ffffff', '#ffd700'],
            shapes: ['circle', 'star'],
            scalar: 1.5
        });

        setTimeout(() => {
            confetti({
                particleCount: 100,
                spread: 70,
                origin: { x: 0.3, y: 0.7 },
                colors: ['#ffd700'],
                shapes: ['star'],
                scalar: 2
            });

            confetti({
                particleCount: 100,
                spread: 70,
                origin: { x: 0.7, y: 0.7 },
                colors: ['#ffd700'],
                shapes: ['star'],
                scalar: 2
            });
        }, 300);
    }
    fireConfetti();
    </script>
    """, height=0)

# ==================== CUSTOM CSS ====================
st.markdown(f"""
<style>
    /* FONT IMPORT */
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;700&family=Montserrat:wght@300;500;700&family=Dancing+Script:wght@700&family=Marcellus&display=swap');

    /* BACKGROUND */
    .stApp {{
        background: linear-gradient(135deg, #fff5f7 0%, #fff0f5 50%, #fff5f7 100%);
        background-size: 200% 200%;
        animation: gradientBG 15s ease infinite;
    }}

    @keyframes gradientBG {{
        0% {{ background-position: 0% 50%; }}
        50% {{ background-position: 100% 50%; }}
        100% {{ background-position: 0% 50%; }}
    }}

    /* MAIN CARD */
    .princess-card {{
        background: rgba(255, 255, 255, 0.85);
        backdrop-filter: blur(12px);
        -webkit-backdrop-filter: blur(12px);
        border-radius: 30px;
        padding: 60px 40px;
        margin: 40px auto;
        max-width: 95%;
        width: 100%;
        box-shadow: 0 20px 60px rgba(210, 54, 105, 0.2);
        text-align: center;
        position: relative;
        overflow: hidden;
        border: 1px solid rgba(255, 215, 0, 0.5);
    }}

    .princess-card::before {{
        content: "";
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: radial-gradient(circle at 20% 30%, rgba(255, 215, 0, 0.15) 0%, transparent 40%),
                        radial-gradient(circle at 80% 70%, rgba(255, 105, 180, 0.15) 0%, transparent 40%);
        z-index: -1;
    }}

    .princess-card h1 {{
        font-family: 'Marcellus', serif;
        font-size: 5.5rem;
        color: #d23669;
        margin: 20px 0;
        text-shadow: 3px 3px 6px rgba(0,0,0,0.08);
        position: relative;
        display: inline-block;
        letter-spacing: 2px;
    }}

    .princess-card h1::after {{
        content: "";
        position: absolute;
        bottom: -20px;
        left: 50%;
        transform: translateX(-50%);
        width: 150px;
        height: 4px;
        background: linear-gradient(90deg, transparent, #ffd700, transparent);
    }}

    .princess-card h2 {{
        font-family: 'Playfair Display', serif;
        font-size: 2.5rem;
        color: #d23669;
        margin: 15px 0;
        font-weight: 400;
    }}

    .princess-card p {{
        font-family: 'Montserrat', sans-serif;
        font-size: 1.2rem;
        color: #555;
        margin: 10px 0;
        letter-spacing: 0.5px;
    }}

    .degree-badge {{
        display: inline-block;
        background: linear-gradient(135deg, #ff69b4, #d23669);
        color: white;
        padding: 10px 25px;
        border-radius: 50px;
        font-family: 'Montserrat', sans-serif;
        font-weight: 700;
        margin: 15px 0;
        box-shadow: 0 8px 20px rgba(210, 54, 105, 0.3);
        letter-spacing: 1px;
    }}

    /* GALLERY */
    .gallery-title {{
        font-family: 'Dancing Script', cursive;
        color: #d23669;
        text-align: center;
        font-size: 4rem;
        margin: 60px 0 30px;
        position: relative;
    }}

    .gallery-title::before, .gallery-title::after {{
        content: "🌸";
        position: absolute;
        top: 50%;
        transform: translateY(-50%);
        font-size: 1.8rem;
    }}

    .gallery-title::before {{ left: 20%; }}
    .gallery-title::after {{ right: 20%; }}

    /* CSS untuk gambar di galeri Streamlit */
    div[data-testid="stImage"] {{
        transition: transform 0.4s ease, box-shadow 0.4s ease;
        border-radius: 20px;
        border: 2px solid #ffb6c1;
        overflow: hidden;
        height: auto; 
        display: block; 
        margin: 0 auto;
    }}

    div[data-testid="stImage"]:hover {{
        transform: translateY(-10px) scale(1.03);
        box-shadow: 0 25px 50px rgba(255, 105, 180, 0.3);
    }}

    div[data-testid="stImage"] img {{
        transition: transform 0.5s ease;
        width: 100%; 
        height: auto; 
        display: block;
    }}

    div[data-testid="stImage"]:hover img {{
        transform: scale(1.1);
    }}
    
    .image-caption {{
        font-family: 'Dancing Script', cursive; 
        font-size: 1.5rem; 
        color: #d23669; 
        margin-top: 15px;
        padding: 10px 20px;
        text-align: center;
        background: rgba(255, 255, 255, 0.85); /* Latar belakang putih semi-transparan */
        border-radius: 10px;
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
        width: fit-content;
        max-width: 90%;
        margin: 15px auto;
    }}

    /* QUOTE SECTION */
    .quote-box {{
        background: rgba(255, 255, 255, 0.8);
        backdrop-filter: blur(8px);
        -webkit-backdrop-filter: blur(8px);
        border-radius: 20px;
        padding: 50px 40px;
        margin: 60px auto;
        max-width: 700px;
        text-align: center;
        position: relative;
        box-shadow: 0 10px 30px rgba(210, 54, 105, 0.1);
        border: 1px solid rgba(255, 215, 0, 0.2);
    }}

    .quote-box::before {{
        content: "\\"";
        position: absolute;
        top: 20px;
        left: 30px;
        font-family: 'Playfair Display', serif;
        font-size: 5rem;
        color: rgba(210, 54, 105, 0.1);
    }}

    .quote-box::after {{
        content: "\\"";
        position: absolute;
        bottom: 20px;
        right: 30px;
        font-family: 'Playfair Display', serif;
        font-size: 5rem;
        color: rgba(210, 54, 105, 0.1);
        transform: rotate(180deg);
    }}

    .quote-text {{
        font-family: 'Playfair Display', serif;
        font-size: 1.8rem;
        color: #d23669;
        line-height: 1.6;
        margin-bottom: 20px;
        font-style: italic;
        position: relative;
        z-index: 1;
    }}

    .quote-author {{
        font-family: 'Montserrat', sans-serif;
        font-weight: 500;
        color: #ff69b4;
        letter-spacing: 1px;
    }}

    /* music title */
    .music-title {{
        font-family: 'Dancing Script', cursive;
        color: #d23669;
        text-align: center;
        font-size: 3.5rem;
        margin: 60px 0 30px;
        position: relative;
    }}

    .music-title::after {{
        content: "🎶";
        position: absolute;
        top: 50%;
        transform: translateY(-50%);
        font-size: 1.5rem;
    }}

    /* BUTTONS */
    .stButton>button {{
        background: linear-gradient(135deg, #d23669 0%, #ff69b4 100%);
        border: none;
        color: white;
        padding: 16px 45px;
        font-size: 1.1rem;
        font-family: 'Montserrat', sans-serif;
        font-weight: 500;
        border-radius: 50px;
        cursor: pointer;
        box-shadow: 0 10px 25px rgba(210, 54, 105, 0.3);
        transition: all 0.3s ease;
        display: block;
        margin: 50px auto;
        position: relative;
        overflow: hidden;
        letter-spacing: 1px;
    }}

    .stButton>button:hover {{
        transform: translateY(-3px);
        box-shadow: 0 15px 35px rgba(210, 54, 105, 0.4);
    }}

    .stButton>button::before {{
        content: "";
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, transparent, rgba(255,255,255,0.2), transparent);
        transition: 0.5s;
    }}

    .stButton>button:hover::before {{
        left: 100%;
    }}

    /* FOOTER */
    .footer {{
        font-family: 'Montserrat', sans-serif;
        text-align: center;
        color: #d23669;
        margin: 70px 0 30px;
        padding-top: 30px;
        position: relative;
        font-weight: 300;
        letter-spacing: 0.5px;
    }}

    .footer::before {{
        content: "";
        position: absolute;
        top: 0;
        left: 50%;
        transform: translateX(-50%);
        width: 100px;
        height: 3px;
        background: linear-gradient(90deg, transparent, #ffd700, transparent);
    }}

    /* RESPONSIVE ADJUSTMENTS */
    @media (max-width: 768px) {{
        .princess-card h1 {{
            font-size: 9vw;
            line-height: 1.2;
        }}

        .princess-card h2 {{
            font-size: 1.8rem;
        }}

        .gallery-title::before, .gallery-title::after {{
            display: none;
        }}

        .quote-text {{
            font-size: 1.4rem;
        }}
        
        div[data-testid="stHorizontalBlock"] {{
            flex-direction: column;
        }}
        
        div[data-testid="stImage"] {{
            max-width: 90%;
            margin: 20px auto;
        }}
    }}
</style>
""", unsafe_allow_html=True)

# ==================== MAIN CONTENT ====================
def main():
    """Fungsi utama untuk menampilkan konten halaman web."""
    st.balloons()

    # KOTAK UCAPAN
    st.markdown(f"""
    <div class="princess-card">
        <h2>Congratulations Princess</h2>
        <h1>{data['name']}</h1>
        <div class="degree-badge">{data['degree']}</div>
        <h2>For Your Magnificent Achievement</h2>
        <p>👑 {data['faculty']} | {data['university']}</p>
    </div>
    """, unsafe_allow_html=True)

    # KOTAK KUTIPAN
    st.markdown(f"""
    <div class="quote-box">
        <div class="quote-text">{data['quote']}</div>
        <div class="quote-author">~ {data['name']} ~</div>
    </div>
    """, unsafe_allow_html=True)

    # GALERI FOTO
    st.markdown('<div class="gallery-title">Memory Lane 🌸</div>', unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.image(gallery[0]['path'], use_container_width=True)
        st.markdown(f"<div class='image-caption'>{gallery[0]['caption']}</div>", unsafe_allow_html=True)

    with col2:
        st.image(gallery[1]['path'], use_container_width=True)
        st.markdown(f"<div class='image-caption'>{gallery[1]['caption']}</div>", unsafe_allow_html=True)

    with col3:
        st.image(gallery[2]['path'], use_container_width=True)
        st.markdown(f"<div class='image-caption'>{gallery[2]['caption']}</div>", unsafe_allow_html=True)

    # PEMUTAR MUSIK
    st.markdown("""
    <div class="music-player-container">
        <div class="music-title">Celebration Anthem</div>
    </div>
    """, unsafe_allow_html=True)

    with open("img/AboutYou.mp3", "rb") as f:
        audio_bytes = f.read()
    audio_base64 = base64.b64encode(audio_bytes).decode()

    try:
        with open("img/piringan.png", "rb") as f:
            img_bytes = f.read()
            img_base64 = base64.b64encode(img_bytes).decode()
    except FileNotFoundError:
        img_base64 = ""
        st.error("File piringan.png tidak ditemukan.")

    lyrics_timed = [
        (0, "...intro..."),
        (44, "I know a place"),
        (54, "It's somewhere I go when I need to remember your face"),
        (64, "We get married in our heads"),
        (74, "Something to do whilst we try to recall how we met"),
        (84, "Do you think I have forgotten?"),
        (89, "Do you think I have forgotten?"),
        (94, "Do you think I have forgotten about you?"),
        (104, "You and I"),
        (109, "Were alive"),
        (114, "With nothing to do I could lay and just look in your eyes"),
        (124, "Wait and pretend"),
        (134, "Hold on and hope that we'll find our way back in the end"),
        (144, "Do you think I have forgotten?"),
        (149, "Do you think I have forgotten?"),
        (154, "Do you think I have forgotten about you?"),
        (164, "Do you think I have forgotten?"),
        (169, "Do you think I have forgotten?"),
        (174, "Do you think I have forgotten about you?"),
        (184, "There was something about you that now I can't remember"),
        (189, "It's the same damn thing that made my heart surrender"),
        (194, "And I'll miss you on a train"),
        (196, "I'll miss you in the morning"),
        (199, "I never know what to think about, so think about you"),
        (203, "(I think about you)"),
        (209, "About you"),
        (214, "Do you think I have forgotten about you?"),
        (224, "About you"),
        (229, "About you"),
        (234, "Do you think I have forgotten about you?"),
        (250, "...end..."),
    ]
    lyrics_js = json.dumps(lyrics_timed)

    html_code = f"""
    <div style="
        background: rgba(255, 255, 255, 0.7);
        backdrop-filter: blur(5px);
        border-radius: 20px;
        padding: 30px;
        margin: 0 auto;
        max-width: 500px;
        text-align: center;
    ">
        <div id="lyrics" style="
            font-family: 'Playfair Display', serif;
            font-size: 1.3rem;
            color: #ffd700;
            margin: 30px 0;
            min-height: 100px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-style: italic;
            line-height: 1.6;
        "></div>

        <div style="
            display: flex;
            justify-content: center;
            margin: 30px 0;
            position: relative;
        ">
            <div style="
                width: 200px;
                height: 200px;
                position: relative;
            ">
                <img id="cassette" src="data:image/png;base64,{img_base64}" style="
                    width: 100%;
                    height: 100%;
                    object-fit: contain;
                    filter: drop-shadow(0 0 15px rgba(255,215,0,0.3));
                ">
                <div style="
                    position: absolute;
                    top: 0;
                    left: 0;
                    width: 100%;
                    height: 100%;
                    border-radius: 50%;
                    box-shadow: inset 0 0 30px rgba(255,215,0,0.3);
                "></div>
            </div>
        </div>
        
        <button id="playBtn" style="
            background: linear-gradient(135deg, #d23669 0%, #ff69b4 100%);
            color: white;
            border: none;
            padding: 14px 35px;
            font-size: 1rem;
            border-radius: 50px;
            cursor: pointer;
            font-family: 'Montserrat', sans-serif;
            font-weight: 500;
            letter-spacing: 1px;
            transition: all 0.3s ease;
            box-shadow: 0 8px 20px rgba(210, 54, 105, 0.3);
            position: relative;
            overflow: hidden;
        ">
            ▶️ Play Royal Anthem
        </button>
    </div>

    <audio id="player" src="data:audio/mp3;base64,{audio_base64}"></audio>

    <script>
    const lyrics = {lyrics_js};
    const player = document.getElementById('player');
    const lyricsDiv = document.getElementById('lyrics');
    const playBtn = document.getElementById('playBtn');
    const cassette = document.getElementById('cassette');

    let animationId = null;
    let startTime = null;
    let isPlaying = false;

    function animate(now) {{
        if (!startTime) startTime = now;
        const elapsed = (now - startTime) / 1000;
        cassette.style.transform = "rotate(" + (elapsed * 120) + "deg)";
        
        let currentLyric = "";
        for (let i = 0; i < lyrics.length; i++) {{
            if (elapsed >= lyrics[i][0]) {{
                currentLyric = lyrics[i][1];
            }}
        }}
        lyricsDiv.innerHTML = currentLyric;

        if (!player.paused) {{
            animationId = requestAnimationFrame(animate);
        }}
    }}

    playBtn.onclick = () => {{
        if (isPlaying) {{
            player.pause();
            cancelAnimationFrame(animationId);
            playBtn.innerHTML = "▶️ Play Royal Anthem";
            isPlaying = false;
        }} else {{
            player.play();
            startTime = null;
            animationId = requestAnimationFrame(animate);
            playBtn.innerHTML = "⏸️ Pause";
            isPlaying = true;
        }}
    }};

    player.onended = () => {{
        cancelAnimationFrame(animationId);
        cassette.style.transform = "rotate(0deg)";
        lyricsDiv.innerHTML = "";
        playBtn.innerHTML = "▶️ Play Royal Anthem";
        isPlaying = false;
    }};
    </script>
    """

    components.html(html_code, height=500)

    # Pastikan tombol ini di tengah dengan st.columns
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("👑 Click for Royal Celebration!"):
            st.balloons()
            st.markdown("""
            <div style="
                font-family: 'Playfair Display', serif;
                color: #d23669;
                font-size: 1.3rem;
                text-align: center;
                margin: 30px 0;
            ">
                Semoga setiap langkahmu selalu dipenuhi cahaya, karena kamu pantas bersinar lebih dari siapapun! ✨
            </div>
            """, unsafe_allow_html=True)

    
    st.markdown(f"""
    <div class="footer">
        Made with 💖 for Princess {data['name']}'s {data['graduation_year']} Graduation
        -by Mon
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
