# 🚀 Gaurav Sharma - Portfolio Website

A modern, responsive portfolio website showcasing my skills, projects, and experience as a Backend Developer specializing in Python and Flask. Built with a live feedback system powered by MySQL database hosted on Aiven Cloud.

![Portfolio Preview](https://img.shields.io/badge/Status-Live-success?style=for-the-badge)
![Deployed on Render](https://img.shields.io/badge/Deployed%20on-Render-46E3B7?style=for-the-badge&logo=render&logoColor=white)
![HTML](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)

## 🌐 Live Demo

**Portfolio URL:** [https://bitcrafter21.onrender.com]

## ✨ Features

### 🎨 Design
- **Dark Modern Theme** with elegant gradient effects
- **Glass-morphism UI** with backdrop blur effects
- **Responsive Design** - Works perfectly on all devices (Desktop, Tablet, Mobile)
- **Smooth Animations** - Minimal and professional animations
- **Gradient Accents** - Beautiful color transitions throughout
- **Mobile Navigation** - Animated hamburger menu for mobile devices

### 🎭 Animations & Interactions
- Floating particle system in hero section
- Smooth fade-in effects on scroll
- Interactive hover states on all cards
- Glowing logo effect with pulsing animation
- Animated scroll indicator
- Sequential text reveal animations
- Staggered mobile menu item animations

### 📱 Sections
1. **Hero Section** - Eye-catching introduction with tech stack badges
2. **About** - Professional summary and background
3. **Skills** - Categorized technical skills with hover effects
4. **Experience** - Smart India Hackathon participation details
5. **Projects** - Featured work with detailed descriptions
6. **Certifications** - Professional credentials and achievements
7. **Contact** - Interactive feedback form with database integration

## 🛠️ Technologies Used

### Frontend
- **HTML5** - Semantic markup
- **CSS3** - Modern styling with animations
  - CSS Grid & Flexbox
  - CSS Variables for theming
  - Backdrop Filters for glass-morphism
  - Keyframe Animations
- **Vanilla JavaScript** - Interactive features
  - Intersection Observer API
  - Smooth Scrolling
  - Dynamic Particle System

### Backend & Database
- **Python3** - Flask Framework - A lightweight framework for small projects

### Deployment
- **Render** - Web hosting platform
- **Continuous Deployment** - Auto-deploy from GitHub

## 🏗️ Architecture

```
Portfolio Architecture
│
├── Frontend (Static Files)
│   ├── index.html
│   ├── Embedded CSS
│   └── Embedded JavaScript
│
├── Backend (Render)
    ├── Python3 app.py
```

## 🚀 Getting Started

### Prerequisites
- Git installed on your machine
- Modern web browser (Chrome, Firefox, Safari, Edge)

### Local Installation

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/portfolio.git
cd portfolio
```

2. **Open in browser**
```bash
# Method 1: Direct file open
# Simply open index.html in your browser

# Method 2: Using Python
python -m http.server 8000
# Then visit http://localhost:8000

# Method 3: Using Node.js
npx serve
```

### Deployment on Render

1. **Push to GitHub**
```bash
git add .
git commit -m "Initial commit"
git push origin main
```

2. **Deploy on Render**
   - Sign up at [Render.com](https://render.com)
   - Create new Web Service
   - Connect your GitHub repository
   - Configure build settings
   - Deploy!


## 🎨 Customization

### Changing Colors
Edit the CSS variables in the `:root` selector:
```css
:root {
    --primary: #6366f1;     /* Primary blue */
    --secondary: #8b5cf6;   /* Secondary purple */
    --accent: #ec4899;      /* Accent pink */
    --dark: #0f172a;        /* Dark background */
    --dark-light: #1e293b;  /* Light dark shade */
}
```

### Adding Projects
Add a new project card in the projects section:
```html
<div class="project-card fade-in">
    <div class="project-header">
        <h3>Your Project Name</h3>
        <div class="project-date">Month Year</div>
    </div>
    <div class="project-body">
        <ul>
            <li>Feature or achievement 1</li>
            <li>Feature or achievement 2</li>
            <li>Feature or achievement 3</li>
        </ul>
    </div>
</div>
```

### Updating Skills
Modify the skill categories in the skills section:
```html
<div class="skill-category fade-in">
    <h3>Category Name</h3>
    <div class="skill-tags">
        <span class="skill-tag">Skill 1</span>
        <span class="skill-tag">Skill 2</span>
        <span class="skill-tag">Skill 3</span>
    </div>
</div>
```

## 📂 Project Structure

```
portfolio/
│
├── index.html              # Main HTML file with embedded CSS & JS
├── README.md              # Project documentation
├── .gitignore             # Git ignore file
│
├── backend/               # (Optional) Backend API files
│   ├── app.py            # Flask/FastAPI application
│   ├── db.py             # Database connection
│   ├── requirements.txt  # Python dependencies
│   └── .env              # Environment variables
│
└── assets/               # (Optional) Additional assets
    ├── images/           # Portfolio images
    ├── icons/            # Custom icons
    └── documents/        # Downloadable documents
```

## 🌟 Key Highlights

- ✅ **No Frontend Framework Dependencies** - Pure HTML, CSS, and JavaScript
- ✅ **Fast Loading** - Optimized for performance
- ✅ **SEO Friendly** - Semantic HTML structure
- ✅ **Accessible** - Follows web accessibility guidelines
- ✅ **Cross-Browser Compatible** - Works on all modern browsers
- ✅ **Mobile-First Design** - Responsive on all devices
- ✅ **Cloud Database** - Scalable and reliable data storage
- ✅ **Continuous Deployment** - Auto-deploy from GitHub to Render
- ✅ **Real-time Feedback** - Live form submissions to MySQL database

## 🔒 Security Features

- ✅ Input validation on client-side
- ✅ Server-side validation and sanitization
- ✅ Prepared statements to prevent SQL injection
- ✅ HTTPS encryption (via Render)
- ✅ Environment variables for sensitive data
- ✅ Rate limiting on form submissions

## 📸 Screenshots
<img width="1920" height="1080" alt="Screenshot from 2025-11-01 00-45-52" src="https://github.com/user-attachments/assets/0b854a6f-fcf2-4fb9-a879-6ebd05ed23a9" />
<img width="1920" height="1080" alt="Screenshot from 2025-11-01 00-45-47" src="https://github.com/user-attachments/assets/8a149bb4-3c91-4c77-99f0-54f011138366" />
<img width="1920" height="1080" alt="Screenshot from 2025-11-01 00-45-42" src="https://github.com/user-attachments/assets/5e05530d-bc85-470c-961a-103cfd7bf44c" />
<img width="1920" height="1080" alt="Screenshot from 2025-11-01 00-45-37" src="https://github.com/user-attachments/assets/41494287-43b2-40e4-acde-92f41318063f" />
<img width="1920" height="1080" alt="Screenshot from 2025-11-01 00-45-27" src="https://github.com/user-attachments/assets/0c4fe7c8-01f3-4c90-90c3-99cc65134a43" />
<img width="1920" height="1080" alt="Screenshot from 2025-11-01 00-45-21" src="https://github.com/user-attachments/assets/a17fba48-f343-4a06-825c-da1618bd8358" />
<img width="1920" height="1080" alt="Screenshot from 2025-11-01 00-45-07" src="https://github.com/user-attachments/assets/49c69d8b-e4e9-4c1e-add5-078348120265" />

## 🎯 Future Enhancements

- [ ] Add dark/light theme toggle
- [ ] Implement admin dashboard for viewing feedback
- [ ] Add blog section with CMS integration
- [ ] Include project case studies with detailed pages
- [ ] Add analytics integration (Google Analytics)
- [ ] Implement progressive web app (PWA) features
- [ ] Add email notifications for form submissions
- [ ] Create API documentation page
- [ ] Add multilingual support (i18n)
- [ ] Integrate social media feeds
- [ ] Add visitor counter and analytics dashboard

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the [issues page](https://github.com/bitcrafter21/portfolio/issues).

### How to Contribute

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 👤 Author

**Gaurav Sharma**

- 📍 Location: Mahesana, Gujarat, India
- 💼 LinkedIn: [bitcrafter21](https://linkedin.com/in/bitcrafter21)
- 🐙 GitHub: [bitcrafter21](https://github.com/bitcrafter21)
- 🌐 Portfolio: [Your Render URL]
- 📧 Email: your.email@example.com

## 🔗 Links

- **Live Site:** [https://bitcrafter21.onrender.com]
- **GitHub Repository:** [https://github.com/yourusername/portfolio](https://github.com/bitcrafter21/portfolio)
- **Render Dashboard:** [https://dashboard.render.com](https://dashboard.render.com)

## 💖 Show your support

Give a ⭐️ if you like this project!

## 🙏 Acknowledgments

- Design inspiration from modern portfolio trends
- [Render](https://render.com) for seamless deployment
- Icons and emojis for visual enhancement
- The open-source community for continuous learning
- Smart India Hackathon for the opportunity to participate
- All visitors and feedback contributors

## 📈 Performance

- **Lighthouse Score:** 95+
- **Page Load Time:** < 2 seconds
- **Mobile Responsive:** 100%
- **Accessibility Score:** 90+
- **SEO Score:** 95+

## 🐛 Known Issues

- None currently reported

If you find any bugs, please report them in the [issues section](https://github.com/yourusername/portfolio/issues).

## 📞 Support

For support, email bitcrafter21@gmail.com or open an issue on GitHub.

---

**Built with 💙 by Gaurav Sharma**

*Deployed on Render*

*Last Updated: November 2025*

---

### 🚀 Quick Deploy Commands

```bash
# Clone the repository
git clone https://github.com/bitcrafter21/portfolio.git

# Navigate to project
cd portfolio

# Install dependencies (if using backend)
pip install -r requirements.txt

# Run locally (if using backend)
python app.py

# Deploy to Render (automatic via GitHub integration)
git push origin main
```

---

**⭐ Star this repository if you found it helpful!**
