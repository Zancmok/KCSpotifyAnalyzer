<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;

class UserController extends Controller
{
    public function me(Request $request)
    {
        $user = $request->user();

        return response()->json([
            'id'           => $user->spotify_id,
            'display_name' => $user->display_name,
            'avatar_url'   => $user->avatar_url,
        ]);
    }
}
