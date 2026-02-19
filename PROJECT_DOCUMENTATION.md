# Smart Text Analyzer - Project Documentation

## 1. Project Overview
**Smart Text Analyzer** is an advanced, AI-powered writing assistant designed to elevate text quality through comprehensive analysis. It transcends basic grammar checking by integrating sophisticated features such as tone detection, plagiarism checking, AI text humanization, and intelligent document interaction via RAG (Retrieval-Augmented Generation).

## 2. Technical Stack
- **Frontend**: React (Vite+SWC), Tailwind CSS, Framer Motion
- **Design**: Glassmorphism, Neon UI, Dual-Theme (Dark/Light)
- **Backend**: Python Flask (Planned)
- **Database**: ChromaDB (Vector), SQLite/PostgreSQL (Relational)
- **AI/ML**: LangChain, Hugging Face Transformers

## 3. Project Structure
```
root/
├── sample/
│   ├── public/
│   │   └── vite.svg
│   ├── src/
│   │   ├── assets/
│   │   │   ├── motion/ (Animation frames)
│   │   │   └── team/ (Team images)
│   │   ├── components/
│   │   │   ├── ui/
│   │   │   │   ├── Button.jsx
│   │   │   │   ├── Card.tsx
│   │   │   │   └── Spotlight.tsx
│   │   │   ├── About.jsx
│   │   │   ├── AboutPage.jsx
│   │   │   ├── ActivityPulse.jsx
│   │   │   ├── Compare.jsx
│   │   │   ├── Dashboard.jsx
│   │   │   ├── EditorTab.jsx
│   │   │   ├── Features.jsx
│   │   │   ├── FeaturesPage.jsx
│   │   │   ├── Footer.jsx
│   │   │   ├── Hero.jsx
│   │   │   ├── Navbar.jsx
│   │   │   ├── ParticleCanvas.jsx
│   │   │   ├── SplineSceneBasic.tsx
│   │   │   └── WelcomeScreen.jsx
│   │   ├── lib/
│   │   │   └── utils.js
│   │   ├── App.jsx
│   │   ├── index.css
│   │   └── main.jsx
│   ├── index.html
│   ├── package.json
│   ├── postcss.config.cjs
│   ├── tailwind.config.js
│   └── vite.config.js
├── PRD.md
└── PROJECT_DOCUMENTATION.md
```

## 4. Product Requirements (PRD)
*(See `PRD.md` for full details)*

### Core Goals
- **Enhance Writing Precision**: Real-time grammar, style, and tone feedback.
- **Guarantee Content Integrity**: Robust plagiarism detection.
- **Bridge AI-Human Gap**: "Humanizer" tools for natural text flow.
- **Document Intelligence**: RAG-powered chat for PDF documents.

### Functional Requirements
1.  **Editor**: Real-time analysis of grammar, tone, and style.
2.  **Dashboard**: User analytics, document history.
3.  **Document Chat**: Upload PDFs and query them using AI.
4.  **Security**: End-to-end encryption for user data.

## 5. Design System
*(See `sample/DESIGN.md` for full details)*

### Visual Identity
- **Dark Mode (Default)**: Deep black (`#030304`) with Neon Green (`#00FF9D`) accents.
- **Light Mode**: Soft blue-grey gradients with Vibrant Blue (`#3b82f6`).
- **Typography**: `Outfit` for headings, `Inter` for body text.

### Key Components
- **Magnetic Button**: Interactive button with magnetic pull effect.
- **Glass Panel**: Translucent backgrounds with `backdrop-filter: blur(12px)`.
- **Chromatic Text**: Text with RGB split effect on hover.
- **Particle Canvas**: Kinetic background effect.

## 6. Setup Instructions

### Prerequisites
- Node.js (v18+)
- Python (v3.10+)

### Installation
1.  **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/Smart_Text_Analyzer.git
    cd Smart_Text_Analyzer/sample
    ```

2.  **Install Frontend Dependencies**:
    ```bash
    npm install
    ```

3.  **Start Development Server**:
    ```bash
    npm run dev
    ```

4.  **Build for Production**:
    ```bash
    npm run build
    ```

## 7. Development Guidelines
- **Commits**: Use conventional commits (e.g., `feat: add tone detection`, `fix: header alignment`).
- **Styling**: Use utility classes (Tailwind) primarily. Create custom components in `src/components/ui` for complex UI elements.
- **State**: Use React Context for global themes and user sessions.

## 8. Roadmap
- **Phase 1**: Core Editor & UI (Complete)
- **Phase 2**: Backend API & Auth (In Progress)
- **Phase 3**: Browser Extension
- **Phase 4**: Team Collaboration Features
