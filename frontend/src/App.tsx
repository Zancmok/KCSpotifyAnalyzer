import { BrowserRouter, Routes, Route } from "react-router-dom";
import { AuthProvider } from "./context/AuthContext";
import RequireAuth from "./components/auth/RequireAuth";
import Index from "./pages/Index";
import Home from "./pages/Home";
import Callback from "./pages/Callback";

export default function App() {
    return (
        <BrowserRouter>
            <AuthProvider>
                <Routes>
                    <Route path="/" element={<Index />} />
                    <Route path="/callback" element={<Callback />} />
                    <Route path="/home" element={
                        <RequireAuth>
                            <Home />
                        </RequireAuth>
                    } />
                </Routes>
            </AuthProvider>
        </BrowserRouter>
    );
}
