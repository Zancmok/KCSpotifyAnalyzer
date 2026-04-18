import {
    HomeIcon
} from "@heroicons/react/24/outline";

import IconLink from "../components/IconLink.tsx";
import YearSetting from "../components/YearSetting.tsx";

export default function Home() {
    return (
        <div className="min-h-screen flex flex-col">

            <header className="app-header">

                <nav className="nav-bar">
                    <IconLink to="/" icon={HomeIcon} />
                </nav>

                <div className="standard-text">
                    <h1>KC SpotifyAnalyzer</h1>
                </div>

                <div className="nav-bar">
                    <YearSetting />
                    <button className="green-button">
                        Logout
                    </button>
                </div>

            </header>

            <section className="page-section standard-text border-b">
                Groups
            </section>

            <main className="page-main">
                Tables
            </main>

            <footer className="page-section standard-text border-t">
                Copyright
            </footer>

        </div>
    );
}
