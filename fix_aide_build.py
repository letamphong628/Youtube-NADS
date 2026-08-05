import os

project_dir = "/sdcard/Youtube_NADS_PureTuber"

# Sửa app/build.gradle thành bản Native thuần nhẹ nhất
build_gradle_app = """apply plugin: 'com.android.application'

android {
    compileSdkVersion 29
    defaultConfig {
        applicationId "com.nads.youtube"
        minSdkVersion 21
        targetSdkVersion 29
        versionCode 1
        versionName "1.0"
    }
}
"""

with open(f"{project_dir}/app/build.gradle", "w", encoding="utf-8") as f:
    f.write(build_gradle_app)

print(">>> ĐÃ TỐI ƯU CẤU HÌNH BUILD CHO AIDE!")
