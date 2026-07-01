import re

with open("build_site.py", "r") as f:
    content = f.read()

about_html = '''        <!-- INNER HERO -->
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
'''

# Find the start and end of about.html content
match = re.search(r'(pages\[\'about\.html\'\] = \{\n.*?\'content\': """)([\s\S]*?)(\n    """\n\})', content)
if match:
    new_content = content[:match.start(2)] + "\n    <main id=\"main-content\">\n" + about_html + "\n    </main>" + content[match.end(2):]
    with open("build_site.py", "w") as f:
        f.write(new_content)
    print("Updated about.html content")
else:
    print("Could not find about.html block")

