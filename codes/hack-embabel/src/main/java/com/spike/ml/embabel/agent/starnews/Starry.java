package com.spike.ml.embabel.agent.starnews;

import com.embabel.ux.form.Text;
import com.fasterxml.jackson.annotation.JsonClassDescription;

@JsonClassDescription("Astrological details for a person")
public record Starry(@Text(label = "Star sign") String sign) {
}