import { useState } from "react";

export default function YearSetting()
{
    const [year, setYear] = useState(new Date().getFullYear());

    return (
        <input
            type="number"
            value={year}
            onChange={(e) => setYear(Number(e.target.value))}
            className="year-input"
        />
    );
}