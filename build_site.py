import os

# --- TEMPLATES ---
def get_header(title, active_nav="home", desc="CCEYD advocates for good governance, environmental sustainability, health education, inclusive education, human trafficking prevention, and child rights.", canonical_url="https://cceyd.org/"):
    # active_nav can be: home, about, programs, impact, get_involved, contact
    
    def active_class(name):
        return 'class="active"' if active_nav == name else ''
    def active_dropdown(name):
        return 'class="active dropdown"' if active_nav == name else 'class="dropdown"'

    # JSON-LD Schema based on page type
    schema_markup = ""
    if active_nav == "home" or active_nav == "about":
        schema_markup = """
    <script type="application/ld+json">
    {
      "@context": "https://schema.org",
      "@type": "NGO",
      "name": "CCEYD",
      "url": "https://cceyd.org",
      "logo": "https://cceyd.org/images/logo.png",
      "description": "Centre For Communities Education and Youth Development (CCEYD) empowers communities worldwide for positive change."
    }
    </script>
    """
    elif active_nav == "programs":
        # Escape double quotes for JSON-LD
        safe_desc = desc.replace('"', '\\"')
        safe_title = title.replace('"', '\\"')
        schema_markup = f"""
    <script type="application/ld+json">
    {{
      "@context": "https://schema.org",
      "@type": "Service",
      "name": "CCEYD Program: {safe_title}",
      "provider": {{
        "@type": "NGO",
        "name": "CCEYD"
      }},
      "description": "{safe_desc}"
    }}
    </script>
    """

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} | CCEYD</title>
    <meta name="description" content="{desc}">
    <link rel="canonical" href="{canonical_url}">
    <link rel="icon" href="images/logo.png" type="image/png">
    
    <!-- Open Graph Tags -->
    <meta property="og:title" content="{title} | CCEYD">
    <meta property="og:description" content="{desc}">
    <meta property="og:url" content="{canonical_url}">
    <meta property="og:type" content="website">
    <meta property="og:image" content="https://cceyd.org/images/hero1.jpg">
    
    <link rel="stylesheet" href="styles.css">
    
    <!-- Google Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=Poppins:wght@500;600;700&display=swap" rel="stylesheet">
    
    <!-- Remix Icons -->
    <link href="https://cdn.jsdelivr.net/npm/remixicon@3.5.0/fonts/remixicon.css" rel="stylesheet">
    {schema_markup}
</head>
<body>
    <!-- CUSTOM LOADER -->
    <div id="loader" class="loader-container">
        <img src="images/logo.png" alt="Loading..." class="loader-logo">
    </div>
    <noscript>
        <style>
            #loader {{ display: none !important; }}
        </style>
    </noscript>
    <a href="#main-content" class="skip-link">Skip to main content</a>
    <!-- HEADER -->
    <header class="header">
        <div class="container header-container">
            <a href="index.html" class="logo" aria-label="CCEYD Home">
                <img src="images/logo.png" alt="CCEYD Logo" style="height: 60px; width: auto; border-radius: 8px;">
            </a>
            
            <nav class="nav-links" aria-label="Main Navigation">
                <a href="index.html" {active_class('home')}>Home</a>
                <a href="about.html" {active_class('about')}>About Us</a>
                
                <div class="nav-item-dropdown">
                    <a href="programs.html" {active_dropdown('programs')} aria-haspopup="true" aria-expanded="false">Programs <i class="ri-arrow-down-s-line" aria-hidden="true"></i></a>
                    <div class="dropdown-menu" aria-label="Programs submenu">
                        <a href="program-governance.html">Good Governance</a>
                        <a href="program-environment.html">Environmental Sustainability</a>
                        <a href="program-health.html">Health Education</a>
                        <a href="program-inclusive-edu.html">Inclusive Education</a>
                        <a href="program-trafficking.html">Human Trafficking Prevention</a>
                        <a href="program-child-rights.html">Child Rights</a>
                    </div>
                </div>
                
                <a href="impact.html" {active_class('impact')}>Impact</a>
                
                <div class="nav-item-dropdown">
                    <a href="#" {active_dropdown('get_involved')} aria-haspopup="true" aria-expanded="false">Get Involved <i class="ri-arrow-down-s-line" aria-hidden="true"></i></a>
                    <div class="dropdown-menu" aria-label="Get Involved submenu">
                        <a href="donate.html">Donate</a>
                        <a href="volunteer.html">Volunteer</a>
                        <a href="partner.html">Partner With Us</a>
                    </div>
                </div>
                
                <a href="contact.html" {active_class('contact')}>Contact</a>
            </nav>

            <div class="header-actions">
                <a href="donate.html" class="btn btn-primary"><i class="ri-heart-3-line" aria-hidden="true"></i> Donate</a>
                <button class="mobile-menu-btn" aria-label="Toggle Menu" aria-expanded="false">
                    <i class="ri-menu-3-line" aria-hidden="true"></i>
                </button>
            </div>
        </div>
    </header>
"""

FOOTER = '''
    <!-- ====== FOOTER ====== -->
    <footer class="footer" id="footer">
        <div class="container">
            <div class="footer-grid">
                <div class="footer-col footer-about">
                    <div class="logo" style="margin-bottom:16px;">
                        <img src="images/logo.png" alt="CCEYD Logo" style="height: 60px; width: auto; border-radius: 8px; background: white; padding: 2px;">
                    </div>
                    <p>Empowering communities worldwide for positive change. Advocating for good governance, education, and human rights.</p>
                    <div class="social-links">
                        <a href="#" aria-label="Facebook"><i class="ri-facebook-fill"></i></a>
                        <a href="#" aria-label="Twitter"><i class="ri-twitter-x-line"></i></a>
                        <a href="#" aria-label="Instagram"><i class="ri-instagram-line"></i></a>
                        <a href="#" aria-label="LinkedIn"><i class="ri-linkedin-fill"></i></a>
                    </div>
                </div>

                <div class="footer-col">
                    <h4>Programs</h4>
                    <div class="footer-links">
                        <a href="program-governance.html">Good Governance</a>
                        <a href="program-environment.html">Environmental Sustainability</a>
                        <a href="program-health.html">Health Education</a>
                        <a href="program-inclusive-edu.html">Inclusive Education</a>
                        <a href="program-trafficking.html">Human Trafficking</a>
                        <a href="program-child-rights.html">Child Rights</a>
                    </div>
                </div>

                <div class="footer-col">
                    <h4>Get Involved</h4>
                    <div class="footer-links">
                        <a href="donate.html">Donate Now</a>
                        <a href="volunteer.html">Volunteer</a>
                        <a href="partner.html">Partner With Us</a>
                        <a href="impact.html">Our Impact</a>
                    </div>
                </div>

                <div class="footer-col">
                    <h4>Contact Us</h4>
                    <div class="footer-contact-item">
                        <i class="ri-map-pin-line"></i>
                        <span>Tamale, Ghana<br>West Africa</span>
                    </div>
                    <div class="footer-contact-item">
                        <i class="ri-phone-line"></i>
                        <span>+233 24 262 5055</span>
                    </div>
                    <div class="footer-contact-item">
                        <i class="ri-mail-line"></i>
                        <span>contact@cceyd.org</span>
                    </div>
                </div>
            </div>

            <div class="footer-bottom">
                <p>&copy; 2026 Centre For Communities Education and Youth Development (CCEYD). All rights reserved.</p>
            </div>
        </div>
    </footer>
    <script src="script.js"></script>
</body>
</html>
'''

def inner_hero(title, subtitle):
    return f"""
    <section class="hero" style="min-height: 40vh; display: flex; align-items: center; padding-top: 100px;">
        <div class="container hero-container" style="display: flex; justify-content: center; text-align: center;">
            <div class="hero-content" style="max-width: 800px;">
                <h1 style="font-size: 3.5rem;">{title}<span class="dot-accent"></span></h1>
                <p class="hero-subtitle" style="margin: 0 auto;">{subtitle}</p>
            </div>
        </div>
    </section>
"""

# --- PAGE CONTENTS ---

pages = {}

pages['index.html'] = {
    'title': 'Home',
    'active': 'home',
    'content': """
    <main id="main-content">
        <!-- HERO SECTION -->
        <section class="hero" id="hero-section">
            <div class="container hero-container">
                <div class="hero-content">
                    <h1>
                        Empowering<br>
                        communities worldwide<br>
                        for positive<br>
                        <span>change</span><span class="dot-accent"></span>
                    </h1>
                    <p class="hero-subtitle">CCEYD advocates for good governance, environmental sustainability, health education, inclusive education, human trafficking prevention, and child rights.</p>
                    <div class="hero-buttons">
                        <a href="donate.html" class="btn btn-dark" id="hero-donate-btn"><i class="ri-heart-3-fill"></i> DONATE NOW</a>
                        <a href="volunteer.html" class="btn btn-outline-pill">VOLUNTEER <i class="ri-group-line"></i></a>
                    </div>
                </div>

                <div class="hero-visual">
                    <div class="hero-img-main">
                        <img src="images/hero1.jpg" alt="Hands holding child hands" class="placeholder-img" style="object-fit: cover; width: 100%; height: 100%;">
                    </div>
                    <div class="hero-img-secondary">
                        <img src="images/hero2.jpg" alt="Adult holding child" class="placeholder-img" style="object-fit: cover; width: 100%; height: 100%;">
                    </div>
                    <div class="hero-orange-dot top"></div>
                    <div class="hero-orange-dot mid"></div>

                    <!-- Decorative dots -->
                    <div class="hero-decor-dots top-left"></div>
                </div>
            </div>
        </section>

        <!-- MAKE A DIFFERENCE SECTION -->
        <section class="difference-section" id="difference-section">
            <div class="container">
                <div class="section-header">
                    <p class="section-label">Our Core Values</p>
                    <h2 class="section-title">What Drives Us</h2>
                    <p class="section-subtitle">We believe in empowering communities through transparent, inclusive, and sustainable actions.</p>
                </div>

                <!-- World map background - SVG inline for faded effect -->
                <div style="position:relative;">
                    <svg class="world-map-svg" viewBox="0 0 1000 500" xmlns="http://www.w3.org/2000/svg" style="position:absolute;top:50%;left:50%;transform:translate(-50%,-50%);width:100%;opacity:0.05;pointer-events:none;">
                        <!-- Simplified world map shapes -->
                        <ellipse cx="500" cy="250" rx="480" ry="220" fill="none" stroke="#d4a574" stroke-width="1" stroke-dasharray="6 4" opacity="0.5"/>
                        <!-- North America -->
                        <path d="M120,100 Q160,80 200,90 Q230,95 250,120 Q260,150 240,180 Q220,200 200,210 Q170,220 150,200 Q130,180 110,160 Q100,140 110,120 Z" fill="#d4a574" opacity="0.3"/>
                        <!-- South America -->
                        <path d="M200,250 Q220,240 240,260 Q250,290 245,320 Q240,350 220,370 Q200,380 190,360 Q180,330 185,300 Q190,270 200,250 Z" fill="#d4a574" opacity="0.3"/>
                        <!-- Europe -->
                        <path d="M430,80 Q460,70 490,85 Q510,100 500,120 Q490,135 470,130 Q450,125 440,110 Q435,95 430,80 Z" fill="#d4a574" opacity="0.3"/>
                        <!-- Africa -->
                        <path d="M450,160 Q480,150 510,165 Q530,190 535,230 Q530,270 520,300 Q500,330 480,340 Q460,335 450,310 Q440,280 440,250 Q445,210 450,160 Z" fill="#d4a574" opacity="0.4"/>
                        <!-- Asia -->
                        <path d="M550,70 Q620,60 700,80 Q760,100 800,130 Q820,160 800,180 Q770,190 730,185 Q690,180 650,170 Q610,155 580,135 Q555,110 550,70 Z" fill="#d4a574" opacity="0.3"/>
                        <!-- Australia -->
                        <path d="M750,300 Q790,290 820,310 Q840,330 830,350 Q810,360 780,355 Q760,340 750,320 Q748,310 750,300 Z" fill="#d4a574" opacity="0.3"/>
                    </svg>

                    <div class="difference-cards stagger-children">
                        <div class="diff-card animate-in" id="card-free-access">
                            <div class="card-icon orange"><i class="ri-shield-star-line"></i></div>
                            <h3>Integrity</h3>
                            <p>We operate with complete transparency and accountability in all our programs.</p>
                        </div>

                        <div class="diff-card animate-in" id="card-locals-for-locals">
                            <div class="card-icon teal"><i class="ri-lightbulb-flash-line"></i></div>
                            <h3>Empowerment</h3>
                            <p>We believe in equipping communities with the tools they need to succeed independently.</p>
                        </div>

                        <div class="diff-card animate-in" id="card-real-impact">
                            <div class="card-icon amber"><i class="ri-group-line"></i></div>
                            <h3>Inclusivity</h3>
                            <p>Every voice matters, regardless of background or circumstance.</p>
                        </div>

                        <div class="diff-card animate-in" id="card-safety-net">
                            <div class="card-icon green"><i class="ri-plant-line"></i></div>
                            <h3>Sustainability</h3>
                            <p>Our solutions are designed to last and protect our natural environment for future generations.</p>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <!-- CHANGING LIVES WITH KNOWLEDGE -->
        <section class="about-section" id="about-section">
            <div class="container">
                <div class="about-grid">
                    <div class="about-img-wrapper animate-in">
                        <div class="about-img-circle">
                            <img src="images/who1.jpg" alt="Mother and child" class="placeholder-img" style="object-fit: cover; width: 100%; height: 100%;">
                        </div>
                    </div>

                    <div class="about-content animate-in">
                        <p class="section-label">Success Stories</p>
                        <h2>Changing Lives with Knowledge</h2>
                        <p class="highlight-text">"The health education provided by CCEYD has completely transformed our village. We now have access to clean water and better sanitation practices." — Aisha M., Tamale, Ghana</p>
                        <p>We focus on building brighter futures through essential programs that truly make an impact across our communities. By working alongside community members, we aim to restore opportunities and build resilience.</p>
                        <div class="about-buttons">
                            <a href="impact.html" class="btn btn-dark" id="about-learn-btn"><i class="ri-arrow-right-line"></i> SEE OUR IMPACT</a>
                            <a href="about.html" class="watch-video-btn" id="about-video-btn">
                                <div class="play-circle"><i class="ri-play-fill"></i></div>
                                <span>WATCH VIDEO</span>
                            </a>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <!-- FEATURED PROGRAMS -->
        <section class="campaigns-section" id="campaigns-section">
            <div class="container">
                <div class="section-header">
                    <p class="section-label">Our Work</p>
                    <h2 class="section-title">Featured Programs</h2>
                    <p class="section-subtitle">Discover how we are making a tangible difference in communities through targeted interventions.</p>
                </div>

                <!-- Background Africa map shape -->
                <svg class="africa-map-bg" viewBox="0 0 400 500" xmlns="http://www.w3.org/2000/svg" style="position:absolute;bottom:0;left:50%;transform:translateX(-50%);width:50%;max-width:600px;opacity:0.04;pointer-events:none;">
                    <path d="M150,20 Q200,10 250,30 Q290,60 310,100 Q330,150 335,200 Q330,260 320,310 Q300,360 270,400 Q240,430 210,450 Q180,460 160,440 Q140,410 130,370 Q120,320 115,270 Q110,220 115,170 Q120,120 130,80 Q140,40 150,20 Z" fill="#d4a574" opacity="0.5"/>
                </svg>

                <div class="campaigns-grid stagger-children">
                    <!-- Campaign Card 1 -->
                    <div class="campaign-card animate-in" id="campaign-1">
                        <div class="card-icon orange" style="margin: 32px auto 0; width: 80px; height: 80px; font-size: 2.5rem; display: flex; align-items: center; justify-content: center; border-radius: var(--radius-md);">
                            <i class="ri-government-line"></i>
                        </div>
                        <div class="campaign-card-body" style="text-align: center;">
                            <h3>Good Governance</h3>
                            <p>Promoting civic education and accountable local governance structures.</p>
                            <a href="program-governance.html" class="btn btn-outline-pill" style="margin-top: 15px;">Learn More</a>
                        </div>
                    </div>

                    <!-- Campaign Card 2 -->
                    <div class="campaign-card animate-in" id="campaign-2">
                        <div class="card-icon green" style="margin: 32px auto 0; width: 80px; height: 80px; font-size: 2.5rem; display: flex; align-items: center; justify-content: center; border-radius: var(--radius-md);">
                            <i class="ri-heart-pulse-line"></i>
                        </div>
                        <div class="campaign-card-body" style="text-align: center;">
                            <h3>Health Education</h3>
                            <p>Providing essential WASH training and healthcare resources in rural areas.</p>
                            <a href="program-health.html" class="btn btn-outline-pill" style="margin-top: 15px;">Learn More</a>
                        </div>
                    </div>

                    <!-- Campaign Card 3 -->
                    <div class="campaign-card animate-in" id="campaign-3">
                        <div class="card-icon teal" style="margin: 32px auto 0; width: 80px; height: 80px; font-size: 2.5rem; display: flex; align-items: center; justify-content: center; border-radius: var(--radius-md);">
                            <i class="ri-book-open-line"></i>
                        </div>
                        <div class="campaign-card-body" style="text-align: center;">
                            <h3>Inclusive Education</h3>
                            <p>Ensuring every child, regardless of ability, has access to quality schooling.</p>
                            <a href="program-inclusive-edu.html" class="btn btn-outline-pill" style="margin-top: 15px;">Learn More</a>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <!-- VOLUNTEER POSITIONS -->
        <section class="volunteer-section" id="volunteer-section" style="padding: 100px 0;">
            <div class="container">
                <div class="volunteer-grid" style="display: grid; grid-template-columns: 1fr 1fr; gap: 60px; align-items: center;">
                    <div class="volunteer-content animate-in">
                        <h2 style="font-size: 2.4rem; margin-bottom: 20px;">Join Our Network</h2>
                        <p style="color: var(--text-light); margin-bottom: 30px; line-height: 1.8;">Join thousands of volunteers making a real difference. Our volunteer programs give you the chance to help communities in need while gaining valuable experience and connections.</p>
                        <a href="volunteer.html" class="btn btn-primary" id="volunteer-apply-btn">Apply Now <i class="ri-arrow-right-line"></i></a>

                        <div class="stats-row" style="display: flex; gap: 40px; margin-top: 40px;">
                            <div class="stat-item">
                                <div class="stat-number" data-count="5000" style="font-size: 2.5rem; font-weight: 700; color: var(--primary); font-family: 'Poppins', sans-serif;">5<span>K+</span></div>
                                <div class="stat-label" style="font-size: 0.9rem; font-weight: 500;">Children Educated</div>
                            </div>
                            <div class="stat-item">
                                <div class="stat-number" data-count="50" style="font-size: 2.5rem; font-weight: 700; color: var(--primary); font-family: 'Poppins', sans-serif;">50<span>+</span></div>
                                <div class="stat-label" style="font-size: 0.9rem; font-weight: 500;">Communities Reached</div>
                            </div>
                            <div class="stat-item">
                                <div class="stat-number" data-count="120" style="font-size: 2.5rem; font-weight: 700; color: var(--primary); font-family: 'Poppins', sans-serif;">120</div>
                                <div class="stat-label" style="font-size: 0.9rem; font-weight: 500;">Projects Completed</div>
                            </div>
                        </div>
                    </div>

                    <div class="volunteer-img-wrapper animate-in" style="border-radius: 20px; overflow: hidden; height: 500px; box-shadow: var(--shadow-md);">
                        <img src="images/impacts/impacts 004.jpg" alt="Volunteers in action" class="placeholder-img" style="object-fit: cover; width: 100%; height: 100%;">
                    </div>
                </div>
            </div>
        </section>

        <!-- NEWSLETTER / CTA -->
        <section class="cta-section" id="cta-section" style="padding: 80px 0; background: var(--bg-cream); text-align: center;">
            <div class="container">
                <h2 style="font-size: 2rem; margin-bottom: 16px;">Join Our Newsletter</h2>
                <p style="color: var(--text-light); margin-bottom: 30px;">Stay updated with our latest campaigns, success stories, and ways to get involved.</p>
                <form class="cta-form" id="newsletter-form" onsubmit="return false;" style="display: flex; max-width: 500px; margin: 0 auto; gap: 10px;">
                    <input type="email" placeholder="Enter your email address" aria-label="Email address" id="newsletter-email" required style="flex: 1; padding: 14px 20px; border: 1px solid #ddd; border-radius: var(--radius-full); font-size: 1rem;">
                    <button type="submit" class="btn btn-primary" id="newsletter-submit-btn">Subscribe</button>
                </form>
            </div>
        </section>
    </main>

    """
}

pages['about.html'] = {
    'title': 'About Us',
    'active': 'about',
    'content': """
    <main id="main-content">
        <!-- INNER HERO -->
        <section class="hero" style="min-height: 40vh; display: flex; align-items: center; padding-top: 100px;">
            <div class="container hero-container" style="display: flex; justify-content: center; text-align: center;">
                <div class="hero-content" style="max-width: 800px;">
                    <h1 style="font-size: 3.5rem;">About <span class="logo-highlight">CCEYD</span><span class="dot-accent"></span></h1>
                    <p class="hero-subtitle" style="margin: 0 auto;">Discover our journey, mission, and the people behind the change.</p>
                </div>
            </div>
        </section>

        <!-- ABOUT CONTENT -->
        <section class="difference-section" style="background-color: var(--bg-white);">
            <div class="container">
                <div class="section-header" style="max-width: 800px; margin: 0 auto 50px;">
                    <p class="section-label">Our History & Background</p>
                    <h2 class="section-title">Who We Are</h2>
                    <p class="section-subtitle">The Centre For Communities Education and Youth Development (CCEYD) was founded in Tamale, Ghana with a singular vision: to empower the most vulnerable populations across West Africa. Over the years, we have grown from a small community initiative into a recognized organization advocating for systemic change and grassroots development.</p>
                </div>

                <div class="about-grid" style="align-items: center; margin-bottom: 80px;">
                    <div class="about-content animate-in">
                        <p class="section-label">Vision & Mission</p>
                        <h2>Empowering communities worldwide</h2>
                        <p class="highlight-text" style="font-style: italic; border-left: 4px solid var(--primary); padding-left: 20px;">
                            "CCEYD advocates for good governance, environmental sustainability, health education, inclusive education, human trafficking prevention, and child rights, empowering communities worldwide for positive change."
                        </p>
                    </div>
                    <div class="about-img-wrapper animate-in" style="justify-content: center;">
                        <div class="placeholder-img group" style="width: 100%; height: 350px; border-radius: 20px; background:linear-gradient(135deg,#f59e0b 0%,#d97706 50%,#fef3c7 100%);"></div>
                    </div>
                </div>

                <div class="section-header" style="margin-top: 80px; margin-bottom: 40px;">
                    <h2 class="section-title">Core Values</h2>
                </div>
                
                <div class="difference-cards stagger-children">
                    <div class="diff-card animate-in">
                        <div class="card-icon orange"><i class="ri-shield-star-line"></i></div>
                        <h3>Integrity</h3>
                        <p>We operate with complete transparency and accountability in all our programs.</p>
                    </div>
                    <div class="diff-card animate-in">
                        <div class="card-icon teal"><i class="ri-lightbulb-flash-line"></i></div>
                        <h3>Empowerment</h3>
                        <p>We believe in equipping communities with the tools they need to succeed independently.</p>
                    </div>
                    <div class="diff-card animate-in">
                        <div class="card-icon amber"><i class="ri-group-line"></i></div>
                        <h3>Inclusivity</h3>
                        <p>Every voice matters, regardless of background or circumstance.</p>
                    </div>
                    <div class="diff-card animate-in">
                        <div class="card-icon green"><i class="ri-plant-line"></i></div>
                        <h3>Sustainability</h3>
                        <p>Our solutions are designed to last and protect our natural environment for future generations.</p>
                    </div>
                </div>
            </div>
        </section>

        <!-- TEAM SECTION -->
        <section class="campaigns-section" style="background: var(--bg-cream);">
            <div class="container">
                <div class="section-header">
                    <p class="section-label">Our Leadership Team</p>
                    <h2 class="section-title">Meet The Team</h2>
                    <p class="section-subtitle">The dedicated individuals driving CCEYD's mission forward.</p>
                </div>

                <div class="campaigns-grid stagger-children">
                    <div class="campaign-card animate-in" style="text-align: center; padding: 40px 20px; background: #fff;">
                        <div style="width: 120px; height: 120px; border-radius: 50%; background-color: var(--primary-light); margin: 0 auto 20px; border: 4px solid white; box-shadow: 0 10px 20px rgba(0,0,0,0.05);"></div>
                        <h3>John Doe</h3>
                        <p style="color: var(--primary); font-weight: 600; font-size: 0.9rem; margin-bottom: 15px;">Executive Director</p>
                        <p style="font-size: 0.9rem; color: var(--text-light);">John brings 15 years of NGO experience focused on education and child rights in West Africa.</p>
                    </div>
                    <div class="campaign-card animate-in" style="text-align: center; padding: 40px 20px; background: #fff;">
                        <div style="width: 120px; height: 120px; border-radius: 50%; background-color: var(--primary-light); margin: 0 auto 20px; border: 4px solid white; box-shadow: 0 10px 20px rgba(0,0,0,0.05);"></div>
                        <h3>Jane Smith</h3>
                        <p style="color: var(--primary); font-weight: 600; font-size: 0.9rem; margin-bottom: 15px;">Head of Programs</p>
                        <p style="font-size: 0.9rem; color: var(--text-light);">Jane oversees all field operations and ensures project milestones are achieved on time.</p>
                    </div>
                    <div class="campaign-card animate-in" style="text-align: center; padding: 40px 20px; background: #fff;">
                        <div style="width: 120px; height: 120px; border-radius: 50%; background-color: var(--primary-light); margin: 0 auto 20px; border: 4px solid white; box-shadow: 0 10px 20px rgba(0,0,0,0.05);"></div>
                        <h3>Kwame Mensah</h3>
                        <p style="color: var(--primary); font-weight: 600; font-size: 0.9rem; margin-bottom: 15px;">Community Outreach</p>
                        <p style="font-size: 0.9rem; color: var(--text-light);">Kwame leads our local engagement initiatives, building trust with community leaders in Tamale.</p>
                    </div>
                </div>
            </div>
        </section>
    </main>

    """
}

# The 6 Program Pages
program_data = [
    {
        'id': 'governance', 
        'name': 'Good Governance', 
        'desc': 'Advocating for transparency, accountability, and strong civic participation.',
        'icon': 'ri-government-line',
        'color': '--card-blue',
        'details': ['Community Leadership Workshops', 'Voter Education Campaigns', 'Local Government Accountability Forums'],
        'impact': 'Over 50 communities have established active citizen accountability forums.',
        'resources': ['Governance Training Manual (PDF)', 'Civic Rights Factsheet']
    },
    {
        'id': 'environment', 
        'name': 'Environmental Sustainability', 
        'desc': 'Protecting our natural resources and promoting sustainable community practices.',
        'icon': 'ri-plant-line',
        'color': '--card-green',
        'details': ['Reforestation & Tree Planting Drives', 'Waste Management Training', 'Sustainable Agriculture Programs'],
        'impact': 'Planted 10,000+ trees and trained 500 farmers in sustainable practices.',
        'resources': ['Sustainable Farming Guide (PDF)', 'Community Recycling Framework']
    },
    {
        'id': 'health', 
        'name': 'Health Education', 
        'desc': 'Providing essential health resources, sanitation awareness, and improving medical care access.',
        'icon': 'ri-heart-pulse-line',
        'color': '--card-pink',
        'details': ['Mobile Health Clinics', 'Maternal & Child Health Seminars', 'WASH (Water, Sanitation and Hygiene) Programs'],
        'impact': 'Reduced local waterborne diseases by 40% through WASH initiatives.',
        'resources': ['WASH Implementation Handbook', 'Maternal Health Checklist']
    },
    {
        'id': 'inclusive-edu', 
        'name': 'Inclusive Education', 
        'desc': 'Ensuring quality education and school partnerships for all children.',
        'icon': 'ri-book-open-line',
        'color': '--card-yellow',
        'details': ['School Accessibility Upgrades', 'Teacher Training on Special Needs', 'Scholarship Programs'],
        'impact': 'Provided scholarships for 200+ marginalized youth and trained 50 teachers.',
        'resources': ['Inclusive Classroom Guide', 'Scholarship Application Form']
    },
    {
        'id': 'trafficking', 
        'name': 'Human Trafficking Prevention', 
        'desc': 'Raising awareness, providing support resources, and protecting the vulnerable.',
        'icon': 'ri-shield-user-line',
        'color': '--card-purple',
        'details': ['Community Awareness Campaigns', 'Survivor Rehabilitation Support', 'Border Community Monitoring'],
        'impact': 'Intercepted and supported 150 potential victims through community watchdogs.',
        'resources': ['Trafficking Indicators List', 'National Hotline Info Card']
    },
    {
        'id': 'child-rights', 
        'name': 'Child Rights Advocacy', 
        'desc': 'Championing the rights framework and resources for child protection.',
        'icon': 'ri-open-arm-line',
        'color': '--card-orange',
        'details': ['Child Labor Prevention Programs', 'Youth Parliament Initiatives', 'Legal Support for Minors'],
        'impact': 'Established 15 Youth Parliaments giving children a voice in local policy.',
        'resources': ['UN CRC Summary for Kids', 'Reporting Abuse Protocol']
    }
]

for prog in program_data:
    file_name = f"program-{prog['id']}.html"
    pages[file_name] = {
        'title': prog['name'],
        'active': 'programs',
        'content': f"""
        <main id="main-content">
            {inner_hero(prog['name'], prog['desc'])}
            <section style="padding: 60px 0;">
                <div class="container" style="max-width: 800px; margin: 0 auto;">
                    <div style="display: flex; align-items: center; gap: 20px; margin-bottom: 40px;">
                        <div style="width: 80px; height: 80px; border-radius: 12px; background: var({prog['color']}); display: flex; align-items: center; justify-content: center; font-size: 2.5rem; color: var(--primary);">
                            <i class="{prog['icon']}"></i>
                        </div>
                        <h2 style="font-size: 2rem;">Description & Objectives</h2>
                    </div>
                    <p style="font-size: 1.1rem; color: var(--text-light); margin-bottom: 40px;">Our {prog['name']} program is designed to create lasting, systemic change at the grassroots level. By focusing on education, direct intervention, and advocacy, we empower communities to take charge of their future.</p>
                    
                    <h3 style="font-size: 1.5rem; margin-bottom: 20px; color: var(--primary);">Current Projects & Initiatives</h3>
                    <ul style="list-style-type: disc; padding-left: 20px; margin-bottom: 40px; color: var(--text-dark); line-height: 1.8;">
                        {''.join([f"<li>{item}</li>" for item in prog['details']])}
                    </ul>

                    <h3 style="font-size: 1.5rem; margin-bottom: 20px; color: var(--primary);">Impact & Beneficiaries</h3>
                    <div style="background: var(--bg-light); padding: 30px; border-radius: 12px; border-left: 4px solid var(--secondary); margin-bottom: 40px;">
                        <p style="font-weight: 600;">{prog['impact']}</p>
                    </div>

                    <h3 style="font-size: 1.5rem; margin-bottom: 20px; color: var(--primary);">Resources & Downloads</h3>
                    <div style="display: flex; flex-direction: column; gap: 10px;">
                        {''.join([f'<a href="#" class="btn btn-outline-pill" style="justify-content: flex-start;"><i class="ri-download-2-line"></i> {item}</a>' for item in prog['resources']])}
                    </div>
                </div>
            </section>
        </main>
        """
    }

# Keep main programs.html as a directory
pages['programs.html'] = {
    'title': 'Our Programs',
    'active': 'programs',
    'content': """
    <main id="main-content">
        """ + inner_hero("Our Programs & Services", "Explore our 6 core focus areas driving change in West Africa.") + """
        <section class="what-we-do" style="padding: 80px 0; background: white;">
            <div class="container">
                <div class="services-grid">
                    """ + "".join([f"""
                    <a href="program-{p['id']}.html" class="service-card">
                        <div class="card-icon" style="background: var({p['color']}); color: var(--primary);"><i class="{p['icon']}"></i></div>
                        <h3>{p['name']}</h3>
                        <p>{p['desc']}</p>
                    </a>
                    """ for p in program_data]) + """
                </div>
            </div>
        </section>
    </main>
    """
}

pages['impact.html'] = {
    'title': 'Our Impact',
    'active': 'impact',
    'content': """
    <main id="main-content">
        """ + inner_hero("Our Impact", "Measuring our success by the lives we touch.") + """
        <!-- DASHBOARD / METRICS -->
        <section class="metrics" style="padding: 80px 0; background: var(--bg-light);">
            <div class="container">
                <div class="stats-grid" style="grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); text-align: center; border: none; padding-top: 0; margin-top: 0;">
                    <div class="stat-block" style="padding: 30px; background: white; border-radius: 12px; box-shadow: 0 4px 6px rgba(0,0,0,0.05);">
                        <h3 style="color: var(--primary); font-size: 2.5rem;">5,000+</h3>
                        <p>Children Educated</p>
                    </div>
                    <div class="stat-block" style="padding: 30px; background: white; border-radius: 12px; box-shadow: 0 4px 6px rgba(0,0,0,0.05);">
                        <h3 style="color: var(--secondary); font-size: 2.5rem;">50+</h3>
                        <p>Communities Reached</p>
                    </div>
                    <div class="stat-block" style="padding: 30px; background: white; border-radius: 12px; box-shadow: 0 4px 6px rgba(0,0,0,0.05);">
                        <h3 style="color: var(--accent); font-size: 2.5rem;">120</h3>
                        <p>Projects Completed</p>
                    </div>
                </div>
            </div>
        </section>

        <!-- GALLERY PORTFOLIO -->
        <section class="gallery-portfolio" style="padding: 80px 0;">
            <div class="container">
                <div class="section-header center" style="margin-bottom: 40px;">
                    <h2 class="section-title">Impact Gallery</h2>
                    <p class="section-text">A visual portfolio of our work across the communities we serve.</p>
                </div>
                
                <div class="gallery-grid" style="display: grid; grid-template-columns: repeat(auto-fill, minmax(280px, 1fr)); gap: 20px;">
                    """ + "".join([f'''
                    <div class="gallery-item" style="border-radius: 12px; overflow: hidden; box-shadow: 0 4px 6px rgba(0,0,0,0.1); transition: transform 0.3s ease; cursor: pointer;" onmouseover="this.style.transform='scale(1.03)'" onmouseout="this.style.transform='scale(1)'">
                        <img src="images/impacts/impacts {i:03d}.jpg" alt="Impact {i}" loading="lazy" style="width: 100%; height: 250px; object-fit: cover; display: block;">
                    </div>''' for i in range(1, 21)]) + """
                </div>
            </div>
        </section>
    </main>
    """
}

pages['donate.html'] = {
    'title': 'Donate',
    'active': 'get_involved',
    'content': """
    <main id="main-content">
        <section class="donate-section" style="padding: 80px 0; background-color: var(--bg-light);">
            <div class="container" style="max-width: 800px;">
                <div class="center" style="margin-bottom: 40px;">
                    <h1 class="section-title">Support Our Cause</h1>
                    <p class="section-text">Your contribution directly funds education, health, and advocacy programs across West Africa. CCEYD is a registered non-profit; your donations may be tax-deductible depending on your local laws.</p>
                </div>
                
                <div style="background: white; border-radius: 16px; box-shadow: 0 10px 25px rgba(0,0,0,0.05); padding: 40px;">
                    
                    <!-- Program Specific -->
                    <div style="margin-bottom: 30px;">
                        <label style="display: block; margin-bottom: 8px; font-weight: 600;">I want to support:</label>
                        <select style="width: 100%; padding: 12px; border: 1px solid #d1d5db; border-radius: 8px; font-family: var(--font-body);">
                            <option>Where it's needed most (General Fund)</option>
                            <option>Good Governance</option>
                            <option>Environmental Sustainability</option>
                            <option>Health Education</option>
                            <option>Inclusive Education</option>
                            <option>Human Trafficking Prevention</option>
                            <option>Child Rights</option>
                        </select>
                    </div>

                    <!-- Frequency -->
                    <div class="btn-group" style="display: flex; gap: 10px; margin-bottom: 30px; flex-wrap: wrap;">
                        <button type="button" class="btn btn-primary freq-btn" id="freq-one-time" style="flex: 1; justify-content: center;">One-time</button>
                        <button type="button" class="btn btn-outline-pill freq-btn" id="freq-monthly" style="flex: 1; justify-content: center;">Monthly Recurring</button>
                    </div>

                    <!-- Amounts with impact text -->
                    <div class="amount-grid" id="amount-grid" style="margin-bottom: 10px;">
                        <button type="button" class="btn btn-outline-pill amount-btn" data-amount="50" style="justify-content: center;">50 GHS</button>
                        <button type="button" class="btn btn-primary amount-btn" data-amount="100" style="justify-content: center;">100 GHS</button>
                        <button type="button" class="btn btn-outline-pill amount-btn" data-amount="250" style="justify-content: center;">250 GHS</button>
                        <button type="button" class="btn btn-outline-pill amount-btn" data-amount="500" style="justify-content: center;">500 GHS</button>
                        <button type="button" class="btn btn-outline-pill amount-btn" data-amount="1000" style="justify-content: center;">1000 GHS</button>
                        <button type="button" class="btn btn-outline-pill amount-btn" data-amount="other" style="justify-content: center;">Other Amount</button>
                    </div>
                    
                    <div id="other-amount-container" style="display: none; margin-bottom: 20px;">
                        <input type="number" id="other-amount-input" placeholder="Enter amount in GHS" style="width: 100%; padding: 12px; border: 1px solid #d1d5db; border-radius: 8px; font-family: var(--font-body);">
                    </div>
                    <p id="impact-text" style="font-size: 0.85rem; color: var(--primary); margin-bottom: 30px; text-align: center; font-style: italic;"><i class="ri-information-line"></i> 100 GHS provides essential school supplies for one child for a year.</p>

                    <!-- Gift option -->
                    <div style="margin-bottom: 30px; display: flex; align-items: center; gap: 10px;">
                        <input type="checkbox" id="gift" style="width: 18px; height: 18px;">
                        <label for="gift" style="font-weight: 500;">Make this donation in honor/memory of someone (Gift Sponsorship)</label>
                    </div>

                    <!-- Payment Methods Info -->
                    <div style="background: #f0fdf4; border: 1px solid #bbf7d0; padding: 20px; border-radius: 8px; margin-bottom: 30px;">
                        <h4 style="color: var(--primary); margin-bottom: 10px; display: flex; align-items: center; gap: 8px;"><i class="ri-smartphone-line"></i> Mobile Money Accepted</h4>
                        <p style="font-size: 0.9rem; color: var(--text-dark);">We support <strong>MTN MoMo</strong>, <strong>Vodafone Cash</strong>, and <strong>AirtelTigo</strong> securely via our payment gateway.</p>
                    </div>

                    <!-- Form -->
                    <form onsubmit="event.preventDefault(); alert('Redirecting to secure Mobile Money / Card payment gateway...');">
                        <div class="grid-2" style="gap: 20px; margin-bottom: 20px;">
                            <div>
                                <label style="display: block; margin-bottom: 8px; font-weight: 500; font-size: 0.9rem;">First Name</label>
                                <input type="text" style="width: 100%; padding: 12px; border: 1px solid #d1d5db; border-radius: 8px;" required>
                            </div>
                            <div>
                                <label style="display: block; margin-bottom: 8px; font-weight: 500; font-size: 0.9rem;">Last Name</label>
                                <input type="text" style="width: 100%; padding: 12px; border: 1px solid #d1d5db; border-radius: 8px;" required>
                            </div>
                        </div>
                        <div style="margin-bottom: 30px;">
                            <label style="display: block; margin-bottom: 8px; font-weight: 500; font-size: 0.9rem;">Email Address (For Tax Receipt)</label>
                            <input type="email" style="width: 100%; padding: 12px; border: 1px solid #d1d5db; border-radius: 8px;" required>
                        </div>
                        
                        <button type="submit" class="btn btn-primary" style="width: 100%; justify-content: center; font-size: 1.1rem; padding: 16px;">Proceed to Payment <i class="ri-secure-payment-line"></i></button>
                    </form>
                </div>
            </div>
        </section>
    </main>
    """
}

pages['volunteer.html'] = {
    'title': 'Volunteer',
    'active': 'get_involved',
    'content': """
    <main id="main-content">
        """ + inner_hero("Volunteer With Us", "Join our global network of changemakers.") + """
        <section style="padding: 80px 0;">
            <div class="container" style="max-width: 1000px;">
                <div class="grid-2">
                    <div>
                        <h2 class="section-title">Why Volunteer?</h2>
                        <ul style="list-style-type: none; padding: 0; display: flex; flex-direction: column; gap: 16px; margin-bottom: 40px;">
                            <li style="display: flex; gap: 12px;"><i class="ri-check-line" style="color: var(--primary); font-size: 1.5rem;"></i> Make a direct impact in local communities.</li>
                            <li style="display: flex; gap: 12px;"><i class="ri-check-line" style="color: var(--primary); font-size: 1.5rem;"></i> Gain fieldwork and NGO experience.</li>
                            <li style="display: flex; gap: 12px;"><i class="ri-check-line" style="color: var(--primary); font-size: 1.5rem;"></i> Receive training and a certificate of service.</li>
                        </ul>
                        
                        <h3 style="margin-bottom: 20px; font-size: 1.5rem;">Open Positions</h3>
                        <div style="border: 1px solid #e5e7eb; border-radius: 12px; padding: 20px; margin-bottom: 16px;">
                            <h4 style="color: var(--primary); margin-bottom: 8px;">Field Educator (Tamale)</h4>
                            <p style="font-size: 0.9rem; color: var(--text-light);">Assist in organizing WASH seminars in rural schools.</p>
                        </div>
                        <div style="border: 1px solid #e5e7eb; border-radius: 12px; padding: 20px;">
                            <h4 style="color: var(--primary); margin-bottom: 8px;">Digital Advocate (Remote)</h4>
                            <p style="font-size: 0.9rem; color: var(--text-light);">Help manage our social media and human trafficking awareness campaigns online.</p>
                        </div>
                    </div>
                    
                    <div style="background: var(--bg-light); padding: 40px; border-radius: 12px;">
                        <h3 style="margin-bottom: 20px; font-size: 1.5rem;">Volunteer Application</h3>
                        <form onsubmit="event.preventDefault(); alert('Application submitted successfully!');">
                            <div style="margin-bottom: 16px;">
                                <label style="display: block; margin-bottom: 8px; font-weight: 500; font-size: 0.9rem;">Full Name</label>
                                <input type="text" style="width: 100%; padding: 12px; border: 1px solid #d1d5db; border-radius: 8px;" required>
                            </div>
                            <div style="margin-bottom: 16px;">
                                <label style="display: block; margin-bottom: 8px; font-weight: 500; font-size: 0.9rem;">Email</label>
                                <input type="email" style="width: 100%; padding: 12px; border: 1px solid #d1d5db; border-radius: 8px;" required>
                            </div>
                            <div style="margin-bottom: 16px;">
                                <label style="display: block; margin-bottom: 8px; font-weight: 500; font-size: 0.9rem;">Area of Interest</label>
                                <select style="width: 100%; padding: 12px; border: 1px solid #d1d5db; border-radius: 8px;">
                                    <option>Field Work (Ghana)</option>
                                    <option>Remote/Digital Advocacy</option>
                                    <option>Fundraising</option>
                                </select>
                            </div>
                            <div style="margin-bottom: 24px;">
                                <label style="display: block; margin-bottom: 8px; font-weight: 500; font-size: 0.9rem;">Tell us why you want to join</label>
                                <textarea rows="4" style="width: 100%; padding: 12px; border: 1px solid #d1d5db; border-radius: 8px;" required></textarea>
                            </div>
                            <button type="submit" class="btn btn-primary" style="width: 100%; justify-content: center;">Submit Application</button>
                        </form>
                    </div>
                </div>
            </div>
        </section>
    </main>
    """
}

pages['partner.html'] = {
    'title': 'Partner With Us',
    'active': 'get_involved',
    'content': """
    <main id="main-content">
        """ + inner_hero("Partner With CCEYD", "Corporate sponsorships and NGO collaborations.") + """
        <section style="padding: 80px 0;">
            <div class="container center" style="max-width: 800px;">
                <h2 class="section-title">Let's Build the Future Together</h2>
                <p class="section-text">We actively seek partnerships with corporations, government bodies, and other NGOs to scale our impact. Whether through CSR funding, capacity building, or joint field operations, your organization can play a pivotal role.</p>
                
                <div class="grid-2" style="margin: 60px 0; text-align: left;">
                    <div style="background: white; padding: 30px; border-radius: 12px; box-shadow: 0 4px 6px rgba(0,0,0,0.05);">
                        <i class="ri-building-4-line" style="font-size: 2.5rem; color: var(--secondary); margin-bottom: 16px; display: block;"></i>
                        <h3 style="margin-bottom: 12px;">Corporate Sponsorships</h3>
                        <p style="font-size: 0.9rem; color: var(--text-light);">Fulfill your Corporate Social Responsibility goals by sponsoring our education or health initiatives. Receive detailed impact reports for your stakeholders.</p>
                    </div>
                    <div style="background: white; padding: 30px; border-radius: 12px; box-shadow: 0 4px 6px rgba(0,0,0,0.05);">
                        <i class="ri-shake-hands-line" style="font-size: 2.5rem; color: var(--primary); margin-bottom: 16px; display: block;"></i>
                        <h3 style="margin-bottom: 12px;">NGO Collaborations</h3>
                        <p style="font-size: 0.9rem; color: var(--text-light);">Share resources, data, and manpower on the ground in West Africa to tackle complex issues like human trafficking and climate change together.</p>
                    </div>
                </div>

                <a href="contact.html" class="btn btn-primary" style="font-size: 1.1rem; padding: 16px 32px;">Contact Our Partnerships Team</a>
            </div>
        </section>
    </main>
    """
}

pages['contact.html'] = {
    'title': 'Contact & Location',
    'active': 'contact',
    'content': """
    <main id="main-content">
        """ + inner_hero("Contact Us", "We'd love to hear from you. Get in touch with our team in Tamale.") + """
        <section style="padding: 80px 0;">
            <div class="container">
                <div class="grid-2">
                    
                    <!-- Contact Info -->
                    <div>
                        <h2 class="section-title">Our Office</h2>
                        <p style="color: var(--text-light); margin-bottom: 40px;">Centre For Communities Education and Youth Development</p>
                        
                        <div style="display: flex; flex-direction: column; gap: 24px; margin-bottom: 40px;">
                            <div style="display: flex; gap: 16px; align-items: flex-start;">
                                <div style="width: 48px; height: 48px; background: var(--bg-light); border-radius: 8px; display: flex; align-items: center; justify-content: center; color: var(--primary); font-size: 1.5rem;"><i class="ri-map-pin-line"></i></div>
                                <div>
                                    <h4 style="margin-bottom: 4px;">Address</h4>
                                    <p style="color: var(--text-light); font-size: 0.95rem;">123 NGO Street<br>Tamale, Northern Region<br>Ghana, West Africa</p>
                                </div>
                            </div>
                            <div style="display: flex; gap: 16px; align-items: flex-start;">
                                <div style="width: 48px; height: 48px; background: var(--bg-light); border-radius: 8px; display: flex; align-items: center; justify-content: center; color: var(--primary); font-size: 1.5rem;"><i class="ri-phone-line"></i></div>
                                <div>
                                    <h4 style="margin-bottom: 4px;">Phone & Office Hours</h4>
                                    <p style="color: var(--text-light); font-size: 0.95rem;">+233242625055<br>Mon-Fri, 9:00 AM - 5:00 PM GMT</p>
                                </div>
                            </div>
                            <div style="display: flex; gap: 16px; align-items: flex-start;">
                                <div style="width: 48px; height: 48px; background: var(--bg-light); border-radius: 8px; display: flex; align-items: center; justify-content: center; color: var(--primary); font-size: 1.5rem;"><i class="ri-mail-line"></i></div>
                                <div>
                                    <h4 style="margin-bottom: 4px;">Email</h4>
                                    <p style="color: var(--text-light); font-size: 0.95rem;">contact@cceyd.org</p>
                                </div>
                            </div>
                        </div>

                        <!-- Map Placeholder -->
                        <div style="width: 100%; height: 250px; background: #e5e7eb; border-radius: 12px; display: flex; align-items: center; justify-content: center; color: #9ca3af;">
                            <i class="ri-map-2-line" style="font-size: 3rem;"></i>
                            <span style="margin-left: 10px;">Google Maps Integration Placeholder</span>
                        </div>
                    </div>

                    <!-- Contact Form -->
                    <div style="background: white; padding: 40px; border-radius: 12px; box-shadow: 0 10px 25px rgba(0,0,0,0.05);">
                        <h3 style="margin-bottom: 24px; font-size: 1.5rem;">Send a Quick Inquiry</h3>
                        <form onsubmit="event.preventDefault(); alert('Message sent!');">
                            <div style="margin-bottom: 16px;">
                                <label style="display: block; margin-bottom: 8px; font-weight: 500; font-size: 0.9rem;">Your Name</label>
                                <input type="text" style="width: 100%; padding: 12px; border: 1px solid #d1d5db; border-radius: 8px;" required>
                            </div>
                            <div style="margin-bottom: 16px;">
                                <label style="display: block; margin-bottom: 8px; font-weight: 500; font-size: 0.9rem;">Email Address</label>
                                <input type="email" style="width: 100%; padding: 12px; border: 1px solid #d1d5db; border-radius: 8px;" required>
                            </div>
                            <div style="margin-bottom: 16px;">
                                <label style="display: block; margin-bottom: 8px; font-weight: 500; font-size: 0.9rem;">Subject</label>
                                <input type="text" style="width: 100%; padding: 12px; border: 1px solid #d1d5db; border-radius: 8px;" required>
                            </div>
                            <div style="margin-bottom: 24px;">
                                <label style="display: block; margin-bottom: 8px; font-weight: 500; font-size: 0.9rem;">Message</label>
                                <textarea rows="5" style="width: 100%; padding: 12px; border: 1px solid #d1d5db; border-radius: 8px;" required></textarea>
                            </div>
                            <button type="submit" class="btn btn-primary" style="width: 100%; justify-content: center;">Send Message <i class="ri-send-plane-line"></i></button>
                        </form>
                    </div>

                </div>
            </div>
        </section>
    </main>
    """
}

# --- BUILD PROCESS ---
page_descriptions = {
    'index.html': 'CCEYD advocates for good governance, environmental sustainability, health education, inclusive education, human trafficking prevention, and child rights.',
    'about.html': 'Learn about CCEYD, our history, mission, core values, and the leadership team driving our grassroots development across West Africa.',
    'programs.html': 'Explore CCEYDs 6 core focus areas driving systemic change in West Africa, from Good Governance to Child Rights.',
    'program-governance.html': 'CCEYD advocates for good governance, transparency, and accountability through community leadership and voter education.',
    'program-environment.html': 'Discover our environmental sustainability programs including reforestation, waste management, and sustainable agriculture.',
    'program-health.html': 'Our health education initiatives provide essential resources, sanitation awareness, and mobile health clinics.',
    'program-inclusive-edu.html': 'CCEYD ensures quality inclusive education and school partnerships for all children, including scholarships.',
    'program-trafficking.html': 'We work on human trafficking prevention by raising awareness, supporting survivors, and border monitoring.',
    'program-child-rights.html': 'Championing child rights advocacy through youth parliaments, legal support, and child labor prevention.',
    'impact.html': 'View the impact and success stories of CCEYD. Over 5,000 children educated and 120 projects completed.',
    'donate.html': 'Support our cause. Your donation directly funds education, health, and advocacy programs across West Africa.',
    'volunteer.html': 'Join our global network of changemakers. Volunteer with CCEYD for fieldwork or digital advocacy.',
    'partner.html': 'Partner with CCEYD. We seek corporate sponsorships, NGO alliances, and government partnerships to scale impact.',
    'contact.html': 'Get in touch with the CCEYD team in Tamale, Ghana. Find our email, phone, and office hours.'
}

import datetime
from urllib.parse import urljoin

base_url = "https://cceyd.org/"
sitemap_urls = []

for filename, data in pages.items():
    desc = page_descriptions.get(filename, "Empowering communities worldwide for positive change.")
    canonical = urljoin(base_url, filename)
    
    html_content = get_header(data['title'], data['active'], desc=desc, canonical_url=canonical) + data['content'] + FOOTER
    with open(filename, 'w') as f:
        f.write(html_content)
        
    sitemap_urls.append(f"""  <url>
    <loc>{canonical}</loc>
    <lastmod>{datetime.datetime.now().strftime("%Y-%m-%d")}</lastmod>
    <changefreq>monthly</changefreq>
    <priority>{1.0 if filename == 'index.html' else 0.8}</priority>
  </url>""")

# Generate Sitemap
sitemap_content = f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
{chr(10).join(sitemap_urls)}
</urlset>"""
with open('sitemap.xml', 'w') as f:
    f.write(sitemap_content)

# Generate robots.txt
with open('robots.txt', 'w') as f:
    f.write(f"User-agent: *\nAllow: /\n\nSitemap: {urljoin(base_url, 'sitemap.xml')}")

print(f"Successfully generated {len(pages)} pages, sitemap.xml, and robots.txt.")
