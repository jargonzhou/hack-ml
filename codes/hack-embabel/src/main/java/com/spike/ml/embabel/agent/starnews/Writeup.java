package com.spike.ml.embabel.agent.starnews;

import com.embabel.agent.domain.library.HasContent;
import com.fasterxml.jackson.annotation.JsonClassDescription;
import com.fasterxml.jackson.annotation.JsonCreator;
import com.fasterxml.jackson.annotation.JsonProperty;

@JsonClassDescription("Writeup relating to a person's horoscope and relevant news")
public record Writeup(String text) implements HasContent {

    @JsonCreator
    public Writeup(@JsonProperty("text") String text) {
        this.text = text;
    }

    @Override
    public String getContent() {
        return text;
    }
}