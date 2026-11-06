import streamlit as st

st.set_page_config(
    page_title="Tikrar | Al-Hamdan Tahfeez",
    page_icon="📖",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# -------------------- VISUAL IDENTITY --------------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Amiri:wght@400;700&family=DM+Sans:wght@400;500;600;700&display=swap');

:root {
    --emerald: #123f32;
    --emerald-deep: #0b2d25;
    --emerald-soft: #e7eee8;
    --ivory: #f7f4eb;
    --paper: #fffdf7;
    --gold: #a8894d;
    --ink: #24352e;
    --muted: #758078;
}
.stApp {
    background:
      radial-gradient(ellipse at 50% 0%, rgba(168,137,77,.10), transparent 45%),
      linear-gradient(135deg, #f8f5ed 0%, #f2efe5 100%);
    color: var(--ink);
    font-family: 'DM Sans', sans-serif;
}
header, footer {visibility: hidden;}
.block-container {
    max-width: 720px;
    padding-top: 2rem;
    padding-bottom: 3rem;
}
.hero {
    position: relative;
    overflow: hidden;
    text-align: center;
    padding: 2.4rem 1.2rem 2rem;
    border-radius: 180px 180px 24px 24px;
    color: #f8f4e9;
    background:
      radial-gradient(circle at 50% 15%, rgba(255,255,255,.08), transparent 40%),
      repeating-linear-gradient(45deg, rgba(255,255,255,.018) 0 1px, transparent 1px 16px),
      linear-gradient(145deg, #174b3b, #0b2d25);
    border: 1px solid rgba(168,137,77,.48);
    box-shadow: 0 16px 38px rgba(15,49,39,.12);
    margin-bottom: 1.4rem;
}
.hero:after {
    content: "۞";
    display: block;
    color: rgba(205,179,120,.72);
    font-size: 1.5rem;
    margin-top: .65rem;
}
.arabic {
    font-family: 'Amiri', serif;
    font-size: 2rem;
    color: #e1c995;
    line-height: 1.4;
}
.hero-title {
    font-size: 1.55rem;
    font-weight: 600;
    letter-spacing: .04em;
    margin-top: .25rem;
}
.hero-sub {
    color: #d9dfd6;
    font-size: .83rem;
    letter-spacing: .12em;
    text-transform: uppercase;
    margin-top: .35rem;
}
.motto {
    color: #d8c69c;
    font-family: 'Amiri', serif;
    font-size: 1.05rem;
    margin-top: .65rem;
}
.section-kicker {
    color: var(--gold);
    text-transform: uppercase;
    letter-spacing: .16em;
    font-size: .69rem;
    font-weight: 700;
    margin-bottom: .35rem;
}
h1, h2, h3 { color: var(--emerald) !important; }
.question-card {
    background: rgba(255,253,247,.92);
    border: 1px solid rgba(168,137,77,.28);
    border-radius: 22px;
    padding: 1.35rem 1.35rem 1rem;
    box-shadow: 0 10px 28px rgba(38,51,42,.055);
}
.question-title {
    color: var(--emerald-deep);
    font-size: 1.35rem;
    font-weight: 600;
    line-height: 1.35;
    margin-bottom: .35rem;
}
.helper {
    color: var(--muted);
    font-size: .88rem;
    margin-bottom: .8rem;
}
div[data-testid="stTextInput"] input {
    border: 1px solid #d9d4c5;
    background: #fffefa;
    border-radius: 15px;
    min-height: 3.25rem;
    color: var(--ink);
    font-size: 1rem;
    padding: .65rem 1rem;
}
div[data-testid="stTextInput"] input:focus {
    border-color: var(--gold);
    box-shadow: 0 0 0 2px rgba(168,137,77,.13);
}
div.stButton > button, div[data-testid="stFormSubmitButton"] button {
    background: var(--emerald) !important;
    color: #fffdf7 !important;
    border: 1px solid var(--emerald) !important;
    border-radius: 14px !important;
    min-height: 3rem;
    font-weight: 600;
    width: 100%;
    transition: background .15s ease;
}
div.stButton > button:hover, div[data-testid="stFormSubmitButton"] button:hover {
    background: var(--emerald-deep) !important;
    border-color: var(--gold) !important;
}
.progress-label {
    display: flex;
    justify-content: space-between;
    color: var(--muted);
    font-size: .78rem;
    margin: .2rem .1rem .45rem;
}
div[data-testid="stProgressBar"] > div > div {
    background: var(--gold);
}
div[data-testid="stAlert"] {
    border-radius: 13px;
}
.summary {
    background: var(--paper);
    border: 1px solid rgba(168,137,77,.32);
    border-radius: 20px;
    padding: 1.2rem 1.3rem;
    margin: .7rem 0;
}
.summary-row {
    display: flex;
    justify-content: space-between;
    gap: 1rem;
    border-bottom: 1px solid #eee9dc;
    padding: .68rem 0;
    font-size: .92rem;
}
.summary-row:last-child {border-bottom: 0;}
.summary-label {color: var(--muted);}
.summary-value {color: var(--emerald-deep); font-weight: 600; text-align: right;}
.pillars {
    text-align: center;
    background: #edf1e9;
    border: 1px solid #d8e0d5;
    color: var(--emerald);
    border-radius: 18px;
    padding: 1.1rem .7rem;
    line-height: 2;
    font-weight: 600;
}
.footer {
    text-align: center;
    color: #8a9087;
    font-size: .76rem;
    margin-top: 2rem;
}
@media (max-width: 600px) {
    .block-container {padding: 1rem .85rem 2rem;}
    .hero {padding: 2rem .9rem 1.6rem; border-radius: 140px 140px 20px 20px;}
    .arabic {font-size: 1.7rem;}
    .hero-title {font-size: 1.3rem;}
    .question-card {padding: 1.1rem .95rem .8rem;}
    .question-title {font-size: 1.2rem;}
}
</style>
""", unsafe_allow_html=True)

# -------------------- ORIGINAL PROGRAM FLOW --------------------
# The original input()/print() sequence is represented as one web prompt
# per Streamlit submission. Validation rules and order are preserved.

QUESTIONS = [
    ("name", "FULL NAME", "Enter the student's full name.", "text"),
    ("gender", "GENDER", "Type Male or Female.", "text"),
    ("phone", "STUDENT PHONE NUMBER", "Enter exactly 11 digits.", "text"),
    ("pgname", "PARENT / GUARDIAN NAME", "Enter the parent or guardian's full name.", "text"),
    ("pgphone", "PARENT / GUARDIAN PHONE", "Enter exactly 11 digits.", "text"),
    ("address", "RESIDENTIAL ADDRESS", "Enter the student's residential address.", "text"),
    ("fluent", "CURRENT QUR'AN FLUENCY LEVEL", "Type Beginner, Intermediate or Fluent with Tajwid.", "text"),
    ("quran", "PREVIOUS QUR'AN MEMORISATION", "Have you participated in a Qur'anic memorisation programme? Type Yes or No.", "text"),
    ("choose", "PREFERRED MEMORISATION METHOD", "Type 1, 2, 3 or 4.", "text"),
    ("schedule", "PREFERRED PROGRAMME SCHEDULE", "Type Morning or Afternoon.", "text"),
]

if "step" not in st.session_state:
    st.session_state.step = 0
if "answers" not in st.session_state:
    st.session_state.answers = {}
if "error" not in st.session_state:
    st.session_state.error = ""

def validate_answer(key, raw):
    """Keep the original conditions while returning browser-friendly errors."""
    value = raw.strip()

    if key == "name":
        return (bool(value), value, "Please enter the student's full name.")
    elif key == "gender":
        if value.lower() in ("male", "female"):
            return True, value.lower(), ""
        return False, None, "INVALID INPUT. Please type Male or Female."
    elif key in ("phone", "pgphone"):
        if value.isdigit() and len(value) == 11:
            return True, value, ""
        return False, None, "MUST CONTAIN EXACTLY 11 DIGITS. TRY AGAIN."
    elif key == "pgname":
        return (bool(value), value, "Please enter the parent or guardian's name.")
    elif key == "address":
        return (bool(value), value, "Please enter the residential address.")
    elif key == "fluent":
        if value.lower() in ("beginner", "intermediate", "fluent with tajwid"):
            return True, value.lower(), ""
        return False, None, "INVALID INPUT. Choose Beginner, Intermediate or Fluent with Tajwid."
    elif key == "quran":
        if value.lower() in ("yes", "no"):
            return True, value.lower(), ""
        return False, None, "INVALID INPUT. Please type Yes or No."
    elif key == "choose":
        try:
            choice = int(value)
        except ValueError:
            return False, None, "INVALID INPUT. Enter a number from 1 to 4."
        if choice in (1, 2, 3, 4):
            return True, choice, ""
        return False, None, "INVALID INPUT. Choose 1, 2, 3 or 4."
    elif key == "schedule":
        if value.lower() in ("morning", "afternoon"):
            return True, value.lower(), ""
        return False, None, "INVALID INPUT. Type Morning or Afternoon."
    return False, None, "Something went wrong. Please try again."

def display_value(key, value):
    if key in ("name", "pgname", "address"):
        return str(value).upper()
    if key in ("gender", "fluent", "quran", "schedule"):
        return str(value).upper()
    if key == "choose":
        labels = {
            1: "1/5 PAGE DAILY",
            2: "2 PAGES DAILY",
            3: "3 PAGES DAILY",
            4: "4 PAGES DAILY",
        }
        return labels.get(value, str(value))
    return str(value)

# -------------------- HEADER --------------------
st.markdown("""
<div class="hero">
  <div class="arabic" dir="rtl">أكاديمية الحمدان</div>
  <div class="hero-title">TIKRAR SYSTEM</div>
  <div class="hero-sub">Qur'an Memorisation Programme Registration</div>
  <div class="motto">Nurturing hearts through Qur'an</div>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="section-kicker">Student registration</div>', unsafe_allow_html=True)

if st.session_state.step < len(QUESTIONS):
    step = st.session_state.step
    key, title, helper, _ = QUESTIONS[step]
    total = len(QUESTIONS)

    st.markdown(
        f'<div class="progress-label"><span>REGISTRATION</span><span>{step + 1} OF {total}</span></div>',
        unsafe_allow_html=True
    )
    st.progress((step + 1) / total)

    st.markdown('<div class="question-card">', unsafe_allow_html=True)
    st.markdown(f'<div class="question-title">{title}</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="helper">{helper}</div>', unsafe_allow_html=True)

    with st.form(key=f"form_{key}", clear_on_submit=False):
        answer = st.text_input(
            "Your answer",
            key=f"input_{key}",
            label_visibility="collapsed",
            placeholder="Type your answer here..."
        )
        submitted = st.form_submit_button("Continue  →", use_container_width=True)

    st.markdown('</div>', unsafe_allow_html=True)

    if st.session_state.error:
        st.error(st.session_state.error)

    if submitted:
        valid, cleaned, message = validate_answer(key, answer)
        if valid:
            st.session_state.answers[key] = cleaned
            st.session_state.error = ""
            st.session_state.step += 1
            st.rerun()
        else:
            st.session_state.error = message
            st.rerun()

    if step > 0:
        if st.button("← Previous question", use_container_width=True):
            st.session_state.step -= 1
            st.session_state.error = ""
            st.rerun()

else:
    a = st.session_state.answers
    st.markdown("### Student information")
    rows = [
        ("FULL NAME", display_value("name", a["name"])),
        ("GENDER", display_value("gender", a["gender"])),
        ("PHONE", a["phone"]),
        ("PARENT / GUARDIAN NAME", display_value("pgname", a["pgname"])),
        ("PARENT / GUARDIAN PHONE", a["pgphone"]),
        ("RESIDENTIAL ADDRESS", display_value("address", a["address"])),
        ("QUR'AN FLUENCY", display_value("fluent", a["fluent"])),
        ("PREVIOUS MEMORISATION PROGRAMME", display_value("quran", a["quran"])),
        ("MEMORISATION METHOD", display_value("choose", a["choose"])),
        ("PREFERRED SCHEDULE", display_value("schedule", a["schedule"])),
    ]
    html_rows = "".join(
        f'<div class="summary-row"><span class="summary-label">{label}</span>'
        f'<span class="summary-value">{value}</span></div>'
        for label, value in rows
    )
    st.markdown(f'<div class="summary">{html_rows}</div>', unsafe_allow_html=True)

    st.markdown("### Our programme pillars")
    st.markdown("""
    <div class="pillars">
      • TIKRAR &nbsp; · &nbsp; • CONNECTION &nbsp; · &nbsp; • REVISION<br>
      <span style="font-family:Amiri,serif;font-size:1.35rem;color:#a8894d;" dir="rtl">تكرار أساس الحفظ</span>
    </div>
    """, unsafe_allow_html=True)
    st.success("Registration details reviewed. This is a local session preview; no information has been saved to a database or sent to the academy.")

    col1, col2 = st.columns(2)
    with col1:
        if st.button("← Edit answers", use_container_width=True):
            st.session_state.step = 0
            st.session_state.error = ""
            st.rerun()
    with col2:
        if st.button("Start a new registration", use_container_width=True):
            st.session_state.step = 0
            st.session_state.answers = {}
            st.session_state.error = ""
            st.rerun()

st.markdown('<div class="footer">أكاديمية الحمدان · TIKRAR SYSTEM<br>Built for consistency, connection and revision.</div>', unsafe_allow_html=True)
