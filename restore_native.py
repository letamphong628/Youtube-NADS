import os

# 1. Tạo thư mục cấu trúc
os.makedirs("app/src/main/java/com/nads/youtube", exist_ok=True)
os.makedirs("app/src/main/res/layout", exist_ok=True)

# 2. AndroidManifest.xml Chuẩn Android 8.1 / 9 (targetSdkVersion 28)
manifest = """<?xml version="1.0" encoding="utf-8"?>
<manifest xmlns:android="http://schemas.android.com/apk/res/android"
    package="com.nads.youtube">

    <uses-sdk android:minSdkVersion="21" android:targetSdkVersion="28" />
    <uses-permission android:name="android.permission.INTERNET" />
    <uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />

    <application
        android:allowBackup="true"
        android:icon="@drawable/ic_youtube"
        android:label="YouTube NADS"
        android:theme="@android:style/Theme.DeviceDefault.NoActionBar">
        
        <activity
            android:name=".MainActivity"
            android:exported="true">
            <intent-filter>
                <action android:name="android.intent.action.MAIN" />
                <category android:name="android.intent.category.LAUNCHER" />
            </intent-filter>
        </activity>
    </application>
</manifest>"""

with open("app/src/main/AndroidManifest.xml", "w", encoding="utf-8") as f:
    f.write(manifest)

# 3. MainActivity.java Chân Chân Native XML 100%
java_code = """package com.nads.youtube;

import android.app.Activity;
import android.os.Bundle;
import android.view.View;
import android.view.Window;
import android.view.WindowManager;
import android.widget.Button;
import android.widget.CheckBox;
import android.widget.CompoundButton;
import android.widget.LinearLayout;
import android.widget.Toast;

public class MainActivity extends Activity {

    private LinearLayout setupScreen;
    private LinearLayout step0, step1, step2, step3;
    private CheckBox chkTerms;
    private Button btnTermsNext;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        
        requestWindowFeature(Window.FEATURE_NO_TITLE);
        getWindow().setFlags(WindowManager.LayoutParams.FLAG_FULLSCREEN, WindowManager.LayoutParams.FLAG_FULLSCREEN);
        
        // Nạp giao diện Native XML chính
        setContentView(R.layout.activity_main);

        setupScreen = (LinearLayout) findViewById(R.id.setupScreen);
        step0 = (LinearLayout) findViewById(R.id.step0);
        step1 = (LinearLayout) findViewById(R.id.step1);
        step2 = (LinearLayout) findViewById(R.id.step2);
        step3 = (LinearLayout) findViewById(R.id.step3);
        chkTerms = (CheckBox) findViewById(R.id.chkTerms);
        btnTermsNext = (Button) findViewById(R.id.btnTermsNext);

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
        Toast.makeText(this, "Mở trang Đăng nhập Google Account...", Toast.LENGTH_SHORT).show();
        if (step2 != null) step2.setVisibility(View.GONE);
        if (step3 != null) step3.setVisibility(View.VISIBLE);
    }

    public void finishSetup(View view) {
        if (setupScreen != null) setupScreen.setVisibility(View.GONE);
        Toast.makeText(this, "Đã hoàn thành thiết lập!", Toast.LENGTH_SHORT).show();
    }

    public void onHeaderBtnClick(View view) {
        if (view == null || view.getTag() == null) return;
        String tag = view.getTag().toString();
        Toast.makeText(this, "Nút Header: " + tag.toUpperCase(), Toast.LENGTH_SHORT).show();
    }

    public void onNavClick(View view) {
        if (view == null || view.getTag() == null) return;
        String tag = view.getTag().toString();
        Toast.makeText(this, "Đã chọn: " + tag.toUpperCase(), Toast.LENGTH_SHORT).show();
    }
}"""

with open("app/src/main/java/com/nads/youtube/MainActivity.java", "w", encoding="utf-8") as f:
    f.write(java_code)

print(">>> ĐÃ KHÔI PHỤC BẢN NATIVE CHUẨN KHÔNG LO ĐEN MÀN HÌNH!")
