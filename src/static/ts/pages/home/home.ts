import { getById } from "../../util.js";
import { me, meResponse } from "../../requests/rest/auth.js";

const userData: meResponse = await me();

const userNameParagraph: HTMLParagraphElement = getById<HTMLParagraphElement>("userName");
const profilePicture: HTMLImageElement = getById<HTMLImageElement>("profilePicture");

userNameParagraph.innerText = userData.name;
profilePicture.src = userData.image_url;
