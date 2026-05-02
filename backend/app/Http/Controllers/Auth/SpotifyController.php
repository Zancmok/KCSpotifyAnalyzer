<?php

namespace App\Http\Controllers\Auth;

use App\Http\Controllers\Controller;
use App\Models\User;
use Laravel\Socialite\Facades\Socialite;

class SpotifyController extends Controller
{
    public function redirect()
    {
        return Socialite::driver('spotify')
            ->scopes(['user-read-private', 'user-read-email'])
            ->stateless()
            ->redirect();
    }

    public function callback()
    {
        $spotifyUser = Socialite::driver('spotify')
            ->stateless()
            ->user();

        $user = User::updateOrCreate(
            ['spotify_id' => $spotifyUser->getId()],
            [
                'display_name' => $spotifyUser->getName(),
                'avatar_url'   => $spotifyUser->getAvatar(),
                'token'        => $spotifyUser->token,
            ]
        );

        $sanctumToken = $user->createToken('api')->plainTextToken;

        return redirect(env('APP_URL') . '/callback?token=' . $sanctumToken);
    }
}
