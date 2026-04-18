import { NavLink } from "react-router-dom";
import type { ElementType } from "react";

type IconLinkProps = {
    to: string;
    icon: ElementType;
};

export default function IconLink({ to, icon: Icon }: IconLinkProps)
{
    return (
        <NavLink
            to={to}
            className={({ isActive }) =>
                `inline-flex items-center justify-center w-12 h-12 rounded-full transition
                ${isActive ? "bg-gray-800" : "hover:bg-gray-800"}`
            }
        >
            <Icon className="w-6 h-6" />
        </NavLink>
    );
}
