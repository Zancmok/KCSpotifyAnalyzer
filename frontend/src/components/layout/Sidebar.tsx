import { useState } from "react";
import GroupList from "../sidebar/GroupList";
import type { Group } from "../../types/group";

type SidebarProps = {
    groups: Group[];
    activeGroupId: string;
    onSelectGroup: (group: Group) => void;
};

export default function Sidebar({ groups, activeGroupId, onSelectGroup }: SidebarProps) {
    const [mobileOpen, setMobileOpen] = useState(false);

    const handleSelect = (group: Group) => {
        onSelectGroup(group);
        setMobileOpen(false);
    };

    return (
        <>
            {/* Sidebar panel */}
            <aside
                className={`
                    w-16 bg-bg border-r border-border flex flex-col items-center py-3
                    md:relative fixed z-40 transition-transform self-start
                    ${mobileOpen ? "translate-x-0" : "-translate-x-full md:translate-x-0"}
                `}
            >
                <div className="overflow-y-auto w-full">
                    <GroupList
                        groups={groups}
                        activeGroupId={activeGroupId}
                        onSelect={handleSelect}
                    />
                </div>
            </aside>

            {/* Mobile overlay backdrop */}
            {mobileOpen && (
                <div
                    className="fixed inset-0 bg-black/50 z-30 md:hidden"
                    onClick={() => setMobileOpen(false)}
                />
            )}

            {/* Mobile toggle button */}
            <button
                className="md:hidden fixed bottom-4 right-4 z-50 bg-brand text-bg p-3 rounded-full shadow-lg"
                onClick={() => setMobileOpen(!mobileOpen)}
                aria-label="Toggle sidebar"
            >
                ☰
            </button>
        </>
    );
}