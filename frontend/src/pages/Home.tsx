import { useState } from "react";
import Layout from "../components/layout/Layout";
import Sidebar from "../components/layout/Sidebar";
import type { Group } from "../types/group";

const groups: Group[] = [
    { id: "global", name: "Global", imageUrl: "https://picsum.photos/seed/global/40/40", isGlobal: true },
    { id: "workout", name: "Workout", imageUrl: "https://picsum.photos/seed/workout/40/40" },
    { id: "chill", name: "Chill", imageUrl: "https://picsum.photos/seed/chill/40/40" },
    { id: "focus", name: "Focus", imageUrl: "https://picsum.photos/seed/focus/40/40" },
];

export default function Home() {
    const [activeGroup, setActiveGroup] = useState<Group>(groups[0]);

    return (
        <Layout title={activeGroup.name} onLogoClick={() => setActiveGroup(groups[0])}>
            <Sidebar
                groups={groups}
                activeGroupId={activeGroup.id}
                onSelectGroup={setActiveGroup}
            />

            <main className="flex-1 p-4 overflow-auto">
                <div className="text-sm text-text-muted mb-4">
                    Active Group:{" "}
                    <span className="text-text">{activeGroup.name}</span>
                </div>

                <div className="border border-border rounded-lg p-6 bg-surface">
                    Main analytics area (coming next)
                </div>
            </main>
        </Layout>
    );
}
