import os

# 1. AndroidManifest.xml Chuẩn Android 10 (minSdkVersion 23, targetSdkVersion 29)
manifest = """<?xml version="1.0" encoding="utf-8"?>
<manifest xmlns:android="http://schemas.android.com/apk/res/android"
    package="com.nads.youtube">

    <uses-sdk android:minSdkVersion="23" android:targetSdkVersion="29" />
    <uses-permission android:name="android.permission.INTERNET" />
    <uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />

    <application
        android:allowBackup="true"
        android:icon="@drawable/ic_youtube"
        android:label="YouTube NADS"
        android:hardwareAccelerated="true"
        android:theme="@android:style/Theme.DeviceDefault.NoActionBar">
        
        <activity
            android:name=".MainActivity"
            android:exported="true"
            android:supportsPictureInPicture="true"
            android:configChanges="orientation|keyboardHidden|screenSize|smallestScreenSize|screenLayout">
            <intent-filter>
                <action android:name="android.intent.action.MAIN" />
                <category android:name="android.intent.category.LAUNCHER" />
            </intent-filter>
        </activity>
    </application>
</manifest>"""

with open("app/src/main/AndroidManifest.xml", "w", encoding="utf-8") as f:
    f.write(manifest)

# 2. MainActivity.java - Tràn màn hình Android 10 + Chặn Ads + Login Google
java_code = """package com.nads.youtube;

import android.app.Activity;
import android.os.Bundle;
import android.view.View;
import android.view.ViewGroup;
import android.view.Window;
import android.view.WindowManager;
import android.webkit.CookieManager;
import android.webkit.WebChromeClient;
import android.webkit.WebSettings;
import android.webkit.WebView;
import android.webkit.WebViewClient;
import android.widget.Button;
import android.widget.CheckBox;
import android.widget.CompoundButton;
import android.widget.FrameLayout;
import android.widget.LinearLayout;
import android.widget.Toast;

public class MainActivity extends Activity {

    private LinearLayout setupScreen;
    private LinearLayout step0, step1, step2, step3;
    private CheckBox chkTerms;
    private Button btnTermsNext;
    private FrameLayout playerContainer;
    private WebView myWebView;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        
        requestWindowFeature(Window.FEATURE_NO_TITLE);
        getWindow().setFlags(WindowManager.LayoutParams.FLAG_FULLSCREEN, WindowManager.LayoutParams.FLAG_FULLSCREEN);
        
        setContentView(R.layout.activity_main);

        setupScreen = (LinearLayout) findViewById(R.id.setupScreen);
        step0 = (LinearLayout) findViewById(R.id.step0);
        step1 = (LinearLayout) findViewById(R.id.step1);
        step2 = (LinearLayout) findViewById(R.id.step2);
        step3 = (LinearLayout) findViewById(R.id.step3);
        chkTerms = (CheckBox) findViewById(R.id.chkTerms);
        btnTermsNext = (Button) findViewById(R.id.btnTermsNext);
        playerContainer = (FrameLayout) findViewById(R.id.playerContainer);

        // Khởi tạo Engine View tràn 100% khung Native
        myWebView = new WebView(this);
        myWebView.setLayoutParams(new FrameLayout.LayoutParams(
                ViewGroup.LayoutParams.MATCH_PARENT,
                ViewGroup.LayoutParams.MATCH_PARENT));
        
        WebSettings webSettings = myWebView.getSettings();
        webSettings.setJavaScriptEnabled(true);
        webSettings.setDomStorageEnabled(true);
        webSettings.setDatabaseEnabled(true);
        webSettings.setAllowFileAccess(true);
        webSettings.setMediaPlaybackRequiresUserGesture(false);
        webSettings.setUserAgentString("Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36");

        CookieManager.getInstance().setAcceptCookie(true);
        CookieManager.getInstance().setAcceptThirdPartyCookies(myWebView, true);

        myWebView.setWebViewClient(new WebViewClient() {
            @Override
            public void onPageFinished(WebView view, String url) {
                // Tự động quét & lọc sạch quảng cáo YouTube
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
        playerContainer.addView(myWebView);
        myWebView.loadUrl("https://m.youtube.com");

        if (chkTerms != null) {
            chkTerms.setOnCheckedChangeListener(new CompoundButton.OnCheckedChangeListener() {
                @Override
                public void onCheckedChanged(CompoundButton buttonView, boolean isChecked) {
                    if (btnTermsNext != null) {
                        btnTermsNext.setEnabled(isChecked);
                        btnTermsNext.setAlpha(isChecked ? 1.0f : 0.4f);
                    }
                }
            });
        }
    }

    public void goToStep(View view) {
        if (view == null || view.getTag() == null) return;
        int tag = Integer.parseInt(view.getTag().toString());
        if (step0 != null) step0.setVisibility(View.GONE);
        if (step1 != null) step1.setVisibility(View.GONE);
        if (step2 != null) step2.setVisibility(View.GONE);
        if (step3 != null) step3.setVisibility(View.GONE);

        switch (tag) {
            case 1: if (step1 != null) step1.setVisibility(View.VISIBLE); break;
            case 2: if (step2 != null) step2.setVisibility(View.VISIBLE); break;
            case 3: if (step3 != null) step3.setVisibility(View.VISIBLE); break;
        }
    }

    public void onAddAccountClick(View view) {
        if (myWebView != null) {
            myWebView.loadUrl("https://accounts.google.com/ServiceLogin?service=youtube");
        }
        if (setupScreen != null) setupScreen.setVisibility(View.GONE);
    }

    public void finishSetup(View view) {
        if (setupScreen != null) setupScreen.setVisibility(View.GONE);
    }

    public void onHeaderBtnClick(View view) {
        if (view == null || view.getTag() == null || myWebView == null) return;
        String tag = view.getTag().toString();
        if (tag.equals("search")) {
            myWebView.loadUrl("https://m.youtube.com/results?search_query=");
        } else if (tag.equals("account")) {
            myWebView.loadUrl("https://m.youtube.com/feed/you");
        } else if (tag.equals("cast")) {
            Toast.makeText(this, "Đang tìm kiếm TV / thiết bị Cast...", Toast.LENGTH_SHORT).show();
        }
    }

    public void onNavClick(View view) {
        if (view == null || view.getTag() == null || myWebView == null) return;
        String tag = view.getTag().toString();
        if (tag.equals("home")) myWebView.loadUrl("https://m.youtube.com");
        else if (tag.equals("shorts")) myWebView.loadUrl("https://m.youtube.com/shorts");
        else if (tag.equals("add")) myWebView.loadUrl("https://m.youtube.com/upload");
        else if (tag.equals("sub")) myWebView.loadUrl("https://m.youtube.com/feed/subscriptions");
        else if (tag.equals("you")) myWebView.loadUrl("https://m.youtube.com/feed/you");
    }

    @Override
    public void onBackPressed() {
        if (myWebView != null && myWebView.canGoBack()) {
            myWebView.goBack();
        } else {
            super.onBackPressed();
        }
    }

    @Override
    protected void onUserLeaveHint() {
        super.onUserLeaveHint();
        try {
            enterPictureInPictureMode();
        } catch (Exception e) {}
    }
}"""

with open("app/src/main/java/com/nads/youtube/MainActivity.java", "w", encoding="utf-8") as f:
    f.write(java_code)

print(">>> ĐÃ ÉP CONFIG VỀ CHUẨN ANDROID 10 (API 29)!")
