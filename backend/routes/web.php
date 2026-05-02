<?php

use App\Http\Controllers\Auth\SpotifyController;
use Illuminate\Support\Facades\Route;

Route::get('/auth/spotify/redirect', [SpotifyController::class, 'redirect']);
Route::get('/auth/spotify/callback', [SpotifyController::class, 'callback']);
