package com.spike.ml.embabel;

import com.embabel.agent.config.annotation.LoggingThemes;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.boot.autoconfigure.security.oauth2.resource.servlet.OAuth2ResourceServerAutoConfiguration;
import org.springframework.boot.autoconfigure.security.servlet.SecurityAutoConfiguration;
import org.springframework.context.ConfigurableApplicationContext;

import java.util.Map;

@SpringBootApplication(exclude = {
        SecurityAutoConfiguration.class,
        OAuth2ResourceServerAutoConfiguration.class
})
public class EmbabelApplication {
    private static final Logger LOG = LoggerFactory.getLogger(EmbabelApplication.class);

    public static void main(String[] args) {
        SpringApplication app = new SpringApplication(EmbabelApplication.class);
        app.setDefaultProperties(Map.of(
                "embabel.agent.logging.personality", LoggingThemes.STAR_WARS
        ));
        ConfigurableApplicationContext ctx = app.run(EmbabelApplication.class, args);
        LOG.info("{} started.", ctx.getApplicationName());
    }
}
