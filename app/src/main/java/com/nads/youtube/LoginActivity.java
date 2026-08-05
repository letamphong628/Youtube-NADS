package com.nads.youtube;

import android.app.Activity;
import android.content.Context;
import android.content.SharedPreferences;
import android.graphics.Color;
import android.os.Bundle;
import android.view.View;
import android.webkit.WebSettings;
import android.webkit.WebView;
import android.webkit.WebViewClient;
import android.widget.LinearLayout;
import android.widget.TextView;

public class LoginActivity extends Activity {

    private WebView loginWebView;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);

        LinearLayout layout = new LinearLayout(this);
        layout.setLayoutParams(new LinearLayout.LayoutParams(-1, -1));
        layout.setOrientation(LinearLayout.VERTICAL);
        layout.setBackgroundColor(Color.parseColor("#0F0F0F"));

        LinearLayout header = new LinearLayout(this);
        header.setLayoutParams(new LinearLayout.LayoutParams(-1, 120));
        header.setBackgroundColor(Color.BLACK);
        header.setPadding(30, 0, 30, 0);
        header.setGravity(16);

        TextView btnClose = new TextView(this);
        btnClose.setText("❌ Hủy");
        btnClose.setTextColor(Color.RED);
        btnClose.setTextSize(16);
        btnClose.setOnClickListener(new View.OnClickListener() {
            @Override public void onClick(View v) { finish(); }
        });

        TextView title = new TextView(this);
        title.setText("  Đăng nhập Google");
        title.setTextColor(Color.WHITE);
        title.setTextSize(16);

        header.addView(btnClose);
        header.addView(title);

        loginWebView = new WebView(this);
        loginWebView.setLayoutParams(new LinearLayout.LayoutParams(-1, -1));

        WebSettings ws = loginWebView.getSettings();
        ws.setJavaScriptEnabled(true);
        ws.setDomStorageEnabled(true);

        loginWebView.setWebViewClient(new WebViewClient() {
            @Override
            public boolean shouldOverrideUrlLoading(WebView view, String url) {
                if (url.contains("youtube.com") && !url.contains("accounts.google.com")) {
                    SharedPreferences prefs = getSharedPreferences("YouTubeNADS_Prefs", Context.MODE_PRIVATE);
                    prefs.edit().putBoolean("is_logged_in", true).putBoolean("just_logged_in", true).apply();
                    finish();
                    return true;
                }
                view.loadUrl(url);
                return true;
            }
        });

        loginWebView.loadUrl("https://accounts.google.com/ServiceLogin?service=youtube");

        layout.addView(header);
        layout.addView(loginWebView);

        setContentView(layout);
    }
}
