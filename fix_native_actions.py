import os

java_code = """package com.nads.youtube;

import android.app.Activity;
import android.content.Intent;
import android.net.Uri;
import android.os.Bundle;
import android.view.View;
import android.view.Window;
import android.view.WindowManager;
import android.widget.Button;
import android.widget.CheckBox;
import android.widget.CompoundButton;
import android.widget.LinearLayout;

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

    private void openActionUrl(String url) {
        try {
            Intent intent = new Intent(Intent.ACTION_VIEW, Uri.parse(url));
            startActivity(intent);
        } catch (Exception e) {}
    }

    // NÚT THÊM TÀI KHOẢN GOOGLE
    public void onAddAccountClick(View view) {
        if (setupScreen != null) setupScreen.setVisibility(View.GONE);
        openActionUrl("https://accounts.google.com/ServiceLogin?service=youtube");
    }

    public void finishSetup(View view) {
        if (setupScreen != null) setupScreen.setVisibility(View.GONE);
    }

    // CÁC NÚT TRÊN HEADER BAR (CHIẾU TV / TÌM KIẾM / HỒ SƠ)
    public void onHeaderBtnClick(View view) {
        if (view == null || view.getTag() == null) return;
        String tag = view.getTag().toString();
        if (tag.equals("search")) {
            openActionUrl("https://m.youtube.com/results?search_query=");
        } else if (tag.equals("account")) {
            openActionUrl("https://m.youtube.com/feed/you");
        } else if (tag.equals("cast")) {
            openActionUrl("https://m.youtube.com");
        }
    }

    // CÁC NÚT TRÊN THANH BOTTOM NAV LIQUID GLASS
    public void onNavClick(View view) {
        if (view == null || view.getTag() == null) return;
        String tag = view.getTag().toString();
        if (tag.equals("home")) {
            openActionUrl("https://m.youtube.com");
        } else if (tag.equals("shorts")) {
            openActionUrl("https://m.youtube.com/shorts");
        } else if (tag.equals("add")) {
            openActionUrl("https://m.youtube.com/upload");
        } else if (tag.equals("sub")) {
            openActionUrl("https://m.youtube.com/feed/subscriptions");
        } else if (tag.equals("you")) {
            openActionUrl("https://m.youtube.com/feed/you");
        }
    }

    // BẤM VÀO CARD VIDEO NATIVE
    public void onVideoCardClick(View view) {
        openActionUrl("https://m.youtube.com");
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

print(">>> ĐÃ GÁN HÀM KÍCH HOẠT HOẠT ĐỘNG THẬT CHO TẤT CẢ NÚT!")
