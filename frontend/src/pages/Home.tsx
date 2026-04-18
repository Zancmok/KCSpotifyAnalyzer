import { useState } from "react";

import {
    HomeIcon, GlobeAltIcon
} from "@heroicons/react/24/outline";

import IconLink from "../components/IconLink.tsx";
import YearSetting from "../components/YearSetting.tsx";
import GroupElement from "../components/GroupElement.tsx";

export default function Home()
{
    type Group = {
        id: string;
        name: string;
        iconUrl: string;
    };

    const groups: Group[] = [
        { id: "everyone", name: "Everyone", iconUrl: "" },
        { id: "cyka", name: "Cyka", iconUrl: ""}
    ];

    const [selectedGroup, setSelectedGroup] = useState<string>("everyone");

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

            <section className="page-section standard-text border-b flex gap-2 overflow-x-auto">
                {
                    groups.map((group) => (
                        <GroupElement
                            name={group.name}
                            icon={group.id == "everyone" ? GlobeAltIcon : undefined}
                            iconUrl={group.iconUrl}
                            active={group.id === selectedGroup}
                            onClick={() => setSelectedGroup(group.id)}
                        />
                    ))
                }
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
