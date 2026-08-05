import os

project_dir = "/sdcard/Youtube_NADS_PureTuber"

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

    private String demoUrl = "https://commondatastorage.googleapis.com/gtv-videos-bucket/sample/BigBuckBunny.mp4";

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

        if (nativeVideoView != null) {
            MediaController mc = new MediaController(this);
            mc.setAnchorView(nativeVideoView);
            nativeVideoView.setMediaController(mc);
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

    private void startPlaying() {
        if (setupScreen != null) {
            setupScreen.setVisibility(View.GONE);
        }
        if (nativeVideoView != null) {
            Toast.makeText(this, "Đang phát Video Native trực tiếp...", Toast.LENGTH_SHORT).show();
            nativeVideoView.setVideoURI(Uri.parse(demoUrl));
            nativeVideoView.start();
        }
    }

    public void onAddAccountClick(View view) {
        startPlaying();
    }

    public void finishSetup(View view) {
        startPlaying();
    }

    public void onHeaderBtnClick(View view) {
        startPlaying();
    }

    public void onNavClick(View view) {
        startPlaying();
    }

    public void onVideoCardClick(View view) {
        startPlaying();
    }

    @Override
    protected void onUserLeaveHint() {
        super.onUserLeaveHint();
        try {
            enterPictureInPictureMode();
        } catch (Exception e) {}
    }
}"""

with open(f"{project_dir}/app/src/main/java/com/nads/youtube/MainActivity.java", "w", encoding="utf-8") as f:
    f.write(java_code)

print(">>> ĐÃ CẬP NHẬT GÁN SỰ KIỆN CLICK TOÀN CỤC!")
