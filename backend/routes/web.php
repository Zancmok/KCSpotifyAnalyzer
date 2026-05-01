<?php

use App\Http\Controllers\Auth\SpotifyController;

Route::get('/auth/spotify/redirect', [SpotifyController::class, 'redirect']);
Route::get('/auth/spotify/callback', [SpotifyController::class, 'callback']);
