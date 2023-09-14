package com.passerellesnumeriquesmada.finalfight;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.webkit.WebView;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

         WebView webView=(WebView) findViewById(R.id.WebView);
         webView.loadUrl("file:///android_asset/index.html");
         webView.getSettings().setJavaScriptEnabled(true);


    }
}