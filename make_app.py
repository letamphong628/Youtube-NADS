import os

# 1. Tạo cấu trúc thư mục
os.makedirs("app/src/main/java/com/nads/youtube", exist_ok=True)
os.makedirs("app/src/main/res/layout", exist_ok=True)
os.makedirs("app/src/main/assets/www", exist_ok=True)

# 2. Tạo AndroidManifest.xml
manifest = """<?xml version="1.0" encoding="utf-8"?>
<manifest xmlns:android="http://schemas.android.com/apk/res/android"
    package="com.nads.youtube">
    <uses-sdk android:minSdkVersion="23" android:targetSdkVersion="34" />
    <uses-permission android:name="android.permission.INTERNET" />
    <uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />

    <application
        android:allowBackup="true"
        android:label="YouTube NADS"
        android:hardwareAccelerated="true"
        android:theme="@android:style/Theme.DeviceDefault.NoActionBar">
        <activity
            android:name=".MainActivity"
            android:exported="true"
            android:configChanges="orientation|keyboardHidden|screenSize">
            <intent-filter>
                <action android:name="android.intent.action.MAIN" />
                <category android:name="android.intent.category.LAUNCHER" />
            </intent-filter>
        </activity>
    </application>
</manifest>"""

with open("app/src/main/AndroidManifest.xml", "w", encoding="utf-8") as f:
    f.write(manifest)

# 3. Tạo MainActivity.java (Chạy YouTube thật + Tự động Chặn Quảng Cáo)
java_code = """package com.nads.youtube;

import android.app.Activity;
import android.os.Bundle;
import android.view.Window;
import android.view.WindowManager;
import android.webkit.CookieManager;
import android.webkit.WebChromeClient;
import android.webkit.WebSettings;
import android.webkit.WebView;
import android.webkit.WebViewClient;

public class MainActivity extends Activity {
    private WebView myWebView;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        
        requestWindowFeature(Window.FEATURE_NO_TITLE);
        getWindow().setFlags(WindowManager.LayoutParams.FLAG_FULLSCREEN, WindowManager.LayoutParams.FLAG_FULLSCREEN);

        myWebView = new WebView(this);
        setContentView(myWebView);

        WebSettings webSettings = myWebView.getSettings();
        webSettings.setJavaScriptEnabled(true);
        webSettings.setDomStorageEnabled(true);
        webSettings.setDatabaseEnabled(true);
        webSettings.setAllowFileAccess(true);
        webSettings.setMediaPlaybackRequiresUserGesture(false);
        webSettings.setUserAgentString("Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Mobile Safari/537.36");

        CookieManager.getInstance().setAcceptCookie(true);
        CookieManager.getInstance().setAcceptThirdPartyCookies(myWebView, true);

        myWebView.setWebViewClient(new WebViewClient() {
            @Override
            public void onPageFinished(WebView view, String url) {
                String adBlockJS = "javascript:(function() { " +
                    "setInterval(function() { " +
                        "var ads = document.querySelectorAll('.ad-showing, .ad-interrupting, .badge-for-adds, ytd-ad-slot-renderer, .ytp-ad-overlay-container'); " +
                        "ads.forEach(function(ad) { ad.remove(); }); " +
                        "var skipBtn = document.querySelector('.ytp-ad-skip-button, .ytp-ad-skip-button-modern, .ytp-skip-ad-button'); " +
                        "if (skipBtn) { skipBtn.click(); } " +
                        "var video = document.querySelector('video'); " +
                        "if (video && document.querySelector('.ad-showing')) { video.currentTime = video.duration || 999; } " +
                    "}, 300); " +
                "})()";
                myWebView.loadUrl(adBlockJS);
            }
        });

        myWebView.setWebChromeClient(new WebChromeClient());
        myWebView.loadUrl("file:///android_asset/www/index.html");
    }

    @Override
    public void onBackPressed() {
        if (myWebView.canGoBack()) {
            myWebView.goBack();
        } else {
            super.onBackPressed();
        }
    }
}"""

with open("app/src/main/java/com/nads/youtube/MainActivity.java", "w", encoding="utf-8") as f:
    f.write(java_code)

# 4. Tạo index.html (Samsung Tizen OS Setup + Icon Outline Viền Trắng + Liquid Glass)
html_code = """<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title>YouTube NADS</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; -webkit-tap-highlight-color: transparent; }
        body { background-color: #000000; color: #ffffff; height: 100vh; overflow: hidden; }

        .icon-svg { width: 22px; height: 22px; stroke: #ffffff; stroke-width: 1.8; stroke-linecap: round; stroke-linejoin: round; fill: none; }

        @keyframes fadeInScale {
            from { opacity: 0; transform: scale(0.95) translateY(10px); }
            to { opacity: 1; transform: scale(1) translateY(0); }
        }

        .setup-screen {
            position: fixed; top: 0; left: 0; right: 0; bottom: 0;
            background: #000000; z-index: 99999;
            display: flex; flex-direction: column; justify-content: center; align-items: center;
            padding: 24px; text-align: center;
        }

        .setup-step { display: none; width: 100%; max-width: 380px; }
        .setup-step.active { display: flex; flex-direction: column; align-items: center; animation: fadeInScale 0.4s ease-out forwards; }

        .btn-white {
            background: #ffffff; color: #000000; border: none;
            padding: 12px 32px; border-radius: 30px; font-weight: 700;
            font-size: 0.95rem; cursor: pointer; margin: 8px;
        }

        .btn-grey {
            background: rgba(255, 255, 255, 0.15); color: #ffffff; border: none;
            padding: 12px 32px; border-radius: 30px; font-weight: 600;
            font-size: 0.95rem; cursor: pointer; margin: 8px;
        }

        .terms-box {
            background: #121212; border: 1px solid rgba(255, 255, 255, 0.2);
            border-radius: 16px; padding: 14px; max-height: 180px; overflow-y: auto;
            text-align: left; font-size: 0.8rem; color: #ccc; margin: 16px 0; line-height: 1.4;
        }

        .app-container { width: 100%; height: 100vh; display: flex; flex-direction: column; }
        
        .header-bar {
            height: 52px; background: #000000; border-bottom: 1px solid rgba(255, 255, 255, 0.1);
            display: flex; justify-content: space-between; align-items: center; padding: 0 16px;
        }

        .logo-box { display: flex; align-items: center; gap: 8px; font-weight: 800; font-size: 1.1rem; }
        .yt-frame { flex: 1; border: none; width: 100%; height: calc(100vh - 110px); }

        .bottom-nav {
            position: fixed; bottom: 12px; left: 16px; right: 16px; height: 58px;
            background: rgba(2, 132, 199, 0.18);
            backdrop-filter: blur(20px); -webkit-backdrop-filter: blur(20px);
            border: 1.5px solid rgba(56, 189, 248, 0.4);
            border-radius: 30px; display: flex; justify-content: space-around; align-items: center; z-index: 1000;
        }

        .nav-item {
            display: flex; flex-direction: column; align-items: center; background: none; border: none;
            color: #888; font-size: 0.65rem; gap: 3px; cursor: pointer;
        }

        .nav-item.active { color: #ffffff; }
    </style>
</head>
<body>

    <!-- MÀN HÌNH SETUP TIZEN OS -->
    <div class="setup-screen" id="setupScreen">
        <!-- Step 0 -->
        <div class="setup-step active" id="step0">
            <svg class="icon-svg" style="width:64px; height:64px;" viewBox="0 0 24 24"><rect x="2" y="4" width="20" height="15" rx="4"/><polygon points="10 8 16 12 10 16"/></svg>
            <h1 style="margin-top:16px;">Xin chào</h1>
            <p style="color:#aaa; margin:12px 0 24px; font-size:0.9rem;">Hãy thiết lập 1 vài thứ để sử dụng ứng dụng 1 cách tốt nhất!</p>
            <select id="langSelect" style="background:#1a1a1a; color:#fff; padding:8px 16px; border-radius:20px; border:1px solid #333; margin-bottom:24px;">
                <option>Tiếng Việt</option>
                <option>English</option>
            </select>
            <div>
                <button class="btn-white" onclick="nextStep(1)">Bắt đầu</button>
                <button class="btn-grey" onclick="finishSetup()">Để sau</button>
            </div>
        </div>

        <!-- Step 1 -->
        <div class="setup-step" id="step1">
            <h2>1. Điều khoản dịch vụ</h2>
            <div class="terms-box">
                <b>DỊCH VỤ CỦA YOUTUBE / YOUTUBE TERMS OF SERVICE</b><br><br>
                1. Bằng việc sử dụng ứng dụng YouTube NADS, bạn đồng ý tuân thủ các quy định Dịch vụ của Google & YouTube.<br>
                2. Hệ thống tự động chặn sạch quảng cáo khi xem video.<br><br>
                <b>ENGLISH TERMS:</b><br>
                By accessing YouTube NADS, you agree to be bound by YouTube Terms of Service and Guidelines.
            </div>
            <label style="font-size:0.85rem; display:flex; align-items:center; gap:8px; margin-bottom:16px;">
                <input type="checkbox" id="chkTerms" onchange="toggleTermsBtn()"> Tôi đồng ý với Điều Khoản
            </label>
            <button class="btn-white" id="btnTermsNext" style="opacity:0.4;" disabled onclick="nextStep(2)">Tiếp theo</button>
        </div>

        <!-- Step 2 -->
        <div class="setup-step" id="step2">
            <svg class="icon-svg" style="width:56px; height:56px;" viewBox="0 0 24 24"><path d="M19 21v-2a4 4 0 0 0-4-4H9a4 4 0 0 0-4 4v2"/><circle cx="12" cy="7" r="4"/></svg>
            <h2 style="margin-top:16px;">2. Thêm Tài Khoản</h2>
            <p style="color:#aaa; font-size:0.85rem; margin:12px 0;">Đăng nhập tài khoản Google / YouTube chính thức của bạn.</p>
            <button class="btn-white" onclick="loginGoogle()">Thêm tài khoản (Google)</button>
            <button class="btn-grey" onclick="nextStep(3)">Để sau</button>
        </div>

        <!-- Step 3 -->
        <div class="setup-step" id="step3">
            <svg class="icon-svg" style="width:56px; height:56px;" viewBox="0 0 24 24"><circle cx="12" cy="12" r="5"/><line x1="12" y1="1" x2="12" y2="3"/><line x1="12" y1="21" x2="12" y2="23"/></svg>
            <h2 style="margin-top:16px;">3. Giao Diện Nền Đen</h2>
            <p style="color:#aaa; font-size:0.85rem; margin:12px 0 24px;">Tối ưu nền đen AMOLED tiết kiệm pin và bảo vệ mắt.</p>
            <button class="btn-white" onclick="nextStep(4)">Tiếp theo</button>
        </div>

        <!-- Step 4 -->
        <div class="setup-step" id="step4">
            <svg class="icon-svg" style="width:64px; height:64px;" viewBox="0 0 24 24"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"/><polyline points="22 4 12 14.01 9 11.01"/></svg>
            <h2 style="margin-top:16px;">Bạn đã hoàn thành!</h2>
            <p style="color:#aaa; font-size:0.85rem; margin:12px 0 24px;">Hãy trải nghiệm ứng dụng ngay nhé!</p>
            <button class="btn-white" onclick="finishSetup()">Bắt đầu trải nghiệm</button>
        </div>
    </div>

    <!-- MAIN APP YOUTUBE THẬT -->
    <div class="app-container">
        <div class="header-bar">
            <div class="logo-box">
                <svg class="icon-svg" style="width:20px; height:20px;" viewBox="0 0 24 24"><rect x="2" y="4" width="20" height="16" rx="4"/><polygon points="10 8 16 12 10 16"/></svg>
                <span>YouTube <span style="color:#ef4444;">NADS</span></span>
            </div>
            <div style="display:flex; gap:16px;">
                <svg class="icon-svg" onclick="navTo('https://m.youtube.com/results?search_query=')" viewBox="0 0 24 24"><circle cx="11" cy="11" r="8"/><line x1="21" x2="16.65" y1="21" y2="16.65"/></svg>
                <svg class="icon-svg" onclick="loginGoogle()" viewBox="0 0 24 24"><path d="M19 21v-2a4 4 0 0 0-4-4H9a4 4 0 0 0-4 4v2"/><circle cx="12" cy="7" r="4"/></svg>
            </div>
        </div>

        <iframe class="yt-frame" id="ytFrame" src="https://m.youtube.com"></iframe>

        <div class="bottom-nav">
            <button class="nav-item active" onclick="navTo('https://m.youtube.com')">
                <svg class="icon-svg" viewBox="0 0 24 24"><path d="m3 9 9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/></svg>
                <span>Trang chủ</span>
            </button>
            <button class="nav-item" onclick="navTo('https://m.youtube.com/shorts')">
                <svg class="icon-svg" viewBox="0 0 24 24"><polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"/></svg>
                <span>Shorts</span>
            </button>
            <button class="nav-item" onclick="navTo('https://m.youtube.com/upload')">
                <svg class="icon-svg" style="width:28px; height:28px;" viewBox="0 0 24 24"><circle cx="12" cy="12" r="10"/><line x1="12" x2="12" y1="8" y2="16"/><line x1="8" x2="16" y1="12" y2="12"/></svg>
            </button>
            <button class="nav-item" onclick="navTo('https://m.youtube.com/feed/subscriptions')">
                <svg class="icon-svg" viewBox="0 0 24 24"><path d="M4 11a1 1 0 0 1 1-1h16a1 1 0 0 1 1 1v9a1 1 0 0 1-1 1H5a1 1 0 0 1-1-1v-9Z"/><path d="M4 6h16"/></svg>
                <span>Đăng ký</span>
            </button>
            <button class="nav-item" onclick="navTo('https://m.youtube.com/feed/you')">
                <svg class="icon-svg" viewBox="0 0 24 24"><path d="M19 21v-2a4 4 0 0 0-4-4H9a4 4 0 0 0-4 4v2"/><circle cx="12" cy="7" r="4"/></svg>
                <span>Bạn</span>
            </button>
        </div>
    </div>

    <script>
        function nextStep(step) {
            document.querySelectorAll(".setup-step").forEach(s => s.classList.remove("active"));
            document.getElementById("step" + step).classList.add("active");
        }

        function toggleTermsBtn() {
            var chk = document.getElementById("chkTerms");
            var btn = document.getElementById("btnTermsNext");
            btn.disabled = !chk.checked;
            btn.style.opacity = chk.checked ? "1" : "0.4";
        }

        function loginGoogle() {
            document.getElementById("ytFrame").src = "https://accounts.google.com/ServiceLogin?service=youtube";
            finishSetup();
        }

        function navTo(url) {
            document.getElementById("ytFrame").src = url;
        }

        function finishSetup() {
            document.getElementById("setupScreen").style.display = "none";
        }
    </script>
</body>
</html>"""

with open("app/src/main/assets/www/index.html", "w", encoding="utf-8") as f:
    f.write(html_code)

print(">>> TẠO CODE THÀNH CÔNG 100%!")
