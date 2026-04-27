import GroupButton from "./GroupButton";
import type { Group } from "../../types/group";

type GroupListProps = {
    groups: Group[];
    activeGroupId: string;
    onSelect: (group: Group) => void;
};

export default function GroupList({ groups, activeGroupId, onSelect }: GroupListProps) {
    return (
        <div className="flex flex-col items-center gap-3 py-3">
            {groups.map((group) => (
                <GroupButton
                    key={group.id}
                    imageUrl={group.imageUrl}
                    name={group.name}
                    isActive={group.id === activeGroupId}
                    onClick={() => onSelect(group)}
                />
            ))}
        </div>
    );
}