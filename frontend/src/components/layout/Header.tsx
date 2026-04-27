const FALLBACK_AVATAR = "https://picsum.photos/seed/account/40/40";

type HeaderProps = {
    title?: string;
    onLogoClick?: () => void;
    avatarUrl?: string;
};

export default function Header({ title = "Home", onLogoClick, avatarUrl }: HeaderProps) {
    return (
        <header className="flex items-center justify-between px-4 py-3 border-b border-border bg-bg">
            {/* Logo */}
            <button
                onClick={onLogoClick}
                className="font-bold text-lg tracking-tight hover:text-brand transition"
            >
                KC SpotifyAnalyzer
            </button>

            {/* Center label */}
            <div className="text-sm text-text-muted">
                {title}
            </div>

            {/* Avatar */}
            <button
                className="w-9 h-9 rounded-full overflow-hidden ring-2 ring-transparent hover:ring-brand transition"
                aria-label="Account"
            >
                <img
                    src={avatarUrl ?? FALLBACK_AVATAR}
                    alt="Profile"
                    className="w-full h-full object-cover"
                />
            </button>
        </header>
    );
}
