import os

# 1. Tạo thư mục chứa mã nguồn
os.makedirs("app/src/main/java/com/nads/youtube", exist_ok=True)
os.makedirs("app/src/main/res/layout", exist_ok=True)

# 2. AndroidManifest.xml chuẩn Android 14 (targetSdkVersion 34)
manifest = """<?xml version="1.0" encoding="utf-8"?>
<manifest xmlns:android="http://schemas.android.com/apk/res/android"
    package="com.nads.youtube">

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

# 3. Giao diện activity_main.xml chuẩn Native (Tràn màn hình 100% không co góc)
layout_xml = """<?xml version="1.0" encoding="utf-8"?>
<RelativeLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:background="#000000">

    <!-- HEADER BAR -->
    <LinearLayout
        android:id="@+id/headerBar"
        android:layout_width="match_parent"
        android:layout_height="56dp"
        android:gravity="center_vertical"
        android:orientation="horizontal"
        android:paddingHorizontal="16dp">

        <ImageView
            android:layout_width="26dp"
            android:layout_height="26dp"
            android:src="@drawable/ic_youtube" />

        <TextView
            android:layout_width="0dp"
            android:layout_height="wrap_content"
            android:layout_weight="1"
            android:layout_marginStart="8dp"
            android:text="YouTube NADS"
            android:textColor="#FFFFFF"
            android:textSize="18sp"
            android:textStyle="bold" />

        <ImageView
            android:layout_width="24dp"
            android:layout_height="24dp"
            android:layout_marginEnd="16dp"
            android:onClick="onHeaderBtnClick"
            android:tag="cast"
            android:src="@drawable/ic_cast" />

        <ImageView
            android:layout_width="24dp"
            android:layout_height="24dp"
            android:layout_marginEnd="16dp"
            android:onClick="onHeaderBtnClick"
            android:tag="search"
            android:src="@drawable/ic_search" />

        <ImageView
            android:layout_width="24dp"
            android:layout_height="24dp"
            android:onClick="onHeaderBtnClick"
            android:tag="account"
            android:src="@drawable/ic_you" />
    </LinearLayout>

    <!-- NỘI DUNG CHÍNH (NATIVE PLAYER CHẠY VIDEO TRỰC TIẾP TRÊN APP) -->
    <FrameLayout
        android:id="@+id/playerContainer"
        android:layout_width="match_parent"
        android:layout_height="match_parent"
        android:layout_below="@id/headerBar"
        android:layout_above="@+id/bottomBar" />

    <!-- THANH BOTTOM NAV LIQUID GLASS BO TRÒN -->
    <LinearLayout
        android:id="@id/bottomBar"
        android:layout_width="match_parent"
        android:layout_height="62dp"
        android:layout_alignParentBottom="true"
        android:layout_margin="12dp"
        android:background="@drawable/bg_liquid_glass"
        android:gravity="center"
        android:orientation="horizontal">

        <LinearLayout
            android:layout_width="0dp"
            android:layout_height="match_parent"
            android:layout_weight="1"
            android:gravity="center"
            android:onClick="onNavClick"
            android:tag="home"
            android:orientation="vertical">
            <ImageView
                android:layout_width="22dp"
                android:layout_height="22dp"
                android:src="@drawable/ic_home" />
            <TextView
                android:layout_width="wrap_content"
                android:layout_height="wrap_content"
                android:text="Trang chủ"
                android:textColor="#38BDF8"
                android:textSize="10sp" />
        </LinearLayout>

        <LinearLayout
            android:layout_width="0dp"
            android:layout_height="match_parent"
            android:layout_weight="1"
            android:gravity="center"
            android:onClick="onNavClick"
            android:tag="shorts"
            android:orientation="vertical">
            <ImageView
                android:layout_width="22dp"
                android:layout_height="22dp"
                android:src="@drawable/ic_shorts" />
            <TextView
                android:layout_width="wrap_content"
                android:layout_height="wrap_content"
                android:text="Shorts"
                android:textColor="#888888"
                android:textSize="10sp" />
        </LinearLayout>

        <LinearLayout
            android:layout_width="0dp"
            android:layout_height="match_parent"
            android:layout_weight="1"
            android:gravity="center"
            android:onClick="onNavClick"
            android:tag="add"
            android:orientation="vertical">
            <ImageView
                android:layout_width="26dp"
                android:layout_height="26dp"
                android:src="@drawable/ic_add" />
        </LinearLayout>

        <LinearLayout
            android:layout_width="0dp"
            android:layout_height="match_parent"
            android:layout_weight="1"
            android:gravity="center"
            android:onClick="onNavClick"
            android:tag="sub"
            android:orientation="vertical">
            <ImageView
                android:layout_width="22dp"
                android:layout_height="22dp"
                android:src="@drawable/ic_sub" />
            <TextView
                android:layout_width="wrap_content"
                android:layout_height="wrap_content"
                android:text="Đăng ký"
                android:textColor="#888888"
                android:textSize="10sp" />
        </LinearLayout>

        <LinearLayout
            android:layout_width="0dp"
            android:layout_height="match_parent"
            android:layout_weight="1"
            android:gravity="center"
            android:onClick="onNavClick"
            android:tag="you"
            android:orientation="vertical">
            <ImageView
                android:layout_width="22dp"
                android:layout_height="22dp"
                android:src="@drawable/ic_you" />
            <TextView
                android:layout_width="wrap_content"
                android:layout_height="wrap_content"
                android:text="Bạn"
                android:textColor="#888888"
                android:textSize="10sp" />
        </LinearLayout>
    </LinearLayout>

    <!-- OVERLAY SETUP TIZEN OS -->
    <LinearLayout
        android:id="@+id/setupScreen"
        android:layout_width="match_parent"
        android:layout_height="match_parent"
        android:background="#000000"
        android:gravity="center"
        android:orientation="vertical"
        android:padding="24dp">

        <LinearLayout
            android:id="@+id/step0"
            android:layout_width="match_parent"
            android:layout_height="wrap_content"
            android:gravity="center"
            android:orientation="vertical">

            <ImageView
                android:layout_width="64dp"
                android:layout_height="64dp"
                android:src="@drawable/ic_youtube" />

            <TextView
                android:layout_width="wrap_content"
                android:layout_height="wrap_content"
                android:layout_marginTop="16dp"
                android:text="Xin chào"
                android:textColor="#FFFFFF"
                android:textSize="28sp"
                android:textStyle="bold" />

            <TextView
                android:layout_width="wrap_content"
                android:layout_height="wrap_content"
                android:layout_marginTop="8dp"
                android:gravity="center"
                android:text="Hãy thiết lập 1 vài thứ để sử dụng ứng dụng 1 cách tốt nhất!"
                android:textColor="#888888"
                android:textSize="14sp" />

            <LinearLayout
                android:layout_width="wrap_content"
                android:layout_height="wrap_content"
                android:layout_marginTop="28dp"
                android:orientation="horizontal">

                <Button
                    android:layout_width="wrap_content"
                    android:layout_height="wrap_content"
                    android:background="@drawable/bg_card_rounded"
                    android:onClick="goToStep"
                    android:tag="1"
                    android:text="Bắt đầu"
                    android:textColor="#FFFFFF" />

                <Button
                    android:layout_width="wrap_content"
                    android:layout_height="wrap_content"
                    android:layout_marginStart="12dp"
                    android:background="@drawable/bg_card_rounded"
                    android:onClick="finishSetup"
                    android:text="Để sau"
                    android:textColor="#888888" />
            </LinearLayout>
        </LinearLayout>

        <LinearLayout
            android:id="@+id/step1"
            android:layout_width="match_parent"
            android:layout_height="wrap_content"
            android:orientation="vertical"
            android:visibility="gone">

            <TextView
                android:layout_width="wrap_content"
                android:layout_height="wrap_content"
                android:text="1. Điều khoản dịch vụ"
                android:textColor="#FFFFFF"
                android:textSize="20sp"
                android:textStyle="bold" />

            <ScrollView
                android:layout_width="match_parent"
                android:layout_height="120dp"
                android:layout_marginTop="12dp"
                android:background="@drawable/bg_card_rounded">

                <TextView
                    android:layout_width="match_parent"
                    android:layout_height="wrap_content"
                    android:padding="12dp"
                    android:text="DỊCH VỤ CỦA YOUTUBE / YOUTUBE TERMS OF SERVICE&#10;&#10;1. Bằng việc sử dụng ứng dụng YouTube NADS, bạn đồng ý tuân thủ các quy định Dịch vụ của Google &amp; YouTube.&#10;2. Hệ thống tự động lọc sạch quảng cáo."
                    android:textColor="#CCCCCC"
                    android:textSize="12sp" />
            </ScrollView>

            <CheckBox
                android:id="@+id/chkTerms"
                android:layout_width="wrap_content"
                android:layout_height="wrap_content"
                android:layout_marginTop="12dp"
                android:text="Tôi đồng ý với Điều Khoản"
                android:textColor="#FFFFFF" />

            <Button
                android:id="@+id/btnTermsNext"
                android:layout_width="match_parent"
                android:layout_height="wrap_content"
                android:layout_marginTop="16dp"
                android:alpha="0.4"
                android:background="@drawable/bg_card_rounded"
                android:enabled="false"
                android:onClick="goToStep"
                android:tag="2"
                android:text="Tiếp theo"
                android:textColor="#FFFFFF" />
        </LinearLayout>

        <LinearLayout
            android:id="@+id/step2"
            android:layout_width="match_parent"
            android:layout_height="wrap_content"
            android:gravity="center"
            android:orientation="vertical"
            android:visibility="gone">

            <TextView
                android:layout_width="wrap_content"
                android:layout_height="wrap_content"
                android:text="2. Thêm Tài Khoản"
                android:textColor="#FFFFFF"
                android:textSize="20sp"
                android:textStyle="bold" />

            <Button
                android:layout_width="wrap_content"
                android:layout_height="wrap_content"
                android:layout_marginTop="20dp"
                android:background="@drawable/bg_card_rounded"
                android:onClick="onAddAccountClick"
                android:text="Thêm tài khoản (Google)"
                android:textColor="#FFFFFF" />
        </LinearLayout>

        <LinearLayout
            android:id="@+id/step3"
            android:layout_width="match_parent"
            android:layout_height="wrap_content"
            android:gravity="center"
            android:orientation="vertical"
            android:visibility="gone">

            <TextView
                android:layout_width="wrap_content"
                android:layout_height="wrap_content"
                android:text="Bạn đã hoàn thành!"
                android:textColor="#FFFFFF"
                android:textSize="22sp"
                android:textStyle="bold" />

            <Button
                android:layout_width="wrap_content"
                android:layout_height="wrap_content"
                android:layout_marginTop="20dp"
                android:background="@drawable/bg_card_rounded"
                android:onClick="finishSetup"
                android:text="Bắt đầu trải nghiệm"
                android:textColor="#FFFFFF" />
        </LinearLayout>
    </LinearLayout>

</RelativeLayout>"""

with open("app/src/main/res/layout/activity_main.xml", "w", encoding="utf-8") as f:
    f.write(layout_xml)

# 4. MainActivity.java Nhúng Player View Lên Khung Native + AdBlocker + Login Google
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

        // Khởi tạo Player View ghép trực tiếp vào layout Native tràn màn hình
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

print(">>> ĐÃ ĐỒNG BỘ GIAO DIỆN NATIVE 100% VÀ TRÀN MÀN HÌNH CHUẨN ANDROID 14!")
