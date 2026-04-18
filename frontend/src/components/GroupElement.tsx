import type {ElementType} from "react";

type GroupElementProps = {
    name: string,
    icon?: ElementType,
    iconUrl?: string,
    onClick?: () => void,
    active: boolean
}

export default function GroupElement({ name, icon: Icon, iconUrl, onClick, active }: GroupElementProps)
{
    return (
      <button
          className={[
              "flex items-center gap-2 gray-button",
              active ? "gray-button--active" : ""
          ].join(" ")}
          onClick={onClick}
      >
          {Icon ? (
              <Icon className="w-6 h-6" />
          ) : (
              <img src={iconUrl} className="w-6 h-6" alt="" />
          )}
          <span>{name}</span>
      </button>
    );
}
