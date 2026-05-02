<?php

namespace App\Models;

use Illuminate\Foundation\Auth\User as Authenticatable;
use Laravel\Sanctum\HasApiTokens;

class User extends Authenticatable
{
    use HasApiTokens;

    protected $fillable = [
        'spotify_id',
        'display_name',
        'avatar_url',
        'token',
    ];

    protected $hidden = [
        'token',
    ];
}
