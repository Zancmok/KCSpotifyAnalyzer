import { createContext, useState, useEffect, type ReactNode } from "react";

// ----------------------------------------
// TODO: Fill in your user shape once your
// auth provider is defined.
// ----------------------------------------
export type AuthUser = {
    id: string;
    display_name: string;
    avatar_url: string;
};

type AuthState =
    | { status: "loading" }
    | { status: "authenticated"; user: AuthUser; accessToken: string }
    | { status: "unauthenticated" };

type AuthContextType = {
    auth: AuthState;
    login: () => void;
    logout: () => void;
    handleTokenReceived: (token: string, user: AuthUser) => void;
};

export const AuthContext = createContext<AuthContextType | null>(null);

export function AuthProvider({ children }: { children: ReactNode }) {
    const [auth, setAuth] = useState<AuthState>({ status: "loading" });

    const handleTokenReceived = (token: string, user: AuthUser) => {
        localStorage.setItem("access_token", token);
        setAuth({ status: "authenticated", user, accessToken: token });
    };

    // On mount: validate any stored token
    useEffect(() => {
        const token = localStorage.getItem("access_token");
        if (!token) {
            setAuth({ status: "unauthenticated" });
            return;
        }
        validateToken(token)
            .then((user) => setAuth({ status: "authenticated", user, accessToken: token }))
            .catch(() => {
                localStorage.removeItem("access_token");
                setAuth({ status: "unauthenticated" });
            });
    }, []);

    // Listen for token posted back from popup window
    useEffect(() => {
        const handler = (event: MessageEvent) => {
            if (event.origin !== window.location.origin) return;
            if (event.data?.type !== "oauth_callback") return;
            handleTokenReceived(event.data.token, event.data.user);
        };
        window.addEventListener("message", handler);
        return () => window.removeEventListener("message", handler);
    }, []);

    const login = () => {
        const isMobile =
            /Mobi|Android|iPhone|iPad/i.test(navigator.userAgent) ||
            window.innerWidth < 768;

        if (isMobile) {
            redirectLogin();
        } else {
            popupLogin();
        }
    };

    const logout = () => {
        localStorage.removeItem("access_token");
        setAuth({ status: "unauthenticated" });
    };

    return (
        <AuthContext.Provider value={{ auth, login, logout, handleTokenReceived }}>
            {children}
        </AuthContext.Provider>
    );
}

// ----------------------------------------
// TODO: Replace with your provider's authorize URL + scopes
// ----------------------------------------
function buildAuthUrl(redirectUri: string): string {
    const params = new URLSearchParams({
        client_id: import.meta.env.VITE_AUTH_CLIENT_ID,
        redirect_uri: redirectUri,
        response_type: "code",
        scope: "TODO",
    });
    return `https://TODO_PROVIDER/oauth/authorize?${params}`;
}

function redirectLogin() {
    const redirectUri = `${window.location.origin}/callback`;
    window.location.href = buildAuthUrl(redirectUri);
}

function popupLogin() {
    const redirectUri = `${window.location.origin}/callback`;
    const url = buildAuthUrl(redirectUri);

    const width = 500;
    const height = 700;
    const left = window.screenX + (window.outerWidth - width) / 2;
    const top = window.screenY + (window.outerHeight - height) / 2;

    const popup = window.open(
        url,
        "oauth_popup",
        `width=${width},height=${height},left=${left},top=${top},toolbar=no,menubar=no`
    );

    // If popup was blocked by the browser, fall back to redirect
    if (!popup || popup.closed) {
        redirectLogin();
    }
}

// ----------------------------------------
// TODO: Replace with your provider's token validation endpoint
// ----------------------------------------
async function validateToken(token: string): Promise<AuthUser> {
    const res = await fetch("https://TODO_PROVIDER/api/me", {
        headers: { Authorization: `Bearer ${token}` },
    });
    if (!res.ok) throw new Error("Invalid token");
    return res.json();
}