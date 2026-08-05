import os

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
        
        // User-Agent Chrome Mobile chuẩn để không bị Google chặn Login
        webSettings.setUserAgentString("Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36");

        CookieManager.getInstance().setAcceptCookie(true);
        CookieManager.getInstance().setAcceptThirdPartyCookies(myWebView, true);

        myWebView.setWebViewClient(new WebViewClient() {
            @Override
            public void onPageFinished(WebView view, String url) {
                // TỰ ĐỘNG LỌC SẠCH QUẢNG CÁO
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
        
        // LOAD TRỰC TIẾP YOUTUBE THẬT
        myWebView.loadUrl("https://m.youtube.com");
    }

    @Override
    public void onBackPressed() {
        if (myWebView.canGoBack()) {
            myWebView.goBack();
        } else {
            super.onBackPressed();
        }
    }

    @Override
    protected void onUserLeaveHint() {
        super.onUserLeaveHint();
        // BẬT CHẾ ĐỘ PIP KHI THOÁT RA BÀN HÌNH CHÍNH
        try {
            enterPictureInPictureMode();
        } catch (Exception e) {}
    }
}"""

with open("app/src/main/java/com/nads/youtube/MainActivity.java", "w", encoding="utf-8") as f:
    f.write(java_code)

print(">>> ĐÃ CẬP NHẬT MAINACTIVITY LOAD YOUTUBE TRỰC TIẾP!")
