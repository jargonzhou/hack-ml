package com.spike.ml.embabel.agent.starnews;

public interface HoroscopeService {
    String dailyHoroscope(String sign);

    record HoroscopeResponse(HoroscopeData data) {
    }

    record HoroscopeData(String date, String sign, String period, String horoscope) {
    }
}
