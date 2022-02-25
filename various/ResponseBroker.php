<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use App\Http\Controllers\Controller;
use Illuminate\Support\Facades\Cookie;

class ResponseBroker extends Controller{

    const DEFAULT_COOKIE_DURATION = 3600;
    const DEFAULT_API_CACHE_DURATION = 3600;
    const DEFAULT_SERVER_DATETIME_OFFSET = [
        "sign" => "+",
        "hours" => 6,
        "minutes" => 30,
        "tzcode" => " MMT"
    ];

    private static $commonHeaders = [];

    public static function sendWebResponse($viewTemplate, $contextData = null,
                                                $statusCode = null, $extraHeaders = null, $extraCookies = null){
        if(!isset($statusCode)){
            $statusCode = 200;
        }

        ResponseBroker::$commonHeaders["Date"] = ResponseBroker::makeServerTime(ResponseBroker::DEFAULT_SERVER_DATETIME_OFFSET);

        if(isset($extraHeaders)){
            ResponseBroker::$commonHeaders += $extraHeaders;
        }

        if($extraCookies == null){
            return response()->view($viewTemplate, $contextData, $statusCode, ResponseBroker::$commonHeaders);
        }

        else{
            foreach($extraCookies as $cookieName => $cookieValue){
                $cookie = cookie($cookieName, $cookieValue, ResponseBroker::DEFAULT_COOKIE_DURATION);
                Cookie::queue($cookie);
            }

            return response()->view($viewTemplate, $contextData, $statusCode, ResponseBroker::$commonHeaders);
        }
    }

    public static function sendApiResponse($apiData, $statusCode = null, $cacheDuration = null, $extraHeaders = null){
        if(!isset($statusCode)){
            $statusCode = 200;
        }

        ResponseBroker::$commonHeaders["Cache-control"] = "public,"."max-age=" .$cacheDuration;
        ResponseBroker::$commonHeaders["Access-Control-Allow-Origin"] = "*";
        ResponseBroker::$commonHeaders["Date"] = ResponseBroker::makeServerTime(ResponseBroker::DEFAULT_SERVER_DATETIME_OFFSET);

        if(!isset($cacheDuration)){
            $cacheDuration = ResponseBroker::DEFAULT_API_CACHE_DURATION;
        }

        if(isset($extraHeaders)){
            ResponseBroker::$commonHeaders += $extraHeaders;
        }

        return response()->json($apiData, $statusCode, ResponseBroker::$commonHeaders);
    }

    private static function makeServerTime(array $offset = null){
        if(!isset($offset)){
            $serverTime = time();
            $serverDateTime = gmdate('D, d M Y\\ H:i:s', $serverTime) . " GMT";
        }

        else{
            if($offset["sign"] == "+"){
                $serverTime = time() + (3600 * $offset["hours"]) + (60 * $offset["minutes"]);
            }
            if($offset["sign"] == "-"){
                $serverTime = time() - ((3600 * $offset["hours"]) + (60 * $offset["minutes"]));
            }
            $serverDateTime = gmdate('D, d M Y\\ H:i:s', $serverTime) . $offset["tzcode"];
        }

        return $serverDateTime;
    }
}
