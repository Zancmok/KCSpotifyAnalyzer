export type meResponse = {
    id: number;
    image_url: string;
    name: string;
    spotify_id: string;
};


export async function me(): Promise<meResponse>
{
    const response: Response = await fetch("/auth/me", {
        method: "POST",
        headers: { "Content-Type": "application/json; charset=UTF-8" }
    });

    return await response.json();
}
