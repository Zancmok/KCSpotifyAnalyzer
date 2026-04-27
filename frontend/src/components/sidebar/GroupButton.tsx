type GroupButtonProps = {
    imageUrl: string;
    name: string;
    isActive?: boolean;
    onClick: () => void;
};

export default function GroupButton({
                                        imageUrl,
                                        name,
                                        isActive = false,
                                        onClick,
                                    }: GroupButtonProps) {
    return (
        <button
            onClick={onClick}
            title={name}
            className={`
                relative flex items-center justify-center
                w-12 h-12 rounded-full
                transition
                ${isActive ? "ring-2 ring-brand" : "hover:bg-hover"}
            `}
        >
            <img
                src={imageUrl}
                alt={name}
                className="w-10 h-10 rounded-full object-cover"
            />
        </button>
    );
}
