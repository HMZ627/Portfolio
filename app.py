import streamlit as st
import streamlit.components.v1 as components

# Set full layout page config for Streamlit
st.set_page_config(
    page_title="HMZ — Portfolio",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Hide default Streamlit padding, header, and footer
st.markdown("""
    <style>
        #MainMenu {visibility: hidden;}
        header {visibility: hidden;}
        footer {visibility: hidden;}
        .block-container {
            padding: 0rem !important;
            max-width: 100% !important;
        }
        iframe {
            border: none;
            width: 100vw;
            height: 100vh;
        }
    </style>
""", unsafe_allow_html=True)

# Complete HTML/CSS/JS single-file application
html_code = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Muhammad Zaki (HMZ) — Portfolio</title>

    <!-- Tailwind CSS -->
    <script src="https://cdn.tailwindcss.com"></script>
    <script>
        tailwind.config = {
            theme: {
                extend: {
                    colors: {
                        midnight: '#0B0B0C',
                        lime: '#C6F432',
                        pakistan: '#01411C',
                        negRed: '#FF3B30',
                        posGreen: '#00C853'
                    },
                    fontFamily: {
                        syne: ['Syne', 'sans-serif'],
                        bebas: ['Bebas Neue', 'sans-serif'],
                        space: ['Space Grotesk', 'sans-serif'],
                        jakarta: ['Plus Jakarta Sans', 'sans-serif']
                    }
                }
            }
        }
    </script>

    <!-- Google Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Plus+Jakarta+Sans:ital,wght@0,300;0,400;0,600;0,700;1,400&family=Space+Grotesk:wght@400;600;700&family=Syne:wght@700;800&display=swap" rel="stylesheet">

    <!-- FontAwesome for Logos -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">

    <style>
        /* Base resets & custom smooth setup */
        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
            user-select: none;
        }

        html, body {
            background-color: #0B0B0C;
            color: #FFFFFF;
            font-family: 'Plus Jakarta Sans', sans-serif;
            overflow-x: hidden;
            scroll-behavior: smooth;
        }

        /* Custom Scrollbar */
        ::-webkit-scrollbar {
            width: 6px;
        }
        ::-webkit-scrollbar-track {
            background: #0B0B0C;
        }
        ::-webkit-scrollbar-thumb {
            background: #222;
            border-radius: 3px;
        }
        ::-webkit-scrollbar-thumb:hover {
            background: #C6F432;
        }

        /* Concentrated Pixelated Blurred Lime Glow in Lower Center */
        .ambient-glow {
            position: fixed;
            bottom: -15vh;
            left: 50%;
            transform: translateX(-50%);
            width: 90vw;
            max-width: 1000px;
            height: 45vh;
            background: radial-gradient(ellipse at bottom, rgba(198, 244, 50, 0.45) 0%, rgba(198, 244, 50, 0.2) 40%, rgba(11, 11, 12, 0) 80%);
            filter: blur(70px);
            pointer-events: none;
            z-index: 1;
            transition: opacity 0.8s ease, filter 0.8s ease, background 0.8s ease;
        }

        .ambient-glow.darkened {
            background: radial-gradient(ellipse at bottom, rgba(198, 244, 50, 0.18) 0%, rgba(198, 244, 50, 0.05) 40%, rgba(11, 11, 12, 0) 80%);
            filter: blur(90px);
        }

        /* Stretched Large Title styling for Muhammad Zaki */
        .stretched-header {
            font-family: 'Bebas Neue', sans-serif;
            letter-spacing: 0.15em;
            transform: scaleY(1.3);
            transform-origin: left;
            text-shadow: 0 0 30px rgba(198, 244, 50, 0.15);
        }

        /* Charging background flash animation */
        @keyframes chargePulse {
            0% { opacity: 0; background-color: transparent; }
            30% { opacity: 0.6; background-color: rgba(198, 244, 50, 0.25); box-shadow: 0 0 50px rgba(198, 244, 50, 0.8); }
            70% { opacity: 1; background-color: rgba(255, 255, 255, 0.3); }
            100% { opacity: 0; background-color: transparent; }
        }

        .charging-discharge {
            animation: chargePulse 0.9s cubic-bezier(0.16, 1, 0.3, 1) forwards;
        }

        /* B&W Portrait with Lime Green Edge Lighting */
        .portrait-cutout {
            position: relative;
            filter: grayscale(100%) contrast(120%) brightness(95%);
            mask-image: linear-gradient(to bottom, rgba(0,0,0,1) 0%, rgba(0,0,0,1) 60%, rgba(0,0,0,0) 100%);
            -webkit-mask-image: linear-gradient(to bottom, rgba(0,0,0,1) 0%, rgba(0,0,0,1) 60%, rgba(0,0,0,0) 100%);
            object-fit: cover;
            object-position: top center;
        }

        /* Green Rim Light Overlay */
        .portrait-container::after {
            content: '';
            position: absolute;
            top: 0;
            right: 0;
            bottom: 0;
            left: 0;
            background: linear-gradient(to left, rgba(198, 244, 50, 0.4) 0%, rgba(198, 244, 50, 0.1) 25%, transparent 60%);
            mix-blend-mode: color-dodge;
            pointer-events: none;
            border-radius: inherit;
        }

        /* 3D Flip Cards */
        .card-perspective {
            perspective: 1200px;
        }

        .flip-card-inner {
            position: relative;
            width: 100%;
            height: 100%;
            transition: transform 0.8s cubic-bezier(0.34, 1.56, 0.64, 1);
            transform-style: preserve-3d;
        }

        .card-perspective:hover .flip-card-inner {
            transform: rotateY(180deg) translateY(-8px);
        }

        .card-perspective:hover {
            filter: drop-shadow(0 0 20px rgba(198, 244, 50, 0.5));
        }

        .flip-card-front, .flip-card-back {
            position: absolute;
            width: 100%;
            height: 100%;
            -webkit-backface-visibility: hidden;
            backface-visibility: hidden;
            border-radius: 1.25rem;
        }

        .flip-card-front {
            background-color: #121214;
            border: 1px solid rgba(255, 255, 255, 0.1);
            display: flex;
            align-items: center;
            justify-content: center;
            text-align: center;
            padding: 2rem;
            transition: border-color 0.3s ease, box-shadow 0.3s ease;
        }

        .card-perspective:hover .flip-card-front {
            border-color: #C6F432;
        }

        .flip-card-back {
            background-color: #FFFFFF;
            color: #0B0B0C;
            transform: rotateY(180deg);
            padding: 2rem;
            display: flex;
            flex-direction: column;
            justify-content: center;
            border: 2px solid #C6F432;
        }

        /* Pakistani Flag Dynamic Overlay */
        #pakistan-flag-overlay {
            position: fixed;
            top: 0;
            left: 0;
            width: 100vw;
            height: 100vh;
            pointer-events: none;
            z-index: 40;
            opacity: 0;
            transition: opacity 1s ease-in-out;
            background: linear-gradient(135deg, rgba(1, 65, 28, 0.85) 0%, rgba(0, 30, 12, 0.95) 100%);
            display: flex;
            align-items: center;
            justify-content: center;
        }

        .flag-crescent-star {
            width: 280px;
            height: 280px;
            opacity: 0.15;
            animation: spinSlow 30s linear infinite;
        }

        @keyframes spinSlow {
            from { transform: rotate(0deg); }
            to { transform: rotate(360deg); }
        }

        /* Glowing Contact Boxes */
        .contact-box {
            transition: transform 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275), box-shadow 0.4s ease, border-color 0.4s ease;
        }

        .contact-box:hover {
            transform: translateY(-10px) scale(1.02);
            border-color: #C6F432;
            box-shadow: 0 0 35px rgba(198, 244, 50, 0.35);
        }

        /* Dynamic blinking cursor */
        .cursor-blink::after {
            content: '|';
            animation: blink 1s infinite;
            color: #C6F432;
        }

        @keyframes blink {
            0%, 100% { opacity: 1; }
            50% { opacity: 0; }
        }
    </style>
</head>

<body class="bg-midnight text-white antialiased selection:bg-lime selection:text-midnight">

    <!-- Ambient Concentrated Pixelated Glow at Lower Center -->
    <div id="ambientGlow" class="ambient-glow"></div>

    <!-- Pakistani Flag Overlay Triggered on "Pakistan" text appearance -->
    <div id="pakistan-flag-overlay">
        <svg class="flag-crescent-star text-white fill-current" viewBox="0 0 100 100">
            <path d="M 50 10 A 40 40 0 1 0 90 50 A 32 32 0 1 1 50 10 Z" />
            <polygon points="65,25 69,37 81,37 71,45 75,57 65,49 55,57 59,45 49,37 61,37" />
        </svg>
    </div>

    <!-- MAIN SCROLL CONTAINER -->
    <div class="relative w-full z-10">

        <!-- SECTION 1: HERO "WHO IS HMZ?" -->
        <section id="section1" class="h-screen w-full flex flex-col justify-center items-center relative px-4">
            
            <!-- Animated Virtual Cursor Effect -->
            <div id="cursorFollower" class="fixed pointer-events-none transition-all duration-300 z-50 flex items-center justify-center opacity-0 scale-50">
                <div class="w-6 h-6 border-2 border-lime rounded-full bg-lime/30 backdrop-blur-sm animate-ping"></div>
                <i class="fa-solid fa-arrow-pointer text-lime text-2xl -ml-2 -mt-4 drop-shadow-[0_0_10px_#C6F432]"></i>
            </div>

            <!-- "Who is HMZ?" Text Header -->
            <div id="heroHeaderContainer" class="text-center transition-all duration-700 transform scale-10 opacity-0 cursor-default">
                <h1 class="text-4xl md:text-7xl lg:text-8xl font-syne font-bold tracking-tight text-white inline-block">
                    Who is <span id="hmzSpan" class="font-bebas text-lime text-5xl md:text-8xl lg:text-9xl ml-3 tracking-wider drop-shadow-[0_0_25px_rgba(198,244,50,0.4)]">HMZ?</span>
                </h1>
            </div>

            <!-- Scroll Indicator -->
            <div id="scrollHint" class="absolute bottom-10 flex flex-col items-center gap-2 opacity-70 animate-bounce">
                <span class="text-xs uppercase tracking-widest text-gray-400 font-jakarta">Scroll Down Slowly</span>
                <i class="fa-solid fa-chevron-down text-lime"></i>
            </div>
        </section>

        <!-- SECTION 2: MUHAMMAD ZAKI & PORTRAIT & TYPEWRITER INFO -->
        <section id="section2" class="min-h-screen w-full relative px-6 md:px-16 lg:px-24 py-20 flex flex-col justify-center">
            
            <!-- Cinematic Cutout Portrait (Fixed right side backdrop inside section 2) -->
            <div id="portraitContainer" class="portrait-container absolute top-10 right-0 w-full md:w-1/2 lg:w-5/12 h-[80vh] pointer-events-none z-0 opacity-0 transition-opacity duration-1000">
                <img id="portraitImg" 
                     src="https://raw.githubusercontent.com/placeholder-user-asset/main/zaki_cutout.png" 
                     alt="Muhammad Zaki" 
                     class="portrait-cutout w-full h-full"
                     onerror="this.src='https://placehold.co/600x900/0B0B0C/FFFFFF?text=Muhammad+Zaki+Portrait'" />
            </div>

            <!-- Discharge Effect Overlay Box -->
            <div id="dischargeFlash" class="absolute inset-0 pointer-events-none z-30"></div>

            <div class="relative z-10 max-w-3xl">
                <!-- Header "Muhammad Zaki" Sticked Left -->
                <div id="nameHeaderContainer" class="opacity-0 transform -translate-x-12 transition-all duration-700">
                    <p class="text-lime font-space text-sm tracking-widest uppercase mb-2">// Letter Format Intro</p>
                    <h1 class="stretched-header text-6xl sm:text-8xl md:text-9xl font-bold text-white uppercase leading-none mb-8">
                        MUHAMMAD ZAKI
                    </h1>
                </div>

                <!-- Scroll-linked Typewriter Details -->
                <div id="typewriterBox" class="space-y-6 text-lg md:text-2xl font-jakarta leading-relaxed font-normal bg-midnight/60 backdrop-blur-md p-6 md:p-8 rounded-2xl border border-white/5 opacity-0 transition-opacity duration-500">
                    
                    <!-- Line 1: Age -->
                    <div id="lineAge" class="opacity-0 transition-opacity duration-300">
                        <span class="text-lime font-space font-bold">Age:</span> <span class="text-white">21 years</span>
                    </div>

                    <!-- Line 2: Origin -->
                    <div id="lineOrigin" class="opacity-0 transition-opacity duration-300">
                        <span class="text-lime font-space font-bold">Origin:</span> <span id="pakistanText" class="font-bold transition-colors duration-500 text-white">Pakistan</span>
                    </div>

                    <!-- Line 3: Does -->
                    <div id="lineDoes" class="opacity-0 transition-opacity duration-300">
                        <span class="text-lime font-space font-bold">Does:</span> <span class="text-white">Vibe-coded web development, Photography, Editing</span>
                    </div>

                    <!-- Line 4: Skills -->
                    <div id="lineSkills" class="opacity-0 transition-opacity duration-300">
                        <span class="text-lime font-space font-bold block mb-1">Skills:</span> 
                        <span class="text-white/90 text-base md:text-xl leading-loose">
                            Good Listener, Cooking, Emotional support <span class="text-gray-400 text-sm md:text-base">(Support for you while making payments)</span>, Mechanic, Electrician, Plumber, Grocery buyer, Half Doctor....... And the list goes on.
                        </span>
                    </div>

                </div>
            </div>
        </section>

        <!-- SECTION 3: FLASHCARDS (PREMIUM VS LOW COST) -->
        <section id="section3" class="min-h-screen w-full px-6 md:px-16 lg:px-24 py-24 flex flex-col justify-center items-center">
            
            <div class="text-center mb-16">
                <span class="text-lime font-space uppercase tracking-widest text-sm">// Web Development Services</span>
                <h2 class="text-3xl md:text-5xl font-syne font-bold text-white mt-2">Choose Your Scale</h2>
            </div>

            <!-- Two Flip Flashcards Grid -->
            <div class="grid grid-cols-1 md:grid-cols-2 gap-8 md:gap-12 w-full max-w-5xl">
                
                <!-- CARD 1: PREMIUM COST -->
                <div class="card-perspective h-[380px] sm:h-[340px] w-full cursor-pointer">
                    <div class="flip-card-inner">
                        <!-- Front -->
                        <div class="flip-card-front shadow-2xl">
                            <div>
                                <div class="w-14 h-14 rounded-2xl bg-lime/10 text-lime flex items-center justify-center mx-auto mb-4 border border-lime/30">
                                    <i class="fa-solid fa-crown text-2xl"></i>
                                </div>
                                <h3 class="font-syne font-bold text-2xl text-white">Premium cost web-development</h3>
                                <p class="text-xs text-gray-400 font-space mt-3 uppercase tracking-wider">Hover / Tap to Reveal Details</p>
                            </div>
                        </div>
                        <!-- Back -->
                        <div class="flip-card-back shadow-2xl">
                            <h4 class="font-syne font-bold text-xl mb-3 text-midnight">Premium Experience</h4>
                            <p class="text-sm md:text-base font-jakarta leading-relaxed text-gray-800">
                                Premium costed website development includes custom bought domains, bought hosted platforms and premium methods, used to develop sites, so that it should be 
                                <span class="text-posGreen font-bold bg-posGreen/10 px-1 py-0.5 rounded">Highly accessible</span>, with 
                                <span class="text-posGreen font-bold bg-posGreen/10 px-1 py-0.5 rounded">High performance score</span> and 
                                <span class="text-posGreen font-bold bg-posGreen/10 px-1 py-0.5 rounded">user experience</span>, disabling sleeping of the website, which 
                                <span class="text-negRed font-bold bg-negRed/10 px-1 py-0.5 rounded">ruins</span> the user experience.
                            </p>
                        </div>
                    </div>
                </div>

                <!-- CARD 2: LOW COST -->
                <div class="card-perspective h-[380px] sm:h-[340px] w-full cursor-pointer">
                    <div class="flip-card-inner">
                        <!-- Front -->
                        <div class="flip-card-front shadow-2xl">
                            <div>
                                <div class="w-14 h-14 rounded-2xl bg-white/5 text-white flex items-center justify-center mx-auto mb-4 border border-white/20">
                                    <i class="fa-solid fa-bolt text-2xl text-lime"></i>
                                </div>
                                <h3 class="font-syne font-bold text-2xl text-white">Low cost web-development</h3>
                                <p class="text-xs text-gray-400 font-space mt-3 uppercase tracking-wider">Hover / Tap to Reveal Details</p>
                            </div>
                        </div>
                        <!-- Back -->
                        <div class="flip-card-back shadow-2xl">
                            <h4 class="font-syne font-bold text-xl mb-2 text-midnight">Budget Tier</h4>
                            <p class="text-xs md:text-sm font-jakarta leading-relaxed text-gray-800 mb-2">
                                Low costed website development includes free domains issued by the hosting platform, hosted for free under the free tier of hosting platforms. 
                                <span class="text-posGreen font-bold bg-posGreen/10 px-1 py-0.5 rounded">Good for starting businesses</span> and highly 
                                <span class="text-posGreen font-bold bg-posGreen/10 px-1 py-0.5 rounded">budget friendly</span>.
                            </p>
                            <p class="text-xs md:text-sm font-jakarta leading-relaxed text-gray-800">
                                <strong class="text-negRed font-bold">Cons are:</strong><br>
                                Website <span class="text-negRed font-bold bg-negRed/10 px-1 py-0.5 rounded">sleeps</span> after some time of 
                                <span class="text-negRed font-bold bg-negRed/10 px-1 py-0.5 rounded">inactivity</span>. 
                                <span class="text-negRed font-bold bg-negRed/10 px-1 py-0.5 rounded">Cannot handle</span> high users traffic at a single time.
                            </p>
                        </div>
                    </div>
                </div>

            </div>
        </section>

        <!-- SECTION 4: CONTACT & FINAL TOUCH -->
        <section id="section4" class="min-h-screen w-full px-6 md:px-16 lg:px-24 py-20 flex flex-col justify-center items-center">
            
            <!-- Scrambled Header Text -->
            <div class="mb-16 text-center">
                <h2 id="scrambleHeader" class="text-3xl sm:text-5xl md:text-6xl font-syne font-bold text-white tracking-tight">
                    Wanna get in touch with me?
                </h2>
                <div class="w-24 h-1 bg-lime mx-auto mt-4 rounded-full"></div>
            </div>

            <!-- Contact Cards -->
            <div class="grid grid-cols-1 md:grid-cols-2 gap-8 w-full max-w-4xl mb-16">
                
                <!-- WHATSAPP BOX -->
                <a href="https://wa.me/923144012872" target="_blank" class="contact-box bg-midnight/90 border border-white/10 p-8 rounded-3xl relative block overflow-hidden group">
                    <div class="absolute top-6 left-6 text-emerald-500 text-3xl">
                        <i class="fa-brands fa-whatsapp"></i>
                    </div>
                    <div class="pt-10 text-left">
                        <h3 class="font-syne font-bold text-2xl text-white mb-2">Got WhatsApp?</h3>
                        <p class="text-gray-400 font-jakarta text-sm mb-4">Reach out on WA</p>
                        <span class="text-lime font-space font-bold text-xl tracking-wider group-hover:underline">0314-4012872</span>
                    </div>
                    <div class="absolute bottom-6 right-6 text-gray-600 group-hover:text-lime transition-colors">
                        <i class="fa-solid fa-arrow-up-right-from-square text-lg"></i>
                    </div>
                </a>

                <!-- INSTAGRAM BOX -->
                <a href="https://instagram.com/hmzaki._.rj" target="_blank" class="contact-box bg-midnight/90 border border-white/10 p-8 rounded-3xl relative block overflow-hidden group">
                    <div class="absolute top-6 left-6 text-pink-500 text-3xl">
                        <i class="fa-brands fa-instagram"></i>
                    </div>
                    <div class="pt-10 text-left">
                        <h3 class="font-syne font-bold text-2xl text-white mb-2">Got Instagram?</h3>
                        <p class="text-gray-400 font-jakarta text-sm mb-4">Reach out on Insta</p>
                        <span class="text-lime font-space font-bold text-xl tracking-wider group-hover:underline">hmzaki._.rj</span>
                    </div>
                    <div class="absolute bottom-6 right-6 text-gray-600 group-hover:text-lime transition-colors">
                        <i class="fa-solid fa-arrow-up-right-from-square text-lg"></i>
                    </div>
                </a>

            </div>

            <!-- Closing Text Block -->
            <div class="text-center space-y-3 font-jakarta max-w-2xl">
                <p class="text-gray-400 text-lg italic">Nervous to talk to me?</p>
                <p class="text-white text-xl font-semibold">"Take the first step, as you did for her"</p>
                <p class="text-lime font-space text-lg font-medium">Trust me, I'm friendly</p>
                <p class="text-gray-300 text-sm md:text-base pt-2 font-light tracking-wide uppercase">Get your ideas converted into your dream-web</p>
            </div>

            <footer class="mt-20 text-xs text-gray-600 font-space tracking-widest">
                &copy; HMZ — MUHAMMAD ZAKI. ALL RIGHTS RESERVED.
            </footer>
        </section>

    </div>

    <!-- JAVASCRIPT CONTROLLERS (Bidirectional Scroll Animations & Logic) -->
    <script>
        document.addEventListener("DOMContentLoaded", () => {
            
            // Initial Page Fade In
            document.body.style.opacity = '0';
            document.body.style.transition = 'opacity 1.2s ease-out';
            setTimeout(() => { document.body.style.opacity = '1'; }, 100);

            // DOM Element Handles
            const heroHeaderContainer = document.getElementById('heroHeaderContainer');
            const cursorFollower = document.getElementById('cursorFollower');
            const portraitContainer = document.getElementById('portraitContainer');
            const nameHeaderContainer = document.getElementById('nameHeaderContainer');
            const typewriterBox = document.getElementById('typewriterBox');
            const dischargeFlash = document.getElementById('dischargeFlash');
            const pakistanText = document.getElementById('pakistanText');
            const flagOverlay = document.getElementById('pakistan-flag-overlay');
            const ambientGlow = document.getElementById('ambientGlow');
            const scrambleHeader = document.getElementById('scrambleHeader');

            const lineAge = document.getElementById('lineAge');
            const lineOrigin = document.getElementById('lineOrigin');
            const lineDoes = document.getElementById('lineDoes');
            const lineSkills = document.getElementById('lineSkills');

            let hasDischarged = false;
            let flagTriggered = false;

            // SECTION 1: Entry Cursor & Text Scale Animation
            setTimeout(() => {
                cursorFollower.style.opacity = '1';
                cursorFollower.style.transform = 'scale(1) translate(-50%, -50%)';
                
                setTimeout(() => {
                    heroHeaderContainer.style.opacity = '1';
                    heroHeaderContainer.style.transform = 'scale(1)';
                    
                    setTimeout(() => {
                        cursorFollower.style.opacity = '0';
                        cursorFollower.style.transform = 'scale(0.2)';
                    }, 800);
                }, 400);
            }, 600);

            // Scramble Text Logic
            const originalScrambleText = "Wanna get in touch with me?";
            const scrambleChars = "!@#$%^&*()_+-=X0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ";
            let scrambleInterval = null;

            function runScramble() {
                let iteration = 0;
                clearInterval(scrambleInterval);
                scrambleInterval = setInterval(() => {
                    scrambleHeader.innerText = originalScrambleText
                        .split("")
                        .map((char, index) => {
                            if (index < iteration) return originalScrambleText[index];
                            if (char === " ") return " ";
                            return scrambleChars[Math.floor(Math.random() * scrambleChars.length)];
                        })
                        .join("");

                    if (iteration >= originalScrambleText.length) {
                        clearInterval(scrambleInterval);
                    }
                    iteration += 1 / 2;
                }, 30);
            }

            // Flag Overlay 5-Second Trigger
            function triggerPakistanFlag() {
                if (flagTriggered) return;
                flagTriggered = true;
                
                // Color change to Dark Green
                pakistanText.style.color = '#01411C';
                flagOverlay.style.opacity = '1';

                setTimeout(() => {
                    flagOverlay.style.opacity = '0';
                    setTimeout(() => {
                        pakistanText.style.color = '#FFFFFF';
                    }, 1000);
                }, 5000);
            }

            // BIDIRECTIONAL SCROLL ENGINE
            window.addEventListener('scroll', () => {
                const scrollY = window.scrollY;
                const windowHeight = window.innerHeight;

                // 1. HERO FADE OUT ON SCROLL
                const heroFadeFactor = Math.max(0, 1 - (scrollY / (windowHeight * 0.6)));
                heroHeaderContainer.style.opacity = heroFadeFactor;
                heroHeaderContainer.style.transform = `scale(${0.6 + (heroFadeFactor * 0.4)})`;

                // 2. SECTION 2 APPEARANCE & PORTRAIT & DISCHARGE ANIMATION
                const sec2Top = document.getElementById('section2').offsetTop;
                if (scrollY > sec2Top - (windowHeight * 0.7) && scrollY < sec2Top + windowHeight) {
                    
                    // Show Name & Portrait
                    nameHeaderContainer.style.opacity = '1';
                    nameHeaderContainer.style.transform = 'translateX(0)';
                    portraitContainer.style.opacity = '1';

                    // Discharge Charging Animation
                    if (!hasDischarged) {
                        hasDischarged = true;
                        dischargeFlash.classList.add('charging-discharge');
                    }

                    // Scroll-driven Typewriter lines reveal
                    const relScroll = scrollY - (sec2Top - windowHeight * 0.4);
                    
                    if (relScroll > 100) lineAge.style.opacity = '1';
                    else lineAge.style.opacity = '0';

                    if (relScroll > 180) {
                        lineOrigin.style.opacity = '1';
                        triggerPakistanFlag();
                    } else lineOrigin.style.opacity = '0';

                    if (relScroll > 260) lineDoes.style.opacity = '1';
                    else lineDoes.style.opacity = '0';

                    if (relScroll > 340) lineSkills.style.opacity = '1';
                    else lineSkills.style.opacity = '0';

                    typewriterBox.style.opacity = '1';
                } else {
                    // Reversible fade-out when scrolling away
                    if (scrollY < sec2Top - (windowHeight * 0.8)) {
                        nameHeaderContainer.style.opacity = '0';
                        nameHeaderContainer.style.transform = 'translateX(-3rem)';
                        portraitContainer.style.opacity = '0';
                        typewriterBox.style.opacity = '0';
                        hasDischarged = false;
                    }
                }

                // Portrait Fade Out into Black when moving to Section 3
                const sec3Top = document.getElementById('section3').offsetTop;
                if (scrollY > sec3Top - (windowHeight * 0.5)) {
                    portraitContainer.style.opacity = '0';
                }

                // 3. DARKEN BACKGROUND AMBIENT GLOW ON DEEPER SCROLL
                const sec4Top = document.getElementById('section4').offsetTop;
                if (scrollY > sec3Top + 100) {
                    ambientGlow.classList.add('darkened');
                } else {
                    ambientGlow.classList.remove('darkened');
                }

                // 4. SCRAMBLE TEXT ON FINAL SECTION
                if (scrollY > sec4Top - (windowHeight * 0.6)) {
                    if (!scrambleHeader.classList.contains('scrambled-done')) {
                        scrambleHeader.classList.add('scrambled-done');
                        runScramble();
                    }
                } else {
                    scrambleHeader.classList.remove('scrambled-done');
                }
            });

        });
    </script>
</body>
</html>
"""

# Render HTML Application inside Streamlit container
components.html(html_code, height=950, scrolling=True)
```

I have assembled the complete code for your introductory website and Streamlit app.

### Key Features Included:
1. **Color & Ambient Glow:** Custom `#0B0B0C` background, `#FFFFFF` text, and `#C6F432` lime accents with a pixelated ambient glow at the bottom center that darkens dynamically upon scrolling.
2. **Hero Animation:** Cursor scaling transition that expands "Who is HMZ?" smoothly before disappearing.
3. **Cinematic Cutout Portrait & Lighting:** The black-and-white cutout portrait sits on the right side behind the left-aligned header text "Muhammad Zaki", featuring a lime green rim lighting highlight that fades cleanly into black as you scroll.
4. **Interactive Scroll & Typewriter Lines:** Smooth scroll-linked typewriter sequence for your age, origin, does, and skills.
5. **Pakistani Flag Effect:** Triggering a 5-second green overlay when the word "Pakistan" appears on screen.
6. **3D Flip Flashcards:** Interactive cards with glowing edges that flip on hover, highlighting positive words in green and negative words in red.
7. **Contact Links & Text Unscrambling:** Direct links to WhatsApp (`0314-4012872`) and Instagram (`hmzaki._.rj`) with custom hover states, complete with the final unscramble header transition.
