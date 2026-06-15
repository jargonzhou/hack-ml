package com.spike.ml.embabel.agent.starnews;

import com.embabel.agent.api.annotation.AchievesGoal;
import com.embabel.agent.api.annotation.Action;
import com.embabel.agent.api.annotation.Agent;
import com.embabel.agent.api.annotation.Export;
import com.embabel.agent.api.common.Ai;
import com.embabel.agent.api.tool.Tool;
import com.embabel.agent.core.CoreToolGroups;
import com.embabel.agent.core.hitl.WaitFor;
import com.embabel.agent.domain.io.UserInput;
import com.embabel.agent.domain.library.Person;
import com.embabel.agent.domain.library.PersonImpl;
import com.embabel.agent.domain.library.RelevantNewsStories;
import com.embabel.common.ai.model.LlmOptions;
import com.spike.ml.embabel.support.ContextDiagnosticTools;
import org.springframework.beans.factory.annotation.Value;

import java.util.stream.Collectors;

// Shell Input:
// execute "write a story about Gemini and Cristiano Ronaldo."


/**
 * Writes an amusing personalised writeup combining a person's horoscope/星座运势
 * and relevant current news stories/时事新闻.
 */
@Agent(name = "JavaStarNewsFinder",
        description = "Write an amusing personalised writeup combining a person's horoscope and current news stories",
        beanName = "javaStarNewsFinder")
public class StarNewsFinderAgent {

    private final HoroscopeService horoscopeService;
    private final int storyCount;

    public StarNewsFinderAgent(HoroscopeService horoscopeService,
                               @Value("${star-news-finder.story.count:5}") int storyCount) {
        this.horoscopeService = horoscopeService;
        this.storyCount = storyCount;
    }

    @Action
    public Person extractPerson(UserInput userInput, Ai ai) {
        return ai
//                .withLlm(OpenAiModels.GPT_41)
                .withDefaultLlm()
                .createObjectIfPossible("""
                        Create a person from this user input, extracting their name:
                        %s""".formatted(userInput.getContent()), PersonImpl.class);
    }

    @Action(cost = 100.0) // Make it costly so it won't be used in a plan unless there's no other path
    public Starry makeStarry(Person person) {
        return WaitFor.formSubmission("Let's get some astrological details for " + person.getName(), Starry.class);
    }

    @Action
    public StarPerson assembleStarPerson(Person person, Starry starry) {
        return new StarPerson(person.getName(), starry.sign());
    }

    @Action
    public StarPerson extractStarPerson(UserInput userInput, Ai ai) {
        return ai
//                .withLlmByRole("best")
                .withDefaultLlm()
                .createObjectIfPossible("""
                        Create a person from this user input, extracting their name and star sign:
                        %s""".formatted(userInput.getContent()), StarPerson.class);
    }

    @Action
    public Horoscope retrieveHoroscope(StarPerson starPerson) {
        return new Horoscope(horoscopeService.dailyHoroscope(starPerson.sign()));
    }

    @Action
    public RelevantNewsStories findNewsStories(StarPerson person, Horoscope horoscope, Ai ai) {
        var prompt = """
                IMPORTANT: Before doing anything else, call the check_tool_call_context tool
                to verify the execution environment. Then proceed with the task below.
                                
                %s is an astrology believer with the sign %s.
                Their horoscope for today is:
                    <horoscope>%s</horoscope>
                Given this, use web tools and generate search queries
                to find %d relevant news stories summarize them in a few sentences.
                Include the URL for each story.
                Do not look for another horoscope reading or return results directly about astrology;
                find stories relevant to the reading above.
                                
                For example:
                - If the horoscope says that they may
                want to work on relationships, you could find news stories about
                novel gifts
                - If the horoscope says that they may want to work on their career,
                find news stories about training courses.""".formatted(person.name(), person.sign(), horoscope.summary(), storyCount);

        return ai.withDefaultLlm().withId("find_news_stories")
                .withToolGroup(CoreToolGroups.WEB)
                .withTool(Tool.fromInstance(new ContextDiagnosticTools())
                        .getFirst())
                .createObject(prompt, RelevantNewsStories.class);
    }

    // The @AchievesGoal annotation indicates that completing this action
    // achieves the given goal, so the agent can be complete
    @AchievesGoal(description = "Write an amusing writeup for the target person based on their horoscope and current news stories",
            export = @Export(remote = true, name = "starNewsWriteupJava", startingInputTypes = {StarPerson.class, UserInput.class}))
    @Action
    public Writeup writeup(StarPerson person, RelevantNewsStories relevantNewsStories, Horoscope horoscope, Ai ai) {
        var newsItems = relevantNewsStories.getItems().stream()
                .map(item -> "- " + item.getUrl() + ": " + item.getSummary())
                .collect(Collectors.joining("\n"));

        var prompt = """
                Take the following news stories and write up something
                amusing for the target person.
                                
                Begin by summarizing their horoscope in a concise, amusing way, then
                talk about the news. End with a surprising signoff.
                                
                %s is an astrology believer with the sign %s.
                Their horoscope for today is:
                    <horoscope>%s</horoscope>
                Relevant news stories are:
                %s
                                
                Format it as Markdown with links.""".formatted(person.name(), person.sign(), horoscope.summary(), newsItems);
        return ai.withLlm(LlmOptions
//                        .withFirstAvailableLlmOf(AnthropicModels.CLAUDE_37_SONNET, OpenAiModels.GPT_41_MINI)
                        .withDefaultLlm()
                        .withTemperature(0.9))
                .createObject(prompt, Writeup.class);
    }
}