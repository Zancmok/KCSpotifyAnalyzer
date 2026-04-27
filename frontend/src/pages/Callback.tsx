import { useEffect } from "react";
import { useNavigate } from "react-router-dom";
import { useAuth } from "../hooks/useAuth";

// This page handles the OAuth redirect for BOTH flows:
// - Redirect flow (mobile): exchanges code, stores token, navigates to /home
// - Popup flow (desktop): exchanges code, posts token back to opener, closes itself

export default function Callback() {
    const navigate = useNavigate();
    const { handleTokenReceived } = useAuth();

    useEffect(() => {
        const code = new URLSearchParams(window.location.search).get("code");
        if (!code) {
            closeOrRedirect("/");
            return;
        }

        exchangeCodeForToken(code)
            .then(async ({ token, user }) => {
                const isPopup = window.opener && !window.opener.closed;

                if (isPopup) {
                    // Popup flow: send token back to main window, then close
                    window.opener.postMessage(
                        { type: "oauth_callback", token, user },
                        window.location.origin
                    );
                    window.close();
                } else {
                    // Redirect flow: set auth state directly and navigate
                    handleTokenReceived(token, user);
                    navigate("/home", { replace: true });
                }
            })
            .catch(() => closeOrRedirect("/"));
    }, [navigate, handleTokenReceived]);

    return (
        <div className="h-screen flex items-center justify-center bg-bg text-text-muted text-sm">
            Logging you in...
        </div>
    );
}

function closeOrRedirect(path: string) {
    if (window.opener && !window.opener.closed) {
        window.close();
    } else {
        window.location.replace(path);
    }
}

// ----------------------------------------
// TODO: Point this at your backend endpoint that does the
// code → token exchange (never expose client_secret in frontend)
// ----------------------------------------
async function exchangeCodeForToken(code: string) {
    const res = await fetch("/api/auth/callback", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ code }),
    });
    if (!res.ok) throw new Error("Token exchange failed");
    return res.json(); // expects { token, user }
}
