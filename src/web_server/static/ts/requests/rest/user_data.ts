export type uploadResponse = {
    success: boolean;
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
