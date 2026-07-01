with open("build_site.py", "r") as f:
    lines = f.readlines()

# 1. Fix FOOTER (line 193 is </footer>, line 194 is ''')
lines[193] = "    </footer>\n    <script src=\"script.js\"></script>\n</body>\n</html>\n"

# 2. Fix index.html (lines 213 to 332 in 0-indexed form are 214-333)
# We will replace lines 213 to 333 (0-indexed) with the new index_html

index_html = '''    <main id="main-content">
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
'''

new_lines = lines[:213] + [index_html + "\n"] + lines[333:]

with open("build_site.py", "w") as f:
    f.writelines(new_lines)

