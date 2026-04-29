import { createContext, useState, useEffect, type ReactNode } from "react";

export type SpotifyUser = {
    id: string;
    display_name: string;
    avatar_url: string;
};

type AuthState =
    | { status: "loading" }
    | { status: "authenticated"; user: SpotifyUser; token: string }
    | { status: "unauthenticated" };

type AuthContextType = {
    auth: AuthState;
    login: () => void;
    logout: () => void;
    handleTokenReceived: (token: string) => void;
};

export const AuthContext = createContext<AuthContextType | null>(null);

const BACKEND_URL = "";

export function AuthProvider({ children }: { children: ReactNode }) {
    const [auth, setAuth] = useState<AuthState>({ status: "loading" });

    const fetchAndSetUser = async (token: string) => {
        const res = await fetch(`${BACKEND_URL}/api/me`, {
            headers: { Authorization: `Bearer ${token}` },
        });
        if (!res.ok) throw new Error("Failed to fetch user");
        const user: SpotifyUser = await res.json();
        setAuth({ status: "authenticated", user, token });
    };

    // On mount: validate any stored token
    useEffect(() => {
        const token = localStorage.getItem("token");
        if (!token) {
            setAuth({ status: "unauthenticated" });
            return;
        }
        fetchAndSetUser(token).catch(() => {
            localStorage.removeItem("token");
            setAuth({ status: "unauthenticated" });
        });
    }, []);

    // Listen for token posted back from popup
    useEffect(() => {
        const handler = (event: MessageEvent) => {
            if (event.origin !== window.location.origin) return;
            if (event.data?.type !== "oauth_callback") return;
            handleTokenReceived(event.data.token);
        };
        window.addEventListener("message", handler);
        return () => window.removeEventListener("message", handler);
    }, []);

    const handleTokenReceived = (token: string) => {
        localStorage.setItem("token", token);
        fetchAndSetUser(token).catch(() => {
            localStorage.removeItem("token");
            setAuth({ status: "unauthenticated" });
        });
    };

    const login = () => {
        const isMobile =
            /Mobi|Android|iPhone|iPad/i.test(navigator.userAgent) ||
            window.innerWidth < 768;

        if (isMobile) {
            window.location.href = `${BACKEND_URL}/auth/spotify/redirect`;
        } else {
            popupLogin();
        }
    };

    const logout = () => {
        localStorage.removeItem("token");
        setAuth({ status: "unauthenticated" });
    };

    return (
        <AuthContext.Provider value={{ auth, login, logout, handleTokenReceived }}>
            {children}
        </AuthContext.Provider>
    );
}

function popupLogin() {
    const width = 500;
    const height = 700;
    const left = window.screenX + (window.outerWidth - width) / 2;
    const top = window.screenY + (window.outerHeight - height) / 2;

    const popup = window.open(
        "/auth/spotify/redirect",
        "oauth_popup",
        `width=${width},height=${height},left=${left},top=${top},toolbar=no,menubar=no`
    );

    // If popup was blocked, fall back to redirect
    if (!popup || popup.closed) {
        window.location.href = "/auth/spotify/redirect";
    }
}
