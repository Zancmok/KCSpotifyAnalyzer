export default function Home()
{
    function onClick(): void
    {
        console.log("Button clicked!");
    }

    return (
        <div className="min-h-screen text-white flex flex-col items-center justify-center px-4">
            <h1 className="text-4xl md:text-5xl font-bold py-4 text-green-600">
                KC SpotifyAnalyzer
            </h1>

            <p className="standart-text text-center max-w-xl mb-8">
                KC SpotifyAnalyzer is a tool for advanced analysis of your Spotify data. 
                Discover listening patterns, explore detailed statistics, and compare your music taste with your friends.
            </p>

            <button onClick={onClick} className="green-button">
                Get Started
            </button>
        </div>
    );
}
