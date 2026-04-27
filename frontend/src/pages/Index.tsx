import { useAuth } from "../hooks/useAuth";

export default function Index() {
    const { login } = useAuth();

    return (
        <div className="min-h-screen flex flex-col items-center justify-center px-4">
            <h1 className="text-4xl md:text-5xl font-bold py-4 text-brand">
                KC SpotifyAnalyzer
            </h1>

            <p className="text-text-muted text-center max-w-xl mb-8">
                KC SpotifyAnalyzer is a tool for advanced analysis of your Spotify data.
                Discover listening patterns, explore detailed statistics, and compare your music taste with your friends.
            </p>

            <button
                onClick={login}
                className="bg-brand text-bg font-semibold px-8 py-3 rounded-full hover:brightness-110 transition"
            >
                Get Started
            </button>
        </div>
    );
}
