import type { ReactNode } from "react";
import Header from "./Header";
import Footer from "./Footer";

type LayoutProps = {
    title?: string;
    onLogoClick?: () => void;
    avatarUrl?: string;
    children: ReactNode;
};

export default function Layout({ title, onLogoClick, avatarUrl, children }: LayoutProps) {
    return (
        <div className="h-screen flex flex-col bg-bg text-text">
            <Header title={title} onLogoClick={onLogoClick} avatarUrl={avatarUrl} />
            <div className="flex flex-1 overflow-hidden">
                {children}
            </div>
            <Footer />
        </div>
    );
}