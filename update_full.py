import os

# 1. Tạo các Icon Vector viền trắng (Outline)
icons = {
    "ic_home.xml": """<vector xmlns:android="http://schemas.android.com/apk/res/android" android:width="24dp" android:height="24dp" android:viewportWidth="24" android:viewportHeight="24"><path android:strokeColor="#FFFFFF" android:strokeWidth="1.8" android:fillColor="#00000000" android:pathData="M3,9 L12,2 L21,9 L21,20 C21,21.1 20.1,22 19,22 L5,22 C3.9,22 3,21.1 3,20 Z"/></vector>""",
    "ic_shorts.xml": """<vector xmlns:android="http://schemas.android.com/apk/res/android" android:width="24dp" android:height="24dp" android:viewportWidth="24" android:viewportHeight="24"><path android:strokeColor="#FFFFFF" android:strokeWidth="1.8" android:fillColor="#00000000" android:pathData="M13,2 L3,14 L12,14 L11,22 L21,10 L12,10 Z"/></vector>""",
    "ic_add.xml": """<vector xmlns:android="http://schemas.android.com/apk/res/android" android:width="28dp" android:height="28dp" android:viewportWidth="24" android:viewportHeight="24"><path android:strokeColor="#FFFFFF" android:strokeWidth="1.8" android:fillColor="#00000000" android:pathData="M12,2 C6.48,2 2,6.48 2,12 C2,17.52 6.48,22 12,22 C17.52,22 22,17.52 22,12 C22,6.48 17.52,2 12,2 Z M12,8 L12,16 M8,12 L16,12"/></vector>""",
    "ic_sub.xml": """<vector xmlns:android="http://schemas.android.com/apk/res/android" android:width="24dp" android:height="24dp" android:viewportWidth="24" android:viewportHeight="24"><path android:strokeColor="#FFFFFF" android:strokeWidth="1.8" android:fillColor="#00000000" android:pathData="M4,11 L20,11 L20,20 L4,20 Z M4,6 L20,6"/></vector>""",
    "ic_you.xml": """<vector xmlns:android="http://schemas.android.com/apk/res/android" android:width="24dp" android:height="24dp" android:viewportWidth="24" android:viewportHeight="24"><path android:strokeColor="#FFFFFF" android:strokeWidth="1.8" android:fillColor="#00000000" android:pathData="M19,21 C19,17.13 15.87,14 12,14 C8.13,14 5,17.13 5,21 M12,11 C14.21,11 16,9.21 16,7 C16,4.79 14.21,3 12,3 C9.79,3 8,4.79 8,7 C8,9.21 9.79,11 12,11 Z"/></vector>""",
    "ic_cast.xml": """<vector xmlns:android="http://schemas.android.com/apk/res/android" android:width="24dp" android:height="24dp" android:viewportWidth="24" android:viewportHeight="24"><path android:strokeColor="#FFFFFF" android:strokeWidth="1.8" android:fillColor="#00000000" android:pathData="M2,16.1 C4.9,16.1 7.1,18.4 7.1,21 M2,11.5 C7.2,11.5 11.5,15.8 11.5,21 M2,7 L20,7 C21.1,7 22,7.9 22,9 L22,19 C22,20.1 21.1,21 20,21 L15,21 M2,20 L2.01,20"/></vector>""",
    "ic_search.xml": """<vector xmlns:android="http://schemas.android.com/apk/res/android" android:width="24dp" android:height="24dp" android:viewportWidth="24" android:viewportHeight="24"><path android:strokeColor="#FFFFFF" android:strokeWidth="1.8" android:fillColor="#00000000" android:pathData="M11,19 C15.4183,19 19,15.4183 19,11 C19,6.58172 15.4183,3 11,3 C6.58172,3 3,6.58172 3,11 C3,15.4183 6.58172,19 11,19 Z M21,21 L16.65,16.65"/></vector>"""
}

for filename, content in icons.items():
    with open(f"app/src/main/res/drawable/{filename}", "w", encoding="utf-8") as f:
        f.write(content)

# 2. Cập nhật activity_main.xml (Đầy đủ Icon + Gán OnClick)
layout_xml = """<?xml version="1.0" encoding="utf-8"?>
<RelativeLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:background="#000000">

    <!-- HEADER BAR BAR -->
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

        <!-- NÚT CHIẾU / TÌM KIẾM / TÀI KHOẢN -->
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

    <!-- TRANG CHỦ -->
    <ScrollView
        android:layout_width="match_parent"
        android:layout_height="match_parent"
        android:layout_below="@id/headerBar"
        android:layout_above="@+id/bottomBar"
        android:padding="16dp">

        <LinearLayout
            android:layout_width="match_parent"
            android:layout_height="wrap_content"
            android:orientation="vertical">

            <LinearLayout
                android:layout_width="match_parent"
                android:layout_height="wrap_content"
                android:background="@drawable/bg_card_rounded"
                android:orientation="vertical"
                android:padding="12dp">

                <View
                    android:layout_width="match_parent"
                    android:layout_height="180dp"
                    android:background="#262626" />

                <TextView
                    android:layout_width="wrap_content"
                    android:layout_height="wrap_content"
                    android:layout_marginTop="10dp"
                    android:text="YouTube NADS Native - Full Icons &amp; Controls"
                    android:textColor="#FFFFFF"
                    android:textSize="15sp"
                    android:textStyle="bold" />
            </LinearLayout>
        </LinearLayout>
    </ScrollView>

    <!-- BOTTOM NAV LIQUID GLASS (ĐẦY ĐỦ ICON VÀ NÚT BẤM) -->
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

# 3. Cập nhật MainActivity.java Xử lý tất cả các Nút Bấm
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
        Toast.makeText(this, "Đang kết nối cổng Đăng nhập Google...", Toast.LENGTH_SHORT).show();
        if (step2 != null) step2.setVisibility(View.GONE);
        if (step3 != null) step3.setVisibility(View.VISIBLE);
    }

    public void finishSetup(View view) {
        if (setupScreen != null) setupScreen.setVisibility(View.GONE);
        Toast.makeText(this, "Chào mừng bạn đến với YouTube NADS!", Toast.LENGTH_SHORT).show();
    }

    public void onHeaderBtnClick(View view) {
        if (view == null || view.getTag() == null) return;
        String tag = view.getTag().toString();
        if (tag.equals("cast")) {
            Toast.makeText(this, "Đang tìm thiết bị TV / Cast xung quanh...", Toast.LENGTH_SHORT).show();
        } else if (tag.equals("search")) {
            Toast.makeText(this, "Mở thanh Tìm Kiếm...", Toast.LENGTH_SHORT).show();
        } else if (tag.equals("account")) {
            Toast.makeText(this, "Mở Thông tin Tài Khoản...", Toast.LENGTH_SHORT).show();
        }
    }

    public void onNavClick(View view) {
        if (view == null || view.getTag() == null) return;
        String tag = view.getTag().toString();
        Toast.makeText(this, "Đã chuyển sang mục: " + tag.toUpperCase(), Toast.LENGTH_SHORT).show();
    }
}"""

with open("app/src/main/java/com/nads/youtube/MainActivity.java", "w", encoding="utf-8") as f:
    f.write(java_code)

print(">>> ĐÃ CẬP NHẬT ĐẦY ĐỦ ICON VÀ XỬ LÝ SỰ KIỆN NÚT BẤM!")
