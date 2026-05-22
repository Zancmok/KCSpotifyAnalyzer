export function getById<T extends HTMLElement>(id: string): T
{
    const element: HTMLElement | null = document.getElementById(id);
    if (!element) throw new Error(`Missing element: ${id}`);
    return element as T;
}
