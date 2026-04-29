import { useEffect } from "react";
import { useNavigate } from "react-router-dom";
import { useAuth } from "../hooks/useAuth";

// Laravel redirects back to /callback?token=JWT after handling the Spotify flow.
// This page reads that token and either:
// - Posts it to the main window and closes itself (popup flow)
// - Stores it and navigates to /home (redirect flow)

export default function Callback() {
    const navigate = useNavigate();
    const { handleTokenReceived } = useAuth();

    useEffect(() => {
        const params = new URLSearchParams(window.location.search);
        const token = params.get("token");

        if (!token) {
            closeOrRedirect("/");
            return;
        }

        const isPopup = window.opener && !window.opener.closed;

        if (isPopup) {
            window.opener.postMessage(
                { type: "oauth_callback", token },
                window.location.origin
            );
            window.close();
        } else {
            handleTokenReceived(token);
            navigate("/home", { replace: true });
        }
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
