import os

# 1. Giao diện activity_main.xml (Có sẵn khung Native VideoView phát trực tiếp)
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

    <!-- TRÌNH PHÁT VIDEO NATIVE NỘI BỘ (CHẠY TRỰC TIẾP TRÊN APP) -->
    <FrameLayout
        android:id="@+id/playerBox"
        android:layout_width="match_parent"
        android:layout_height="match_parent"
        android:layout_below="@id/headerBar"
        android:layout_above="@+id/bottomBar">

        <VideoView
            android:id="@+id/nativeVideoView"
            android:layout_width="match_parent"
            android:layout_height="match_parent"
            android:layout_gravity="center" />
    </FrameLayout>

    <!-- THANH BOTTOM NAV LIQUID GLASS -->
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

# 2. Code MainActivity.java điều khiển VideoView trực tiếp
java_code = """package com.nads.youtube;

import android.app.Activity;
import android.net.Uri;
import android.os.Bundle;
import android.view.View;
import android.view.Window;
import android.view.WindowManager;
import android.widget.Button;
import android.widget.CheckBox;
import android.widget.CompoundButton;
import android.widget.LinearLayout;
import android.widget.MediaController;
import android.widget.Toast;
import android.widget.VideoView;

public class MainActivity extends Activity {

    private LinearLayout setupScreen;
    private LinearLayout step0, step1, step2, step3;
    private CheckBox chkTerms;
    private Button btnTermsNext;
    private VideoView nativeVideoView;

    // Link Stream MP4 trực tiếp để phát ngay trên App
    private String demoStreamUrl = "https://commondatastorage.googleapis.com/gtv-videos-bucket/sample/BigBuckBunny.mp4";

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
        nativeVideoView = (VideoView) findViewById(R.id.nativeVideoView);

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

        // Cấu hình trình phát Video Native trong app
        if (nativeVideoView != null) {
            MediaController mediaController = new MediaController(this);
            mediaController.setAnchorView(nativeVideoView);
            nativeVideoView.setMediaController(mediaController);
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

    public void playVideoNative(String url) {
        if (nativeVideoView != null) {
            Toast.makeText(this, "Đang tải luồng Video Native...", Toast.LENGTH_SHORT).show();
            nativeVideoView.setVideoURI(Uri.parse(url));
            nativeVideoView.start();
        }
    }

    public void onAddAccountClick(View view) {
        if (setupScreen != null) setupScreen.setVisibility(View.GONE);
        Toast.makeText(this, "Quản lý Tài Khoản Native", Toast.LENGTH_SHORT).show();
    }

    public void finishSetup(View view) {
        if (setupScreen != null) setupScreen.setVisibility(View.GONE);
        playVideoNative(demoStreamUrl);
    }

    public void onHeaderBtnClick(View view) {
        if (view == null || view.getTag() == null) return;
        playVideoNative(demoStreamUrl);
    }

    public void onNavClick(View view) {
        if (view == null || view.getTag() == null) return;
        playVideoNative(demoStreamUrl);
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

print(">>> ĐÃ ĐỔI NGUYÊN LÝ PHÁT VIDEO TRỰC TIẾP BẰNG NATIVE VIDEOVIEW!")
