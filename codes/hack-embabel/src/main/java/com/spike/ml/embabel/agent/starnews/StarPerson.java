package com.spike.ml.embabel.agent.starnews;

import com.embabel.agent.domain.library.Person;
import com.fasterxml.jackson.annotation.JsonClassDescription;
import com.fasterxml.jackson.annotation.JsonCreator;
import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.annotation.JsonPropertyDescription;
import com.fasterxml.jackson.databind.annotation.JsonDeserialize;

@JsonClassDescription("Person with astrology details")
@JsonDeserialize(as = StarPerson.class)
public record StarPerson(
        String name,
        @JsonPropertyDescription("Star sign") String sign
) implements Person {

    @JsonCreator
    public StarPerson(
            @JsonProperty("name") String name,
            @JsonProperty("sign") String sign
    ) {
        this.name = name;
        this.sign = sign;
    }

    @Override
    public String getName() {
        return name;
    }
}