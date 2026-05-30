export type meResponse = {
    id: number;
    image_url: string;
    name: string;
    spotify_id: string;
};

export type uploadResponse = {
    success: boolean;
}


export async function me(): Promise<meResponse>
{
    const response: Response = await fetch("/user_data/me", {
        method: "POST",
        headers: { "Content-Type": "application/json; charset=UTF-8" }
    });

    return await response.json();
}

export async function upload(file: File): Promise<uploadResponse>
{
    const formData: FormData = new FormData();
    formData.append("file", file);

    const response: Response = await fetch("/user_data/upload", {
        method: "POST",
        body: formData
    });

    return await response.json();
}
