import streamlit as st

# ---------- PAGE CONFIG ----------
st.set_page_config(
    page_title="Ti Malice Aux pays Des lettres",
    page_icon="📖",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ---------- CUSTOM CSS FOR BACKGROUND & STYLING ----------
def get_css():
    return """
    <style>
    /* Full page background for login */
    .stApp {
        background: linear-gradient(135deg, #1e3c2c, #2a5a3a);
    }
    .login-bg {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background-image: url('https://raw.githubusercontent.com/Deslandes1/Ti-Malice-Aux-Pays-des-Lettres-built-by-Gesner/main/IMG_2077.JPG');
        background-size: contain;
        background-repeat: no-repeat;
        background-position: center;
        opacity: 0.9;
        z-index: -1;
    }
    .login-container {
        text-align: center;
        background: rgba(0,0,0,0.6);
        padding: 2rem;
        border-radius: 50px;
        max-width: 500px;
        margin: 20% auto;
        backdrop-filter: blur(5px);
    }
    .big-title {
        font-size: 3rem;
        font-weight: bold;
        color: #ffdd99;
        text-shadow: 4px 4px 0 #aa6f20;
        margin-bottom: 1rem;
    }
    .subtitle {
        font-size: 1.2rem;
        color: #ffeecc;
    }
    .page-card {
        background: #fffef7;
        border-radius: 30px;
        padding: 1.5rem;
        margin-bottom: 1rem;
        box-shadow: 0 8px 20px rgba(0,0,0,0.2);
        border-left: 10px solid #ffaa44;
    }
    .letter-header {
        font-size: 4rem;
        font-weight: bold;
        color: #2c5a2e;
        text-align: center;
        margin-bottom: 0;
    }
    .arrow {
        font-size: 2rem;
        text-align: center;
        color: #e67e22;
    }
    .word-list {
        display: flex;
        flex-wrap: wrap;
        justify-content: center;
        gap: 1rem;
        margin: 1rem 0;
        background: #f0f4e8;
        padding: 1rem;
        border-radius: 30px;
    }
    .word {
        background: #ffaa44;
        padding: 0.4rem 1rem;
        border-radius: 40px;
        font-weight: bold;
        font-size: 1.1rem;
        color: #2c2c2c;
    }
    .reading {
        background: #e8f0e0;
        padding: 1rem;
        border-radius: 20px;
        margin-top: 1rem;
        font-style: italic;
    }
    .footer-note {
        text-align: right;
        margin-top: 1rem;
        font-size: 0.9rem;
        color: #777;
        border-top: 1px solid #ccc;
        padding-top: 0.5rem;
    }
    .stTextArea textarea {
        background-color: #fef9e6;
        border-radius: 20px;
        font-family: monospace;
        font-size: 1rem;
    }
    div.stButton > button {
        background-color: #e67e22;
        color: white;
        border: none;
        border-radius: 30px;
        padding: 0.5rem 1.5rem;
        font-weight: bold;
    }
    div.stButton > button:hover {
        background-color: #f39c12;
    }
    </style>
    """

# ---------- DATA FOR 20 LETTERS ----------
lessons = [
    {   # Page 1: A
        "letter": "A",
        "words": ["abite", "ale", "apre", "avèk", "ayiti", "alfabè", "anpil", "atansyon", "ak", "anba"],
        "reading": "Alfa se yon ti gason ki renmen aprann. Li ale lekòl chak jou. Avèk zanmi li yo, li etidye alfabè a. Apre klas, li al jwe. Ayiti se peyi li. Li renmen anpil bèl peyi a."
    },
    {   # Page 2: B
        "letter": "B",
        "words": ["bèl", "bon", "bwè", "boutèy", "bannann", "bagay", "bato", "bouch", "bri", "bwat"],
        "reading": "Bèl bannann nan mache a. Bon gou li genyen. Mwen bwè dlo nan boutèy. Bato a navige sou lanmè. Bouch mwen pa fè bri lè m ap manje."
    },
    {   # Page 3: CH
        "letter": "CH",
        "words": ["chita", "chante", "cheve", "chodyè", "chak", "chen", "chèz", "cho", "chans", "chapo"],
        "reading": "Chita sou chèz la. Chen an ap chante? Non, li pa chante. Manman ap kwit manje nan chodyè. Chak jou, mwen mete chapo mwen. Cheve mwen long."
    },
    {   # Page 4: D
        "letter": "D",
        "words": ["dlo", "diri", "dan", "demen", "dòmi", "dife", "dous", "dwa", "doktè", "drapo"],
        "reading": "Dlo se lavi. Mwen manje diri ak pwa. Dan mwen blan. Demen mwen pral lekòl. Lannwit, mwen ale dòmi. Drapo Ayiti a bèl."
    },
    {   # Page 5: E
        "letter": "E",
        "words": ["ede", "eske", "etidye", "ekri", "eseye", "ede", "ekskize", "egzamen", "epi", "e"],
        "reading": "Mwen ede manman mwen. Èske ou vle etidye avè m? Nou ekri lèt. M ap eseye reponn kesyon an. Ekskize m, mwen dwe ale. Epi apre, nou pral jwe."
    },
    {   # Page 6: È
        "letter": "È",
        "words": ["èd", "èklè", "èkri", "èspwa", "èstime", "èvèk", "èzitasyon", "èlèv", "èdtan", "èlimine"],
        "reading": "Èd se yon bèl bagay. Lè gen èklè nan syèl la, fè atansyon. Nou gen èspwa pou demen. Èlèv yo etidye maten an. Yon èdtan ap pase vit."
    },
    {   # Page 7: F
        "letter": "F",
        "words": ["fè", "fanmi", "fò", "fimen", "fèy", "fwi", "fèm", "fèt", "fich", "frigidè"],
        "reading": "Mwen fè manje pou fanmi mwen. Gason an fò anpil. Pa fimen, se mal pou sante. Fèy bwa tonbe atè. Mwen renmen manje fwi."
    },
    {   # Page 8: G
        "letter": "G",
        "words": ["gade", "gran", "grangou", "gason", "gou", "gen", "gita", "goud", "gwo", "gaz"],
        "reading": "Gade solèy la, li klere. Granmè a te vye. Mwen grangou, mwen vle manje. Ti gason an jwe gita. Li gen yon gwo machin."
    },
    {   # Page 9: H
        "letter": "H",
        "words": ["haiti", "hen", "hotèl", "hewo", "hopital", "hè", "houl", "houm", "hou", "hann"],
        "reading": "Ayiti se peyi mwen. Mwen di 'hen' pou m ap pale. Nou rete nan yon hotèl. Li se yon hewo. Hopital la toupre."
    },
    {   # Page 10: I
        "letter": "I",
        "words": ["ide", "imè", "imajine", "imite", "inan", "infòmasyon", "inivèsite", "interesan", "isit", "itil"],
        "reading": "Mwen gen yon ide. Imè li bon. Imajine w ap vole. Timoun yo imite granmoun. Inivèsite a gwo. Isit la bèl. Sa a itil."
    },
    {   # Page 11: J
        "letter": "J",
        "words": ["jwe", "je", "jaden", "jounen", "jan", "jodi", "jenn", "jistis", "jwèt", "jete"],
        "reading": "Nou jwe boul nan lakou. Je mwen wè yon zwazo. Jaden an plen flè. Jounen an bèl. Jan li pale a komik. Jodi a se yon bèl jou."
    },
    {   # Page 12: K
        "letter": "K",
        "words": ["kay", "kafe", "kisa", "kijan", "kontan", "koute", "kwit", "kounye", "kreyòl", "kè"],
        "reading": "Kay mwen an bèl. Mwen bwè kafe maten. Kisa ou ap fè? Kijan ou ye? Mwen kontan wè ou. Koute mizik. Manman kwit manje."
    },
    {   # Page 13: L
        "letter": "L",
        "words": ["li", "liv", "le", "lè", "lapè", "lalin", "lanmè", "leve", "limyè", "lòt"],
        "reading": "Mwen li yon liv. Le li cho, mwen bwè dlo. Lè solèy kouche, lalin parèt. Lanmè a ble. Leve bonè maten. Limyè klere."
    },
    {   # Page 14: M
        "letter": "M",
        "words": ["manman", "mwen", "mache", "manje", "mèsi", "maten", "mizik", "moun", "montay", "mo"],
        "reading": "Manman mwen renmen m. Mwen mache vit. Manje a bon. Mèsi anpil. Maten an fre. Mizik la dous. Gen anpil moun."
    },
    {   # Page 15: N
        "letter": "N",
        "words": ["nwa", "naj", "nan", "nèf", "non", "nòt", "nasyon", "nivo", "nwit", "nimewo"],
        "reading": "Koulè nwa se fènwa. Mwen naj nan lanmè. Liv la nan tab la. Nèf (9) se yon nimewo. Non mwen se Ti Malice. Nòt mwen yo bon."
    },
    {   # Page 16: NG
        "letter": "NG",
        "words": ["nga", "ngal", "nganga", "ngan", "ngondò", "ngoul", "ngèt", "ngò", "nganbè", "ngaye"],
        "reading": "Nga se yon bèt. Ngal se yon ti mòn. Li fè ngan. Nganbè se yon dans. Nou byen kontan."
    },
    {   # Page 17: O
        "letter": "O",
        "words": ["okenn", "oswa", "oranje", "odyans", "ofrann", "ogmante", "okipasyon", "olojis", "omelette", "opera"],
        "reading": "Mwen pa gen okenn pwoblèm. Ou ka vini oswa ou pa. Koulè oranje bèl. Odyans lan aplodi. Li ofrann yon ti kado."
    },
    {   # Page 18: Ò
        "letter": "Ò",
        "words": ["òkès", "òganize", "òd", "òl", "òmaj", "òmòn", "òp", "òtèy", "òvè", "òj"],
        "reading": "Òkès la jwe mizik. Nou òganize yon fèt. Mete kay la nan lòd. Li bay òmaj a granmoun. Òmòn yo bèl."
    },
    {   # Page 19: OU
        "letter": "OU",
        "words": ["ou", "out", "oulè", "ous", "ouka", "oukoup", "ouragan", "ousi", "ouve", "ouvi"],
        "reading": "Ou se zanmi m. Li out fè sèl. Oulè vann machandiz. Yon gwo ouragan ap vini. Ouve pòt la."
    },
    {   # Page 20: P
        "letter": "P",
        "words": ["pale", "piti", "pè", "pwa", "pye", "pòv", "pou", "papa", "piman", "pase"],
        "reading": "Mwen pale Kreyòl. Ti pitit la jwe. Mwen pè chen an. Pwa se yon manje. Pye bwa a wo. Pòv moun yo bezwen èd."
    }
]

# ---------- SESSION STATE FOR WRITING SECTIONS ----------
if "writing_texts" not in st.session_state:
    st.session_state.writing_texts = ["" for _ in range(20)]

def erase_text(page_idx):
    st.session_state.writing_texts[page_idx] = ""
    st.rerun()

# ---------- LOGIN PAGE ----------
def login_page():
    st.markdown(get_css(), unsafe_allow_html=True)
    st.markdown('<div class="login-bg"></div>', unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        st.markdown('<div class="login-container">', unsafe_allow_html=True)
        st.markdown('<div class="big-title">📖 Ti Malice<br>Aux pays Des lettres</div>', unsafe_allow_html=True)
        st.markdown('<p class="subtitle">Aprann alfabè kreyòl la ak Ti Malice !</p>', unsafe_allow_html=True)
        if st.button("🎈 Antre nan liv la 🎈", use_container_width=True):
            st.session_state.page = "book"
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)

# ---------- BOOK MAIN PAGE ----------
def book_page():
    st.markdown(get_css(), unsafe_allow_html=True)
    st.markdown('<h1 style="text-align:center; color:#ffdd99; text-shadow: 2px 2px 0 #aa6f20;">📘 Ti Malice Aux pays Des lettres</h1>', unsafe_allow_html=True)
    st.markdown('<p style="text-align:center; color:#fff; font-size:1.2rem;">Aprann ekri ak li alfabè kreyòl la, paj pa paj.</p>', unsafe_allow_html=True)
    
    with st.sidebar:
        st.image("https://raw.githubusercontent.com/Deslandes1/Ti-Malice-Aux-Pays-des-Lettres-built-by-Gesner/main/IMG_2077.JPG", use_container_width=True, caption="Ti Malice")
        st.markdown("## 🧭 Chapit yo")
        for i, les in enumerate(lessons):
            st.markdown(f"[Paj {i+1}: Let {les['letter']}](#{les['letter']})")
        st.markdown("---")
        if st.button("🚪 Soti (Exit)"):
            st.session_state.page = "login"
            st.rerun()
    
    for idx, les in enumerate(lessons):
        letter = les["letter"]
        words = les["words"]
        reading = les["reading"]
        
        with st.expander(f"📄 Paj {idx+1}: Let {letter}", expanded=(idx==0)):
            st.markdown(f'<div class="page-card">', unsafe_allow_html=True)
            st.markdown(f'<div class="letter-header">{letter}</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="arrow">↓</div>', unsafe_allow_html=True)
            st.markdown('<div class="word-list">', unsafe_allow_html=True)
            for w in words:
                st.markdown(f'<span class="word">{w}</span>', unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)
            
            st.markdown("### ✍️ Ede w ekri mo sa yo (Practice writing):")
            text_val = st.text_area("Kopye mo yo isit la (Copy the words here):", 
                                     value=st.session_state.writing_texts[idx],
                                     height=150,
                                     key=f"write_{idx}")
            st.session_state.writing_texts[idx] = text_val
            col_a, col_b = st.columns([1,4])
            with col_a:
                if st.button("🗑️ Efase (Erase)", key=f"erase_{idx}"):
                    erase_text(idx)
            
            st.markdown("### 📖 Li ti istwa sa a (Read this story):")
            st.markdown(f'<div class="reading">📖 {reading}</div>', unsafe_allow_html=True)
            st.markdown('<div class="footer-note">Written by Gesner Deslandes</div>', unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)

# ---------- MAIN APP ----------
def main():
    if "page" not in st.session_state:
        st.session_state.page = "login"
    if st.session_state.page == "login":
        login_page()
    else:
        book_page()

if __name__ == "__main__":
    main()
