package com.spike.ml.embabel.agent.starnews;

import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.databind.ObjectMapper;
import org.apache.commons.lang3.StringUtils;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.http.client.JdkClientHttpRequestFactory;
import org.springframework.stereotype.Service;
import org.springframework.web.client.RestClient;

import java.net.http.HttpClient;
import java.util.Objects;

@Service
public class HoroscopeAppApiHoroscopeService implements HoroscopeService {
    private static final Logger LOG = LoggerFactory.getLogger(HoroscopeAppApiHoroscopeService.class);

    private RestClient restClient = RestClient.builder()
            // https://freehoroscopeapi.com/api/v1/get-horoscope/daily?sign=Gemini
            // https://horoscope-app-api.vercel.app
            .baseUrl("https://freehoroscopeapi.com")
            .requestFactory(new JdkClientHttpRequestFactory(
                    HttpClient.newBuilder()
                            .version(HttpClient.Version.HTTP_2)
                            .followRedirects(HttpClient.Redirect.NORMAL).build()))
            .build();

    private ObjectMapper objectMapper = new ObjectMapper();

    @Override
    public String dailyHoroscope(String sign) {
        LOG.info("Sign = {}", sign);
        String defaultResult = "Unable to retrieve horoscope for " + sign + " today.";
        String body = null;
        try {
            body = restClient.get()
                    .uri("/api/v1/get-horoscope/daily?sign={sign}", sign.toLowerCase())
                    .header("User-Agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64)")
                    .retrieve()
                    .body(String.class);
        } catch (Exception e) {
            LOG.error("Query daily horoscope using RestClient failed", e);
            return defaultResult;
        }

        if (StringUtils.isBlank(body)) {
            return defaultResult;
        }


        HoroscopeResponse response = null;
        try {
            response = objectMapper.readValue(body, HoroscopeResponse.class);
        } catch (JsonProcessingException e) {
            LOG.error("", e);
            return defaultResult;
        }
        if (Objects.nonNull(response) &&
                Objects.nonNull(response.data()) &&
                StringUtils.isNotBlank(response.data().horoscope())) {
            return response.data().horoscope();
        }
        return defaultResult;
    }
}
