import streamlit as st

# Set Streamlit page configuration to full width
st.set_page_config(
    page_title="HMZ | Portfolio",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Render complete HTML/CSS/JS web application inside Streamlit
st.components.v1.html(
    """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Muhammad Zaki | Portfolio</title>
  <!-- Google Fonts -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400;600;700&family=Outfit:wght@400;600;800;900&family=Press+Start+2P&family=Space+Grotesk:wght@400;700&display=swap" rel="stylesheet">
  <!-- FontAwesome Icons -->
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
  
  <style>
    /* CSS RESET & VARIABLES */
    * {
      margin: 0;
      padding: 0;
      box-sizing: border-box;
    }
    
    :root {
      --bg-black: #0B0B0C;
      --text-white: #FFFFFF;
      --lime-green: #C6F432;
      --pk-green: #01411C;
      --pos-green: #2ECC71;
      --neg-red: #E74C3C;
      --font-header: 'Outfit', sans-serif;
      --font-sub: 'Space Grotesk', sans-serif;
      --font-body: 'Montserrat', sans-serif;
      --font-pixel: 'Press Start 2P', monospace;
    }

    html, body {
      background-color: var(--bg-black);
      color: var(--text-white);
      font-family: var(--font-body);
      overflow-x: hidden;
      scroll-behavior: smooth;
    }

    /* SMOOTH PAGE ENTRY FADE-IN */
    body {
      opacity: 0;
      animation: pageFadeIn 1.5s ease-out forwards;
    }
    @keyframes pageFadeIn {
      to { opacity: 1; }
    }

    /* BACKGROUND GLOW AT LOWER CENTER */
    .bg-glow {
      position: fixed;
      bottom: -150px;
      left: 50%;
      transform: translateX(-50%);
      width: 600px;
      height: 400px;
      background: radial-gradient(circle, rgba(198, 244, 50, 0.45) 0%, rgba(198, 244, 50, 0.15) 45%, rgba(11, 11, 12, 0) 80%);
      filter: blur(60px);
      pointer-events: none;
      z-index: 1;
      transition: opacity 0.8s ease, filter 0.8s ease;
    }

    /* PAKISTANI FLAG OVERLAY */
    .flag-overlay {
      position: fixed;
      inset: 0;
      background: linear-gradient(90deg, #ffffff 25%, #01411C 25%);
      opacity: 0;
      pointer-events: none;
      z-index: 2;
      transition: opacity 1s ease-in-out;
    }
    .flag-overlay.active {
      opacity: 0.18;
    }

    /* MAIN CONTAINER */
    .container {
      position: relative;
      z-index: 5;
      max-width: 1200px;
      margin: 0 auto;
      padding: 0 20px;
    }

    /* SECTION 1: HERO OVERLAY ("Who is HMZ?") */
    .hero-section {
      height: 100vh;
      display: flex;
      flex-direction: column;
      justify-content: center;
      align-items: center;
      text-align: center;
      position: relative;
    }
    .who-is-wrapper {
      position: sticky;
      top: 40vh;
      transition: opacity 0.6s ease-out, transform 0.6s ease-out;
    }
    .who-is-title {
      font-family: var(--font-header);
      font-size: 1.5rem;
      transform: scale(0.1);
      opacity: 0;
      letter-spacing: 2px;
      animation: expandText 2s cubic-bezier(0.25, 1, 0.5, 1) forwards 0.5s;
    }
    .who-is-title span.hmz {
      font-family: var(--font-pixel);
      color: var(--lime-green);
      font-size: 1.2em;
    }
    .cursor-anim {
      display: inline-block;
      width: 12px;
      height: 35px;
      background-color: var(--lime-green);
      margin-left: 8px;
      animation: blink 0.8s infinite alternate;
    }

    @keyframes expandText {
      0% { transform: scale(0.05); opacity: 0; }
      70% { opacity: 1; }
      100% { transform: scale(2.8); opacity: 1; }
    }
    @keyframes blink {
      0% { opacity: 1; }
      100% { opacity: 0; }
    }

    /* SECTION 2: MUHAMMAD ZAKI & PORTRAIT */
    .profile-section {
      min-height: 120vh;
      display: flex;
      align-items: center;
      position: relative;
      padding: 100px 0;
    }
    .profile-content {
      width: 55%;
      z-index: 10;
    }

    /* CHARGING GLOW ANIMATION FOR NAME */
    .zaki-name {
      font-family: var(--font-header);
      font-weight: 900;
      font-size: 4.8rem;
      text-transform: uppercase;
      letter-spacing: 4px;
      transform: scaleX(1.15);
      transform-origin: left;
      line-height: 1;
      margin-bottom: 30px;
      position: relative;
      color: #333;
      transition: color 0.3s ease, text-shadow 0.3s ease;
    }
    .zaki-name.charged {
      color: var(--text-white);
      text-shadow: 0 0 20px rgba(198, 244, 50, 0.8), 0 0 40px rgba(198, 244, 50, 0.4);
      animation: dischargeFlash 0.6s ease-out forwards;
    }

    @keyframes dischargeFlash {
      0% { text-shadow: 0 0 60px #C6F432, 0 0 100px #C6F432; color: #fff; }
      50% { text-shadow: 0 0 30px #C6F432; }
      100% { text-shadow: 0 0 10px rgba(198, 244, 50, 0.4); color: #fff; }
    }

    /* PORTRAIT CONTAINER & CINEMATIC LIGHTING */
    .portrait-wrapper {
      position: absolute;
      right: 0;
      top: 50%;
      transform: translateY(-50%);
      width: 45%;
      height: 80vh;
      opacity: 0;
      transition: opacity 1s ease, transform 1s ease;
      pointer-events: none;
      z-index: 4;
      display: flex;
      justify-content: flex-end;
      align-items: center;
    }
    .portrait-wrapper.visible {
      opacity: 1;
    }
    .portrait-img {
      max-height: 100%;
      max-width: 100%;
      object-fit: contain;
      filter: grayscale(100%) contrast(120%);
      mask-image: linear-gradient(to bottom, black 50%, transparent 95%), linear-gradient(to left, black 70%, transparent 100%);
      -webkit-mask-image: linear-gradient(to bottom, black 50%, transparent 95%);
    }
    /* Lime green side light hitting face from outer right */
    .portrait-wrapper::after {
      content: '';
      position: absolute;
      top: 15%;
      right: -20px;
      width: 250px;
      height: 350px;
      background: radial-gradient(ellipse at right, rgba(198, 244, 50, 0.65) 0%, rgba(198, 244, 50, 0.2) 50%, transparent 80%);
      mix-blend-mode: color-dodge;
      pointer-events: none;
    }

    /* TYPEWRITER BIO DETAILS */
    .bio-box {
      font-family: var(--font-sub);
      font-size: 1.15rem;
      line-height: 1.8;
      margin-top: 20px;
    }
    .bio-line {
      opacity: 0;
      transform: translateY(15px);
      transition: opacity 0.6s ease, transform 0.6s ease;
      margin-bottom: 12px;
    }
    .bio-line.show {
      opacity: 1;
      transform: translateY(0);
    }
    .lbl {
      color: var(--lime-green);
      font-weight: 700;
      font-family: var(--font-header);
    }
    .pk-text {
      color: var(--pk-green);
      font-weight: 800;
      text-shadow: 0 0 8px rgba(1, 65, 28, 0.8);
      background: rgba(255, 255, 255, 0.9);
      padding: 2px 6px;
      border-radius: 4px;
    }

    /* SECTION 3: 3D FLIP CARDS */
    .cards-section {
      padding: 120px 0;
      min-height: 100vh;
      display: flex;
      flex-direction: column;
      justify-content: center;
    }
    .cards-grid {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 35px;
      margin-top: 40px;
    }
    .flip-card {
      background-color: transparent;
      height: 340px;
      perspective: 1000px;
      cursor: pointer;
    }
    .flip-card-inner {
      position: relative;
      width: 100%;
      height: 100%;
      text-align: left;
      transition: transform 0.8s cubic-bezier(0.175, 0.885, 0.32, 1.275);
      transform-style: preserve-3d;
      border-radius: 16px;
    }
    .flip-card:hover .flip-card-inner {
      transform: rotateY(180deg) translateY(-8px);
    }
    .flip-card-front, .flip-card-back {
      position: absolute;
      width: 100%;
      height: 100%;
      -webkit-backface-visibility: hidden;
      backface-visibility: hidden;
      border-radius: 16px;
      padding: 35px;
      display: flex;
      flex-direction: column;
      justify-content: center;
    }
    /* Front Card Style */
    .flip-card-front {
      background: #141416;
      border: 2px solid rgba(198, 244, 50, 0.2);
      box-shadow: 0 10px 30px rgba(0,0,0,0.5);
      transition: border-color 0.4s ease, box-shadow 0.4s ease;
    }
    .flip-card:hover .flip-card-front,
    .flip-card:hover .flip-card-inner {
      box-shadow: 0 0 25px rgba(198, 244, 50, 0.5);
    }
    .card-front-title {
      font-family: var(--font-header);
      font-size: 1.8rem;
      color: var(--lime-green);
      display: flex;
      align-items: center;
      gap: 15px;
    }
    .card-hint {
      margin-top: 15px;
      font-size: 0.85rem;
      color: #888;
      text-transform: uppercase;
      letter-spacing: 1.5px;
    }

    /* Back Card Style (White background with black text) */
    .flip-card-back {
      background-color: #FFFFFF;
      color: #0B0B0C;
      transform: rotateY(180deg);
      border: 2px solid var(--lime-green);
      font-family: var(--font-body);
      font-size: 0.95rem;
      line-height: 1.6;
    }

    /* HIGHLIGHT WORD STYLING */
    .good-word {
      color: var(--pos-green) !important;
      font-weight: 700;
    }
    .bad-word {
      color: var(--neg-red) !important;
      font-weight: 700;
    }

    /* SECTION 4: CONTACT & OUTRO */
    .contact-section {
      padding: 120px 0 80px 0;
      min-height: 100vh;
      text-align: center;
      display: flex;
      flex-direction: column;
      justify-content: center;
      align-items: center;
    }
    .scramble-header {
      font-family: var(--font-header);
      font-size: 2.8rem;
      margin-bottom: 50px;
      min-height: 70px;
      letter-spacing: 1px;
    }

    .boxes-wrapper {
      display: flex;
      gap: 40px;
      justify-content: center;
      width: 100%;
      max-width: 850px;
      margin-bottom: 60px;
    }
    .contact-box {
      flex: 1;
      background: #141416;
      border-radius: 20px;
      padding: 35px 25px;
      position: relative;
      text-decoration: none;
      color: var(--text-white);
      border: 2px solid #222;
      transition: transform 0.4s ease, border-color 0.4s ease, box-shadow 0.4s ease;
      text-align: left;
      display: block;
    }
    .contact-box:hover {
      transform: translateY(-10px);
      border-color: var(--lime-green);
      box-shadow: 0 0 30px rgba(198, 244, 50, 0.4);
    }
    .box-icon {
      position: absolute;
      top: 25px;
      left: 25px;
      font-size: 2rem;
    }
    .box-icon.wa { color: #25D366; }
    .box-icon.insta {
      background: -webkit-linear-gradient(45deg, #f09433 0%, #e6683c 25%, #dc2743 50%, #cc2366 75%, #bc1888 100%);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
    }
    .box-content {
      margin-top: 45px;
    }
    .box-heading {
      font-family: var(--font-header);
      font-size: 1.4rem;
      margin-bottom: 8px;
    }
    .box-sub {
      color: #aaa;
      font-size: 0.95rem;
      margin-bottom: 12px;
    }
    .box-detail {
      font-family: var(--font-sub);
      color: var(--lime-green);
      font-weight: 700;
      font-size: 1.1rem;
    }

    /* OUTRO TEXT LINES */
    .outro-container {
      margin-top: 20px;
      line-height: 2;
    }
    .outro-line-1 { font-size: 1.1rem; color: #888; font-style: italic; }
    .outro-line-2 { font-size: 1.2rem; color: #ccc; }
    .outro-line-3 { font-size: 1.3rem; color: var(--lime-green); font-weight: 600; }
    .outro-line-4 { font-size: 1.6rem; font-family: var(--font-header); font-weight: 800; margin-top: 10px; }

    /* RESPONSIVE DESIGN */
    @media (max-width: 900px) {
      .cards-grid, .boxes-wrapper { grid-template-columns: 1fr; flex-direction: column; }
      .profile-content { width: 100%; }
      .portrait-wrapper { width: 100%; opacity: 0.2 !important; }
      .zaki-name { font-size: 3rem; }
      .who-is-title { font-size: 1rem; }
    }
  </style>
</head>
<body>

  <!-- BACKGROUND GLOW & FLAG OVERLAY -->
  <div class="bg-glow" id="bgGlow"></div>
  <div class="flag-overlay" id="flagOverlay"></div>

  <div class="container">
    
    <!-- SECTION 1: HERO OVERLAY -->
    <section class="hero-section">
      <div class="who-is-wrapper" id="whoIsWrapper">
        <h1 class="who-is-title">Who is <span class="hmz">HMZ?</span><span class="cursor-anim"></span></h1>
      </div>
    </section>

    <!-- SECTION 2: PROFILE & BIO -->
    <section class="profile-section" id="profileSection">
      <!-- PORTRAIT IMAGE CUTOUT -->
      <div class="portrait-wrapper" id="portraitWrapper">
        <!-- SVG CUTOUT PLACEHOLDER IN BLACK & WHITE WITH LIGHTING EFFECT -->
        <svg class="portrait-img" viewBox="0 0 400 600" width="380" height="570" xmlns="http://www.w3.org/2000/svg">
          <defs>
            <filter id="bw">
              <feColorMatrix type="matrix" values="0.33 0.33 0.33 0 0  0.33 0.33 0.33 0 0  0.33 0.33 0.33 0 0  0 0 0 1 0"/>
            </filter>
          </defs>
          <g filter="url(#bw)">
            <!-- Head & Hair Silhouette -->
            <path d="M 170 120 Q 200 70 250 110 Q 290 140 270 200 Q 260 250 220 270 Q 170 280 150 220 Q 140 160 170 120 Z" fill="#2a2a2c"/>
            <path d="M 180 85 Q 240 70 270 115 Q 240 100 210 110 Z" fill="#111"/>
            <!-- Face & Neck Cutout -->
            <path d="M 180 140 Q 240 150 255 200 Q 230 255 190 245 Q 165 210 180 140 Z" fill="#666"/>
            <!-- Beard / Facial Outline -->
            <path d="M 185 200 Q 240 210 245 240 Q 210 260 185 240 Z" fill="#1c1c1e"/>
            <!-- Coat & Torso (Chest part) -->
            <path d="M 100 320 Q 200 270 310 320 L 350 600 L 60 600 Z" fill="#18181a"/>
            <path d="M 160 290 L 200 450 L 240 290 Z" fill="#0d0d0e"/>
            <path d="M 190 280 L 210 350 L 190 400 Z" fill="#3a3a3c"/>
          </g>
        </svg>
      </div>

      <div class="profile-content">
        <h2 class="zaki-name" id="zakiName">Muhammad Zaki</h2>
        
        <div class="bio-box">
          <div class="bio-line" id="line1"><span class="lbl">Age:</span> 21 years</div>
          <div class="bio-line" id="line2"><span class="lbl">Origin:</span> <span class="pk-text">Pakistan</span></div>
          <div class="bio-line" id="line3"><span class="lbl">Does:</span> Vibe-coded web development<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Photography, Editing</div>
          <div class="bio-line" id="line4"><span class="lbl">Skills:</span> "Good Listener, Cooking, Emotional support<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;(Support for you while making payments),<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Mechanic, Electrician, Plumber, Grocery<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;buyer, Half Doctor....... And the list goes on."</div>
        </div>
      </div>
    </section>

    <!-- SECTION 3: 3D FLIP FLASH CARDS -->
    <section class="cards-section">
      <div class="cards-grid">
        
        <!-- CARD 1: PREMIUM COST -->
        <div class="flip-card">
          <div class="flip-card-inner">
            <div class="flip-card-front">
              <div class="card-front-title">
                <i class="fa-solid fa-crown"></i>
                <span>Premium cost web-development</span>
              </div>
              <div class="card-hint">Hover to flip card <i class="fa-solid fa-rotate"></i></div>
            </div>
            <div class="flip-card-back">
              <p>
                Premium costed website development includes custom bought domains, bought hosted platforms and premium methods, used to develop sites, so that it should be <span class="good-word">highly accessible</span>, with <span class="good-word">high performance score</span> and user experience, disabling sleeping of the website, which <span class="bad-word">ruins</span> the user experience.
              </p>
            </div>
          </div>
        </div>

        <!-- CARD 2: LOW COST -->
        <div class="flip-card">
          <div class="flip-card-inner">
            <div class="flip-card-front">
              <div class="card-front-title">
                <i class="fa-solid fa-bolt"></i>
                <span>Low cost web-development</span>
              </div>
              <div class="card-hint">Hover to flip card <i class="fa-solid fa-rotate"></i></div>
            </div>
            <div class="flip-card-back">
              <p>
                Low costed website development includes free domains issued by the hosting platform, hosted for free under the free tier of hosting platforms. Good for starting businesses and highly <span class="good-word">budget friendly</span>.<br><br>
                <span class="bad-word">Cons</span> are:<br>
                Website sleeps after some time of inactivity.<br>
                <span class="bad-word">Cannot handle</span> high users traffic at a single time.
              </p>
            </div>
          </div>
        </div>

      </div>
    </section>

    <!-- SECTION 4: CONTACT & FINAL OUTRO -->
    <section class="contact-section">
      <h2 class="scramble-header" id="scrambleHeader">Wanna get in touch with me?</h2>

      <div class="boxes-wrapper">
        <!-- WHATSAPP BOX -->
        <a href="https://wa.me/923144012872" target="_blank" class="contact-box">
          <i class="fa-brands fa-whatsapp box-icon wa"></i>
          <div class="box-content">
            <div class="box-heading">Got WhatsApp?</div>
            <div class="box-sub">Reach out on WA</div>
            <div class="box-detail">0314-4012872</div>
          </div>
        </a>

        <!-- INSTAGRAM BOX -->
        <a href="https://instagram.com/hmzaki._.rj" target="_blank" class="contact-box">
          <i class="fa-brands fa-instagram box-icon insta"></i>
          <div class="box-content">
            <div class="box-heading">Got Instagram?</div>
            <div class="box-sub">Reach out on Insta</div>
            <div class="box-detail">hmzaki._.rj</div>
          </div>
        </a>
      </div>

      <!-- OUTRO TEXT LINES -->
      <div class="outro-container">
        <p class="outro-line-1">Nervous to talk to me?</p>
        <p class="outro-line-2">"Take the first step, as you did for her"</p>
        <p class="outro-line-3">"Trust me, I'm friendly"</p>
        <p class="outro-line-4">"Get your ideas converted into your dream-web"</p>
      </div>
    </section>

  </div>

  <!-- INTERACTIVE SCROLL & ANIMATION SCRIPT -->
  <script>
    const whoIsWrapper = document.getElementById('whoIsWrapper');
    const zakiName = document.getElementById('zakiName');
    const portraitWrapper = document.getElementById('portraitWrapper');
    const flagOverlay = document.getElementById('flagOverlay');
    const bgGlow = document.getElementById('bgGlow');
    const scrambleHeader = document.getElementById('scrambleHeader');
    
    const lines = [
      document.getElementById('line1'),
      document.getElementById('line2'),
      document.getElementById('line3'),
      document.getElementById('line4')
    ];

    let flagTriggered = false;

    // SCRAMBLE TEXT EFFECT
    const targetText = "Wanna get in touch with me?";
    const chars = "!@#$%^&*()_+-=AXBYCZ123456789";
    let scrambleInterval = null;

    function runScramble() {
      let iteration = 0;
      clearInterval(scrambleInterval);
      scrambleInterval = setInterval(() => {
        scrambleHeader.innerText = targetText.split("")
          .map((letter, index) => {
            if(index < iteration) return targetText[index];
            return chars[Math.floor(Math.random() * chars.length)];
          }).join("");

        if(iteration >= targetText.length) {
          clearInterval(scrambleInterval);
        }
        iteration += 1 / 2;
      }, 30);
    }

    // MAIN SCROLL HANDLER (BIDIRECTIONAL)
    window.addEventListener('scroll', () => {
      const scrollY = window.scrollY;
      const windowHeight = window.innerHeight;

      // 1. "Who is HMZ?" Fade Away on Scroll
      const heroFadeThreshold = windowHeight * 0.5;
      if (scrollY < heroFadeThreshold) {
        whoIsWrapper.style.opacity = 1 - (scrollY / heroFadeThreshold);
        whoIsWrapper.style.transform = `translateY(-${scrollY * 0.4}px)`;
      } else {
        whoIsWrapper.style.opacity = 0;
      }

      // 2. "Muhammad Zaki" Discharge & Portrait Fade-In
      const profileSection = document.getElementById('profileSection');
      const profileRect = profileSection.getBoundingClientRect();

      if (profileRect.top < windowHeight * 0.75 && profileRect.bottom > 0) {
        zakiName.classList.add('charged');
        portraitWrapper.classList.add('visible');
      } else {
        zakiName.classList.remove('charged');
        portraitWrapper.classList.remove('visible');
      }

      // 3. Typewriter Line Reveal & Pakistan Flag Pulse
      lines.forEach((line, idx) => {
        if (profileRect.top < windowHeight * (0.6 - idx * 0.1)) {
          line.classList.add('show');
          
          // Trigger Pakistani Flag on line 2 ("Pakistan")
          if (idx === 1 && !flagTriggered) {
            flagTriggered = true;
            flagOverlay.classList.add('active');
            setTimeout(() => {
              flagOverlay.classList.remove('active');
            }, 5000);
          }
        } else {
          line.classList.remove('show');
          if (idx === 1) flagTriggered = false;
        }
      });

      // 4. Background Glow Darkening near Contact Section
      const totalDocHeight = document.documentElement.scrollHeight - windowHeight;
      const scrollPercent = scrollY / totalDocHeight;
      
      if (scrollPercent > 0.6) {
        bgGlow.style.opacity = Math.max(0.2, 1 - (scrollPercent - 0.6) * 2);
        bgGlow.style.filter = "blur(100px)";
      } else {
        bgGlow.style.opacity = 1;
        bgGlow.style.filter = "blur(60px)";
      }

      // 5. Scramble Text Header Animation on Scroll into view
      const contactSection = document.querySelector('.contact-section');
      const contactRect = contactSection.getBoundingClientRect();

      if (contactRect.top < windowHeight * 0.8 && !scrambleHeader.dataset.scrambled) {
        scrambleHeader.dataset.scrambled = "true";
        runScramble();
      } else if (contactRect.top >= windowHeight * 0.8) {
        scrambleHeader.dataset.scrambled = "";
      }
    });
  </script>
</body>
</html>
    """,
    height=3200,
    scrolling=True
)
