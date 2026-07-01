import re

with open("build_site.py", "r") as f:
    content = f.read()

# Replace get_header
header_new = """def get_header(active_nav=""):
    def active_class(name):
        return 'class="active"' if active_nav == name else ''
    
    def active_dropdown(group):
        groups = {
            'programs': ['program_governance', 'program_environment', 'program_health', 'program_inclusive_edu', 'program_trafficking', 'program_child_rights'],
            'get_involved': ['donate', 'volunteer', 'partner']
        }
        return 'class="dropdown active"' if active_nav in groups.get(group, []) else 'class="dropdown"'

    return f'''
    <!-- LOADER -->
    <div id="loader" class="loader-container">
        <div class="loader-spinner"></div>
    </div>
    <noscript>
        <style>
            #loader {{ display: none !important; }}
        </style>
    </noscript>

    <a href="#main-content" class="skip-link">Skip to main content</a>

    <!-- ====== HEADER ====== -->
    <header class="header" id="header">
        <div class="container header-container">
            <a href="index.html" class="logo" aria-label="CCEYD Home">
                <img src="images/logo.png" alt="CCEYD Logo" style="height: 60px; width: auto; border-radius: 8px;">
            </a>

            <nav class="nav-links" aria-label="Main Navigation">
                <a href="index.html" {active_class('home')}>HOME</a>
                <a href="about.html" {active_class('about')}>ABOUT US</a>

                <div class="nav-item-dropdown">
                    <a href="programs.html" {active_dropdown('programs')} aria-haspopup="true" aria-expanded="false">PROGRAMS <i class="ri-arrow-down-s-line"></i></a>
                    <div class="dropdown-menu" aria-label="Programs submenu">
                        <a href="program-governance.html">Good Governance</a>
                        <a href="program-environment.html">Environmental Sustainability</a>
                        <a href="program-health.html">Health Education</a>
                        <a href="program-inclusive-edu.html">Inclusive Education</a>
                        <a href="program-trafficking.html">Human Trafficking Prevention</a>
                        <a href="program-child-rights.html">Child Rights</a>
                    </div>
                </div>

                <a href="impact.html" {active_class('impact')}>IMPACT</a>

                <div class="nav-item-dropdown">
                    <a href="#" {active_dropdown('get_involved')} aria-haspopup="true" aria-expanded="false">GET INVOLVED <i class="ri-arrow-down-s-line"></i></a>
                    <div class="dropdown-menu" aria-label="Get Involved submenu">
                        <a href="donate.html">Donate</a>
                        <a href="volunteer.html">Volunteer</a>
                        <a href="partner.html">Partner With Us</a>
                    </div>
                </div>

                <a href="contact.html" {active_class('contact')}>CONTACT US</a>
            </nav>

            <div class="header-right">
                <a href="donate.html" class="btn btn-primary btn-sm" id="header-donate-btn">DONATE NOW</a>

                <button class="mobile-menu-btn" aria-label="Toggle Menu" aria-expanded="false" id="mobile-menu-toggle">
                    <i class="ri-menu-3-line"></i>
                </button>
            </div>
        </div>
    </header>

    <!-- Mobile Nav Overlay -->
    <div class="mobile-overlay" id="mobile-overlay"></div>
    <nav class="mobile-nav" id="mobile-nav" aria-label="Mobile Navigation">
        <div class="mobile-nav-header">
            <span class="logo"><img src="images/logo.png" alt="CCEYD Logo" style="height: 40px; width: auto; border-radius: 4px;"></span>
            <button class="mobile-nav-close" id="mobile-nav-close" aria-label="Close Menu"><i class="ri-close-line"></i></button>
        </div>
        <a href="index.html">Home</a>
        <a href="about.html">About Us</a>
        <a href="programs.html">Programs</a>
        <a href="impact.html">Impact</a>
        <a href="volunteer.html">Volunteer</a>
        <a href="contact.html">Contact Us</a>
        <a href="donate.html" class="btn btn-primary" style="margin-top:20px; display:block; text-align:center;">Donate Now</a>
    </nav>
    '''
"""
content = re.sub(r'def get_header\(active_nav=""\):.*?(?=\nFOOTER = )', header_new, content, flags=re.DOTALL)

# Replace FOOTER
footer_new = """FOOTER = '''
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
'''
"""
content = re.sub(r'FOOTER = """.*?(?=\ndef inner_hero)', footer_new, content, flags=re.DOTALL)

with open("build_site.py", "w") as f:
    f.write(content)

