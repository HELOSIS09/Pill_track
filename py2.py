# import streamlit as st

# # ------------------------------------------------------------------
# # Page config
# # ------------------------------------------------------------------
# st.set_page_config(
#     page_title="TourCraft AI",
#     page_icon="🧭",
#     layout="wide",
#     initial_sidebar_state="collapsed",
# )

# ACCENT = "#6D28D9"
# ACCENT_LIGHT = "#8B5CF6"

# # ------------------------------------------------------------------
# # Global CSS
# # ------------------------------------------------------------------
# st.markdown(
#     f"""
#     <style>
#         .stApp {{ background: #ffffff; }}
#         #MainMenu, footer, header {{visibility: hidden;}}
#         .block-container {{ padding-top: 2.5rem; max-width: 1100px; }}

#         .hero {{
#             text-align: center;
#             padding: 1rem 0 2.5rem 0;
#         }}
#         .hero-title {{
#             font-size: 3.4rem;
#             font-weight: 800;
#             letter-spacing: -1.5px;
#             background: linear-gradient(90deg, {ACCENT} 0%, {ACCENT_LIGHT} 100%);
#             -webkit-background-clip: text;
#             -webkit-text-fill-color: transparent;
#             margin-bottom: 0.3rem;
#         }}
#         .hero-sub {{
#             font-size: 1.2rem;
#             color: #6b6b7b;
#             font-weight: 400;
#         }}

#         .card {{
#             background: #ffffff;
#             border: 1px solid #ece6f7;
#             border-radius: 22px;
#             padding: 2.2rem 2.4rem;
#             box-shadow: 0 10px 34px rgba(109, 40, 217, 0.07);
#             margin-bottom: 1.8rem;
#         }}

#         .section-label {{
#             font-weight: 700;
#             color: {ACCENT};
#             font-size: 0.95rem;
#             text-transform: uppercase;
#             letter-spacing: 0.5px;
#             margin-bottom: 0.5rem;
#         }}

#         div.stButton > button {{
#             background: linear-gradient(90deg, {ACCENT} 0%, {ACCENT_LIGHT} 100%);
#             color: white;
#             font-size: 1.2rem;
#             font-weight: 700;
#             padding: 0.85rem 0;
#             width: 100%;
#             border: none;
#             border-radius: 16px;
#             box-shadow: 0 8px 22px rgba(109, 40, 217, 0.35);
#             transition: transform 0.15s ease;
#         }}
#         div.stButton > button:hover {{
#             transform: translateY(-2px);
#             color: white;
#         }}

#         .itin-header {{
#             text-align: center;
#             font-size: 2.1rem;
#             font-weight: 800;
#             color: #2d1b4e;
#             margin-bottom: 0.2rem;
#         }}
#         .itin-sub {{ text-align: center; color: #8a8a9a; margin-bottom: 2rem; }}

#         .day-title {{
#             font-size: 1.25rem;
#             font-weight: 800;
#             color: {ACCENT};
#             margin-bottom: 0.9rem;
#             border-bottom: 2px solid #ece0fb;
#             padding-bottom: 0.5rem;
#         }}
#         .slot {{
#             padding: 0.55rem 0;
#             font-size: 0.98rem;
#             color: #3a3350;
#         }}
#         .slot b {{ color: {ACCENT}; }}

#         .tag {{
#             display: inline-block;
#             background: #f5eefe;
#             color: {ACCENT};
#             padding: 0.35rem 0.9rem;
#             border-radius: 20px;
#             font-size: 0.88rem;
#             font-weight: 600;
#             margin: 0.25rem 0.3rem 0.25rem 0;
#         }}

#         .budget-row {{
#             display: flex;
#             justify-content: space-between;
#             padding: 0.6rem 0;
#             border-bottom: 1px dashed #e2d6f7;
#             font-size: 1.02rem;
#         }}
#         .budget-row:last-child {{ border-bottom: none; font-weight: 800; color: {ACCENT}; font-size: 1.15rem; }}
#     </style>
#     """,
#     unsafe_allow_html=True,
# )

# # ------------------------------------------------------------------
# # Hero
# # ------------------------------------------------------------------
# st.markdown(
#     """
#     <div class="hero">
#         <div class="hero-title">TourCraft AI</div>
#         <div class="hero-sub">Craft unforgettable journeys with AI</div>
#     </div>
#     """,
#     unsafe_allow_html=True,
# )

# # ------------------------------------------------------------------
# # Search / planning card
# # ------------------------------------------------------------------
# st.markdown('<div class="card">', unsafe_allow_html=True)

# c1, c2 = st.columns([2, 1])
# with c1:
#     st.markdown('<div class="section-label">📍 Destination</div>', unsafe_allow_html=True)
#     destination = st.text_input("Destination", placeholder="Search a destination e.g. Da Nang, Vietnam", label_visibility="collapsed")
# with c2:
#     st.markdown('<div class="section-label">👥 Travelers</div>', unsafe_allow_html=True)
#     travelers = st.selectbox("Travelers", ["1", "2", "3", "4", "5+"], label_visibility="collapsed")

# c3, c4 = st.columns(2)
# with c3:
#     st.markdown('<div class="section-label">📅 Trip Duration (Days)</div>', unsafe_allow_html=True)
#     num_days = st.slider("Duration", 1, 15, 5, label_visibility="collapsed")
# with c4:
#     st.markdown('<div class="section-label">💰 Budget (INR)</div>', unsafe_allow_html=True)
#     budget = st.number_input("Budget", min_value=0, step=1000, value=75000, label_visibility="collapsed")

# st.markdown('<div class="section-label" style="margin-top:0.8rem;">🎒 Travel Style</div>', unsafe_allow_html=True)
# styles = ["Adventure", "Family", "Honeymoon", "Luxury", "Solo", "Friends"]
# style = st.radio("Travel Style", styles, horizontal=True, label_visibility="collapsed")

# st.write("")
# generate = st.button("✨ Generate Complete Itinerary")

# st.markdown("</div>", unsafe_allow_html=True)

# # ------------------------------------------------------------------
# # Dummy itinerary output
# # ------------------------------------------------------------------
# if generate:
#     if not destination.strip():
#         st.warning("Please enter a destination to generate your itinerary.")
#     else:
#         st.markdown(
#             f"""
#             <div class="itin-header">Your {style} Trip to {destination}</div>
#             <div class="itin-sub">{num_days} Days · {travelers} Traveler(s) · Budget ₹{budget:,.0f}</div>
#             """,
#             unsafe_allow_html=True,
#         )

#         # 1. Destination overview
#         st.markdown('<div class="card">', unsafe_allow_html=True)
#         st.markdown('<div class="section-label">🌏 Destination Overview</div>', unsafe_allow_html=True)
#         st.write(
#             f"{destination} is a captivating destination known for its blend of culture, nature, "
#             "and unforgettable experiences. From scenic coastlines to vibrant local markets, this "
#             f"{num_days}-day journey is tailored for {style.lower()} travelers seeking a memorable escape."
#         )
#         st.markdown('<div class="section-label" style="margin-top:1.2rem;">☀️ Best Time to Visit</div>', unsafe_allow_html=True)
#         st.write("March to August offers the most pleasant weather, with clear skies and comfortable temperatures ideal for sightseeing and outdoor activities.")
#         st.markdown("</div>", unsafe_allow_html=True)

#         # 2. Day-wise itinerary (dummy, capped at 5 days display)
#         st.markdown('<div class="card">', unsafe_allow_html=True)
#         st.markdown('<div class="section-label">🗓️ Day-wise Itinerary</div>', unsafe_allow_html=True)
#         dummy_plan = [
#             ("Sunrise viewpoint hike & local breakfast", "City heritage walk & museum visit", "Rooftop dinner with skyline views"),
#             ("Boat cruise along the coastline", "Beach relaxation & water sports", "Street food night market tour"),
#             ("Day trip to nearby countryside villages", "Traditional craft workshop", "Cultural dance show & dinner"),
#             ("Mountain cable car & scenic photography", "Local market shopping", "Rooftop bar & live music"),
#             ("Leisure morning & spa session", "Farewell lunch cruise", "Sunset departure send-off"),
#         ]
#         tabs = st.tabs([f"Day {i+1}" for i in range(min(num_days, 5))])
#         for i, tab in enumerate(tabs):
#             with tab:
#                 morning, afternoon, evening = dummy_plan[i % len(dummy_plan)]
#                 st.markdown(f'<div class="day-title">Day {i+1}</div>', unsafe_allow_html=True)
#                 st.markdown(f'<div class="slot">🌅 <b>Morning:</b> {morning}</div>', unsafe_allow_html=True)
#                 st.markdown(f'<div class="slot">☀️ <b>Afternoon:</b> {afternoon}</div>', unsafe_allow_html=True)
#                 st.markdown(f'<div class="slot">🌆 <b>Evening:</b> {evening}</div>', unsafe_allow_html=True)
#         if num_days > 5:
#             st.caption(f"+ {num_days - 5} more day(s) will be detailed in your full AI-generated itinerary.")
#         st.markdown("</div>", unsafe_allow_html=True)

#         # 3 & 4. Food + Attractions
#         col_a, col_b = st.columns(2)
#         with col_a:
#             st.markdown('<div class="card">', unsafe_allow_html=True)
#             st.markdown('<div class="section-label">🍜 Food Recommendations</div>', unsafe_allow_html=True)
#             for item in ["Local street noodles", "Fresh seafood platters", "Traditional coffee house", "Riverside night market bites"]:
#                 st.markdown(f'<span class="tag">{item}</span>', unsafe_allow_html=True)
#             st.markdown("</div>", unsafe_allow_html=True)
#         with col_b:
#             st.markdown('<div class="card">', unsafe_allow_html=True)
#             st.markdown('<div class="section-label">📸 Must-Visit Attractions</div>', unsafe_allow_html=True)
#             for item in ["Old Town Quarter", "Golden Bridge", "Marble Mountains", "Ancient Temple Complex"]:
#                 st.markdown(f'<span class="tag">{item}</span>', unsafe_allow_html=True)
#             st.markdown("</div>", unsafe_allow_html=True)

#         # 5. Travel tips
#         st.markdown('<div class="card">', unsafe_allow_html=True)
#         st.markdown('<div class="section-label">💡 Travel Tips</div>', unsafe_allow_html=True)
#         tips = [
#             "Carry local currency in small denominations for markets and street vendors.",
#             "Book popular attractions early morning to avoid crowds.",
#             "Keep a translated copy of your hotel address handy.",
#             "Try local transport apps for affordable and quick rides.",
#         ]
#         for t in tips:
#             st.markdown(f"- {t}")
#         st.markdown("</div>", unsafe_allow_html=True)

#         # 6. Budget summary
#         st.markdown('<div class="card">', unsafe_allow_html=True)
#         st.markdown('<div class="section-label">💰 Budget Summary</div>', unsafe_allow_html=True)
#         accommodation = budget * 0.35
#         food = budget * 0.20
#         transport = budget * 0.20
#         activities = budget * 0.15
#         misc = budget - (accommodation + food + transport + activities)
#         rows = [
#             ("Accommodation", accommodation),
#             ("Food & Dining", food),
#             ("Local Transport", transport),
#             ("Activities & Entry Fees", activities),
#             ("Miscellaneous", misc),
#             ("Total Budget", budget),
#         ]
#         for label, val in rows:
#             st.markdown(
#                 f'<div class="budget-row"><span>{label}</span><span>₹ {val:,.0f}</span></div>',
#                 unsafe_allow_html=True,
#             )
#         st.markdown("</div>", unsafe_allow_html=True)

#         st.info("This itinerary uses sample data. AI-powered personalized generation will be added in the next phase.")
#         # py -m streamlit run app.py
        



import streamlit as st

st.set_page_config(page_title="TourCraft AI", page_icon="✦", layout="wide", initial_sidebar_state="collapsed")

ACCENT = "#8B5CF6"
ACCENT_SOFT = "#A78BFA"
BG = "#0E0B12"
CARD = "#17131D"
BORDER = "#2A2433"
TEXT = "#F5F1EA"
MUTED = "#9C93A8"

TRAVEL_STYLES = ["Adventure", "Relaxation", "Family", "Honeymoon", "Luxury", "Backpacking", "Culture", "Food"]
INTERESTS = ["Food", "Nature", "History", "Beaches", "Nightlife", "Shopping", "Architecture", "Adventure"]

DESTINATIONS = [
    {
        "name": "Bali",
        "desc": "Volcanic hillsides, rice terraces and quiet coastal temples.",
        "days": "7-10 days",
        "img": "https://images.unsplash.com/photo-1537996194471-e657df975ab4?w=600&q=80",
    },
    {
        "name": "Vietnam",
        "desc": "Ancient towns, limestone bays and vibrant street food culture.",
        "days": "10-14 days",
        "img": "https://images.unsplash.com/photo-1528127269322-539801943592?w=600&q=80",
    },
    {
        "name": "Japan",
        "desc": "Neon cities, quiet shrines and precise seasonal beauty.",
        "days": "9-12 days",
        "img": "https://images.unsplash.com/photo-1493976040374-85c8e12f0c0e?w=600&q=80",
    },
    {
        "name": "Rajasthan",
        "desc": "Desert forts, royal palaces and a rich living heritage.",
        "days": "6-9 days",
        "img": "https://images.unsplash.com/photo-1477587458883-47145ed94245?w=600&q=80",
    },
]


def inject_css():
    st.markdown(
        f"""
        <style>
        #MainMenu, header, footer {{ visibility: hidden; }}
        .stApp {{ background: radial-gradient(circle at 20% 0%, #1A1424 0%, {BG} 55%); color: {TEXT}; }}
        .block-container {{ max-width: 1180px; padding-top: 1.5rem; padding-bottom: 3rem; }}

        html, body, [class*="css"] {{ font-family: 'Segoe UI', 'Inter', -apple-system, sans-serif; }}

        input, textarea {{
            background-color: #1C1724 !important;
            color: {TEXT} !important;
            border: 1px solid {BORDER} !important;
            border-radius: 12px !important;
        }}
        div[data-baseweb="select"] > div {{
            background-color: #1C1724 !important;
            border: 1px solid {BORDER} !important;
            border-radius: 12px !important;
            color: {TEXT} !important;
        }}
        .stSlider [data-baseweb="slider"] {{ padding-top: 6px; }}

        div.stButton > button {{
            background: linear-gradient(135deg, {ACCENT} 0%, #5B21B6 100%);
            color: #FFFFFF;
            border: none;
            border-radius: 12px;
            padding: 0.65rem 1.3rem;
            font-weight: 600;
            font-size: 0.95rem;
            box-shadow: 0 6px 20px rgba(139,92,246,0.25);
            transition: transform 0.15s ease, box-shadow 0.15s ease;
        }}
        div.stButton > button:hover {{
            transform: translateY(-1px);
            box-shadow: 0 10px 26px rgba(139,92,246,0.4);
            color: #FFFFFF;
        }}

        .navbar {{
            display: flex; justify-content: space-between; align-items: center;
            padding: 0.6rem 0 1.6rem 0; border-bottom: 1px solid {BORDER}; margin-bottom: 2.4rem;
        }}
        .nav-left .brand {{ font-size: 1.25rem; font-weight: 700; letter-spacing: -0.3px; color: {TEXT}; }}
        .nav-left .tagline {{ font-size: 0.78rem; color: {MUTED}; margin-top: -2px; }}
        .nav-right {{ display: flex; align-items: center; gap: 1.8rem; }}
        .nav-link {{ color: {MUTED}; font-size: 0.92rem; font-weight: 500; }}
        .nav-avatar {{
            width: 34px; height: 34px; border-radius: 50%;
            background: linear-gradient(135deg, {ACCENT}, #4C1D95);
            display: flex; align-items: center; justify-content: center;
            color: white; font-size: 0.85rem; font-weight: 700;
        }}

        .hero {{ text-align: center; padding: 1.5rem 0 2.4rem 0; }}
        .hero-label {{
            display: inline-block; color: {ACCENT_SOFT}; font-size: 0.72rem; font-weight: 700;
            letter-spacing: 2px; margin-bottom: 1rem; text-transform: uppercase;
        }}
        .hero-title {{ font-size: 2.9rem; font-weight: 700; letter-spacing: -1.2px; line-height: 1.15; margin-bottom: 0.9rem; }}
        .hero-sub {{ font-size: 1.05rem; color: {MUTED}; max-width: 620px; margin: 0 auto 2rem auto; line-height: 1.6; }}

        .card {{
            background: linear-gradient(180deg, {CARD} 0%, #14101B 100%);
            border: 1px solid {BORDER};
            border-radius: 20px;
            padding: 2.1rem 2.3rem;
            box-shadow: 0 20px 50px rgba(0,0,0,0.35);
            margin-bottom: 2rem;
        }}
        .card-title {{ font-size: 1.3rem; font-weight: 700; margin-bottom: 1.4rem; letter-spacing: -0.3px; }}
        .field-label {{ font-size: 0.78rem; color: {MUTED}; font-weight: 600; letter-spacing: 0.4px; text-transform: uppercase; margin-bottom: 0.4rem; }}

        .section-heading {{ text-align: center; margin: 1rem 0 0.3rem 0; font-size: 1.7rem; font-weight: 700; letter-spacing: -0.5px; }}
        .section-sub {{ text-align: center; color: {MUTED}; margin-bottom: 2rem; font-size: 0.95rem; }}

        .dest-card {{
            border-radius: 18px; overflow: hidden; border: 1px solid {BORDER};
            background: {CARD}; margin-bottom: 1.4rem; box-shadow: 0 12px 28px rgba(0,0,0,0.3);
        }}
        .dest-img {{ width: 100%; height: 150px; object-fit: cover; display: block; background: #1C1724; }}
        .dest-body {{ padding: 1.1rem 1.2rem 1.3rem 1.2rem; }}
        .dest-name {{ font-size: 1.08rem; font-weight: 700; margin-bottom: 0.35rem; }}
        .dest-desc {{ font-size: 0.85rem; color: {MUTED}; line-height: 1.45; margin-bottom: 0.7rem; min-height: 55px; }}
        .dest-days {{ font-size: 0.76rem; color: {ACCENT_SOFT}; font-weight: 600; margin-bottom: 0.8rem; }}

        .summary-card {{
            background: linear-gradient(180deg, #1B1526 0%, {CARD} 100%);
            border: 1px solid {ACCENT}; border-radius: 20px; padding: 2rem 2.3rem; margin-top: 1rem;
        }}
        .summary-title {{ font-size: 1.25rem; font-weight: 700; margin-bottom: 0.3rem; }}
        .summary-note {{ color: {MUTED}; font-size: 0.9rem; margin-bottom: 1.3rem; }}
        .summary-row {{ display: flex; justify-content: space-between; padding: 0.55rem 0; border-bottom: 1px solid {BORDER}; font-size: 0.92rem; }}
        .summary-row:last-child {{ border-bottom: none; }}
        .summary-key {{ color: {MUTED}; }}
        .summary-val {{ color: {TEXT}; font-weight: 600; text-align: right; }}

        .footer {{ text-align: center; padding: 2.4rem 0 0.5rem 0; border-top: 1px solid {BORDER}; margin-top: 2.5rem; }}
        .footer-brand {{ font-weight: 700; font-size: 1rem; margin-bottom: 0.2rem; }}
        .footer-tag {{ color: {MUTED}; font-size: 0.85rem; }}

        div[data-testid="stVerticalBlockBorderWrapper"] {{ border-radius: 16px; }}
        </style>
        """,
        unsafe_allow_html=True,
    )


def render_navbar():
    st.markdown(
        """
        <div class="navbar">
            <div class="nav-left">
                <div class="brand">TourCraft AI</div>
                <div class="tagline">Intelligent Travel Planning</div>
            </div>
            <div class="nav-right">
                <div class="nav-link">Explore</div>
                <div class="nav-link">My Trips</div>
                <div class="nav-link">About</div>
                <div class="nav-avatar">A</div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_hero():
    st.markdown(
        """
        <div class="hero">
            <div class="hero-label">AI-Powered Travel Planning</div>
            <div class="hero-title">Your journey, intelligently crafted.</div>
            <div class="hero-sub">Build detailed, personalized travel experiences in seconds —
            from destination ideas to day-by-day plans.</div>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.text_input("Search", placeholder="⌖  Where do you want to go?", label_visibility="collapsed", key="hero_search")


def render_planner():
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown('<div class="card-title">Tell us about your trip</div>', unsafe_allow_html=True)

    r1c1, r1c2 = st.columns(2)
    with r1c1:
        st.markdown('<div class="field-label">Destination</div>', unsafe_allow_html=True)
        destination = st.text_input("Destination", placeholder="City or country", label_visibility="collapsed")
    with r1c2:
        st.markdown('<div class="field-label">Duration</div>', unsafe_allow_html=True)
        duration = st.slider("Duration", 1, 30, 7, label_visibility="collapsed")

    r2c1, r2c2 = st.columns(2)
    with r2c1:
        st.markdown('<div class="field-label">Travelers</div>', unsafe_allow_html=True)
        travelers = st.selectbox("Travelers", ["1", "2", "3", "4", "5+"], label_visibility="collapsed")
    with r2c2:
        st.markdown('<div class="field-label">Budget (INR)</div>', unsafe_allow_html=True)
        budget = st.number_input("Budget", min_value=0, step=1000, value=80000, label_visibility="collapsed")

    st.markdown('<div class="field-label" style="margin-top:0.6rem;">Travel Style</div>', unsafe_allow_html=True)
    style = st.radio("Travel Style", TRAVEL_STYLES, horizontal=True, label_visibility="collapsed")

    st.markdown('<div class="field-label" style="margin-top:1.2rem;">What are you interested in?</div>', unsafe_allow_html=True)
    interests = st.multiselect("Interests", INTERESTS, label_visibility="collapsed", placeholder="Select all that apply")

    st.write("")
    create = st.button("✦  Create My Journey")
    st.markdown('</div>', unsafe_allow_html=True)

    if create:
        if not destination.strip():
            st.warning("Please enter a destination to continue.")
        else:
            st.markdown(
                f"""
                <div class="summary-card">
                    <div class="summary-title">Your journey is ready to be crafted.</div>
                    <div class="summary-note">Here is what we'll build your plan around.</div>
                    <div class="summary-row"><span class="summary-key">Destination</span><span class="summary-val">{destination}</span></div>
                    <div class="summary-row"><span class="summary-key">Duration</span><span class="summary-val">{duration} days</span></div>
                    <div class="summary-row"><span class="summary-key">Travelers</span><span class="summary-val">{travelers}</span></div>
                    <div class="summary-row"><span class="summary-key">Budget</span><span class="summary-val">₹ {budget:,.0f}</span></div>
                    <div class="summary-row"><span class="summary-key">Travel Style</span><span class="summary-val">{style}</span></div>
                    <div class="summary-row"><span class="summary-key">Interests</span><span class="summary-val">{', '.join(interests) if interests else '—'}</span></div>
                </div>
                """,
                unsafe_allow_html=True,
            )


def render_inspiration():
    st.markdown('<div class="section-heading">Popular journeys</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-sub">Start with an idea and make it yours.</div>', unsafe_allow_html=True)

    cols = st.columns(4)
    for col, dest in zip(cols, DESTINATIONS):
        with col:
            st.markdown(
                f"""
                <div class="dest-card">
                    <img class="dest-img" src="{dest['img']}" onerror="this.style.display='none'" />
                    <div class="dest-body">
                        <div class="dest-name">{dest['name']}</div>
                        <div class="dest-desc">{dest['desc']}</div>
                        <div class="dest-days">{dest['days']}</div>
                    </div>
                </div>
                """,
                unsafe_allow_html=True,
            )
            st.button("Explore", key=f"explore_{dest['name']}")


def render_footer():
    st.markdown(
        """
        <div class="footer">
            <div class="footer-brand">TourCraft AI</div>
            <div class="footer-tag">Plan less. Experience more.</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def main():
    inject_css()
    render_navbar()
    render_hero()
    render_planner()
    render_inspiration()
    render_footer()


if __name__ == "__main__":
    main()