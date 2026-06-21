import { getById } from "../../util.js";
import { upload } from "../../requests/rest/user_data.js";

async function fileInputChanged(): Promise<void>
{
    const fileInput: HTMLInputElement = getById<HTMLInputElement>("fileInput");

    if (!fileInput.files)
    { return; }
    const file: File = fileInput.files[0];

    await upload(file);
}

function uploadButtonPressed(): void
{
    const fileInput: HTMLInputElement = getById<HTMLInputElement>("fileInput");

    fileInput.click();
}

function displayUserData(userData: any): void
{
    const userNameParagraph: HTMLParagraphElement = getById<HTMLParagraphElement>("userName");
    const profilePicture: HTMLImageElement = getById<HTMLImageElement>("profilePicture");

    userNameParagraph.innerText = userData.name;
    profilePicture.src = userData.image_url;
}

async function main(): Promise<void>
{
    // displayUserData();

    const fileInput: HTMLInputElement = getById<HTMLInputElement>("fileInput");
    fileInput.addEventListener('change', fileInputChanged);

    const uploadDataButton: HTMLButtonElement = getById<HTMLButtonElement>("uploadData");
    uploadDataButton.onclick = uploadButtonPressed;
}

await main();
