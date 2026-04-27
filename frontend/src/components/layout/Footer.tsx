export default function Footer() {
    return (
        <footer className="flex items-center justify-between px-4 py-3 border-t border-border bg-bg text-sm text-text-muted">
            {/* Left */}
            <div>
                © {new Date().getFullYear()} KC SpotifyAnalyzer
            </div>

            {/* Center (optional metadata) */}
            <div className="hidden md:block">
                v1.0.0
            </div>

            {/* Right */}
            <a
                href="https://github.com/Zancmok/KCSpotifyAnalyzer"
                target="_blank"
                rel="noopener noreferrer"
                className="hover:text-brand transition"
            >
                GitHub
            </a>
        </footer>
    );
}
