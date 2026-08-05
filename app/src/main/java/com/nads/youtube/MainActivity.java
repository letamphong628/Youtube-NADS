package com.nads.youtube;

import android.app.Activity;
import android.app.AlertDialog;import android.app.PictureInPictureParams;
import android.content.Context;
import android.content.DialogInterface;
import android.content.Intent;
import android.content.SharedPreferences;
import android.graphics.Color;
import android.graphics.Typeface;
import android.net.Uri;
import android.os.Build;
import android.os.Bundle;
import android.util.Rational;
import android.view.Gravity;
import android.view.View;
import android.view.animation.AlphaAnimation;
import android.webkit.WebChromeClient;
import android.webkit.WebSettings;
import android.webkit.WebView;
import android.webkit.WebViewClient;
import android.widget.CheckBox;
import android.widget.EditText;
import android.widget.ImageView;
import android.widget.LinearLayout;
import android.widget.ScrollView;
import android.widget.TextView;
import android.widget.Toast;

public class MainActivity extends Activity implements View.OnClickListener {

    private LinearLayout rootLayout, setupOverlay, mainAppLayout;
    private LinearLayout step0, step1, step2, step3;
    private LinearLayout contentContainer;
    private WebView mainWebView;
    private LinearLayout navHomeLayout, navShortsLayout, navSubLayout, navYouLayout;
    private ImageView imgHome, imgShorts, imgSub, imgYou;
    private TextView txtHome, txtShorts, txtSub, txtYou;
    private CheckBox chkAgree;

    private static final String PREF_NAME = "YouTubeNADS_Prefs";
    private static final String KEY_SETUP_DONE = "is_setup_done";

    private static final int COLOR_ACTIVE = Color.parseColor("#00A2FF");
    private static final int COLOR_INACTIVE = Color.parseColor("#FFFFFF");

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);

        try {
            rootLayout = new LinearLayout(this);
            rootLayout.setLayoutParams(new LinearLayout.LayoutParams(-1, -1));
            rootLayout.setOrientation(LinearLayout.VERTICAL);
            rootLayout.setBackgroundColor(Color.parseColor("#0F0F0F"));

            createMainAppUI();
            createSetupOverlayUI();

            rootLayout.addView(mainAppLayout);
            rootLayout.addView(setupOverlay);

            setContentView(rootLayout);
            checkSetupState();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    @Override
    protected void onResume() {
        super.onResume();
        SharedPreferences prefs = getSharedPreferences(PREF_NAME, Context.MODE_PRIVATE);
        if (prefs.getBoolean("just_logged_in", false)) {
            prefs.edit().putBoolean("just_logged_in", false).apply();
            if (step2 != null && step2.getVisibility() == View.VISIBLE) {
                animateTransition(step2, step3);
            }
        }
    }

    @Override
    protected void onUserLeaveHint() {
        super.onUserLeaveHint();
        // TỰ ĐỘNG BẬT PIP KHI VUỐT BẤM VỀ MÀN HÌNH CHÍNH (ANDROID 8.0+)
        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.O) {
            try {
                PictureInPictureParams params = new PictureInPictureParams.Builder()
                        .setAspectRatio(new Rational(16, 9))
                        .build();
                enterPictureInPictureMode(params);
            } catch (Exception e) {
                e.printStackTrace();
            }
        }
    }

    private void checkSetupState() {
        SharedPreferences prefs = getSharedPreferences(PREF_NAME, Context.MODE_PRIVATE);
        boolean isSetupDone = prefs.getBoolean(KEY_SETUP_DONE, false);

        if (isSetupDone) {
            setupOverlay.setVisibility(View.GONE);
            mainAppLayout.setVisibility(View.VISIBLE);
            loadYouTubeUrl("https://m.youtube.com");
        } else {
            setupOverlay.setVisibility(View.VISIBLE);
            mainAppLayout.setVisibility(View.GONE);
        }
    }

    private void markSetupAsCompleted() {
        SharedPreferences prefs = getSharedPreferences(PREF_NAME, Context.MODE_PRIVATE);
        prefs.edit().putBoolean(KEY_SETUP_DONE, true).apply();
    }

    private void createMainAppUI() {
        mainAppLayout = new LinearLayout(this);
        mainAppLayout.setLayoutParams(new LinearLayout.LayoutParams(-1, -1));
        mainAppLayout.setOrientation(LinearLayout.VERTICAL);

        // Top Bar
        LinearLayout topBar = new LinearLayout(this);
        topBar.setLayoutParams(new LinearLayout.LayoutParams(-1, dp(56)));
        topBar.setOrientation(LinearLayout.HORIZONTAL);
        topBar.setPadding(dp(16), 0, dp(16), 0);
        topBar.setGravity(Gravity.CENTER_VERTICAL);
        topBar.setBackgroundColor(Color.parseColor("#0F0F0F"));

        TextView logo = new TextView(this);
        logo.setText("▶ YouTube NADS");
        logo.setTextColor(Color.WHITE);
        logo.setTextSize(18);
        logo.setTypeface(Typeface.DEFAULT_BOLD);
        logo.setLayoutParams(new LinearLayout.LayoutParams(0, -2, 1.0f));

        ImageView btnCast = createHeaderVectorIcon(R.drawable.ic_cast);
        ImageView btnBell = createHeaderVectorIcon(R.drawable.ic_bell);
        ImageView btnSearch = createHeaderVectorIcon(R.drawable.ic_search);

        btnCast.setOnClickListener(new View.OnClickListener() {
            @Override public void onClick(View v) { handleCastAction(); }
        });
        btnBell.setOnClickListener(new View.OnClickListener() {
            @Override public void onClick(View v) { loadYouTubeUrl("https://m.youtube.com/feed/notifications"); }
        });
        btnSearch.setOnClickListener(new View.OnClickListener() {
            @Override public void onClick(View v) { showSearchDialog(); }
        });

        topBar.addView(logo);
        topBar.addView(btnCast);
        topBar.addView(btnBell);
        topBar.addView(btnSearch);

        // Content Area
        contentContainer = new LinearLayout(this);
        contentContainer.setLayoutParams(new LinearLayout.LayoutParams(-1, 0, 1.0f));
        contentContainer.setOrientation(LinearLayout.VERTICAL);

        mainWebView = new WebView(this);
        mainWebView.setLayoutParams(new LinearLayout.LayoutParams(-1, -1));

        WebSettings ws = mainWebView.getSettings();
        ws.setJavaScriptEnabled(true);
        ws.setDomStorageEnabled(true);
        ws.setDatabaseEnabled(true);
        // HỖ TRỢ PHÁT ÂM THANH TRONG NỀN KHÔNG CẦN TƯƠNG TÁC TAY
        ws.setMediaPlaybackRequiresUserGesture(false);
        ws.setUserAgentString("Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36");

        mainWebView.setWebChromeClient(new WebChromeClient());

        mainWebView.setWebViewClient(new WebViewClient() {
            @Override
            public boolean shouldOverrideUrlLoading(WebView view, String url) {
                view.loadUrl(url);
                return true;
            }

            @Override
            public void onPageFinished(WebView view, String url) {
                // INJECT CSS/JS: 
                // 1. Ẩn thanh bottom web
                // 2. Kéo thanh phân loại (Tất cả, Âm nhạc...) lên sát Header
                // 3. Auto Skip Ad & Tự ẩn Banner Quảng Cáo
                String injectScript = "javascript:(function() { " +
                        "var css = 'ytm-pivot-bar-renderer, .pivot-bar-renderer, ytm-app-bar-renderer, ytm-mobile-topbar-renderer, .ad-showing, .ad-container, .ytp-ad-overlay-container { display: none !important; } " +
                        "ytm-feed-filter-chip-bar-renderer { margin-top: 0px !important; padding-top: 0px !important; top: 0px !important; position: sticky !important; z-index: 999 !important; }';" +
                        "var style = document.createElement('style'); " +
                        "style.type = 'text/css'; " +
                        "style.appendChild(document.createTextNode(css)); " +
                        "document.head.appendChild(style); " +
                        "setInterval(function() { " +
                        "   var skipBtn = document.querySelector('.ytp-ad-skip-button, .ytp-ad-skip-button-modern, .ytp-skip-ad-button'); " +
                        "   if (skipBtn) { skipBtn.click(); } " +
                        "}, 500); " +
                        "})()";
                view.loadUrl(injectScript);
            }
        });

        contentContainer.addView(mainWebView);

        // Bottom Navigation Bar
        LinearLayout bottomNav = new LinearLayout(this);
        bottomNav.setLayoutParams(new LinearLayout.LayoutParams(-1, dp(60)));
        bottomNav.setOrientation(LinearLayout.HORIZONTAL);
        bottomNav.setBackgroundColor(Color.parseColor("#0F0F0F"));

        navHomeLayout = createNavTab(R.drawable.ic_nav_home, "Trang chủ", true);
        navShortsLayout = createNavTab(R.drawable.ic_nav_shorts, "Shorts", false);
        navSubLayout = createNavTab(R.drawable.ic_nav_sub, "Đăng ký", false);
        navYouLayout = createNavTab(R.drawable.ic_nav_you, "Bạn", false);

        imgHome = (ImageView) navHomeLayout.getChildAt(0);
        txtHome = (TextView) navHomeLayout.getChildAt(1);

        imgShorts = (ImageView) navShortsLayout.getChildAt(0);
        txtShorts = (TextView) navShortsLayout.getChildAt(1);

        imgSub = (ImageView) navSubLayout.getChildAt(0);
        txtSub = (TextView) navSubLayout.getChildAt(1);

        imgYou = (ImageView) navYouLayout.getChildAt(0);
        txtYou = (TextView) navYouLayout.getChildAt(1);

        navHomeLayout.setOnClickListener(this);
        navShortsLayout.setOnClickListener(this);
        navSubLayout.setOnClickListener(this);
        navYouLayout.setOnClickListener(this);

        bottomNav.addView(navHomeLayout);
        bottomNav.addView(navShortsLayout);
        bottomNav.addView(navSubLayout);
        bottomNav.addView(navYouLayout);

        mainAppLayout.addView(topBar);
        mainAppLayout.addView(contentContainer);
        mainAppLayout.addView(bottomNav);
    }

    private void handleCastAction() {
        try {
            String currentUrl = mainWebView != null ? mainWebView.getUrl() : "https://m.youtube.com";
            Intent intent = new Intent(Intent.ACTION_VIEW, Uri.parse(currentUrl));
            intent.setPackage("com.google.android.youtube");
            startActivity(intent);
        } catch (Exception e) {
            Toast.makeText(this, "Đang quét thiết bị Cast không dây...", Toast.LENGTH_SHORT).show();
        }
    }

    private LinearLayout createNavTab(int iconRes, String label, boolean active) {
        LinearLayout tab = new LinearLayout(this);
        tab.setLayoutParams(new LinearLayout.LayoutParams(0, -1, 1.0f));
        tab.setOrientation(LinearLayout.VERTICAL);
        tab.setGravity(Gravity.CENTER);

        ImageView icon = new ImageView(this);
        icon.setImageResource(iconRes);
        icon.setLayoutParams(new LinearLayout.LayoutParams(dp(22), dp(22)));
        icon.setColorFilter(active ? COLOR_ACTIVE : COLOR_INACTIVE);

        TextView text = new TextView(this);
        text.setText(label);
        text.setTextSize(10);
        text.setTextColor(active ? COLOR_ACTIVE : COLOR_INACTIVE);
        text.setGravity(Gravity.CENTER);
        text.setPadding(0, dp(2), 0, 0);

        tab.addView(icon);
        tab.addView(text);
        return tab;
    }

    private void loadYouTubeUrl(String url) {
        if (mainWebView != null) {
            mainWebView.loadUrl(url);
        }
    }

    private void showSearchDialog() {
        AlertDialog.Builder builder = new AlertDialog.Builder(this);
        builder.setTitle("🔍 Tìm kiếm Video");

        LinearLayout layout = new LinearLayout(this);
        layout.setOrientation(LinearLayout.VERTICAL);
        layout.setPadding(dp(20), dp(10), dp(20), dp(10));

        final EditText input = new EditText(this);
        input.setHint("Nhập từ khóa...");
        input.setTextColor(Color.WHITE);
        input.setHintTextColor(Color.GRAY);
        layout.addView(input);

        builder.setView(layout);
        builder.setPositiveButton("Tìm", new DialogInterface.OnClickListener() {
            @Override public void onClick(DialogInterface dialog, int which) {
                String q = input.getText().toString().trim();
                if(!q.isEmpty()) {
                    loadYouTubeUrl("https://m.youtube.com/results?search_query=" + q.replace(" ", "+"));
                }
            }
        });
        builder.setNegativeButton("Hủy", null);
        builder.show();
    }

    private void createSetupOverlayUI() {
        setupOverlay = new LinearLayout(this);
        setupOverlay.setLayoutParams(new LinearLayout.LayoutParams(-1, -1));
        setupOverlay.setOrientation(LinearLayout.VERTICAL);
        setupOverlay.setGravity(Gravity.CENTER);
        setupOverlay.setPadding(dp(24), dp(24), dp(24), dp(24));

        step0 = new LinearLayout(this);
        step0.setLayoutParams(new LinearLayout.LayoutParams(-1, -2));
        step0.setOrientation(LinearLayout.VERTICAL);
        step0.setGravity(Gravity.CENTER);

        TextView tvWelcome = new TextView(this);
        tvWelcome.setText("Xin chào");
        tvWelcome.setTextColor(Color.WHITE);
        tvWelcome.setTextSize(22);
        tvWelcome.setTypeface(Typeface.DEFAULT_BOLD);
        tvWelcome.setGravity(Gravity.CENTER);

        TextView tvIcon = new TextView(this);
        tvIcon.setText("▶");
        tvIcon.setTextSize(60);
        tvIcon.setTextColor(Color.WHITE);
        tvIcon.setGravity(Gravity.CENTER);
        tvIcon.setPadding(0, dp(16), 0, dp(16));

        TextView tvSubWelcome = new TextView(this);
        tvSubWelcome.setText("Hãy thiết lập 1 vài thứ để sử dụng ứng dụng 1 cách tốt nhất!");
        tvSubWelcome.setTextColor(Color.GRAY);
        tvSubWelcome.setTextSize(14);
        tvSubWelcome.setGravity(Gravity.CENTER);

        LinearLayout btnGroup0 = new LinearLayout(this);
        btnGroup0.setLayoutParams(new LinearLayout.LayoutParams(-1, -2));
        btnGroup0.setOrientation(LinearLayout.HORIZONTAL);
        btnGroup0.setGravity(Gravity.CENTER);
        btnGroup0.setPadding(0, dp(24), 0, 0);

        TextView btnStart = createButton("Bắt đầu", COLOR_ACTIVE);
        TextView btnSkip = createButton("Để sau", Color.parseColor("#272727"));

        btnStart.setOnClickListener(new View.OnClickListener() {
            @Override public void onClick(View v) { animateTransition(step0, step1); }
        });
        btnSkip.setOnClickListener(new View.OnClickListener() {
            @Override public void onClick(View v) {
                markSetupAsCompleted();
                animateTransition(setupOverlay, mainAppLayout); 
                loadYouTubeUrl("https://m.youtube.com");
            }
        });

        btnGroup0.addView(btnStart);
        btnGroup0.addView(btnSkip);

        step0.addView(tvIcon);
        step0.addView(tvWelcome);
        step0.addView(tvSubWelcome);
        step0.addView(btnGroup0);

        step1 = new LinearLayout(this);
        step1.setLayoutParams(new LinearLayout.LayoutParams(-1, -1));
        step1.setOrientation(LinearLayout.VERTICAL);
        step1.setVisibility(View.GONE);

        TextView tvTermsTitle = new TextView(this);
        tvTermsTitle.setText("1. Điều Khoản và Quyền Riêng Tư");
        tvTermsTitle.setTextColor(Color.WHITE);
        tvTermsTitle.setTextSize(18);
        tvTermsTitle.setTypeface(Typeface.DEFAULT_BOLD);

        ScrollView svText = new ScrollView(this);
        svText.setLayoutParams(new LinearLayout.LayoutParams(-1, 0, 1.0f));
        svText.setPadding(dp(12), dp(12), dp(12), dp(12));
        svText.setBackgroundColor(Color.parseColor("#1B1B1B"));

        TextView tvTermsBody = new TextView(this);
        tvTermsBody.setText("ĐIỀU KHOẢN DỊCH VỤ YOUTUBE NADS\n\n1. Tuân thủ quy định dịch vụ nội dung YouTube.\n\n2. Quyền riêng tư: Không thu thập dữ liệu trái phép.");
        tvTermsBody.setTextColor(Color.LTGRAY);
        svText.addView(tvTermsBody);

        chkAgree = new CheckBox(this);
        chkAgree.setText("Tôi đồng ý với điều khoản dịch vụ");
        chkAgree.setTextColor(Color.WHITE);

        TextView btnNext1 = createButton("Tiếp theo", COLOR_ACTIVE);
        btnNext1.setOnClickListener(new View.OnClickListener() {
            @Override public void onClick(View v) {
                if (chkAgree.isChecked()) {
                    animateTransition(step1, step2);
                } else {
                    Toast.makeText(MainActivity.this, "Vui lòng tích chọn đồng ý!", Toast.LENGTH_SHORT).show();
                }
            }
        });

        step1.addView(tvTermsTitle);
        step1.addView(svText);
        step1.addView(chkAgree);
        step1.addView(btnNext1);

        step2 = new LinearLayout(this);
        step2.setLayoutParams(new LinearLayout.LayoutParams(-1, -2));
        step2.setOrientation(LinearLayout.VERTICAL);
        step2.setGravity(Gravity.CENTER);
        step2.setVisibility(View.GONE);

        TextView tvAccTitle = new TextView(this);
        tvAccTitle.setText("2. Thêm Tài Khoản Google Của Bạn");
        tvAccTitle.setTextColor(Color.WHITE);
        tvAccTitle.setTextSize(18);
        tvAccTitle.setTypeface(Typeface.DEFAULT_BOLD);

        TextView tvAccSub = new TextView(this);
        tvAccSub.setText("Đăng nhập để xem danh sách kênh đã đăng ký.");
        tvAccSub.setTextColor(Color.GRAY);
        tvAccSub.setPadding(0, dp(12), 0, dp(24));

        TextView btnAddAcc = createButton("Thêm Tài Khoản", COLOR_ACTIVE);
        TextView btnSkipAcc = createButton("Để sau", Color.parseColor("#272727"));

        btnAddAcc.setOnClickListener(new View.OnClickListener() {
            @Override public void onClick(View v) {
                Intent intent = new Intent(MainActivity.this, LoginActivity.class);
                startActivity(intent);
            }
        });

        btnSkipAcc.setOnClickListener(new View.OnClickListener() {
            @Override public void onClick(View v) { animateTransition(step2, step3); }
        });

        step2.addView(tvAccTitle);
        step2.addView(tvAccSub);
        step2.addView(btnAddAcc);
        step2.addView(btnSkipAcc);

        step3 = new LinearLayout(this);
        step3.setLayoutParams(new LinearLayout.LayoutParams(-1, -2));
        step3.setOrientation(LinearLayout.VERTICAL);
        step3.setGravity(Gravity.CENTER);
        step3.setVisibility(View.GONE);

        TextView tvDoneTitle = new TextView(this);
        tvDoneTitle.setText("3. Chào mừng bạn đến với YouTube NADS");
        tvDoneTitle.setTextColor(Color.WHITE);
        tvDoneTitle.setTextSize(20);
        tvDoneTitle.setTypeface(Typeface.DEFAULT_BOLD);

        TextView tvDoneSub = new TextView(this);
        tvDoneSub.setText("Bạn đã thiết lập xong, hãy bắt đầu sử dụng ứng dụng nhé!");
        tvDoneSub.setTextColor(Color.GRAY);
        tvDoneSub.setPadding(0, dp(12), 0, dp(32));

        TextView btnFinish = createButton("Bắt đầu sử dụng", COLOR_ACTIVE);
        btnFinish.setOnClickListener(new View.OnClickListener() {
            @Override public void onClick(View v) { 
                markSetupAsCompleted();
                animateTransition(setupOverlay, mainAppLayout); 
                loadYouTubeUrl("https://m.youtube.com");
            }
        });

        step3.addView(tvDoneTitle);
        step3.addView(tvDoneSub);
        step3.addView(btnFinish);

        setupOverlay.addView(step0);
        setupOverlay.addView(step1);
        setupOverlay.addView(step2);
        setupOverlay.addView(step3);
    }

    private void animateTransition(View hideView, View showView) {
        AlphaAnimation fadeOut = new AlphaAnimation(1.0f, 0.0f);
        fadeOut.setDuration(200);
        hideView.startAnimation(fadeOut);
        hideView.setVisibility(View.GONE);

        showView.setVisibility(View.VISIBLE);
        AlphaAnimation fadeIn = new AlphaAnimation(0.0f, 1.0f);
        fadeIn.setDuration(250);
        showView.startAnimation(fadeIn);
    }

    private ImageView createHeaderVectorIcon(int resId) {
        ImageView iv = new ImageView(this);
        iv.setImageResource(resId);
        iv.setPadding(dp(10), dp(10), dp(10), dp(10));
        iv.setLayoutParams(new LinearLayout.LayoutParams(dp(44), dp(44)));
        return iv;
    }

    private TextView createButton(String text, int bgColor) {
        TextView btn = new TextView(this);
        LinearLayout.LayoutParams lp = new LinearLayout.LayoutParams(dp(130), dp(44));
        lp.setMargins(dp(6), dp(8), dp(6), dp(8));
        btn.setLayoutParams(lp);
        btn.setText(text);
        btn.setTextColor(Color.WHITE);
        btn.setTextSize(14);
        btn.setTypeface(Typeface.DEFAULT_BOLD);
        btn.setGravity(Gravity.CENTER);
        btn.setBackgroundColor(bgColor);
        return btn;
    }

    private int dp(int value) {
        return (int) (value * getResources().getDisplayMetrics().density);
    }

    @Override
    public void onBackPressed() {
        if (mainWebView != null && mainWebView.canGoBack()) {
            mainWebView.goBack();
        } else {
            super.onBackPressed();
        }
    }

    @Override
    public void onClick(View v) {
        imgHome.setColorFilter(COLOR_INACTIVE);
        txtHome.setTextColor(COLOR_INACTIVE);

        imgShorts.setColorFilter(COLOR_INACTIVE);
        txtShorts.setTextColor(COLOR_INACTIVE);

        imgSub.setColorFilter(COLOR_INACTIVE);
        txtSub.setTextColor(COLOR_INACTIVE);

        imgYou.setColorFilter(COLOR_INACTIVE);
        txtYou.setTextColor(COLOR_INACTIVE);

        if (v == navHomeLayout) {
            imgHome.setColorFilter(COLOR_ACTIVE);
            txtHome.setTextColor(COLOR_ACTIVE);
            loadYouTubeUrl("https://m.youtube.com");
        } else if (v == navShortsLayout) {
            imgShorts.setColorFilter(COLOR_ACTIVE);
            txtShorts.setTextColor(COLOR_ACTIVE);
            loadYouTubeUrl("https://m.youtube.com/shorts");
        } else if (v == navSubLayout) {
            imgSub.setColorFilter(COLOR_ACTIVE);
            txtSub.setTextColor(COLOR_ACTIVE);
            loadYouTubeUrl("https://m.youtube.com/feed/subscriptions");
        } else if (v == navYouLayout) {
            imgYou.setColorFilter(COLOR_ACTIVE);
            txtYou.setTextColor(COLOR_ACTIVE);
            loadYouTubeUrl("https://m.youtube.com/feed/library");
        }
    }
}
