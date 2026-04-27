import type { ReactNode } from "react";
import { Navigate } from "react-router-dom";
import { useAuth } from "../../hooks/useAuth";

export default function RequireAuth({ children }: { children: ReactNode }) {
    const { auth } = useAuth();

    if (auth.status === "loading") {
        // Avoid flashing the login page while we validate a stored token
        return (
            <div className="h-screen flex items-center justify-center bg-bg text-text-muted text-sm">
                Loading...
            </div>
        );
    }

    if (auth.status === "unauthenticated") {
        return <Navigate to="/" replace />;
    }

    return <>{children}</>;
}
